---
---

杩欐槸涓€浠?**MarkItDown 鐨勮缁嗕娇鐢ㄦ墜鍐?*銆傚畠鏄竴娆剧敱寰蒋寮€婧愮殑杞婚噺绾?Python 宸ュ叿锛岃兘灏?PDF銆乄ord銆丒xcel銆丳PT銆佸浘鍍忋€侀煶棰戠瓑澶氱鏂囦欢鏍煎紡锛岄珮鏁堝湴杞崲涓?LLM锛堝ぇ璇█妯″瀷锛夋槗浜庣悊瑙ｅ拰澶勭悊鐨?Markdown 鏍煎紡銆?
---

## 馃摉 蹇€熶竴瑙?
| 椤圭洰 | 淇℃伅 |
| :--- | :--- |
| **椤圭洰鍚嶇О** | MarkItDown |
| **寮€鍙戣€?* | Microsoft |
| **GitHub** | [github.com/microsoft/markitdown](https://github.com/microsoft/markitdown) |
| **鏍稿績鍔熻兘** | 灏嗗绉嶆枃浠舵牸寮忚浆鎹负 LLM 灏辩华鐨?Markdown 鏂囨湰 |
| **涓昏鐢ㄩ€?* | 涓?AI 宸ヤ綔娴併€佹枃鏈垎鏋愩€佹枃妗ｇ储寮曞噯澶囬珮璐ㄩ噺鏁版嵁 |
| **杈撳嚭鐗规€?* | 淇濈暀鏂囨。缁撴瀯锛堟爣棰樸€佸垪琛ㄣ€佽〃鏍肩瓑锛夛紝Token 鏁堢巼楂?|

---

## 馃殌 1. 鐜鍑嗗涓庡畨瑁?
### 鐜瑕佹眰
*   **Python**: 鐗堟湰 3.10 鎴栨洿楂樸€?*   **pip**: Python 鐨勫寘绠＄悊宸ュ叿銆?
### 瀹夎姝ラ

#### 1. 鏈€鎺ㄨ崘鐨勬柟寮忥細涓€閿畨瑁呮墍鏈夊姛鑳斤紙`[all]`锛?濡傛灉甯屾湜 MarkItDown 鏀寔灏藉彲鑳藉鐨勬枃浠舵牸寮忥紝璇锋墽琛屼互涓嬪懡浠わ細
```bash
pip install markitdown[all]
```
杩欑鏂规硶浼氬畨瑁呭寘鎷?PDF銆丒xcel銆佸浘鍍忋€侀煶棰戠瓑澶勭悊鎵€闇€鐨勬墍鏈夊彲閫変緷璧栧簱銆?
#### 2. 鎸夐渶瀹夎锛堣妭鐪佺┖闂达級
濡傛灉浣犲彧闇€瑕佸鐞嗙壒瀹氱被鍨嬬殑鏂囦欢锛屽彲浠ュ彧瀹夎鏍稿績搴撳拰瀵瑰簲鐨勪緷璧栵細
```bash
pip install markitdown[pdf, docx, pptx]
```

#### 3. 浠庢簮浠ｇ爜瀹夎锛堣幏鍙栨渶鏂扮壒鎬э級
濡傛灉浣犳兂浣撻獙鏈€鏂扮殑寮€鍙戠増鍔熻兘锛屽彲浠ヤ粠 GitHub 鍏嬮殕骞跺畨瑁咃細
```bash
git clone git@github.com:microsoft/markitdown.git
cd markitdown
pip install -e packages/markitdown[all]
```

#### 4. 楠岃瘉瀹夎
瀹夎鎴愬姛鍚庯紝鍙互閫氳繃浠ヤ笅鍛戒护鏌ョ湅鐗堟湰淇℃伅鏉ラ獙璇侊細
```bash
markitdown --version
```

#### 5. (鍙€? 浣跨敤铏氭嫙鐜
涓轰簡閬垮厤涓嶅悓 Python 椤圭洰闂寸殑渚濊禆鍐茬獊锛屽缓璁湪铏氭嫙鐜涓畨瑁咃細
```bash
# 鍒涘缓铏氭嫙鐜
python -m venv markitdown-env
# 婵€娲昏櫄鎷熺幆澧?(Windows)
markitdown-env\Scripts\activate
# 婵€娲昏櫄鎷熺幆澧?(macOS/Linux)
source markitdown-env/bin/activate
# 鐒跺悗鍦ㄨ櫄鎷熺幆澧冧腑瀹夎
pip install markitdown[all]
```

---

## 馃捇 2. 鍛戒护琛岀晫闈?(CLI) 浣跨敤鎸囧崡

MarkItDown 鎻愪緵浜嗛潪甯镐究鎹风殑鍛戒护琛屽伐鍏凤紝閫傚悎蹇€熻浆鎹㈡垨闆嗘垚鍒拌剼鏈腑銆?
### 鍩烘湰鐢ㄦ硶锛氭爣鍑嗚緭鍑?鏈€绠€鍗曠殑鐢ㄦ硶鏄皢杞崲缁撴灉鐩存帴鎵撳嵃鍦ㄧ粓绔笂锛?```bash
markitdown 璺緞/鍒?浣犵殑鏂囦欢.pdf
```
浣犱篃鍙互浣跨敤閲嶅畾鍚戞搷浣滅 `>` 灏嗗唴瀹逛繚瀛樺埌 `.md` 鏂囦欢涓細
```bash
markitdown 璺緞/鍒?浣犵殑鏂囦欢.docx > 杈撳嚭鏂囨。.md
```

### 淇濆瓨鍒版枃浠讹細浣跨敤 `-o` 閫夐」
鏇存帹鑽愪娇鐢?`-o` 鎴?`--output` 閫夐」锛岃繖鏍峰彲浠ョ洿鎺ユ寚瀹氳緭鍑烘枃浠讹紝閬垮厤閲嶅畾鍚戝彲鑳藉甫鏉ョ殑缂栫爜闂锛?```bash
markitdown 璺緞/鍒?浣犵殑婕旂ず鏂囩.pptx -o 婕旇绋?md
```
鎵ц鍚庯紝Markdown 鍐呭浼氳鍐欏叆 `婕旇绋?md` 鏂囦欢涓€?
### 澶勭悊鏍囧噯杈撳叆 (stdin)锛氫粠绠￠亾璇诲彇
浣犲彲浠ラ€氳繃绠￠亾灏嗘枃浠跺唴瀹逛紶閫掔粰 `markitdown` 鍛戒护锛岃繖鍦ㄥ鐞嗗姩鎬佺敓鎴愮殑鍐呭鏃堕潪甯告湁鐢細
```bash
cat 鏈煡绫诲瀷鏂囦欢.bin | markitdown
```
鎴栬€呴€氳繃杈撳叆閲嶅畾鍚戯細
```bash
markitdown < 杈撳叆鏂囦欢.txt
```

### 甯哥敤鍛戒护琛岄€夐」鍙傝€?CLI 鎻愪緵浜嗗涓€夐」锛岃浣犺兘绮剧‘鎺у埗杞崲琛屼负銆?
| 閫夐」 | 绠€鍐?| 鎻忚堪 | 绀轰緥 |
| :--- | :--- | :--- | :--- |
| `--output` | `-o` | 灏嗙粨鏋滃啓鍏ユ寚瀹氭枃浠?| `markitdown -o out.md in.pdf` |
| `--extension` | `-x` | **锛堥噸瑕侊級** 褰撲粠 stdin 杈撳叆鏃讹紝鎸囧畾鏂囦欢鎵╁睍鍚嶄互甯姪璇嗗埆鏍煎紡 | `markitdown -x pdf < input.bin` |
| `--mime-type` | `-m` | 褰撲粠 stdin 杈撳叆鏃讹紝鎸囧畾鏂囦欢鐨?MIME 绫诲瀷 | `markitdown -m application/pdf < input.bin` |
| `--charset` | `-c` | 鎸囧畾鏂囨湰杈撳叆鏂囦欢鐨勫瓧绗﹂泦 | `markitdown -c utf-8 < input.txt` |
| `--version` | `-v` | 鏄剧ず褰撳墠 MarkItDown 鐨勭増鏈彿 | `markitdown -v` |

### 馃挕 瀹炵敤鎶€宸э細浣跨敤 `-o` 浠ｆ浛閲嶅畾鍚?`>`
褰撹浆鎹㈠寘鍚潪鑻辨枃瀛楃锛堝涓枃銆佹硶璇€佸痉璇瓑锛夌殑鏂囦欢鏃讹紝浣跨敤閲嶅畾鍚?`>` 鍙兘浼氶亣鍒?`UnicodeEncodeError` 閿欒銆傛鏃讹紝浣跨敤 `-o` 閫夐」灏嗙粨鏋滅洿鎺ュ啓鍏ユ枃浠舵槸鏇村彲闈犵殑閫夋嫨锛屽洜涓哄畠鑳芥洿濂藉湴澶勭悊 UTF-8 缂栫爜銆?
---

## 馃悕 3. Python API 浣跨敤鎸囧崡

鍦?Python 鑴氭湰鎴?Jupyter Notebook 涓娇鐢?MarkItDown 鍙互瀹炵幇鏇村鏉傜殑闆嗘垚鍜岃嚜鍔ㄥ寲銆?
### 鍩虹杞崲
浣跨敤 MarkItDown 鐨?API 闈炲父绠€鍗曪紝鍙渶涓夋锛?
1.  瀵煎叆 `MarkItDown` 绫汇€?2.  鍒涘缓 `MarkItDown` 瀹炰緥銆?3.  璋冪敤 `convert()` 鏂规硶銆?
```python
from markitdown import MarkItDown

# 1. 鍒涘缓杞崲鍣ㄥ疄渚?md = MarkItDown()

# 2. 杞崲鏂囦欢锛屾敮鎸佺粷瀵硅矾寰勬垨鐩稿璺緞
result = md.convert("璐㈠姟鏁版嵁.xlsx")

# 3. 鎵撳嵃杞崲鍚庣殑 Markdown 鏂囨湰
print(result.text_content)
```

### 鍦ㄤ笉鍚屽満鏅腑鐨勫簲鐢?
#### 鍦烘櫙涓€锛氬鐞?Word 鏂囨。
Word 鏂囨。涓殑鏍囬銆佸垪琛ㄥ拰鍔犵矖鏂囨湰绛夋牸寮忥紝鍦ㄨ浆鎹㈠悗浼氫繚鐣欎负 Markdown 鏍煎紡銆?```python
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("骞村害鎶ュ憡.docx")
print(result.text_content)
```

#### 鍦烘櫙浜岋細杞崲 PowerPoint 骞荤伅鐗?MarkItDown 浼氭彁鍙栨瘡寮犲够鐏墖鐨勬爣棰樺拰椤圭洰绗﹀彿鏂囨湰锛屽苟浠ュ够鐏墖缂栧彿涓哄垎闅旇緭鍑恒€?```python
result = md.convert("浜у搧浠嬬粛.pptx")
print(result.text_content)
```

#### 鍦烘櫙涓夛細瑙ｆ瀽 Excel 琛ㄦ牸
杞崲鍣ㄤ細灏嗙數瀛愯〃鏍间腑鐨勭粨鏋勫寲鏁版嵁杞崲涓烘竻鏅扮殑 Markdown 琛ㄦ牸锛岄潪甯镐究浜?LLM 鐞嗚В鏁版嵁闂寸殑鍒楀搴斿叧绯汇€?```python
result = md.convert("閿€鍞暟鎹?xlsx")
print(result.text_content)
```

#### 鍦烘櫙鍥涳細浠?ZIP 鏂囦欢涓彁鍙栧唴瀹?MarkItDown 鑳藉鑷姩閬嶅巻 ZIP 鍘嬬缉鍖呭唴鐨勬枃浠跺苟閫愪竴杞崲锛岀劧鍚庡皢鎵€鏈夌粨鏋滃悎骞惰緭鍑恒€?```python
result = md.convert("鏂囨。璧勬枡搴?zip")
print(result.text_content) # 灏嗚緭鍑烘墍鏈夊唴閮ㄦ枃浠剁殑杞崲缁撴灉
```

---

## 馃 4. 楂樼骇鍔熻兘

### 馃 涓?LLM 闆嗘垚锛氫负鍥剧墖鐢熸垚鎻忚堪
MarkItDown 鍙互涓庡ぇ璇█妯″瀷锛堝 GPT-4锛夌粨鍚堬紝涓哄浘鐗囩敓鎴愬噯纭殑鏂囨湰鎻忚堪銆?```python
from markitdown import MarkItDown
from openai import OpenAI

# 鍒濆鍖?OpenAI 瀹㈡埛绔紙闇€瑕佽缃?API Key锛?client = OpenAI()

# 鍒涘缓 MarkItDown 瀹炰緥鏃讹紝浼犲叆 LLM 瀹㈡埛绔拰妯″瀷鍚嶇О
md = MarkItDown(llm_client=client, llm_model="gpt-4o")

# 杞崲鍥剧墖鏃讹紝浼氳嚜鍔ㄨ皟鐢?LLM 鐢熸垚鎻忚堪
result = md.convert("椋庢櫙鐓х墖.jpg")
print(result.text_content)
```
> **娉ㄦ剰**: 浣跨敤姝ゅ姛鑳介渶瑕?OpenAI API Key 鍜岀綉缁滆闂潈闄愩€?
### 馃敡 鎻掍欢绯荤粺
MarkItDown 鏀寔閫氳繃鎻掍欢鏉ユ墿灞曞姛鑳姐€傜涓夋柟杞崲鍣ㄥ彲浠ラ€氳繃 Python 鐨勫叆鍙ｇ偣绯荤粺娉ㄥ唽杩涙潵銆?```python
from markitdown import MarkItDown

md = MarkItDown()

# 鍚敤鎵€鏈夊凡瀹夎鐨勭涓夋柟鎻掍欢
md.enable_plugins()
```
鍦ㄥ懡浠よ涓紝浣犲彲浠ヤ娇鐢?`--use-plugins` 鍜?`--list-plugins` 閫夐」鏉ョ鐞嗘彃浠躲€?
### 馃帥锔?杞崲鍣ㄤ紭鍏堢骇绯荤粺
MarkItDown 鍐呴儴浣跨敤浼樺厛绾х郴缁熸潵鍐冲畾浣跨敤鍝釜杞崲鍣ㄦ潵澶勭悊鏂囦欢銆備紭鍏堢骇鍊艰秺浣庯紝杞崲鍣ㄨ秺鍏堣灏濊瘯銆?
*   **鐗瑰畾鏍煎紡杞崲鍣?* (`PRIORITY_SPECIFIC_FILE_FORMAT = 0.0`): 渚嬪 `PdfConverter`銆乣DocxConverter`锛屼細浼樺厛浜庨€氱敤杞崲鍣ㄨ璋冪敤銆?*   **閫氱敤杞崲鍣?* (`PRIORITY_GENERIC_FILE_FORMAT = 10.0`): 渚嬪 `PlainTextConverter`銆乣ZipConverter`锛屼綔涓哄悗澶囨柟妗堛€?
杩欎釜鏈哄埗纭繚浜嗙郴缁熸€绘槸涓烘枃浠堕€夋嫨鏈€鍚堥€傜殑杞崲鍣ㄣ€?
### 鈽侊笍 Azure Document Intelligence 闆嗘垚
MarkItDown 鍙互闆嗘垚 Azure 鐨勬枃妗ｆ櫤鑳芥湇鍔★紝鐢ㄤ簬鏇撮珮绾х殑鏂囨湰鎻愬彇锛屼緥濡備粠澶嶆潅鐨?PDF 琛ㄥ崟涓彁鍙栨暟鎹€?```bash
markitdown 澶嶆潅琛ㄥ崟.pdf --use-docintel --endpoint "浣犵殑Azure鏈嶅姟绔偣URL"
```

---

## 鉂?5. 鏁呴殰鎺掗櫎涓庡父瑙侀棶棰?
### 1. 杩愯鏃跺嚭鐜?`UnicodeEncodeError` 閿欒
*   **闂**: 褰撹浆鎹㈢殑鏂囦欢鍖呭惈闈炶嫳鏂囧瓧绗︼紙濡備腑鏂囥€佹硶璇瓧姣嶏級鏃讹紝鍦?Windows 鍛戒护琛屼腑浣跨敤閲嶅畾鍚?`>` 淇濆瓨鏂囦欢鏃跺彲鑳藉嚭鐜扮紪鐮侀敊璇€?*   **瑙ｅ喅鏂规**:
    *   **鏂规硶涓€锛堟帹鑽愶級**: 浣跨敤 `-o` 閫夐」鏇夸唬閲嶅畾鍚戙€備緥濡傦細`markitdown 涓枃鏂囨。.pdf -o 杈撳嚭.md`銆?    *   **鏂规硶浜?*: 鍦ㄨ繍琛?Python 鑴氭湰鍓嶏紝鍏堣缃幆澧冨彉閲?`PYTHONIOENCODING=utf-8`銆?
### 2. 鏃犳硶杞崲缃戠粶椹卞姩鍣ㄤ笂鐨勬枃浠?*   **闂**: 褰撴枃浠朵綅浜庢槧灏勭殑缃戠粶椹卞姩鍣ㄤ笂鏃讹紝杞崲鍙兘鍥犳潈闄愰棶棰樿€屽け璐ャ€?*   **瑙ｅ喅鏂规**: 鍏堝皢鏂囦欢澶嶅埗鍒版湰鍦伴┍鍔ㄥ櫒锛堝 `C:\` 鐩橈級锛岀劧鍚庡鏈湴鍓湰杩涜杞崲銆傝浆鎹㈡垚鍔熷悗锛屽啀鏍规嵁闇€瑕佸鐞嗗師鏂囦欢銆?
### 3. 濡備綍澶勭悊澶ф枃浠讹紵
*   **闂**: 澶勭悊闈炲父澶х殑鏂囦欢鍙兘浼氭秷鑰楀ぇ閲忓唴瀛樺拰鏃堕棿銆?*   **瑙ｅ喅鏂规**: 纭繚浣犵殑璁＄畻鏈烘湁瓒冲鐨勫唴瀛樸€傚鏋滃彲鑳斤紝鑰冭檻灏嗗ぇ鏂囦欢鎷嗗垎鎴愯緝灏忕殑閮ㄥ垎鍚庡啀杩涜杞崲銆?
---

## 馃摎 闄勫綍

### 鏀寔鐨勬枃浠舵牸寮忔竻鍗?
| 绫诲瀷 | 鏀寔鐨勬牸寮?|
| :--- | :--- |
| **馃搫 鍔炲叕鏂囨。** | PDF (.pdf), Word (.docx), PowerPoint (.pptx), Excel (.xlsx/.xls) |
| **馃寪 缃戦〉涓庢枃鏈?* | HTML, 绾枃鏈?(.txt), CSV, JSON, XML |
| **馃柤锔?澶氬獟浣?* | 鍥剧墖 (JPEG, PNG, GIF绛夛紝鏀寔OCR), 闊抽 (MP3, WAV绛夛紝鏀寔璇煶杞綍) |
| **馃棞锔?鍘嬬缉鏂囦欢** | ZIP 鍘嬬缉鍖?(鍙亶鍘嗗唴閮ㄦ枃浠跺苟閫愪竴杞崲) |
| **馃摎 鐢靛瓙涔?* | EPUB 鏍煎紡 |
| **馃摟 閭欢** | Outlook 閭欢鏂囦欢 (.msg) |
| **馃捇 浠ｇ爜鏂囦欢** | 澶氱缂栫▼璇█婧愪唬鐮佹枃浠讹紝骞惰兘淇濈暀璇硶楂樹寒鏍煎紡 |

### MarkItDown vs. Pandoc

| 鐗规€?| MarkItDown | Pandoc |
| :--- | :--- | :--- |
| **璁捐鐩爣** | 涓?LLM 鍜?AI 绠￠亾蹇€熻浆鎹㈡枃鏈?| 楂樺害淇濈湡鐨勬枃妗ｆ牸寮忚浆鎹紝杩芥眰瑙嗚甯冨眬杩樺師 |
| **杈撳嚭璐ㄩ噺** | 淇濈暀鏂囨。缁撴瀯锛屽鏈哄櫒鍙嬪ソ | 淇濈暀澶嶆潅甯冨眬鍜屾牸寮忥紝瀵逛汉绫婚槄璇诲弸濂?|
| **閫熷害** | 蹇€?| 鐩稿杈冩參 |
| **閫傜敤鍦烘櫙** | AI 璁粌鏁版嵁鍑嗗銆佹壒閲忔枃鏈垎鏋?| 鏂囨。鍑虹増銆佹牸寮忕簿纭縼绉?|
| **鎬荤粨** | 杩芥眰閫熷害鍜?AI 闆嗘垚搴?| 杩芥眰鏍煎紡瀹屾暣鎬у拰绮剧‘搴?|

鏍规嵁浠诲姟闇€姹傦紝浣犲彲浠ュ湪 MarkItDown 鐨?**閫熷害涓?AI 鍙嬪ソ鎬?* 鍜?Pandoc 鐨?**鏍煎紡涓庤瑙夐珮淇濈湡搴?* 涔嬮棿鍋氬嚭閫夋嫨銆?
### 鍙傝€冭祫婧?*   **瀹樻柟 GitHub 浠撳簱**: [https://github.com/microsoft/markitdown](https://github.com/microsoft/markitdown)
*   **PyPI 椤圭洰椤?*: [https://pypi.org/project/markitdown/](https://pypi.org/project/markitdown/)
*   **闂鍙嶉**: 鍦?GitHub 浠撳簱鐨?[Issues](https://github.com/microsoft/markitdown/issues) 椤甸潰鎻愪氦銆?
---

甯屾湜杩欎唤鎵嬪唽鑳藉府鍔╀綘椤哄埄涓婃墜 MarkItDown銆傚鏋滃湪浣跨敤杩囩▼涓亣鍒板叾浠栭棶棰橈紝闅忔椂鍙互鍐嶆彁闂€
