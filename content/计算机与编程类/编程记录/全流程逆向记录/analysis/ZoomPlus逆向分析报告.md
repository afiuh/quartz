---
---

# ZoomPlus.exe 閫嗗悜鍒嗘瀽鎶ュ憡

鍒嗘瀽瀵硅薄锛歚閫嗗悜涓荤▼搴?ZoomPlus.exe`锛?3,956,608 瀛楄妭锛?鍒嗘瀽鏂规硶锛歅E 缁撴瀯鍒嗘瀽銆佸鍏ヨ〃鍒嗘瀽銆佸叏閲忓瓧绗︿覆鎻愬彇銆丯uitka 妯″潡鍏冩暟鎹噸寤?鍒嗘瀽鏃ユ湡锛?026-08-05

## 0. 缁撹鎽樿

1. **鎵撳寘鏂瑰紡**锛歂uitka standalone锛圥ython 3.12.7 鈫?C 鈫?MSVC 19.51 LTCG 缂栬瘧锛夛紝**涓嶆槸 PyInstaller**锛屽洜姝?pyinstxtractor-ng 鏃犳硶瑙ｆ瀽銆?2. **鏃犲３**锛欴IE 鐨?".rsrc 鍘嬬缉" 涓?"Rust" 鍧囦负鍚彂寮忚鎶ワ紱瀵煎叆琛ㄩ潤鎬佷緷璧?`python312.dll`锛岀鍚?Nuitka 浜х墿鐗瑰緛銆?3. **绋嬪簭鎬ц川**锛氬晢涓氬寲鐨?AI 榧犳爣瀹?鐬勫噯杈呭姪锛坅imbot锛夛紝闈㈠悜 Apex/CS2/OW2/褰╄櫣鍏彿/杩滃厜84 绛?FPS 娓告垙锛屽唴缃睆骞曟崟鑾?+ ONNX 鐩爣妫€娴?+ PID/杩借釜鍣ㄧ瀯鍑?+ 鑷姩寮€鐏?+ 澶氱‖浠惰緭鍑洪€氶亾銆?4. **鍏抽敭瀵规姉鐗规€?*锛氱‖浠舵寚绾归噰闆嗐€佸弽浣滃紛杩涚▼妫€娴嬨€丄rduino 浼鎴愮綏鎶€榧犳爣銆乂iGEmBus 铏氭嫙鎵嬫焺銆丠VCI 妫€娴嬨€丟itHub 鏇存柊鍣ㄣ€?5. **鏈彂鐜?*锛氭湰浜岃繘鍒跺唴娌℃湁鍗″瘑/鎺堟潈鏈嶅姟鍣ㄤ氦浜掗€昏緫锛涙満鍣ㄧ爜浠呯敤浜庡惎鍔ㄨ瘖鏂棩蹇楄緭鍑恒€?
## 1. 浜岃繘鍒惰韩浠?
| 椤圭洰 | 鍊?|
|---|---|
| PE 鏋舵瀯 | x64 (0x8664) |
| 鑺傚尯 | .text / .rdata / .data / .pdata / .rsrc / .reloc锛? 鑺傦紝鏃犲紓甯歌妭鍖哄悕锛?|
| 瀵煎叆琛?| KERNEL32銆乂CRUNTIME140銆乤pi-ms-win-crt-*銆?*python312.dll锛堥潤鎬佸鍏ワ級** |
| DIE 妫€娴?| MSVC 19.51 LTCG锛汻ust/.rsrc 鍘嬬缉鍧囦负璇姤 |
| 鐗堟湰璧勬簮 | ZoomPlus 1.0.0.0 |
| Python | 3.12.7 (tags/v3.12.7:0b05ead) |
| Nuitka 鐗瑰緛 | 280+ 澶?`__nuitka_*` / `NUITKA_PACKAGE_*` 瀛楃涓诧紝鏃?PyInstaller COOKIE/PYZ |

## 2. 缂栬瘧杩?exe 鐨勫簲鐢ㄦ簮鐮佹枃浠讹紙妯″潡娓呭崟锛?
```
main.py                      # 绋嬪簭鍏ュ彛涓庡惎鍔ㄩ€昏緫
core\__init__.py
core\ai_aiming.py            # 鐬勫噯璁＄畻锛堝ご閮ㄧ被銆佺鍚搞€丳ID+杩借釜+璐濆灏旂绾匡級
core\ai_loop.py              # AI 涓诲惊鐜紙鎹曡幏/鎺ㄧ悊/鍙戝竷绾跨▼绠＄悊锛?core\ai_loop_state.py        # LoopState 鏁版嵁绫?core\ai_loop_utils.py        # 鍑嗘槦/妫€娴嬪尯鍩?闃熷垪宸ュ叿
core\auto_fire.py            # 鑷姩寮€鐏惊鐜?core\config.py               # 閰嶇疆绫伙紙绫诲瀷瀹夊叏 JSON锛?core\config_manager.py       # 棰勮閰嶇疆绠＄悊锛堝鍒犳敼瀵煎叆瀵煎嚭锛?core\inference.py            # ONNX 棰勫鐞?鍚庡鐞?+ PID 鎺у埗鍣?core\key_listener.py         # 鐑敭鐩戝惉
core\language_manager.py     # 璇█
core\logging_config.py       # 鏃ュ織/宕╂簝閽╁瓙/鍚姩璇婃柇/鏈哄櫒鐮?core\path_utils.py           # 璺緞瑙ｆ瀽
core\roboflow_utils.py       # Roboflow 浜戞帹鐞嗛€傞厤
core\screen_capture.py       # dxcam/MSS 鎹曡幏
core\session_utils.py        # ONNX 浼氳瘽浼樺寲/璁惧閫夋嫨/棰勭儹
core\smart_tracker.py        # 鐩爣杩愬姩棰勬祴杩借釜
core\updater.py              # GitHub 鏇存柊妫€鏌?gui\disclaimer_dialog.py     # 鍏嶈矗澹版槑
gui\overlay.py               # 灞忓箷瑕嗙洊灞?gui\fluent_app\*             # PyQt-Fluent-Widgets 鐣岄潰锛坵indow/setup_wizard/base_page/pages\aim|configs|keys|trigger|visuals/theme_*锛?win_utils\admin.py           # 绠＄悊鍛樻潈闄?win_utils\console.py         # 鎺у埗鍙版樉绀?闅愯棌
win_utils\key_utils.py       # 鎸夐敭妫€娴?win_utils\vk_codes.py        # 铏氭嫙閿爜
win_utils\mouse_move.py      # SendInput / mouse_event 绉诲姩
win_utils\mouse_click.py     # 鐐瑰嚮锛坰endinput/hardware/mouse_event/ddxoft锛?win_utils\ddxoft_mouse.py    # DDXoft 榧犳爣妯℃嫙
win_utils\arduino_mouse.py   # Arduino Leonardo USB HID 榧犳爣
win_utils\arduino_spoofer.py # 浼 Arduino 涓虹綏鎶€ G502
win_utils\makcu_mouse.py     # MAKCU KM Host 纭欢榧犳爣
win_utils\xbox_controller.py # ViGEmBus 铏氭嫙 Xbox 鎵嬫焺 + 鍙嶄綔寮婃娴?win_utils\xinput_handler.py  # 瀹炰綋鎵嬫焺璇诲彇
win_utils\gamepad_input.py   # XInput 鎽囨潌/姝诲尯澶勭悊
win_utils\priority.py        # 绾跨▼/杩涚▼浼樺厛绾?```

## 3. 鎬讳綋鏁版嵁娴?
```
灞忓箷鎹曡幏 (dxcam DXGI / MSS)
   鈹? BGR 甯?   鈻?AI 鎺ㄧ悊 (ONNX Runtime DirectML/CPU锛屾垨 Roboflow 浜?
   鈹? boxes / confidences / class_ids
   鈻?鍚庡鐞?(YOLOv5/v8 鏍煎紡妫€娴嬨€丯MS銆丗OV/绫诲埆杩囨护)
   鈹?   鈻?鐩爣閫夋嫨 鈫?PID 鎺у埗鍣?+ SmartTracker 棰勬祴 + 璐濆灏斿钩婊?+ 纾佸惛
   鈹? move_x / move_y
   鈻?杈撳嚭璁惧锛堟寜閰嶇疆閫夋嫨锛夛細
   Xbox 铏氭嫙鎵嬫焺 (ViGEmBus锛岄粯璁? / DDXoft / SendInput /
   mouse_event / Arduino Leonardo / MAKCU 纭欢榧犳爣
   鈹?   鈹溾攢 鑷姩寮€鐏嚎绋嬶紙鐙珛锛屾寜閿Е鍙?+ 鍛戒腑鍒ゅ畾 + 瀹氭椂鐐瑰嚮锛?   鈹斺攢 瑕嗙洊灞?(PyQtOverlay) 缁樺埗妗?FPS 闈㈡澘
```

## 4. 鏍稿績妯″潡璇﹁В

### 4.1 鍏ュ彛 main.py
- DPI 鎰熺煡璁剧疆锛圫etProcessDpiAwarenessContext / SetProcessDPIAware锛夈€?- 棰勫姞杞?pywin32 DLL锛坄python\dependencies\win32\lib` 涓嬬殑 pywintypes/pythoncom锛夈€?- 鍒濆鍖栨棩蹇?鈫?鍔犺浇閰嶇疆 鈫?绠＄悊鍛樻鏌?鈫?杩涚▼浼樺厛绾?鈫?HVCI 妫€鏌?鈫?DDXoft 灏辩华妫€鏌ャ€?- 棣栨杩愯寮瑰厤璐ｅ０鏄?璁剧疆鍚戝锛涢殢鍚庡垱寤鸿鐩栧眰涓庝富绐楀彛銆?- 鍚姩 5 涓嚎绋嬶細`ai_logic_loop`銆乣auto_fire_loop`銆乣aim_toggle_key_listener`銆乣window_toggle_key_listener`銆乣lock_category_key_listener`銆?- ONNX 妯″瀷鍏冩暟鎹彁鍙栫被鍒悕锛堟敮鎸?JSON / Python repr / 鎹㈣涓夌 `names` 鏍煎紡锛夛紝鎴栧洖閫€ Roboflow 浜戞帹鐞嗐€?
### 4.2 core.logging_config 鈥?鍚姩璇婃柇涓庢満鍣ㄧ爜
- 鐢?PowerShell 璋?`Get-CimInstance` 閲囬泦 7 绫荤‖浠朵俊鎭細
  - Win32_Processor锛堝惈 ProcessorId锛夈€乄in32_BaseBoard锛圫erialNumber锛夈€乄in32_BIOS锛圫erialNumber锛夈€乄in32_ComputerSystemProduct锛圲UID锛夈€乄in32_VideoController銆乄in32_PhysicalMemory銆乄in32_OperatingSystem銆?- `machine_code` = 瀵?`hostname + mac_node + processor_id + baseboard_serial + computer_uuid + bios_serial` 鍙?**SHA256 hexdigest**銆?- 鍚姩鏃朵互 JSON 褰㈠紡鍐欏叆 `zoomplus_crash.log`锛堜笌瀹炴祴鏃ュ織瀹屽叏鍚诲悎锛夈€?- 鍙﹀惈宕╂簝閽╁瓙锛氫富绾跨▼/宸ヤ綔绾跨▼鏈崟鑾峰紓甯搞€乫aulthandler銆丵t 娑堟伅閲嶅畾鍚戙€佸叏绾跨▼鍫嗘爤杞偍銆?
### 4.3 core.ai_loop 鈥?涓诲惊鐜?- `_PreprocessCache`锛欱GRA鈫払GR銆佺洿鎺?resize 涓?YOLOv5 letterbox锛堢伆鑹?114 濉厖锛変袱绉嶉澶勭悊銆?- 鎹曡幏宸ヤ綔绾跨▼锛歞xcam DXGI video_mode锛堥珮甯х巼銆佸尯鍩熸崟鑾枫€佺幆褰㈠抚缂撳啿锛夛紝澶辫触鑷姩鍥為€€ MSS銆?- 宸﹀彸鎽囨潌鐩撮€氱嚎绋嬨€丄I 瑕嗙洊灞傝緭鍑虹嚎绋嬶紙500Hz 瑙ｈ€︼級銆?- 妯″瀷鐑垏鎹細妫€娴?model_path 鍙樺寲 鈫?閲嶅缓 ONNX 浼氳瘽锛堣緭鍏ュ昂瀵稿彉鍖栨椂鑱斿姩棰勫鐞嗙紦瀛橈級銆?- 寤惰繜缁熻锛欵MA 鍒嗛樁娈电粺璁?capture/pre/inf/post锛岄珮绮惧害瀹氭椂鍣?+ FPS 涓婇檺銆?
### 4.4 core.inference 鈥?鎺ㄧ悊涓?PID
- YOLOv5/v8 杈撳嚭鏍煎紡鑷姩鍒ゅ埆锛堟寜缁村害褰㈢姸鍚彂寮忥級銆?- YOLOv5 letterbox 鍙傝€?Matias Kovero 浠撳簱锛涘潗鏍囪浆鎹€乷bjectness脳class 缃俊搴︺€丯MS銆?- `PIDController`锛氳宸鍖恒€佺Н鍒嗛檺骞呫€佸井鍒嗕綆閫氥€佸姩鎬?P 澧炵泭锛?~50% 绾挎€с€?0~100% 鍔犻€熻嚦 200%锛夈€?
### 4.5 core.ai_aiming 鈥?鐬勫噯绠＄嚎
- `_HEAD_CLASS_KEYWORDS`锛歨ead / enemyHead / enemy_head / ct_head / t_head銆?- 鐬勫噯鐐癸細澶撮儴绫荤洿鎺ュ彇妗嗕腑蹇冿紝鍏朵綑鎸?`aim_y_offset_ratio`锛?=椤讹紝0.5=涓紝1=搴曪級鍙栧€笺€?- `calculate_sticky_pull`锛氱鍚稿悜閲忥紝闈犺繎鐩爣妗嗘椂寮恒€佸悜 FOV 杈圭紭琛板噺銆?- `process_aiming`锛氱被鍒繃婊?鈫?鏈€杩戠洰鏍囨帓搴?鈫?PID 鈫?SmartTracker 棰勬祴锛堟姈鍔ㄥ钩婊?鎬ュ仠娓呴浂/浣嶇疆姝诲尯锛夆啋 璐濆灏旀洸绾垮钩婊?鈫?鍙嶈壊/鎽囨潌鏄犲皠 鈫?鍙戦€佺Щ鍔ㄣ€?
### 4.6 core.auto_fire 鈥?鑷姩寮€鐏?- 鐙珛瀹堟姢绾跨▼锛氱洃鍚紑鐏敭锛堝弻閿厤缃級鎴栧父寮€妯″紡銆?- 浠庢娴嬮槦鍒楀彇妗?鈫?璁＄畻鐬勫噯鐐?鈫?鍒ゅ畾鍑嗘槦鏄惁鍦ㄧ洰鏍囪寖鍥村唴 鈫?鎸?`aim_part`锛坔ead/body/both锛夎Е鍙戠偣鍑汇€?- 鏀寔 `auto_fire_delay`銆乣auto_fire_interval`銆佹鏇存柊闂撮殧锛涚偣鍑昏蛋 `mouse_click_method` 閫氶亾銆?
### 4.7 core.updater 鈥?鏇存柊鍣?- `https://api.github.com/repos/` + `REPO_OWNER` + `/` + `REPO_NAME` + `/releases/latest`銆?- **REPO_OWNER = `iishong0w0`锛孯EPO_NAME = `ZoomPlus-AI-Aimbot`**锛沀ser-Agent = `ZoomPlus-AI-Aimbot/<__version__>`銆?- 瑙ｆ瀽 tag锛坄'v1.0.2' -> (1,0,2)` 寮忥級锛屽彂 `update_available/up_to_date/check_failed` 淇″彿锛屾祻瑙堝櫒鎵撳紑鏇存柊椤点€?- 璇ヤ粨搴撳綋鍓嶈繑鍥?404锛堢鏈?宸插垹闄?浠庢湭鍏紑锛夈€?
### 4.8 core.roboflow_utils 鈥?浜戞帹鐞?- `RoboflowInferenceAdapter`锛氬抚鍐欎复鏃舵枃浠?鈫?`model.predict()` 浜戞帹鐞嗭紙浣滆€呮敞鏄庡崟娆″線杩?200~800ms锛夆啋 杞崲 boxes/confidences/class_ids銆?- 鍐呯疆棰勮锛歚MatiasKovero`锛坋nemy锛夈€乣CSGO_4Class`锛坈t_body/ct_head/t_body/t_head锛夌瓑锛沗download_roboflow_model` 鏀寔浠?Roboflow 涓嬭浇 ONNX銆?- 閰嶇疆榛樿 workspace=`fortnite-ai-aim`銆乸roject=`cod-mw-warzone-catlb`銆?
### 4.9 win_utils 鈥?杈撳叆杈撳嚭涓庡鎶?- **xbox_controller锛堥粯璁よ緭鍑猴級**锛歏iGEmBus 铏氭嫙 Xbox 360 鎵嬫焺锛屽彸鎽囨潌鏄犲皠瑙嗚锛涘惈鐏垫晱搴?姝诲尯銆佺粺璁°€佽瘖鏂€佽櫄鎷熸Ы浣嶅啿绐佹娴嬨€?- **鍙嶄綔寮婃娴?*锛堣繘绋嬪悕鏋氫妇锛夛細
  - vgc.exe / vgtray.exe 鈫?Vanguard锛圧iot/Valorant锛?  - easyanticheat.exe / eac_launcher.exe 鈫?Easy Anti-Cheat
  - beclient.dll / beservice.exe / bedaisy.sys 鈫?BattlEye
  - atvi-ricochet.exe 鈫?Ricochet锛圕OD锛?  - nprotect.exe / gameguard.des 鈫?GameGuard
  - xigncode.exe 鈫?XIGNCODE3锛泆ncheater.exe 鈫?Uncheater锛沠aceit.exe / faceitclient.exe 鈫?FACEIT
- **arduino_spoofer**锛氭敼鍐?Arduino IDE 鐨?`boards.txt`锛堣嚜鍔ㄥ浠?.bak锛夛紝鎶?Leonardo 鐨?VID/PID/浜у搧鍚嶆敼涓?**Logitech G502 HERO Gaming Mouse锛?x046D / 0xC07D锛?*锛屼娇鏋氫妇缁撴灉闅愯棌涓虹湡瀹為紶鏍囷紱闄勯獙璇佸嚱鏁般€?- **ddxoft_mouse**锛欴DXoft 椹卞姩榧犳爣妯℃嫙锛屽甫 HVCI锛堝唴瀛樺畬鏁存€э級妫€娴嬩笌绂佺敤鎻愮ず銆?- **makcu_mouse**锛歁AKCU KM Host 纭欢閫氶亾锛堝畼鏂?API 鏂囨。锛歨ttps://www.makcu.com/cn/api锛夈€?- **gamepad_input/xinput_handler**锛氬疄浣?XInput 鎵嬫焺璇诲彇锛屽緞鍚戞鍖猴紝鎸夐敭涓婂崌娌夸簨浠躲€?
### 4.10 GUI锛圥yQt-Fluent-Widgets锛?- 椤甸潰锛歛im / configs / keys / trigger / visuals锛泂etup_wizard銆乼heme_manager銆乷verlay銆?- 瑕嗙洊灞傦細妫€娴嬫銆丗PS 鐘舵€侀潰鏉裤€丗OV 鍦堢瓑锛堥粯璁ゅ叏閮ㄥ叧闂紝浠呯姸鎬侀潰鏉垮紑锛夈€?
## 5. 瀵规姉/闅愯斀鐗规€ф眹鎬?
1. 纭欢鎸囩汗閲囬泦锛圕IM + SHA256 鏈哄櫒鐮侊級鈥斺€旂敤浜庢縺娲荤粦瀹?椋庢帶锛堟湰鏋勫缓浠呮棩蹇楄緭鍑猴級銆?2. 鍙嶄綔寮婅繘绋嬫娴嬶紙14 椤癸紝瑕嗙洊涓绘祦鍙嶄綔寮婏級銆?3. Arduino Leonardo 浼缃楁妧 G502鈥斺€旂‖浠?HID 绾ч紶鏍囩Щ鍔紝瑙勯伩杞欢灞傞紶鏍?API 妫€娴嬨€?4. ViGEmBus 铏氭嫙鎵嬫焺鈥斺€旀墜鏌勮緭鍏ヨ矾寰勶紝瑙勯伩榧犳爣杈撳叆鐩戞帶銆?5. HVCI 妫€娴嬧€斺€擠DXoft 椹卞姩涓嶅彲鐢ㄦ椂鐨勯檷绾ф彁绀恒€?6. 楂樼簿搴﹀畾鏃跺櫒銆佸绾跨▼瑙ｈ€︺€丒MA 寤惰繜缁熻鈥斺€旀€ц兘/闅愯斀鍏奸【銆?7. 鍚庡彴 GitHub 鏇存柊妫€鏌モ€斺€斿彲鎸佺画鎺ㄩ€佹柊鐗堟湰銆?
## 6. 鍒嗘瀽浜х墿锛坅nalysis/ 鐩綍锛?
- `strings_ascii.txt` / `strings_utf16.txt`锛氬叏閲忓瓧绗︿覆锛?7.9 涓囨潯 ASCII锛夈€?- `strings_cjk.txt`锛歎TF-8 涓枃涓诧紙9486 鏉★紝鐣岄潰鏂囨浠ョ箒浣撲负涓伙級銆?- `cat_*.txt`锛歎RL / 婧愮爜璺緞 / Nuitka / 鏈哄櫒鐮?/ 缃戠粶 / Roboflow / 杈撳叆杈撳嚭 鍒嗙被銆?- `modules/`锛氭瘡涓簲鐢ㄦā鍧楃殑瀛楃涓蹭笂涓嬫枃瀵煎嚭锛堝惈鍋忕Щ锛夈€?
## 7. 鍚庣画寤鸿

1. **鍑芥暟绾ц繕鍘?*锛氳 Ghidra锛堟垨 radare2锛夛紝鐢?Nuitka 妯″潡鍏冩暟鎹?+ 瀛楃涓蹭氦鍙夊紩鐢ㄥ畾浣嶅悇妯″潡鍑芥暟锛涙湰鎶ュ憡宸茬粰鍑烘ā鍧楀悕銆佸嚱鏁板悕銆佸父閲忎笌婧愭枃浠惰矾寰勬槧灏勩€?2. **楠岃瘉鏈哄櫒鐮佺畻娉?*锛氭湰鏈鸿繍琛?exe 鍚庡姣旀棩蹇椾腑鐨?machine_code 涓?CIM 鍘熷鍊硷紝鍙‘璁ゅ搱甯岃緭鍏ラ『搴忋€?3. **鏇存柊鍣ㄥ垎鏋?*锛氭姄 `api.github.com/repos/iishong0w0/ZoomPlus-AI-Aimbot/releases/latest` 鐨勬祦閲忥紙鑻ヤ粨搴撳娲伙級銆?4. **妯″瀷鍒嗘瀽**锛歄NNX 妯″瀷鍙洿鎺ョ敤 netron/onnx 宸ュ叿鎵撳紑锛岀‘璁ょ被鍒畾涔変笌璁粌鏉ユ簮锛圷OLOv8锛夈€?5. **鍔ㄦ€佽涓?*锛氭矙绠卞唴杩愯 + Process Monitor/API Monitor 鎶撴敞鍐岃〃銆佹枃浠朵笌缃戠粶琛屼负锛岄獙璇侀潤鎬佺粨璁恒€?
