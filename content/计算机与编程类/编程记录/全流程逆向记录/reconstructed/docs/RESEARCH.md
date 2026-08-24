# 逆向研究过程（ZoomPlus 行为等价重建）

## 一、目标与边界

- 目标：把 ZoomPlus.exe（Nuitka 编译打包的 Python 自瞄程序）还原为**行为等价**的干净 Python 工程，可在本机跑通，并支持后续改造。
- 边界：行为等价而非源码等价（Nuitka 样板无法逐行还原，核心公式以动态验证为准）；第三方开源包不逆向，直接官方安装；机器学习模型不反推，复用原模型文件。

## 二、工具链

- 静态：DIE（PE / 编译信息识别）、pyinstxtractor-ng（载荷分析）、Ghidra 12.1.2 headless 全量分析（`-process -noanalysis` + 自研定位 / 反编译脚本）、字符串引用定位核心函数。
- 动态：Frida（内嵌 Python312），hook `PyObject_GetAttr` 等定位配置读取点，hook 目标函数采集入参 / 出参 / 寄存器值；靶场实采。
- 运行环境：嵌入式 Python 3.12 + onnxruntime-gpu（CUDA EP），DLL 随包部署。

## 三、研究阶段

1. **识别**：确认 ZoomPlus.exe 为 Nuitka 打包、Python 3.12.7、Qt6 GUI、onnxruntime 推理。
2. **定位**：Ghidra 全量分析 + 字符串引用 → 定位 `core.ai_aiming` / `process_aiming` / `PIDController` 等核心函数。
3. **静态重建**：core（config / inference / ai_aiming / smart_tracker / ai_loop / screen_capture 等）、win_utils（输出通道）、telemetry、tests。
4. **动态验证**（Frida + 靶场）：
   - PIDController.update：2032/2032 样本回放
   - calculate_aim_target：712/712（后扩至 1086+）
   - SmartTracker：4691/4691
   - 贝塞尔误差旋转公式：2635 帧
   - process_aiming 状态机：374 组
5. **运行环境**：嵌入式 Python 3.12 + CUDA，系统残留清理，依赖经清华镜像安装。
6. **实机联调**（2026-08-06 ~ 08-07）：截图 → 推理 → 瞄准 → 输出全链路跑通，靶场正常锁人。

## 四、关键发现与结论

| 发现 | 证据 | 结论 / 处理 |
|---|---|---|
| ddxoft 驱动惰性初始化 | 穷举 dd63330.dll 导出 | `DD_btn(0)` 触发装驱动，修复 `ensure_ddxoft_ready` |
| dxcam 混合显卡限制 | 微软官方文档 + 本机实测 | Optimus 下对独显 `DuplicateOutput` 必失败；独显直连可复活；原版在本机实际靠 mss 兜底 |
| v11 模型输出 cxcywh | 512 模型输出布局统计（仅 4.9% 满足 xyxy） | 修复转换，瞄准点恢复正常 |
| NMS 漏接 | 原版 Frida 每帧单框 vs 本版每帧 15 框 | 接回 NMS，瞄准不再乱跳 |
| DPI 感知缺失 | GetSystemMetrics 1536x864 vs 实际 1920x1080 | 进程启动置 DPI 感知，坐标系一致 |
| bezier_curve_steps 不参与瞄准 | probe_bezier_reads：3771 次读取仅 enabled / strength | steps 为 UI 占位，重构版保持不生效 |
| 动态预判滞后 | 遥测：预判超前 +8.5px vs 理想 +31px | 参数问题（预判时间 / 平滑 / 延迟补偿），非代码缺陷 |

## 五、验证方法论

- 行为等价判定以"同输入 → 同输出"的样本回放为准（Frida 实采样本离线回放，浮点对齐）。
- 单测 46 个：PID / 目标点 / 追踪器 / 贝塞尔 / 配置 / 遥测 / 输出分发。
- 实机端到端：靶场实测 + 遥测交叉验证（测试模式窗口标记切分数据）。

## 六、后续研究点

- 动态 P 大误差段公式（需大误差样本）
- xbox 响应映射
- 追踪器延迟补偿调优（预判时间 / 平滑系数，测试模式可采集验证）
- auto_fire（搁置）
- GUI（PyQt6，待做）
