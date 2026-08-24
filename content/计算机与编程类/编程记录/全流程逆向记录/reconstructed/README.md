---
---

# ZoomPlus 行为等价重建

> 目标：把 ZoomPlus.exe（Nuitka 打包�?Python 自瞄）还原为**行为等价**的干净 Python 工程�?> 说明：行为等价而非源码等价；Nuitka 样板无法逐行还原，核心公式以动态验证为准�?
## 2026-08-07：端到端实机验证收口

- 实机（RTX 4050 笔记本）全链路跑通：dxcam 截图 �?512 模型推理 �?坐标映射 �?瞄准 �?ddxoft 输出，靶场可正常锁人�?- 本轮修复的关键问题：
  - YOLOv8/v11 输出 cxcywh→xyxy 转换（v11s 模型输出为中心点+宽高�?  - 推理�?NMS 去重漏接（原版每帧单框，此前每帧多框导致瞄准乱跳�?  - DPI 感知缺失�?25% 缩放�?GetSystemMetrics 虚拟尺寸与截图真实像素错位）
  - ddxoft 驱动惰性初始化（DD_btn 触发装驱动）
- 测试模式：`python main.py --test` = 真实瞄准 + 循环采集�?s 满性能 / 1s 记录，窗口标记切分数据）；`python main.py --dry-run` = 干跑不动鼠标�?- 验证状态：46/46 单测通过；PID 2032/2032、目标点 712+/1086+、追踪器 4691/4691、贝塞尔 2635 帧�?- 已知研究点：动�?P 大误差段公式、xbox 映射、追踪器延迟补偿调优、auto_fire（搁置）�?
## 模块地图

```
reconstructed/
├── core/
�?  ├── config.py            # Config 类（85 字段，config.json 地面真值）�?�?  ├── config_manager.py    # 游戏预设管理（aimlab/apex）✅
�?  ├── inference.py         # PIDController（已验证�? YOLO 推理管线
�?  ├── ai_aiming.py         # 目标选择/瞄准�?process_aiming（状态级已验证）
�?  ├── smart_tracker.py     # 智能预判（语义版，待动态验证）
�?  ├── ai_loop.py           # 主循环调度（骨架�?�?  ├── ai_loop_state.py     # LoopState（字段来自实�?repr）✅
�?  ├── ai_loop_utils.py     # 循环辅助（FPS/间隔�?�?  ├── key_listener.py      # 热键监听（推断）
�?  ├── screen_capture.py    # dxcam/mss 截图（推断）
�?  ├── auto_fire.py         # 自动开火（已搁置，占位�?�?  └── 基础设施：path/logging/language/session/roboflow/updater
├── win_utils/               # 输出通道包（13 子模块）
�?  ├── mouse_move.py        # 方法分发器（ddxoft/win32/xbox/arduino/makcu�?�?  ├── ddxoft_mouse.py      # DD_movR 驱动输出（运行时确认）✅
�?  ├── xbox_controller.py   # 手柄映射（推断，待验证）
�?  ├── mouse_click.py / 其余系统工具
└── tests/                   # 单元测试�?/6 通过�?```

## 验证状�?
| 状�?| 内容 |
|---|---|
| �?已验�?| PIDController.update�?032/2032）、calculate_aim_target�?086+）、is_head_class、process_aiming 状态机、DD_movR 输出通道 |
| 🔶 语义推断 | smart_tracker、key_listener、screen_capture、xbox 映射、YOLO 解码 |
| �?待动态验�?| 贝塞尔操作数、追踪器精确公式、_calculate_adjusted_kp、xbox、YOLO 解码细节 |
| �?刻意省略 | 机器许可校验、更新、反作弊规避（spoofer 等） |

## 运行

```bash
# 环境：Python 3.12，依赖见 requirements.txt（含 CUDA 加速与重建说明�?python -m unittest discover -s tests          # 运行测试
python -m pip install -r requirements.txt     # 重建依赖（清华镜像加 -i https://pypi.tuna.tsinghua.edu.cn/simple�?```

程序入口（main.py）与 GUI 在动态验证收口后添加�?本地嵌入式环境位�?`../tool/python312`（自包含，已配置 CUDA 加速）�?进度记录�?`docs/PROGRESS.md`�?
## 动态验�?
`../analysis/frida/capture_all.py` 一次会话收集：
贝塞�?6 个调用点寄存器值、SmartTracker 方法、动态P、主循环节拍、输出通道�?
