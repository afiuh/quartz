---
---

# process_aiming 閲嶅缓绗旇

鐩爣鍑芥暟锛欶UN_14075b770锛?0 鍙傛暟锛?064 琛屽弽缂栬瘧 C锛?
## 鍙傛暟锛團rida 瀹炴祴纭锛岄『搴忎笌鍙嶇紪璇戜竴鑷达級

```python
def process_aiming(
    config,            # core.config.Config
    boxes,             # List[List[float]]  [x1,y1,x2,y2]
    crosshair_x: int,  # 灞忓箷涓績/鍑嗘槦 x
    crosshair_y: int,
    pid_x,             # core.inference.PIDController锛圶 杞达級
    pid_y,             # core.inference.PIDController锛圷 杞达級
    mouse_method: str, # 'ddxoft' / 'xbox' / ...
    state,             # core.ai_loop_state.LoopState
    current_time: float,
    class_ids,         # List[int] 姣忎釜妫€娴嬫鐨勭被鍒?ID锛堜笌 boxes 涓€涓€瀵瑰簲锛?):
```

## 绫诲埆璇箟锛堢敤鎴风‘璁わ紝鏉ヨ嚜涓荤▼搴忚缃晫闈級

| 绫诲埆 ID | 鍚箟 |
|---|---|
| 0 | 鏁屼汉锛堣嚜鐬勭洰鏍囷級 |
| 1 | 鍊掑湴鐨勬晫浜?|
| 2 | 闃熷弸 |

杩囨护閫昏緫锛氫粎淇濈暀 `class_ids[idx] 鈭?config.enabled_class_ids` 鐨勬娴嬫銆?瀹炴祴锛?12 缁勬牱鏈?boxes 鍧囦负 1 妗嗐€乧lass_ids 鍧囦负 [0]锛堟晫浜猴級锛岄暱搴︿竴涓€瀵瑰簲锛岄浂涓嶄竴鑷淬€?
瀹炴祴鏍锋湰锛歚<Config> | [[984.49, 541.05, 990.98, 555.14]] | 960 | 540 | <PIDController> | <PIDController> | ddxoft | LoopState(...) | 1785932564.79 | [0] => None`

## 灞€閮ㄥ彉閲忥紙鏉ヨ嚜瀛楃涓茶〃锛孨uitka 淇濈暀瀹屾暣鍙橀噺鍚嶏級

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

## 鎺ㄦ柇娴佺▼锛堝緟鍙嶇紪璇戦€愭纭锛?
## 宸茬‘璁ゆ祦绋嬶紙鍙嶇紪璇?+ Frida 鍙岃瘉鎹級

1. 璇?config.enabled_class_ids锛沗for idx, box in enumerate(boxes)` 寰幆
2. 绫诲埆杩囨护锛歚class_ids[idx] 鈭?enabled_class_ids` 鎵嶄繚鐣欙紙0=鏁屼汉/1=鍊掑湴/2=闃熷弸锛?3. 瀵逛繚鐣?box 璋冪敤 `calculate_aim_target(box, config.aim_y_offset_ratio, class_name)`锛團rida 瀹為噰 3 鍙傛暟锛?4. `error_x = target_x - crosshair_x`锛宍error_y = target_y - crosshair_y`
5. `distance_sq = error_x虏 + error_y虏`
6. 姣忔潯鍊欓€夌粍鎴?4 鍏冪粍杩藉姞杩?valid_targets
7. `valid_targets.sort(key=lambda c: c[0])`锛坙ambda=FUN_1407606f0锛宬ey=绗?0 椤?璺濈锛夆啋 鍗囧簭
8. 鍙?`valid_targets[0]`锛堟渶杩戠洰鏍囷級锛岃В鍖?4 鍏冪粍
9. valid_targets 涓虹┖ 鈫?`state.target_locked = False` 鐩存帴杩斿洖
10. PID 鏂规硶鑾峰彇锛坧id_x/pid_y 鐨?update锛夛紱mouse_method 鍒ゆ柇锛坸box / 鍏朵粬锛?
## 瀹屾暣绠＄嚎锛堢涓夎疆锛氬叏閮ㄧ‘璁わ級

1. `for idx, box in enumerate(boxes)` + 绫诲埆杩囨护锛坈lass_ids[idx] 鈭?enabled_class_ids锛?2. 鍊欓€?= (distance_sq, target_x, target_y, box)锛泂ort(key=位 c[0]) 鍙栨渶杩?3. 鏃犵洰鏍?鈫?`state.target_locked = False` 杩斿洖
4. 鏈夌洰鏍?鈫?`state.target_locked = True`
5. 閲嶇畻 error_x/error_y = target - crosshair
6. SmartTracker 娈碉細璋冩ā鍧?getter(FUN_140758b70鈫扗AT_143343590)锛? 鍙傛暟璋冪敤锛?   缁撴灉鍐?state 瀛楁锛圖AT_1433435a8锛夛紱璇?config.tracker_prediction_time 绛?[缁嗚妭寰呰涓洪獙璇乚
7. PID锛歚moveX = pid_x.update(error_x)`銆乣moveY = pid_y.update(error_y)`
8. 璐濆灏旓紙鑻?enabled锛夛細`(error_x, error_y, box, strength, steps)` 鈫?(move_x, move_y)
9. `move_x = int(round(move_x))`銆乣move_y = int(round(move_y))`
10. invert_x/invert_y 涓虹湡 鈫?鍙栬礋
11. move_x==0 and move_y==0 鈫?璺宠繃鍙戦€?12. mouse_method=='xbox' 鈫?set_ai_overlay_target_xbox(move_x, move_y)
    鍚﹀垯 鈫?send_mouse_move(move_x, move_y)
13. 娓呯悊骞惰繑鍥?None

getter 鏄犲皠锛欶UN_140758730=calculate_aim_target銆丗UN_140758840=璐濆灏斿嚱鏁般€?FUN_140758c80=send_mouse_move銆丗UN_140758d90=set_ai_overlay_target_xbox銆?FUN_140758b70=杩借釜鏂规硶婧愩€丗UN_1407585d0=鏈煡锛堢鍚革紵锛夈€丗UN_1407606f0=鎺掑簭 lambda

## 琛屼负楠岃瘉缁撴灉锛堢鍥涜疆锛欶rida 鍓嶅悗鐘舵€?374 缁勶級

- calculate_aim_target锛?74/374 闆惰宸紙鏈 ratio=0.0 閰嶇疆锛屽叕寮忎粛绮剧‘锛?- tracker_last_time锛?74/374 姣忔璋冪敤鏇存柊锛? current_time锛?- tracker_last_target_box锛?72/374 鏇存柊锛? 鏈閫変腑鐩爣妗嗭級
- target_locked 杞彉锛?4 鏉″叏閮?False鈫扵rue锛堥噸鏂伴攣瀹氱洰鏍囷級
- bezier_curve_scalar锛氭伆濂戒笌 target_locked 杞彉鍚屾锛?4/44锛夛紝鑼冨洿绾?[-1, 1]
  鈫?鏂伴攣瀹氱洰鏍囨椂鐢熸垚鏂伴殢鏈烘爣閲忥紱鎸佺画閿佸畾鏃朵繚鎸佷笉鍙?
缁撹锛?  姣忔鏈夌洰鏍囪皟鐢細tracker_last_time/tracker_last_target_box 鏇存柊
  閿佸畾杞彉鏃讹紙False鈫扵rue锛夛細target_locked=True + bezier_curve_scalar=random.uniform(-1,1)
  鏃犵洰鏍囨椂锛歵arget_locked=False

寰呰ˉ锛歴end_mouse_move 瀹為檯鍙傛暟锛坉dxoft 閫氶亾鏈寕閽╋紝闇€ hook win_utils 鍙戦€佸嚱鏁帮級銆?      SmartTracker 鍐呴儴鐘舵€侊紙repr 涓嶅彲瑙侊紝琛屼负绛変环娴嬭瘯浠?LoopState 鍙樺寲涓哄噯锛?
## 楠岃瘉绱犳潗

- analysis/frida/ai_aiming_capture.txt锛?12 缁勭湡瀹?process_aiming 璋冪敤锛堝惈 LoopState 鍏ㄥ瓧娈碉級
- analysis/modules/core_ai_aiming.txt锛氭ā鍧楀瓧绗︿覆琛紙鍙橀噺鍚?甯搁噺锛?- GhidraWork/decompiled_ai_aiming/FUN_14075b770.c锛氬弽缂栬瘧鍘熸枃

