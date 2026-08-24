---
---


### 馃摉 Pandoc 鏄粈涔堬紵

浣犲彲浠ユ妸 Pandoc 鐞嗚В涓轰竴鏈竾鑳借瘝鍏革紝瀹冭兘鍦ㄨ秴杩?40 绉嶆枃妗ｆ牸寮忛棿杩涜绮剧‘杞崲锛屾槸鐪熸鐨勨€滄枃妗ｆ牸寮忚浆鎹㈢憺澹啗鍒€鈥濄€?
*   **鏍煎紡鏀寔骞挎硾**锛氬皬鍒?Markdown銆丠TML锛屽ぇ鍒?Word锛?docx锛夈€丳PT銆丳DF锛岀敋鑷崇數瀛愪功锛圗PUB锛夛紝瀹冮兘鑳借交鏉炬悶瀹氥€?*   **璐ㄩ噺楂?*锛氳浆鎹㈢殑鏍稿績鏄В鏋愭枃妗ｇ殑鈥滅粨鏋勨€濓紙濡傛爣棰樸€佹钀姐€佽〃鏍硷級锛岃€岄潪鏍峰紡锛屽洜姝よ兘鏈€澶х▼搴︿繚璇佸唴瀹圭殑鍑嗙‘鎬с€?
### 馃捇 绗竴姝ワ細瀹夎

Pandoc 鏀寔 Windows銆乵acOS 鍜?Linux锛屽畨瑁呭緢绠€鍗曘€?
*   **Windows 鐢ㄦ埛**
    *   **鎺ㄨ崘鏂规硶**锛氫粠瀹樼綉涓嬭浇 `.msi` 瀹夎绋嬪簭锛屽弻鍑绘寜鎻愮ず鎿嶄綔鍗冲彲锛屽畨瑁呯▼搴忎細鑷姩閰嶇疆濂界幆澧冦€?    *   **鍖呯鐞嗗櫒**锛氫娇鐢?`winget install --id JohnMacFarlane.Pandoc` 鎴?`choco install pandoc`銆?
*   **macOS 鐢ㄦ埛**
    *   鍚屾牱鎺ㄨ崘浠庡畼缃戜笅杞?`.pkg` 瀹夎绋嬪簭銆備範鎯敤 Homebrew 鐨勫紑鍙戣€咃紝鍙墽琛?`brew install pandoc`銆?
*   **Linux 鐢ㄦ埛**
    *   浠?Ubuntu/Debian 涓轰緥锛屽湪缁堢鎵ц `sudo apt-get install pandoc` 鍗冲彲銆?
瀹夎瀹屾垚鍚庯紝鎵撳紑缁堢锛堝懡浠ゆ彁绀虹鎴?PowerShell锛夛紝杈撳叆 `pandoc --version`锛屽鏋滆兘鐪嬪埌鐗堟湰淇℃伅锛屽氨琛ㄧず瀹夎鎴愬姛鍟︺€?
### 鉁?绗簩姝ワ細鏍稿績璇硶

Pandoc 鐨勬牳蹇冨懡浠ゅ彧鏈変竴涓畝鍗曞叕寮忥細`pandoc [杈撳叆鏂囦欢] -o [杈撳嚭鏂囦欢]`銆?
瀹冪殑鏅鸿兘涔嬪鍦ㄤ簬锛屼細鑷姩鏍规嵁鏂囦欢鍚庣紑鍚嶅垽鏂牸寮忋€傛瘮濡傦紝瑕佹妸 Markdown 绗旇杞垚 Word 鎶ュ憡锛屽彧闇€锛?
```bash
pandoc my_note.md -o my_report.docx
```

*   鑻ユ兂绮剧‘鎺у埗锛屼篃鍙敤 `-f`锛堣緭鍏ユ牸寮忥級鍜?`-t`锛堣緭鍑烘牸寮忥級鏉ユ寚瀹氥€?*   涓虹敓鎴愬畬鏁存枃妗ｏ紝寤鸿鍔犱笂 `-s` 鎴?`--standalone`銆?
### 馃殌 绗笁姝ワ細楂橀杞崲鍦烘櫙

**1. Word 杞?Markdown**
杩欐槸浣犳瀯寤虹煡璇嗗簱鐨勫叧閿竴姝ワ紝鍛戒护鍚屾牱寰堢畝鍗曪細

```bash
pandoc "浣犵殑鏂囨。.docx" -f docx -t markdown -o "杈撳嚭鏂囦欢.md"
```

*   `-f docx`锛氭寚瀹氳緭鍏ユ牸寮忔槸 Word銆?*   `-t markdown`锛氭寚瀹氳緭鍑烘牸寮忔槸 Markdown銆?*   `-o "杈撳嚭鏂囦欢.md"`锛氭寚瀹氳緭鍑烘枃浠跺悕銆?
**2. Markdown 杞?Word**
濡傛灉浣犵殑鏂囩珷鏄?Markdown 鏍煎紡锛屾兂杞垚 Word 鏍煎紡淇濆瓨锛屽彲浠ョ敤杩欎釜鍛戒护锛?
```bash
pandoc report.md -o final_report.docx
```

**3. Markdown 杞?PDF**
濡傛灉浣犵殑 Markdown 绗旇鍖呭惈琛ㄦ牸鎴栦唬鐮侊紝鎯宠鎵撳嵃鎴栧垎浜紝PDF 鏄緢濂界殑閫夋嫨銆?
```bash
pandoc paper.md -s -o paper.pdf
```

> 鈿狅笍 **娉ㄦ剰浜嬮」**锛歅DF 杞崲闇€瑕佷緷璧?LaTeX 寮曟搸锛屽鏋滀綘鐨勭數鑴戞槸棣栨杩愯姝ゅ懡浠わ紝Pandoc 鍙兘浼氳嚜鍔ㄤ笅杞藉繀瑕佺殑缁勪欢銆?>
> **涓枃鏀寔**锛氶粯璁ゅ紩鎿庡彲鑳戒笉鏀寔涓枃锛岄渶瑕佹寚瀹?`xelatex` 寮曟搸鍜屼腑鏂囧瓧浣擄細
> ```bash
> pandoc paper.md -o paper.pdf --pdf-engine=xelatex -V mainfont="SimSun"
> ```

**4. 澶氭枃浠跺悎骞?*
鍐欓暱鏂囨垨鐢靛瓙涔︽椂锛屽彲浠ュ皢澶氫釜 Markdown 鏂囦欢鍚堝苟鎴愪竴涓€?
*   **鍚堝苟涓?EPUB 鐢靛瓙涔?*
    ```bash
    pandoc title.md ch1.md ch2.md -o mybook.epub
    ```

*   **鍚堝苟涓?Word 闀挎姤鍛?*
    ```bash
    pandoc *.md -o full_report.docx
    ```

**5. 鎵归噺杞崲锛圵indows锛?*
涓轰簡鎵归噺澶勭悊 `.md` 鏂囦欢锛屼綘鍙互浣跨敤 PowerShell 鑴氭湰銆傝繖閲屾彁渚涗袱绉嶅父鐢ㄥ満鏅細

*   **鍦烘櫙涓€锛氭壒閲忓皢褰撳墠鐩綍涓嬫墍鏈?`.md` 鏂囦欢杞崲涓?`.docx`**
    ```powershell
    Get-ChildItem -Path . -Filter *.md | ForEach-Object {
        pandoc $_.FullName -o "$($_.BaseName).docx"
        Write-Host "宸茶浆鎹? $($_.Name)"
    }
    Write-Host "鎵归噺杞崲瀹屾垚锛?
    ```

*   **鍦烘櫙浜岋細鎵归噺灏嗗綋鍓嶇洰褰曚笅鎵€鏈?`.docx` 鏂囦欢杞崲涓?`.md`**
    ```powershell
    Get-ChildItem -Path . -Filter *.docx | ForEach-Object {
        pandoc $_.FullName -f docx -t markdown -o "$($_.BaseName).md"
        Write-Host "宸茶浆鎹? $($_.Name)"
    }
    Write-Host "鎵归噺杞崲瀹屾垚锛?
    ```
    > 浣犲彲浠ユ妸鑴氭湰淇濆瓨涓?`.ps1` 鏂囦欢锛堝 `convert.ps1`锛夛紝鏀惧湪闇€瑕佽浆鎹㈢殑鏂囦欢澶逛腑锛屽彸閿€夋嫨鈥滀娇鐢?PowerShell 杩愯鈥濆嵆鍙€?
### 馃敡 绗洓姝ワ細甯哥敤閫夐」

| 閫夐」 | 鍔熻兘 | 绀轰緥 |
| :--- | :--- | :--- |
| `-f` / `--from` | 鎸囧畾杈撳叆鏍煎紡 | `-f markdown` |
| `-t` / `--to` | 鎸囧畾杈撳嚭鏍煎紡 | `-t html` |
| `-o` / `--output` | 鎸囧畾杈撳嚭鏂囦欢鍚?| `-o output.docx` |
| `-s` / `--standalone` | 鐢熸垚瀹屾暣鏂囨。 | `pandoc -s file.md -o out.html` |
| `--toc` | 鐢熸垚鐩綍 | `pandoc --toc file.md -o out.pdf` |
| `--template` | 浣跨敤鑷畾涔夋ā鏉?| `pandoc --template=mytemplate.tex file.md -o out.pdf` |
| `--pdf-engine` | 鎸囧畾 PDF 寮曟搸 | `--pdf-engine=xelatex` |
| `-V` / `--variable` | 璁剧疆鍙橀噺 | `-V mainfont="SimSun"` |

### 馃敟 绗簲姝ワ細楂樼骇鐜╂硶

**1. 鑷畾涔?Word 妯℃澘**
鎯虫嫢鏈夊畬鍏ㄧ鍚堝績鎰忕殑 Word 鏍峰紡锛熷彲浠ヨ繖鏍峰仛锛?
1.  **鑾峰彇榛樿妯℃澘**锛氬湪缁堢杈撳叆 `pandoc -o custom-reference.docx --print-default-data-file reference.docx`锛屽氨浼氱敓鎴愪竴涓?`custom-reference.docx` 鏂囦欢銆?2.  **淇敼鏍峰紡**锛氱敤 Word 鎵撳紑锛屽敖鎯呬慨鏀瑰叾涓殑瀛椾綋銆佹钀姐€侀〉杈硅窛绛変竴鍒囨牱寮忋€?3.  **搴旂敤妯℃澘**锛氳浆鎹㈡椂锛岄€氳繃 `--reference-doc` 鍙傛暟鎸囧畾浣犳敼濂界殑妯℃澘鏂囦欢鍗冲彲锛屽 `pandoc input.md -o output.docx --reference-doc=custom-reference.docx`銆?
**2. 绠＄悊鍏冩暟鎹?*
鍦?Markdown 鏂囦欢鏈€椤堕儴娣诲姞浠?`---` 鍖呰９鐨?YAML 鏍煎紡淇℃伅锛屽彲浠ユ柟渚垮湴瀹氫箟鏂囨。鐨勬爣棰樸€佷綔鑰呫€佹棩鏈熺瓑銆?
```yaml
---
title: 杩欐槸鏍囬
author: 寮犱笁
date: 2023-10-20
---
```

### 鉂?绗叚姝ワ細甯歌闂涓庤В鍐虫柟妗?
*   **涓枃 PDF 涔辩爜鎴栫┖鐧?*
    榛樿寮曟搸 `pdflatex` 涓嶆敮鎸佷腑鏂囥€傞渶瑕佹寚瀹氬紩鎿庡拰涓枃瀛椾綋锛?    ```bash
    pandoc input.md -o output.pdf --pdf-engine=xelatex -V mainfont="SimSun"
    ```
*   **Word 杞?Markdown 鍚庢牸寮忔贩涔?*
    鍙互灏濊瘯杈撳嚭鏇寸函鍑€鐨?Markdown 鏍煎紡锛?    ```bash
    pandoc input.docx -f docx -t markdown-strict -o output.md
    ```
*   **杞崲鍑虹殑鏂囦欢鏃犳硶鎵撳紑**
    濡傛灉杞崲鐨勬槸 RTF 绛夋牸寮忥紝璁板緱鍔犱笂 `-s` 鍙傛暟锛屼互纭繚鐢熸垚瀹屾暣鐨勬枃妗ｇ粨鏋勶紝鑰岄潪鍐呭鐗囨銆?
### 馃拵 鎬荤粨

鎺屾彙 Pandoc锛屽氨濡傚悓涓鸿嚜宸遍厤澶囦簡涓€浣嶆枃妗ｆ牸寮忕殑涓囪兘杞崲澶у笀銆傛棤璁烘槸鏋勫缓涓汉鐭ヨ瘑搴擄紝杩樻槸澶勭悊鏃ュ父鐨勫鏈拰宸ヤ綔鏂囨。锛屽畠閮借兘璁╀綘浜嬪崐鍔熷€嶃€?
甯屾湜杩欎唤鎸囧崡瀵逛綘鏈夋墍甯姪銆
