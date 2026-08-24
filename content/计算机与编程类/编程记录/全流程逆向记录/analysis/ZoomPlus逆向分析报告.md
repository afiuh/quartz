# ZoomPlus.exe 逆向分析报告

分析对象：`逆向主程序/ZoomPlus.exe`（53,956,608 字节）
分析方法：PE 结构分析、导入表分析、全量字符串提取、Nuitka 模块元数据重建
分析日期：2026-08-05

## 0. 结论摘要

1. **打包方式**：Nuitka standalone（Python 3.12.7 → C → MSVC 19.51 LTCG 编译），**不是 PyInstaller**，因此 pyinstxtractor-ng 无法解析。
2. **无壳**：DIE 的 ".rsrc 压缩" 与 "Rust" 均为启发式误报；导入表静态依赖 `python312.dll`，符合 Nuitka 产物特征。
3. **程序性质**：商业化的 AI 鼠标宏/瞄准辅助（aimbot），面向 Apex/CS2/OW2/彩虹六号/远光84 等 FPS 游戏，内置屏幕捕获 + ONNX 目标检测 + PID/追踪器瞄准 + 自动开火 + 多硬件输出通道。
4. **关键对抗特性**：硬件指纹采集、反作弊进程检测、Arduino 伪装成罗技鼠标、ViGEmBus 虚拟手柄、HVCI 检测、GitHub 更新器。
5. **未发现**：本二进制内没有卡密/授权服务器交互逻辑；机器码仅用于启动诊断日志输出。

## 1. 二进制身份

| 项目 | 值 |
|---|---|
| PE 架构 | x64 (0x8664) |
| 节区 | .text / .rdata / .data / .pdata / .rsrc / .reloc（6 节，无异常节区名） |
| 导入表 | KERNEL32、VCRUNTIME140、api-ms-win-crt-*、**python312.dll（静态导入）** |
| DIE 检测 | MSVC 19.51 LTCG；Rust/.rsrc 压缩均为误报 |
| 版本资源 | ZoomPlus 1.0.0.0 |
| Python | 3.12.7 (tags/v3.12.7:0b05ead) |
| Nuitka 特征 | 280+ 处 `__nuitka_*` / `NUITKA_PACKAGE_*` 字符串，无 PyInstaller COOKIE/PYZ |

## 2. 编译进 exe 的应用源码文件（模块清单）

```
main.py                      # 程序入口与启动逻辑
core\__init__.py
core\ai_aiming.py            # 瞄准计算（头部类、磁吸、PID+追踪+贝塞尔管线）
core\ai_loop.py              # AI 主循环（捕获/推理/发布线程管理）
core\ai_loop_state.py        # LoopState 数据类
core\ai_loop_utils.py        # 准星/检测区域/队列工具
core\auto_fire.py            # 自动开火循环
core\config.py               # 配置类（类型安全 JSON）
core\config_manager.py       # 预设配置管理（增删改导入导出）
core\inference.py            # ONNX 预处理/后处理 + PID 控制器
core\key_listener.py         # 热键监听
core\language_manager.py     # 语言
core\logging_config.py       # 日志/崩溃钩子/启动诊断/机器码
core\path_utils.py           # 路径解析
core\roboflow_utils.py       # Roboflow 云推理适配
core\screen_capture.py       # dxcam/MSS 捕获
core\session_utils.py        # ONNX 会话优化/设备选择/预热
core\smart_tracker.py        # 目标运动预测追踪
core\updater.py              # GitHub 更新检查
gui\disclaimer_dialog.py     # 免责声明
gui\overlay.py               # 屏幕覆盖层
gui\fluent_app\*             # PyQt-Fluent-Widgets 界面（window/setup_wizard/base_page/pages\aim|configs|keys|trigger|visuals/theme_*）
win_utils\admin.py           # 管理员权限
win_utils\console.py         # 控制台显示/隐藏
win_utils\key_utils.py       # 按键检测
win_utils\vk_codes.py        # 虚拟键码
win_utils\mouse_move.py      # SendInput / mouse_event 移动
win_utils\mouse_click.py     # 点击（sendinput/hardware/mouse_event/ddxoft）
win_utils\ddxoft_mouse.py    # DDXoft 鼠标模拟
win_utils\arduino_mouse.py   # Arduino Leonardo USB HID 鼠标
win_utils\arduino_spoofer.py # 伪装 Arduino 为罗技 G502
win_utils\makcu_mouse.py     # MAKCU KM Host 硬件鼠标
win_utils\xbox_controller.py # ViGEmBus 虚拟 Xbox 手柄 + 反作弊检测
win_utils\xinput_handler.py  # 实体手柄读取
win_utils\gamepad_input.py   # XInput 摇杆/死区处理
win_utils\priority.py        # 线程/进程优先级
```

## 3. 总体数据流

```
屏幕捕获 (dxcam DXGI / MSS)
   │  BGR 帧
   ▼
AI 推理 (ONNX Runtime DirectML/CPU，或 Roboflow 云)
   │  boxes / confidences / class_ids
   ▼
后处理 (YOLOv5/v8 格式检测、NMS、FOV/类别过滤)
   │
   ▼
目标选择 → PID 控制器 + SmartTracker 预测 + 贝塞尔平滑 + 磁吸
   │  move_x / move_y
   ▼
输出设备（按配置选择）：
   Xbox 虚拟手柄 (ViGEmBus，默认) / DDXoft / SendInput /
   mouse_event / Arduino Leonardo / MAKCU 硬件鼠标
   │
   ├─ 自动开火线程（独立，按键触发 + 命中判定 + 定时点击）
   └─ 覆盖层 (PyQtOverlay) 绘制框/FPS 面板
```

## 4. 核心模块详解

### 4.1 入口 main.py
- DPI 感知设置（SetProcessDpiAwarenessContext / SetProcessDPIAware）。
- 预加载 pywin32 DLL（`python\dependencies\win32\lib` 下的 pywintypes/pythoncom）。
- 初始化日志 → 加载配置 → 管理员检查 → 进程优先级 → HVCI 检查 → DDXoft 就绪检查。
- 首次运行弹免责声明/设置向导；随后创建覆盖层与主窗口。
- 启动 5 个线程：`ai_logic_loop`、`auto_fire_loop`、`aim_toggle_key_listener`、`window_toggle_key_listener`、`lock_category_key_listener`。
- ONNX 模型元数据提取类别名（支持 JSON / Python repr / 换行三种 `names` 格式），或回退 Roboflow 云推理。

### 4.2 core.logging_config — 启动诊断与机器码
- 用 PowerShell 调 `Get-CimInstance` 采集 7 类硬件信息：
  - Win32_Processor（含 ProcessorId）、Win32_BaseBoard（SerialNumber）、Win32_BIOS（SerialNumber）、Win32_ComputerSystemProduct（UUID）、Win32_VideoController、Win32_PhysicalMemory、Win32_OperatingSystem。
- `machine_code` = 对 `hostname + mac_node + processor_id + baseboard_serial + computer_uuid + bios_serial` 取 **SHA256 hexdigest**。
- 启动时以 JSON 形式写入 `zoomplus_crash.log`（与实测日志完全吻合）。
- 另含崩溃钩子：主线程/工作线程未捕获异常、faulthandler、Qt 消息重定向、全线程堆栈转储。

### 4.3 core.ai_loop — 主循环
- `_PreprocessCache`：BGRA→BGR、直接 resize 与 YOLOv5 letterbox（灰色 114 填充）两种预处理。
- 捕获工作线程：dxcam DXGI video_mode（高帧率、区域捕获、环形帧缓冲），失败自动回退 MSS。
- 左右摇杆直通线程、AI 覆盖层输出线程（500Hz 解耦）。
- 模型热切换：检测 model_path 变化 → 重建 ONNX 会话（输入尺寸变化时联动预处理缓存）。
- 延迟统计：EMA 分阶段统计 capture/pre/inf/post，高精度定时器 + FPS 上限。

### 4.4 core.inference — 推理与 PID
- YOLOv5/v8 输出格式自动判别（按维度形状启发式）。
- YOLOv5 letterbox 参考 Matias Kovero 仓库；坐标转换、objectness×class 置信度、NMS。
- `PIDController`：误差死区、积分限幅、微分低通、动态 P 增益（0~50% 线性、50~100% 加速至 200%）。

### 4.5 core.ai_aiming — 瞄准管线
- `_HEAD_CLASS_KEYWORDS`：head / enemyHead / enemy_head / ct_head / t_head。
- 瞄准点：头部类直接取框中心，其余按 `aim_y_offset_ratio`（0=顶，0.5=中，1=底）取值。
- `calculate_sticky_pull`：磁吸向量，靠近目标框时强、向 FOV 边缘衰减。
- `process_aiming`：类别过滤 → 最近目标排序 → PID → SmartTracker 预测（抖动平滑/急停清零/位置死区）→ 贝塞尔曲线平滑 → 反色/摇杆映射 → 发送移动。

### 4.6 core.auto_fire — 自动开火
- 独立守护线程：监听开火键（双键配置）或常开模式。
- 从检测队列取框 → 计算瞄准点 → 判定准星是否在目标范围内 → 按 `aim_part`（head/body/both）触发点击。
- 支持 `auto_fire_delay`、`auto_fire_interval`、框更新间隔；点击走 `mouse_click_method` 通道。

### 4.7 core.updater — 更新器
- `https://api.github.com/repos/` + `REPO_OWNER` + `/` + `REPO_NAME` + `/releases/latest`。
- **REPO_OWNER = `iishong0w0`，REPO_NAME = `ZoomPlus-AI-Aimbot`**；User-Agent = `ZoomPlus-AI-Aimbot/<__version__>`。
- 解析 tag（`'v1.0.2' -> (1,0,2)` 式），发 `update_available/up_to_date/check_failed` 信号，浏览器打开更新页。
- 该仓库当前返回 404（私有/已删除/从未公开）。

### 4.8 core.roboflow_utils — 云推理
- `RoboflowInferenceAdapter`：帧写临时文件 → `model.predict()` 云推理（作者注明单次往返 200~800ms）→ 转换 boxes/confidences/class_ids。
- 内置预设：`MatiasKovero`（enemy）、`CSGO_4Class`（ct_body/ct_head/t_body/t_head）等；`download_roboflow_model` 支持从 Roboflow 下载 ONNX。
- 配置默认 workspace=`fortnite-ai-aim`、project=`cod-mw-warzone-catlb`。

### 4.9 win_utils — 输入输出与对抗
- **xbox_controller（默认输出）**：ViGEmBus 虚拟 Xbox 360 手柄，右摇杆映射视角；含灵敏度/死区、统计、诊断、虚拟槽位冲突检测。
- **反作弊检测**（进程名枚举）：
  - vgc.exe / vgtray.exe → Vanguard（Riot/Valorant）
  - easyanticheat.exe / eac_launcher.exe → Easy Anti-Cheat
  - beclient.dll / beservice.exe / bedaisy.sys → BattlEye
  - atvi-ricochet.exe → Ricochet（COD）
  - nprotect.exe / gameguard.des → GameGuard
  - xigncode.exe → XIGNCODE3；uncheater.exe → Uncheater；faceit.exe / faceitclient.exe → FACEIT
- **arduino_spoofer**：改写 Arduino IDE 的 `boards.txt`（自动备份 .bak），把 Leonardo 的 VID/PID/产品名改为 **Logitech G502 HERO Gaming Mouse（0x046D / 0xC07D）**，使枚举结果隐藏为真实鼠标；附验证函数。
- **ddxoft_mouse**：DDXoft 驱动鼠标模拟，带 HVCI（内存完整性）检测与禁用提示。
- **makcu_mouse**：MAKCU KM Host 硬件通道（官方 API 文档：https://www.makcu.com/cn/api）。
- **gamepad_input/xinput_handler**：实体 XInput 手柄读取，径向死区，按键上升沿事件。

### 4.10 GUI（PyQt-Fluent-Widgets）
- 页面：aim / configs / keys / trigger / visuals；setup_wizard、theme_manager、overlay。
- 覆盖层：检测框、FPS 状态面板、FOV 圈等（默认全部关闭，仅状态面板开）。

## 5. 对抗/隐蔽特性汇总

1. 硬件指纹采集（CIM + SHA256 机器码）——用于激活绑定/风控（本构建仅日志输出）。
2. 反作弊进程检测（14 项，覆盖主流反作弊）。
3. Arduino Leonardo 伪装罗技 G502——硬件 HID 级鼠标移动，规避软件层鼠标 API 检测。
4. ViGEmBus 虚拟手柄——手柄输入路径，规避鼠标输入监控。
5. HVCI 检测——DDXoft 驱动不可用时的降级提示。
6. 高精度定时器、多线程解耦、EMA 延迟统计——性能/隐蔽兼顾。
7. 后台 GitHub 更新检查——可持续推送新版本。

## 6. 分析产物（analysis/ 目录）

- `strings_ascii.txt` / `strings_utf16.txt`：全量字符串（77.9 万条 ASCII）。
- `strings_cjk.txt`：UTF-8 中文串（9486 条，界面文案以繁体为主）。
- `cat_*.txt`：URL / 源码路径 / Nuitka / 机器码 / 网络 / Roboflow / 输入输出 分类。
- `modules/`：每个应用模块的字符串上下文导出（含偏移）。

## 7. 后续建议

1. **函数级还原**：装 Ghidra（或 radare2），用 Nuitka 模块元数据 + 字符串交叉引用定位各模块函数；本报告已给出模块名、函数名、常量与源文件路径映射。
2. **验证机器码算法**：本机运行 exe 后对比日志中的 machine_code 与 CIM 原始值，可确认哈希输入顺序。
3. **更新器分析**：抓 `api.github.com/repos/iishong0w0/ZoomPlus-AI-Aimbot/releases/latest` 的流量（若仓库复活）。
4. **模型分析**：ONNX 模型可直接用 netron/onnx 工具打开，确认类别定义与训练来源（YOLOv8）。
5. **动态行为**：沙箱内运行 + Process Monitor/API Monitor 抓注册表、文件与网络行为，验证静态结论。
