# process_aiming 重建笔记

目标函数：FUN_14075b770（10 参数，4064 行反编译 C）

## 参数（Frida 实测确认，顺序与反编译一致）

```python
def process_aiming(
    config,            # core.config.Config
    boxes,             # List[List[float]]  [x1,y1,x2,y2]
    crosshair_x: int,  # 屏幕中心/准星 x
    crosshair_y: int,
    pid_x,             # core.inference.PIDController（X 轴）
    pid_y,             # core.inference.PIDController（Y 轴）
    mouse_method: str, # 'ddxoft' / 'xbox' / ...
    state,             # core.ai_loop_state.LoopState
    current_time: float,
    class_ids,         # List[int] 每个检测框的类别 ID（与 boxes 一一对应）
):
```

## 类别语义（用户确认，来自主程序设置界面）

| 类别 ID | 含义 |
|---|---|
| 0 | 敌人（自瞄目标） |
| 1 | 倒地的敌人 |
| 2 | 队友 |

过滤逻辑：仅保留 `class_ids[idx] ∈ config.enabled_class_ids` 的检测框。
实测：712 组样本 boxes 均为 1 框、class_ids 均为 [0]（敌人），长度一一对应，零不一致。

实测样本：`<Config> | [[984.49, 541.05, 990.98, 555.14]] | 960 | 540 | <PIDController> | <PIDController> | ddxoft | LoopState(...) | 1785932564.79 | [0] => None`

## 局部变量（来自字符串表，Nuitka 保留完整变量名）

```python
model_class_names, aim_y_offset_ratio,
valid_targets, idx, box, cls_id, cls_name,
target_x, target_y, moveX, moveY, distance_sq,
tracker_enabled, current_box_tuple, last_box, last_cx, last_cy, curr_cx, curr_cy, box_distance_sq,
prediction_time, pred_x, pred_y, errorX, errorY,
strength, perp_x, perp_y, offset_x, offset_y,
sticky_enabled, sticky_strength, fov_radius, pull_x, pull_y,
move_x, move_y
```

## 推断流程（待反编译逐段确认）

## 已确认流程（反编译 + Frida 双证据）

1. 读 config.enabled_class_ids；`for idx, box in enumerate(boxes)` 循环
2. 类别过滤：`class_ids[idx] ∈ enabled_class_ids` 才保留（0=敌人/1=倒地/2=队友）
3. 对保留 box 调用 `calculate_aim_target(box, config.aim_y_offset_ratio, class_name)`（Frida 实采 3 参数）
4. `error_x = target_x - crosshair_x`，`error_y = target_y - crosshair_y`
5. `distance_sq = error_x² + error_y²`
6. 每条候选组成 4 元组追加进 valid_targets
7. `valid_targets.sort(key=lambda c: c[0])`（lambda=FUN_1407606f0，key=第 0 项=距离）→ 升序
8. 取 `valid_targets[0]`（最近目标），解包 4 元组
9. valid_targets 为空 → `state.target_locked = False` 直接返回
10. PID 方法获取（pid_x/pid_y 的 update）；mouse_method 判断（xbox / 其他）

## 完整管线（第三轮：全部确认）

1. `for idx, box in enumerate(boxes)` + 类别过滤（class_ids[idx] ∈ enabled_class_ids）
2. 候选 = (distance_sq, target_x, target_y, box)；sort(key=λ c[0]) 取最近
3. 无目标 → `state.target_locked = False` 返回
4. 有目标 → `state.target_locked = True`
5. 重算 error_x/error_y = target - crosshair
6. SmartTracker 段：调模块 getter(FUN_140758b70→DAT_143343590)，2 参数调用，
   结果写 state 字段（DAT_1433435a8）；读 config.tracker_prediction_time 等 [细节待行为验证]
7. PID：`moveX = pid_x.update(error_x)`、`moveY = pid_y.update(error_y)`
8. 贝塞尔（若 enabled）：`(error_x, error_y, box, strength, steps)` → (move_x, move_y)
9. `move_x = int(round(move_x))`、`move_y = int(round(move_y))`
10. invert_x/invert_y 为真 → 取负
11. move_x==0 and move_y==0 → 跳过发送
12. mouse_method=='xbox' → set_ai_overlay_target_xbox(move_x, move_y)
    否则 → send_mouse_move(move_x, move_y)
13. 清理并返回 None

getter 映射：FUN_140758730=calculate_aim_target、FUN_140758840=贝塞尔函数、
FUN_140758c80=send_mouse_move、FUN_140758d90=set_ai_overlay_target_xbox、
FUN_140758b70=追踪方法源、FUN_1407585d0=未知（磁吸？）、FUN_1407606f0=排序 lambda

## 行为验证结果（第四轮：Frida 前后状态 374 组）

- calculate_aim_target：374/374 零误差（本次 ratio=0.0 配置，公式仍精确）
- tracker_last_time：374/374 每次调用更新（= current_time）
- tracker_last_target_box：372/374 更新（= 本次选中目标框）
- target_locked 转变：44 条全部 False→True（重新锁定目标）
- bezier_curve_scalar：恰好与 target_locked 转变同步（44/44），范围约 [-1, 1]
  → 新锁定目标时生成新随机标量；持续锁定时保持不变

结论：
  每次有目标调用：tracker_last_time/tracker_last_target_box 更新
  锁定转变时（False→True）：target_locked=True + bezier_curve_scalar=random.uniform(-1,1)
  无目标时：target_locked=False

待补：send_mouse_move 实际参数（ddxoft 通道未挂钩，需 hook win_utils 发送函数）、
      SmartTracker 内部状态（repr 不可见，行为等价测试以 LoopState 变化为准）

## 验证素材

- analysis/frida/ai_aiming_capture.txt：712 组真实 process_aiming 调用（含 LoopState 全字段）
- analysis/modules/core_ai_aiming.txt：模块字符串表（变量名/常量）
- GhidraWork/decompiled_ai_aiming/FUN_14075b770.c：反编译原文
