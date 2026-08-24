---
---

# 椤圭洰杩涘害璁板綍

> 鏈€杩戞洿鏂帮細2026-08-06锛堣繍琛岀幆澧?+ CUDA 鍔犻€熸敹鍙ｏ級

## 2026-08-07锛氱鍒扮瀹炴満楠岃瘉鏀跺彛

### 鏈鎴愭灉
- 瀹炴満鍏ㄩ摼璺窇閫氾細dxcam锛堢嫭鏄剧洿杩烇級鈫?512 妯″瀷锛圕UDA锛夆啋 鐬勫噯 鈫?ddxoft锛岄澏鍦烘甯搁攣浜猴紱娴嬭瘯妯″紡 5s 婊℃€ц兘 / 1s 寰幆閲囬泦钀藉湴銆?- 淇娓呭崟锛堝惈璇佹嵁锛夛細
  - v11 妯″瀷 cxcywh鈫抶yxy 杞崲锛堟ā鍨嬭緭鍑哄竷灞€缁熻锛氫粎 4.9% 婊¤冻 xyxy锛屽疄閿や腑蹇冪偣+瀹介珮锛?  - NMS 鍘婚噸婕忔帴锛堝師鐗?Frida 瀹為噰姣忓抚鍗曟锛屾湰鐗堟瘡甯?15 妗嗭級
  - DPI 鎰熺煡缂哄け锛圙etSystemMetrics 1536x864 vs 瀹為檯 1920x1080锛?  - ddxoft 鎯版€у垵濮嬪寲锛圖D_btn 绌蜂妇纭锛?  - 娴嬭瘯濂椾欢鎸傝捣锛坱est_build_loop 鏈?mock 椹卞姩鍒濆鍖栵級
  - 妯″瀷姣忕閲嶈浇 bug锛坰wap_model_if_changed 璺緞姣旇緝閿欒 鈫?鎺ㄧ悊 p90 灏栧嘲 333ms锛屽凡淇骞堕獙璇佷笉鍐嶉噸杞斤級
- 鐮旂┒缁撹锛?  - dxcam 鍦ㄦ贩鍚堟樉鍗＄瑪璁版湰 Optimus 妯″紡涓嬪鐙樉璋冩闈㈠鍒跺繀澶辫触锛堝井杞枃妗ｈ璁￠檺鍒讹級锛涚嫭鏄剧洿杩炲彲澶嶆椿锛涘師鐗堝湪鏈満瀹為檯闈?mss 鍏滃簳銆?  - bezier_curve_steps 缁?Frida 鎺㈡祴锛?771 娆″睘鎬ц鍙栵級纭鍘熺増鐬勫噯鐑矾寰勪粠涓嶈鍙栵紝灞?UI 鍗犱綅锛岄噸鏋勭増淇濇寔涓嶇敓鏁堛€?  - 鍔ㄦ€侀鍒ゆ粸鍚庝负鍙傛暟闂锛堥鍒ゆ椂闂?骞虫粦/寤惰繜琛ュ伩锛夛紝闈炰唬鐮佺己闄凤紱寤惰繜琛ュ伩鍒椾负鍚庣画璋冧紭鐐广€?
### 寰呭姙鏇存柊锛?026-08-07 澶嶆牳锛?| 浼樺厛绾?| 鍐呭 |
|---|---|
| 楂?| GUI锛圥yQt6锛?|
| 楂?| 浼樺寲椤?1/2 瀹炵幇锛堣嚜閫傚簲甯х巼 + 鍔ㄦ€侀鍒や笌澧炲己鐬勫噯锛岃璁″凡纭锛?|
| 涓?| 浼樺寲椤?3~8锛堝尯鍩熺洿浼?/ 妯″瀷妗ｄ綅 / 璐濆灏?/ 姝诲尯閰嶇疆鍖?/ 鍔ㄦ€丳 鐮旂┒ / 鎴浘鑷剤锛?|
| 涓?| 娴佹按绾垮苟琛岋紙鍘熼樁娈?3锛屽疄楠岄」锛?|
| 浣?| xbox 鍝嶅簲鏄犲皠銆乤uto_fire锛堟悂缃級 |
| 鎵╁睍 | TensorRT锛團P32锛夈€乄GC 鎴浘閫氶亾锛圤ptimus 鍏煎鐨勫仴澹€х己鍙ｏ級 |

## 涓€銆佹€讳綋鐘舵€?
| 闃舵 | 鐘舵€?|
|---|---|
| 閫嗗悜鍒嗘瀽锛圢uitka 纭 / Ghidra 瀹氫綅锛?| 鉁?|
| 闈欐€佽繕鍘燂紙core / win_utils / telemetry / tests锛?| 鉁?涓讳綋瀹屾垚 |
| 鍔ㄦ€侀獙璇侊紙Frida + 闈跺満锛?| 馃敹 鏍稿績宸查獙璇侊紝缁嗚妭寰呰ˉ |
| 浠ｇ爜浼樺寲锛堥樁娈?1锛?| 鉁?|
| 杩愯鐜锛堝祵鍏ュ紡 3.12 + CUDA锛?| 鉁?鏈鏀跺彛 |
| GUI锛圥yQt6锛?| 鈴?寰呭仛 |

## 浜屻€佸凡瀹屾垚

### 閫嗗悜鍒嗘瀽
- 纭 ZoomPlus.exe 涓?Nuitka 鎵撳寘鐨?Python 搴旂敤锛汫hidra 12.1.2 headless 瀹屾垚鍏ㄩ噺鍒嗘瀽
- 瀛楃涓?寮曠敤瀹氫綅鍒?`core.ai_aiming`銆乣process_aiming` 绛夋牳蹇冨嚱鏁?
### 闈欐€佽繕鍘?- `core/`锛歝onfig锛?5 瀛楁锛夈€乧onfig_manager銆乮nference锛圥IDController + YOLO 鎺ㄧ悊绠＄嚎锛夈€?  ai_aiming銆乻mart_tracker銆乤i_loop锛?state/utils锛夈€乲ey_listener銆乻creen_capture銆?  auto_fire锛堝崰浣嶏級銆佸熀纭€璁炬柦锛坧ath/logging/language/session/roboflow/updater锛?- `win_utils/`锛?3 涓緭鍑洪€氶亾瀛愭ā鍧楋紙ddxoft / win32 / xbox / arduino / makcu锛?- `telemetry/`锛歵racer锛堢幆缂撳啿 + JSONL锛? dry_run锛堟祴璇曟ā寮忥紝涓嶇湡鍔ㄩ紶鏍囷級
- `tests/`锛氬崟鍏冩祴璇?6/6 閫氳繃

### 鍔ㄦ€侀獙璇侊紙Frida + 闈跺満瀹炴祴锛?- 宸查獙璇侊細PIDController.update锛?032/2032锛夈€乧alculate_aim_target锛?086+锛夈€?  is_head_class銆乸rocess_aiming 鐘舵€佹満銆丏D_movR 杈撳嚭閫氶亾銆佽礉濉炲皵鏇茬嚎
- 宸查噰闆嗭細鍔ㄦ€?P銆丼martTracker 鍐呴儴鍊笺€佷富寰幆鑺傛媿銆佽緭鍑洪€氶亾锛坈apture_all.py锛?
### 浠ｇ爜浼樺寲锛堥樁娈?1锛岃瑙?optimization_plan.md锛?- EP 鑷姩閫夋嫨锛圕UDA鈫扗ML鈫扖PU锛孎P32 涓嶉檷绮惧害锛夈€佷細璇濅紭鍖栥€佸紶閲忓鐢ㄣ€?  screen 灏哄缂撳瓨銆侀仴娴?骞茶窇鍏ュ彛銆侀珮绮惧害闄愬抚

### 杩愯鐜锛堟湰娆★級
- 宓屽叆寮?Python 3.12.4 鈫?`../tool/python312`锛堣嚜鍖呭惈锛屽彲鏁翠綋甯﹁蛋锛?- 鏂规 C 绮剧畝锛?0.3 GB 鈫?3.1 GB锛屼粎淇濈暀椤圭洰渚濊禆锛堝師 ~orch 绛?4.3 GB 鍨冨溇宸叉竻锛?- CUDA 鍔犻€燂細onnxruntime-gpu 1.20.2 + CUDA 12.9 + cuDNN 9.24
  - 瀹炴祴锛欳UDA ~3.1 ms/甯?vs CPU ~10.6 ms/甯э紙绾?3.4x锛?  - DLL 鍏ㄩ儴閮ㄧ讲鍦?python312 鏍圭洰褰曪紝涓嶄緷璧栫郴缁熷畨瑁?- 渚濊禆娓呭崟锛歚../requirements.txt`锛堝惈閲嶅缓/澶嶇幇璇存槑锛?- 绯荤粺娓呯悊锛歅ython 3.14.3 娈嬬暀娉ㄥ唽璁板綍娓呴櫎锛涘師 Python312 鐩綍鍨冨溇娓呴櫎

### 绔埌绔啋鐑燂紙鏈锛?-test 骞茶窇锛?- `main.py --test` 绋冲畾杩愯鏃犳姤閿欙紙鎴浘/寰幆/鐢熷懡鍛ㄦ湡姝ｅ父锛?- 淇涓夊闂锛?  - `AILoop.start()` 缂哄け 鈫?琛ュ悗鍙扮嚎绋嬪惎鍔紙main.py 鐢熷懡鍛ㄦ湡瀵归綈锛?  - CUDA DLL 鍔犺浇澶辫触閫€鍥?CPU 鈫?`path_utils` 鍚姩鏃堕鍔犺浇 CUDA/cuDNN
    鏍稿績搴擄紙瀹炴祴蹇呰锛宍add_dll_directory` 瀵?ORT 鏃犳晥锛?  - mss 鍏滃簳鎴浘杩斿洖 PIL 鍥惧儚瀵艰嚧 cv2 鎶ラ敊 鈫?杞?numpy BGR锛堜笌 dxcam 涓€鑷达級
  - ddxoft 鏈垵濮嬪寲 鈫?`ai_loop` 鍛ㄦ湡妫€鏌ユ椂鎺ュ叆 `ensure_ddxoft_ready()`
    锛坉d63330.dll 瑕佹眰**绠＄悊鍛樻潈闄?*锛岄潪鎻愭潈浼氬脊 "Run as Administrator"锛?- 闆嗘垚楠岃瘉锛氶厤缃姞杞?鈫?CUDA 浼氳瘽锛坅pex_v5_320_best.onnx锛夆啋 鎺ㄧ悊 鈫?鍚庡鐞?鍏ㄩ摼璺€氳繃

## 涓夈€佸緟鍔?
| 浼樺厛绾?| 鍐呭 |
|---|---|
| 楂?| GUI锛圥yQt6锛屽師鐗堝甫 Qt6 鍏ㄥ锛涘悗绔敹鍙ｅ悗鍋氾級 |
| 涓?| 闃舵 2锛氳拷韪櫒 alpha 绮剧‘鎷熷悎 + 寤惰繜琛ュ伩 |
| 涓?| 闃舵 3锛氭祦姘寸嚎骞惰瀹為獙 + 鏁版嵁鍒嗘瀽鑴氭湰 |
| 浣?| 闃舵 4锛氬姩鎬?P 澶ц宸鍏紡銆亁box 鍝嶅簲鏇茬嚎 |
| 浣?| auto_fire锛堟悂缃紝鍗犱綅锛?|
| 鎵╁睍 | TensorRT锛堜粎 FP32锛孋UDA 涓嶅蹇啀涓婏級 |

## 鍥涖€佺幆澧冨熀绾?
- 纭欢锛歂VIDIA GeForce RTX 4050 Laptop GPU锛? GB锛孋ompute Capability 8.9锛岄┍鍔?596.08
- 杩愯鏃讹細`../tool/python312`锛圥ython 3.12.4锛屽祵鍏ュ紡锛?- 鎺ㄧ悊锛歰nnxruntime-gpu 1.20.2锛孋UDAExecutionProvider锛圕UDA鈫扗ML鈫扖PU 鑷姩閫夋嫨锛?- 闀滃儚锛氭竻鍗?PyPI锛坄https://pypi.tuna.tsinghua.edu.cn/simple`锛岄亣浠ｇ悊鎶ラ敊鍏堟竻浠ｇ悊鐜鍙橀噺锛?
## 浜斻€佸喅绛栬褰曡鐐?
- 閫嗙紪璇戜骇鐗╀负**琛屼负绛変环**锛岄潪婧愮爜绛変环锛涙牳蹇冨叕寮忎互鍔ㄦ€侀獙璇佷负鍑?- 绗笁鏂瑰紑婧愬寘涓嶉€嗗悜锛岀洿鎺ュ畼鏂逛笅杞斤紙cv2 / dxcam / mss / vgamepad / comtypes 绛夛級
- 妯″瀷绮惧害涓嶅Ε鍗忥紙鍚︽帀 FP16 / INT8锛?- 鎺ㄧ悊鍚庣閫?CUDA锛堣拷姹傛瀬闄愭€ц兘锛夛紱鍘熺増璧?DML锛孋UDA 涓哄叾鍗囩骇璺緞
- 闅愯棌鍔熻兘锛堢鍚?/ xbox 鏄犲皠锛変笉娣辨寲锛屾渶鍚庡仛

