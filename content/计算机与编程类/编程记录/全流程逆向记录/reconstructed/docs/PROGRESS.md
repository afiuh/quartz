---
---

# 项目进度记录

> 最近更新：2026-08-06（运行环�?+ CUDA 加速收口）

## 2026-08-07：端到端实机验证收口

### 本次成果
- 实机全链路跑通：dxcam（独显直连）�?512 模型（CUDA）→ 瞄准 �?ddxoft，靶场正常锁人；测试模式 5s 满性能 / 1s 循环采集落地�?- 修复清单（含证据）：
  - v11 模型 cxcywh→xyxy 转换（模型输出布局统计：仅 4.9% 满足 xyxy，实锤中心点+宽高�?  - NMS 去重漏接（原�?Frida 实采每帧单框，本版每�?15 框）
  - DPI 感知缺失（GetSystemMetrics 1536x864 vs 实际 1920x1080�?  - ddxoft 惰性初始化（DD_btn 穷举确认�?  - 测试套件挂起（test_build_loop �?mock 驱动初始化）
  - 模型每秒重载 bug（swap_model_if_changed 路径比较错误 �?推理 p90 尖峰 333ms，已修复并验证不再重载）
- 研究结论�?  - dxcam 在混合显卡笔记本 Optimus 模式下对独显调桌面复制必失败（微软文档设计限制）；独显直连可复活；原版在本机实际�?mss 兜底�?  - bezier_curve_steps �?Frida 探测�?771 次属性读取）确认原版瞄准热路径从不读取，�?UI 占位，重构版保持不生效�?  - 动态预判滞后为参数问题（预判时�?平滑/延迟补偿），非代码缺陷；延迟补偿列为后续调优点�?
### 待办更新�?026-08-07 复核�?| 优先�?| 内容 |
|---|---|
| �?| GUI（PyQt6�?|
| �?| 优化�?1/2 实现（自适应帧率 + 动态预判与增强瞄准，设计已确认�?|
| �?| 优化�?3~8（区域直�?/ 模型档位 / 贝塞�?/ 死区配置�?/ 动态P 研究 / 截图自愈�?|
| �?| 流水线并行（原阶�?3，实验项�?|
| �?| xbox 响应映射、auto_fire（搁置） |
| 扩展 | TensorRT（FP32）、WGC 截图通道（Optimus 兼容的健壮性缺口） |

## 一、总体状�?
| 阶段 | 状�?|
|---|---|
| 逆向分析（Nuitka 确认 / Ghidra 定位�?| �?|
| 静态还原（core / win_utils / telemetry / tests�?| �?主体完成 |
| 动态验证（Frida + 靶场�?| 🔶 核心已验证，细节待补 |
| 代码优化（阶�?1�?| �?|
| 运行环境（嵌入式 3.12 + CUDA�?| �?本次收口 |
| GUI（PyQt6�?| �?待做 |

## 二、已完成

### 逆向分析
- 确认 ZoomPlus.exe �?Nuitka 打包�?Python 应用；Ghidra 12.1.2 headless 完成全量分析
- 字符�?引用定位�?`core.ai_aiming`、`process_aiming` 等核心函�?
### 静态还�?- `core/`：config�?5 字段）、config_manager、inference（PIDController + YOLO 推理管线）�?  ai_aiming、smart_tracker、ai_loop�?state/utils）、key_listener、screen_capture�?  auto_fire（占位）、基础设施（path/logging/language/session/roboflow/updater�?- `win_utils/`�?3 个输出通道子模块（ddxoft / win32 / xbox / arduino / makcu�?- `telemetry/`：tracer（环缓冲 + JSONL�? dry_run（测试模式，不真动鼠标）
- `tests/`：单元测�?6/6 通过

### 动态验证（Frida + 靶场实测�?- 已验证：PIDController.update�?032/2032）、calculate_aim_target�?086+）�?  is_head_class、process_aiming 状态机、DD_movR 输出通道、贝塞尔曲线
- 已采集：动�?P、SmartTracker 内部值、主循环节拍、输出通道（capture_all.py�?
### 代码优化（阶�?1，详�?optimization_plan.md�?- EP 自动选择（CUDA→DML→CPU，FP32 不降精度）、会话优化、张量复用�?  screen 尺寸缓存、遥�?干跑入口、高精度限帧

### 运行环境（本次）
- 嵌入�?Python 3.12.4 �?`../tool/python312`（自包含，可整体带走�?- 方案 C 精简�?0.3 GB �?3.1 GB，仅保留项目依赖（原 ~orch �?4.3 GB 垃圾已清�?- CUDA 加速：onnxruntime-gpu 1.20.2 + CUDA 12.9 + cuDNN 9.24
  - 实测：CUDA ~3.1 ms/�?vs CPU ~10.6 ms/帧（�?3.4x�?  - DLL 全部部署�?python312 根目录，不依赖系统安�?- 依赖清单：`../requirements.txt`（含重建/复现说明�?- 系统清理：Python 3.14.3 残留注册记录清除；原 Python312 目录垃圾清除

### 端到端冒烟（本次�?-test 干跑�?- `main.py --test` 稳定运行无报错（截图/循环/生命周期正常�?- 修复三处问题�?  - `AILoop.start()` 缺失 �?补后台线程启动（main.py 生命周期对齐�?  - CUDA DLL 加载失败退�?CPU �?`path_utils` 启动时预加载 CUDA/cuDNN
    核心库（实测必要，`add_dll_directory` �?ORT 无效�?  - mss 兜底截图返回 PIL 图像导致 cv2 报错 �?�?numpy BGR（与 dxcam 一致）
  - ddxoft 未初始化 �?`ai_loop` 周期检查时接入 `ensure_ddxoft_ready()`
    （dd63330.dll 要求**管理员权�?*，非提权会弹 "Run as Administrator"�?- 集成验证：配置加�?�?CUDA 会话（apex_v5_320_best.onnx）→ 推理 �?后处�?全链路通过

## 三、待�?
| 优先�?| 内容 |
|---|---|
| �?| GUI（PyQt6，原版带 Qt6 全套；后端收口后做） |
| �?| 阶段 2：追踪器 alpha 精确拟合 + 延迟补偿 |
| �?| 阶段 3：流水线并行实验 + 数据分析脚本 |
| �?| 阶段 4：动�?P 大误差段公式、xbox 响应曲线 |
| �?| auto_fire（搁置，占位�?|
| 扩展 | TensorRT（仅 FP32，CUDA 不够快再上） |

## 四、环境基�?
- 硬件：NVIDIA GeForce RTX 4050 Laptop GPU�? GB，Compute Capability 8.9，驱�?596.08
- 运行时：`../tool/python312`（Python 3.12.4，嵌入式�?- 推理：onnxruntime-gpu 1.20.2，CUDAExecutionProvider（CUDA→DML→CPU 自动选择�?- 镜像：清�?PyPI（`https://pypi.tuna.tsinghua.edu.cn/simple`，遇代理报错先清代理环境变量�?
## 五、决策记录要�?
- 逆编译产物为**行为等价**，非源码等价；核心公式以动态验证为�?- 第三方开源包不逆向，直接官方下载（cv2 / dxcam / mss / vgamepad / comtypes 等）
- 模型精度不妥协（否掉 FP16 / INT8�?- 推理后端�?CUDA（追求极限性能）；原版�?DML，CUDA 为其升级路径
- 隐藏功能（磁�?/ xbox 映射）不深挖，最后做

