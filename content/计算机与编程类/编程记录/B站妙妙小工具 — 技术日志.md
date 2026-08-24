---
---

# B绔欏濡欏皬宸ュ叿 鈥?鎶€鏈棩蹇?
> 2026-07-28
> 璁板綍褰撳墠妗嗘灦鐘舵€併€佸凡鐭ラ棶棰樺拰鎶€鏈喅绛?
---

## 涓€銆佹鏋舵灦鏋?
### 鐩綍缁撴瀯

```
B绔欏伐鍏锋鏋?
鈹溾攢鈹€ __main__.py              # 鍏ュ彛锛歊EPL / _exec 鍐呴儴鍛戒护
鈹溾攢鈹€ start.bat                # 鍙屽嚮鍚姩 REPL
鈹溾攢鈹€ core/
鈹?  鈹溾攢鈹€ __init__.py           # 鐗堟湰鍙?鈹?  鈹溾攢鈹€ api.py                # B绔?API 宸ュ叿灞?鈹?  鈹溾攢鈹€ cache.py              # 閿欒鏃ュ織缂撳瓨绯荤粺
鈹?  鈹溾攢鈹€ cli.py                # 鍙傛暟瑙ｆ瀽鍣紙淇濈暀澶囩敤锛?鈹?  鈹溾攢鈹€ config.py             # 鍏ㄥ眬閰嶇疆锛坉ata_root, plugin_dir, cache_dir锛?鈹?  鈹溾攢鈹€ registry.py           # 鎻掍欢鍙戠幇涓庨噸杞?鈹?  鈹斺攢鈹€ repl.py               # REPL 涓诲惊鐜紙prompt_toolkit锛?鈹溾攢鈹€ plugins/
鈹?  鈹溾攢鈹€ demo/                 # 娴嬭瘯鎻掍欢
鈹?  鈹溾攢鈹€ transcribe/           # 杞枃瀛楁彃浠?鈹?  鈹?  鈹溾攢鈹€ __init__.py       # 涓婚€昏緫锛坋xecute + cli_run锛?鈹?  鈹?  鈹溾攢鈹€ audio_convert.py  # 闊抽鏍煎紡杞崲锛歭ibrosa 鈫?scipy 鈫?soundfile
鈹?  鈹?  鈹溾攢鈹€ audio.py          # whisper.cpp 杞綍锛堟祦寮?stdout锛?鈹?  鈹?  鈹溾攢鈹€ onnx_transcribe.py # ONNX Paraformer 杞綍锛堟祦寮忓瓙杩涚▼锛?鈹?  鈹?  鈹溾攢鈹€ subtitle.py       # CC 瀛楀箷鎻愬彇
鈹?  鈹?  鈹斺攢鈹€ onnx_transcribe.py
鈹?  鈹斺攢鈹€ transcribe/
鈹溾攢鈹€ scripts/
鈹?  鈹溾攢鈹€ export_paraformer_onnx.py  # 瀵煎嚭涓変釜 ONNX 妯″瀷
鈹?  鈹斺攢鈹€ onnx_infer.py              # ONNX 鎺ㄧ悊瀛愯繘绋?鈹斺攢鈹€ tests/
    鈹溾攢鈹€ test_cli.py           # CLI 鍙傛暟瑙ｆ瀽娴嬭瘯锛?0 涓級
    鈹溾攢鈹€ test_plugins.py       # 鎻掍欢鍙戠幇娴嬭瘯锛? 涓級
    鈹斺攢鈹€ test_transcribe.py    # 杞綍鍔熻兘娴嬭瘯锛?3 涓級
```

### 宸ヤ綔娴?
```
鐢ㄦ埛鍙屽嚮 start.bat
  鈫?REPL 鎸囨尌瀹樼獥鍙ｏ紙prompt_toolkit锛?  鈹?  鈹溾攢鈹€ list          鈫?鍒楀嚭鎻掍欢
  鈹溾攢鈹€ run <鎻掍欢>     鈫?寮规柊 cmd 绐楀彛锛圕REATE_NEW_CONSOLE锛?  鈹?                   鈫?  鈹?              _exec 鍐呴儴鍛戒护鍦ㄦ柊绐楀彛涓繍琛?  鈹?                   鈫?  鈹?              鎻掍欢 cli_run() 鈫?execute(params, emit)
  鈹?                   鈫?  鈹?              emit("log", ...) 鈫?绐楀彛鏄剧ず + 鍚屾椂鍐欏叆瀹炴椂琛?  鈹?              emit("progress", ...) 鈫?杩涘害鏉?  鈹?              raise RuntimeError 鈫?瑙﹀彂閿欒缂撳瓨鍐欏叆
  鈹?  鈹溾攢鈹€ logs <id>     鈫?鏌ョ湅閿欒鏃ュ織
  鈹溾攢鈹€ reload        鈫?閲嶆柊鎵弿鎻掍欢鐩綍
  鈹溾攢鈹€ clean         鈫?娓呯悊缂撳瓨鏃ュ織
  鈹斺攢鈹€ exit          鈫?閫€鍑?```

### 鍏抽敭绫?
**閿欒缂撳瓨 (`core/cache.py`)**
- 姣忔 `_exec` 鎶涘紓甯告椂鍐欏叆 `~/.bili_tool/cache/task_N_name_timestamp.json`
- 鍙啓 WARN/ERROR 绾ф棩蹇?+ 瀹屾暣 traceback + 绯荤粺鐜
- 鑷姩淇濈暀鏈€杩?10 涓紝`clean` 娓呯┖鍏ㄩ儴

---

## 浜屻€佽浆褰曟ā鍧楃幇鐘?
### 鍙屽紩鎿庣瓥鐣?
```
execute(params, emit)
  鈹?  鈹溾攢 鏈?audio_path 鈫?ensure_wav() 鈫?_transcribe()
  鈹?                                    鈹?  鈹?                          鈹屸攢鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹粹攢鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹€鈹?  鈹?                     ONNX 鍙敤?            ONNX 涓嶅彲鐢?  鈹?                          鈹?                    鈹?  鈹?                    transcribe_onnx()     whisper transcribe()
  鈹?                    锛堝瓙杩涚▼锛?              锛堝瓙杩涚▼锛?  鈹?                      澶辫触鈫?                   鈫?  鈹?                   鍥為€€ whisper.cpp         缁撴灉
  鈹?  鈹斺攢 鏈?url 鈫?fetch_cc() 鈫?鏈夊瓧骞曞垯鎻愬彇锛屾棤瀛楀箷鍒欐彁绀?```

### whisper.cpp 璺緞锛堝綋鍓嶅彲鐢?鉁咃級

| 姝ラ | 鏂规硶 | 鑰楁椂 |
|------|------|------|
| 闊抽杞崲 | librosa.load() + scipy.resample + soundfile.write | 杈冨揩 |
| 杞綍 | 瀛愯繘绋?whisper-cli.exe --stdout | GPU 姝ｅ父 |
| 杈撳嚭 | 閫愯璇诲彇 stdout 鈫?emit 鍒扮獥鍙?| 瀹炴椂 |
| 缁撴灉 | 娓呮礂鏃堕棿鎴冲悗杩斿洖 text | 鈥?|

### ONNX Paraformer 璺緞锛堝綋鍓嶄笉鍙敤 鉂岋級

| 姝ラ | 鐘舵€?| 鍘熷洜 |
|------|:----:|------|
| 妯″瀷鏂囦欢 | 鉁?宸插鍑?| paraformer(603MB) + predictor(3MB) + decoder(218MB) |
| Python 鐜 | 鉁?渚濊禆榻?| numpy, torch, soundfile, librosa, onnxruntime-gpu 1.24.1 |
| GPU 鐜 | 鉂?cuDNN 缂哄け | 缂?`cudnn64_9.dll`锛屽洖閫€ CPU |
| 缂栫爜鍣ㄦ帹鐞?| 鉂?妯″瀷 bug | dummy 甯ф暟 50 澶煭锛宻elf-attention mask baken 姝伙紝杈撳叆 2841 甯ф椂鎶ラ敊(1) |

_(1) `onnxruntime::BroadcastIterator::Init axis == 1 || axis == largest was false. Attempting to broadcast an axis by a dimension other than 1. 50 by 2841`_

### 宸茬煡闂

| 闂 | 褰卞搷 | 鐘舵€?|
|------|:----:|------|
| ONNX 缂栫爜鍣?dummy 甯ф暟涓嶈冻 | ONNX 璺緞涓嶅彲鐢?| 寰呬慨锛氶噸鏂板鍑猴紝dummy 鏀逛负 1000 甯?|
| cuDNN 9.x 鏈畨瑁?| ONNX 璺戝湪 CPU 涓?| 寰呰 |
| torchcodec + FFmpeg 缂?DLL | 鏃犳硶鐢?torchaudio 璇诲啓闊抽 | 宸茬粫杩囷細鏀圭敤 librosa + scipy + soundfile |
| whisper 缁撴灉鍙竻娲楁椂闂存埑锛屾湭鍒嗘 | 杈撳嚭涓鸿繛缁枃鏈?| 鍙紭鍖栵紙闈為樆濉烇級 |
| 鎻掍欢 render_* 鍑芥暟宸插垹闄?| 涓嶅奖鍝嶅姛鑳?| 宸插畬鎴?|
| TaskManager 宸茬Щ闄?| 鏀逛负姣忎换鍔＄嫭绔嬭繘绋?| 宸插畬鎴?|

---

## 涓夈€佸叧閿妧鏈喅绛?
| 鍐崇瓥 | 璇存槑 |
|------|------|
| **CREATE_NEW_CONSOLE 寮圭獥** | 涓嶈蛋 `start cmd /k`锛岄伩鍏嶄腑鏂囪矾寰勭紪鐮侀棶棰?|
| **subprocess stdout 娴佸紡璇诲彇** | `asyncio.run_coroutine_threadsafe()` 鍦ㄧ嚎绋嬩腑姣忚 emit |
| **PYTHONIOENCODING=utf-8** | 瀛愯繘绋嬭緭鍑?pipe 缂栫爜涓€鑷存€?|
| **閿欒缂撳瓨涓嶅瓨鎴愬姛浠诲姟** | 鍙湁鎶涘嚭寮傚父鎵嶅啓鍏ワ紝姝ｅ父瀹屾垚涓嶇暀鏂囦欢 |
| **librosa 璇?+ scipy 閲嶉噰鏍?+ soundfile 鍐?* | 褰诲簳缁曞紑 torchcodec 鍜?FFmpeg 渚濊禆 |
| **onnxruntime-gpu 1.24.1** | 鍏煎 CUDA 12.0锛屼笉瑕佹眰 CUDA 13.x |
| **28 涓祴璇曞叏閮ㄩ€氳繃** | pytest 瑕嗙洊 CLI銆佹彃浠跺彂鐜般€佽浆褰曞姛鑳?|

---

## 鍥涖€佺幆澧冭鏍?
| 缁勪欢 | 鐗堟湰 |
|------|------|
| Python | 3.14.6 |
| CUDA | 12.0 |
| onnxruntime-gpu | 1.24.1 |
| torch | 2.13.0+cpu |
| torchaudio | 鈥旓紙鏈娇鐢級 |
| whisper.cpp | 闇€瑕佺敤鎴疯嚜琛岀紪璇戞垨涓嬭浇 |

