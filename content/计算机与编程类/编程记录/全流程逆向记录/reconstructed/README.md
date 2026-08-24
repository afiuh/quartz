---
---

# ZoomPlus 琛屼负绛変环閲嶅缓

> 鐩爣锛氭妸 ZoomPlus.exe锛圢uitka 鎵撳寘鐨?Python 鑷瀯锛夎繕鍘熶负**琛屼负绛変环**鐨勫共鍑€ Python 宸ョ▼銆?> 璇存槑锛氳涓虹瓑浠疯€岄潪婧愮爜绛変环锛汵uitka 鏍锋澘鏃犳硶閫愯杩樺師锛屾牳蹇冨叕寮忎互鍔ㄦ€侀獙璇佷负鍑嗐€?
## 2026-08-07锛氱鍒扮瀹炴満楠岃瘉鏀跺彛

- 瀹炴満锛圧TX 4050 绗旇鏈級鍏ㄩ摼璺窇閫氾細dxcam 鎴浘 鈫?512 妯″瀷鎺ㄧ悊 鈫?鍧愭爣鏄犲皠 鈫?鐬勫噯 鈫?ddxoft 杈撳嚭锛岄澏鍦哄彲姝ｅ父閿佷汉銆?- 鏈疆淇鐨勫叧閿棶棰橈細
  - YOLOv8/v11 杈撳嚭 cxcywh鈫抶yxy 杞崲锛坴11s 妯″瀷杈撳嚭涓轰腑蹇冪偣+瀹介珮锛?  - 鎺ㄧ悊鍚?NMS 鍘婚噸婕忔帴锛堝師鐗堟瘡甯у崟妗嗭紝姝ゅ墠姣忓抚澶氭瀵艰嚧鐬勫噯涔辫烦锛?  - DPI 鎰熺煡缂哄け锛?25% 缂╂斁涓?GetSystemMetrics 铏氭嫙灏哄涓庢埅鍥剧湡瀹炲儚绱犻敊浣嶏級
  - ddxoft 椹卞姩鎯版€у垵濮嬪寲锛圖D_btn 瑙﹀彂瑁呴┍鍔級
- 娴嬭瘯妯″紡锛歚python main.py --test` = 鐪熷疄鐬勫噯 + 寰幆閲囬泦锛?s 婊℃€ц兘 / 1s 璁板綍锛岀獥鍙ｆ爣璁板垏鍒嗘暟鎹級锛沗python main.py --dry-run` = 骞茶窇涓嶅姩榧犳爣銆?- 楠岃瘉鐘舵€侊細46/46 鍗曟祴閫氳繃锛汸ID 2032/2032銆佺洰鏍囩偣 712+/1086+銆佽拷韪櫒 4691/4691銆佽礉濉炲皵 2635 甯с€?- 宸茬煡鐮旂┒鐐癸細鍔ㄦ€?P 澶ц宸鍏紡銆亁box 鏄犲皠銆佽拷韪櫒寤惰繜琛ュ伩璋冧紭銆乤uto_fire锛堟悂缃級銆?
## 妯″潡鍦板浘

```
reconstructed/
鈹溾攢鈹€ core/
鈹?  鈹溾攢鈹€ config.py            # Config 绫伙紙85 瀛楁锛宑onfig.json 鍦伴潰鐪熷€硷級鉁?鈹?  鈹溾攢鈹€ config_manager.py    # 娓告垙棰勮绠＄悊锛坅imlab/apex锛夆渽
鈹?  鈹溾攢鈹€ inference.py         # PIDController锛堝凡楠岃瘉锛? YOLO 鎺ㄧ悊绠＄嚎
鈹?  鈹溾攢鈹€ ai_aiming.py         # 鐩爣閫夋嫨/鐬勫噯鐐?process_aiming锛堢姸鎬佺骇宸查獙璇侊級
鈹?  鈹溾攢鈹€ smart_tracker.py     # 鏅鸿兘棰勫垽锛堣涔夌増锛屽緟鍔ㄦ€侀獙璇侊級
鈹?  鈹溾攢鈹€ ai_loop.py           # 涓诲惊鐜皟搴︼紙楠ㄦ灦锛?鈹?  鈹溾攢鈹€ ai_loop_state.py     # LoopState锛堝瓧娈垫潵鑷疄閲?repr锛夆渽
鈹?  鈹溾攢鈹€ ai_loop_utils.py     # 寰幆杈呭姪锛團PS/闂撮殧锛?鈹?  鈹溾攢鈹€ key_listener.py      # 鐑敭鐩戝惉锛堟帹鏂級
鈹?  鈹溾攢鈹€ screen_capture.py    # dxcam/mss 鎴浘锛堟帹鏂級
鈹?  鈹溾攢鈹€ auto_fire.py         # 鑷姩寮€鐏紙宸叉悂缃紝鍗犱綅锛?鈹?  鈹斺攢鈹€ 鍩虹璁炬柦锛歱ath/logging/language/session/roboflow/updater
鈹溾攢鈹€ win_utils/               # 杈撳嚭閫氶亾鍖咃紙13 瀛愭ā鍧楋級
鈹?  鈹溾攢鈹€ mouse_move.py        # 鏂规硶鍒嗗彂鍣紙ddxoft/win32/xbox/arduino/makcu锛?鈹?  鈹溾攢鈹€ ddxoft_mouse.py      # DD_movR 椹卞姩杈撳嚭锛堣繍琛屾椂纭锛夆渽
鈹?  鈹溾攢鈹€ xbox_controller.py   # 鎵嬫焺鏄犲皠锛堟帹鏂紝寰呴獙璇侊級
鈹?  鈹溾攢鈹€ mouse_click.py / 鍏朵綑绯荤粺宸ュ叿
鈹斺攢鈹€ tests/                   # 鍗曞厓娴嬭瘯锛?/6 閫氳繃锛?```

## 楠岃瘉鐘舵€?
| 鐘舵€?| 鍐呭 |
|---|---|
| 鉁?宸查獙璇?| PIDController.update锛?032/2032锛夈€乧alculate_aim_target锛?086+锛夈€乮s_head_class銆乸rocess_aiming 鐘舵€佹満銆丏D_movR 杈撳嚭閫氶亾 |
| 馃敹 璇箟鎺ㄦ柇 | smart_tracker銆乲ey_listener銆乻creen_capture銆亁box 鏄犲皠銆乊OLO 瑙ｇ爜 |
| 鈴?寰呭姩鎬侀獙璇?| 璐濆灏旀搷浣滄暟銆佽拷韪櫒绮剧‘鍏紡銆乢calculate_adjusted_kp銆亁box銆乊OLO 瑙ｇ爜缁嗚妭 |
| 鉀?鍒绘剰鐪佺暐 | 鏈哄櫒璁稿彲鏍￠獙銆佹洿鏂般€佸弽浣滃紛瑙勯伩锛坰poofer 绛夛級 |

## 杩愯

```bash
# 鐜锛歅ython 3.12锛屼緷璧栬 requirements.txt锛堝惈 CUDA 鍔犻€熶笌閲嶅缓璇存槑锛?python -m unittest discover -s tests          # 杩愯娴嬭瘯
python -m pip install -r requirements.txt     # 閲嶅缓渚濊禆锛堟竻鍗庨暅鍍忓姞 -i https://pypi.tuna.tsinghua.edu.cn/simple锛?```

绋嬪簭鍏ュ彛锛坢ain.py锛変笌 GUI 鍦ㄥ姩鎬侀獙璇佹敹鍙ｅ悗娣诲姞銆?鏈湴宓屽叆寮忕幆澧冧綅浜?`../tool/python312`锛堣嚜鍖呭惈锛屽凡閰嶇疆 CUDA 鍔犻€燂級銆?杩涘害璁板綍瑙?`docs/PROGRESS.md`銆?
## 鍔ㄦ€侀獙璇?
`../analysis/frida/capture_all.py` 涓€娆′細璇濇敹闆嗭細
璐濆灏?6 涓皟鐢ㄧ偣瀵勫瓨鍣ㄥ€笺€丼martTracker 鏂规硶銆佸姩鎬丳銆佷富寰幆鑺傛媿銆佽緭鍑洪€氶亾銆?
