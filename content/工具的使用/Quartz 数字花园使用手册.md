---
---


## 1. 鏍稿績宸ヤ綔娴佺▼

浣犵殑鏁板瓧鑺卞洯鏄竴涓?Git 浠撳簱 + GitHub Actions 鑷姩鏋勫缓鐨勯潤鎬佺綉绔欍€傛棩甯镐娇鐢ㄥ彧闇€瑕佷笁姝ワ細

1. **缂栬緫鍐呭**锛氬湪 `content` 鏂囦欢澶逛腑娣诲姞銆佷慨鏀规垨鍒犻櫎 `.md` 鏂囦欢銆?2. **鎻愪氦鍙樻洿**锛氫娇鐢?Git 鍛戒护鎻愪氦鏈湴鏇存敼銆?3. **鎺ㄩ€佷笂绾?*锛氬皢鎻愪氦鎺ㄩ€佸埌 GitHub锛孉ctions 鑷姩鏋勫缓骞舵洿鏂扮綉绔欍€?
> 鏁翠釜娴佺▼绾?1 鍒嗛挓鐢熸晥锛屾棤闇€鎵嬪姩瑙﹀彂鏋勫缓锛堥櫎闈炰綘鍏抽棴浜嗚嚜鍔ㄩ儴缃诧級銆?
---

## 2. 绠＄悊绗旇鍐呭

### 2.1 娣诲姞鏂扮瑪璁?
- **浣嶇疆**锛氭墍鏈夌瑪璁板繀椤绘斁鍦?[content](file:///C:%5C鏈夌敤杞欢%5Cobsidian-web%5Cquartz%5Ccontent) 鏂囦欢澶瑰唴锛堝彲浠ュ垱寤哄瓙鏂囦欢澶瑰垎绫伙級銆?- **鏂囦欢鏍煎紡**锛歚.md`锛圡arkdown锛夈€?- **鍛藉悕瑙勮寖**锛?*寮虹儓寤鸿浣跨敤鑻辨枃**锛屽 `my-article.md`銆傞伩鍏嶇┖鏍笺€佷腑鏂囥€佺壒娈婄鍙凤紙`@#$%` 绛夛級銆?  - 鉁?`obsidian-tips.md`
  - 鉂?`Obsidian鎶€宸?md`
  - 鉁?`how-to-use-git.md`
- **鍐呭妯℃澘**锛堝彲閫夛級锛氬湪鏂囦欢寮€澶存坊鍔?YAML Frontmatter 鍙互鎺у埗椤甸潰鏍囬銆佹棩鏈熴€佹爣绛剧瓑銆?
```markdown
---
title: 鎴戠殑鏂囩珷鏍囬锛堜細鏄剧ず鍦ㄦ祻瑙堝櫒鏍囩椤靛拰椤甸潰椤堕儴锛?date: 2026-04-20
tags:
  - obsidian
  - quartz
---

姝ｆ枃浣跨敤鏍囧噯 Markdown 璇硶...
```

### 2.2 璁剧疆鏍囬鍜屾棩鏈?
- **鏍囬**锛氬鏋滃啓浜?`title`锛岀綉椤典細浣跨敤瀹冿紱鍚﹀垯浣跨敤鏂囦欢鍚嶏紙鍘婚櫎鎵╁睍鍚嶏級銆?- **鏃ユ湡**锛歈uartz 榛樿浼氫粠 Git 鎻愪氦鍘嗗彶涓鍙栧垱寤哄拰淇敼鏃堕棿銆備篃鍙互鎵嬪姩鎸囧畾锛?  ```yaml
  date: 2026-04-20
  updated: 2026-04-21
  ```

### 2.3 鎻掑叆鍥剧墖鍜岄檮浠?
- 灏嗗浘鐗囷紙`.png`, `.jpg` 绛夛級鎴?PDF 绛夋枃浠舵斁鍦?`content` 鏂囦欢澶瑰唴鐨勪换鎰忎綅缃紙寤鸿寤虹珛 `assets` 鎴?`images` 瀛愭枃浠跺す锛夈€?- 鍦?Markdown 涓娇鐢?*鐩稿璺緞**寮曠敤锛?
```markdown
![鍥剧墖璇存槑](./images/example.png)
[涓嬭浇 PDF](./files/manual.pdf)
```

> 娉ㄦ剰锛氫笉鏀寔 Obsidian 鐨?`![[attachment]]` 璇硶锛屽繀椤讳娇鐢ㄦ爣鍑?Markdown 鍥剧墖閾炬帴銆?
### 2.4 鍐呴儴鍙岄摼

Quartz 瀹岀編鏀寔 `[[鍙岄摼]]` 璇硶锛屽氨鍍忓湪 Obsidian 涓竴鏍枫€?
- 閾炬帴鍒板彟涓€绡囩瑪璁帮細`[[鍙︿竴绡囩瑪璁扮殑鏂囦欢鍚峕]`
- 甯﹀埆鍚嶏細`[[鍙︿竴绡囩瑪璁皘鏄剧ず鐨勬枃瀛梋]`
- 閾炬帴鍒版爣棰橈細`[[鍙︿竴绡囩瑪璁?灏忔爣棰榏]`

> 鍙岄摼鐨勬枃浠跺悕**涓嶉渶瑕佸姞 `.md`**锛屼笖娉ㄦ剰澶у皬鍐欙紙寤鸿缁熶竴浣跨敤灏忓啓+杩炲瓧绗︼級銆?
### 2.5 鍒犻櫎绗旇

- 鐩存帴鍒犻櫎 `content` 涓殑瀵瑰簲 `.md` 鏂囦欢銆?- 鎻愪氦骞舵帹閫侊紝缃戠珯浼氳嚜鍔ㄧЩ闄よ椤甸潰銆?
---

## 3. 鎻愪氦涓庡彂甯?
### 3.1 浣跨敤 Git 鍛戒护锛堟帹鑽愶級

鎵撳紑缁堢锛圥owerShell銆丆MD 鎴?Git Bash锛夛紝杩涘叆浣犵殑 Quartz 椤圭洰鏍圭洰褰曪紙鍗冲寘鍚?`content` 鏂囦欢澶瑰拰 `quartz.config.ts` 鐨勭洰褰曪級銆?
```bash
# 1. 鏌ョ湅褰撳墠鍙樻洿
git status

# 2. 娣诲姞鎵€鏈夋洿鏀癸紙鏂板銆佷慨鏀广€佸垹闄わ級
git add .

# 3. 鎻愪氦骞跺啓鎻忚堪
git commit -m "鏇存柊鍐呭锛氭坊鍔犱簡鍏充簬XXX鐨勭瑪璁?

# 4. 鎺ㄩ€佸埌 GitHub
git push origin v4
```

> 濡傛灉浣犵殑榛樿鍒嗘敮涓嶆槸 `v4`锛岃灏嗘渶鍚庣殑 `v4` 鏇挎崲涓轰綘鐨勪富鍒嗘敮鍚嶏紙濡?`main`锛夈€?
### 3.2 鍦?GitHub 缃戦〉涓婄洿鎺ユ搷浣滐紙閫傚悎灏戦噺蹇€熶慨鏀癸級

- 杩涘叆浠撳簱 鈫?`content` 鏂囦欢澶?鈫?鐐瑰嚮鏂囦欢杩涜缂栬緫锛屾垨鐐瑰嚮 **Add file** 涓婁紶鏂版枃浠躲€?- 鎻愪氦鍚庝細鑷姩瑙﹀彂鏋勫缓銆?
### 3.3 娉ㄦ剰浜嬮」

- **閬垮厤鏂囦欢鍗犵敤閿欒**锛氬鏋滃湪 Windows 涓婇亣鍒?`EBUSY` 閿欒锛岃鏄庢湁绋嬪簭锛堝 Obsidian銆佹枃浠惰祫婧愮鐞嗗櫒锛夋鍦ㄥ崰鐢?`content` 鏂囦欢澶广€傚叧闂繖浜涚▼搴忓悗閲嶆柊 `git add .` 鍗冲彲銆?- **涓嶈鐢?Obsidian 鐩存帴鎵撳紑 Quartz 椤圭洰鏂囦欢澶?*锛屽惁鍒?Obsidian 浼氶攣瀹氭枃浠躲€傚缓璁皢 Obsidian 绗旇搴撴斁鍦ㄥ彟涓€涓洰褰曪紝鍙妸闇€瑕佸彂甯冪殑绗旇澶嶅埗鍒?`content`銆?
---

## 4. 鑷畾涔夌綉绔欏瑙備笌琛屼负

Quartz 鐨勯厤缃泦涓湪涓や釜 TypeScript 鏂囦欢锛歚quartz.config.ts` 鍜?`quartz.layout.ts`銆備慨鏀瑰悗闇€瑕侀噸鏂版瀯寤哄苟鎺ㄩ€併€?
### 4.1 鍩烘湰閰嶇疆 (`quartz.config.ts`)

| 閰嶇疆椤?| 璇存槑 | 绀轰緥 |
|--------|------|------|
| `pageTitle` | 缃戠珯鏍囬锛堟樉绀哄湪娴忚鍣ㄦ爣绛鹃〉锛?| `"鎴戠殑鏁板瓧鑺卞洯"` |
| `pageTitleSuffix` | 鏍囬鍚庣紑锛堝彲閫夛級 | `" | Obsidian"` |
| `enableSPA` | 鏄惁鍚敤鍗曢〉搴旂敤妯″紡锛堝钩婊戝垏鎹級 | `true` / `false` |
| `enablePopovers` | 榧犳爣鎮仠鏃舵樉绀洪摼鎺ラ瑙?| `true` / `false` |
| `locale` | 鐣岄潰璇█ | `"zh-CN"` 涓枃锛宍"en-US"` 鑻辨枃 |
| `baseUrl` | 浣犵殑缃戠珯鍩熷悕锛堜笉鍖呭惈 `https://`锛?| `"yourname.github.io/quartz"` |
| `ignorePatterns` | 蹇界暐鐨勬枃浠?鏂囦欢澶癸紙姝ｅ垯锛?| `["private", "drafts/*"]` |

### 4.2 甯冨眬閰嶇疆 (`quartz.layout.ts`)

鎺у埗椤甸潰鍚勪釜鍖哄煙锛堥〉鐪夈€侀〉鑴氥€佷晶杈规爮锛夋樉绀哄摢浜涚粍浠躲€?
```typescript
export const defaultLayout: Layout = {
  pageBody: "Page",           // 涓讳綋鍐呭
  header: [
    { type: "Component", name: "Header" },
    { type: "Search", name: "Search" },     // 鎼滅储妗?  ],
  left: [
    { type: "PageList", name: "PageList" }, // 鏂囦欢鍒楄〃
    { type: "RecentNotes", name: "Recent" },// 鏈€杩戠瑪璁?    { type: "DesktopOnly", name: "TableOfContents" }, // 鐩綍锛堜粎妗岄潰锛?  ],
  right: [
    { type: "Graph", name: "Graph" },       // 灞€閮ㄥ叧绯诲浘璋?    { type: "Backlinks", name: "Backlinks" }, // 鍙嶅悜閾炬帴
  ],
  footer: [
    { type: "Links", name: "Links" },       // 椤佃剼閾炬帴
  ],
}
```

浣犲彲浠ユ敞閲婃帀涓嶉渶瑕佺殑缁勪欢锛屾垨璋冩暣椤哄簭銆?
### 4.3 鏇存崲涓婚棰滆壊

缂栬緫 `quartz/styles/custom.scss`锛堝鏋滄病鏈夊氨鏂板缓锛夈€備緥濡傦細

```scss
:root {
  --primary: #2e6e9e;      // 涓昏壊璋冿紙閾炬帴銆佹寜閽級
  --background: #f5f5f5;   // 鑳屾櫙鑹?  --gray: #4a5568;         // 鏂囧瓧鐏?}
```

淇敼鍚庨渶瑕侀噸鏂版瀯寤猴紙`npx quartz build`锛夊苟鎺ㄩ€併€?
### 4.4 娣诲姞鑷畾涔夐〉闈紙濡傗€滃叧浜庘€濓級

鍦?`content` 鐩綍涓嬪垱寤轰竴涓?`.md` 鏂囦欢锛屼緥濡?`about.md`銆傜劧鍚庡湪 `quartz.layout.ts` 鐨勯〉鐪夌粍浠朵腑娣诲姞瀵艰埅閾炬帴锛?
```typescript
header: [
  { type: "Component", name: "Header" },
  { type: "PageList", name: "PageList" },
  { type: "Links", name: "CustomLinks", links: [
    { title: "鍏充簬", link: "/about" },
    { title: "GitHub", link: "https://github.com/浣犵殑鐢ㄦ埛鍚? },
  ]},
]
```

### 4.5 鍚敤璇勮鍔熻兘

鎺ㄨ崘浣跨敤 **Giscus**锛堝熀浜?GitHub Discussions锛夈€傞厤缃柟娉曪細

1. 瀹夎 Giscus 鎻掍欢锛堝湪 `quartz.config.ts` 鐨?`plugins` 鏁扮粍涓坊鍔狅級銆?2. 鑾峰彇浣犵殑 Giscus 浠撳簱閰嶇疆锛堥渶瑕?GitHub 浠撳簱鍏紑锛夈€?3. 鍦?`quartz.layout.ts` 鐨?`footer` 鍖哄煙娣诲姞 `{ type: "Giscus", name: "Giscus" }`銆?
鍏蜂綋鍙傝€?[Giscus 瀹樼綉](https://giscus.app/)銆?
---

## 5. 鏈湴棰勮锛堝彲閫夛級

鍦ㄦ帹閫佸墠锛屼綘鍙互鍦ㄦ湰鍦伴瑙堢綉绔欐晥鏋滐紝閬垮厤鍙嶅鎻愪氦銆?
### 5.1 鍚姩鏈湴鏈嶅姟鍣?
纭繚宸插畨瑁?Node.js锛?=22锛夈€傚湪椤圭洰鏍圭洰褰曟墽琛岋細

```bash
npx quartz build --serve
```

缁堢浼氭樉绀?`Started a Quartz server listening at http://localhost:8080`锛岀敤娴忚鍣ㄦ墦寮€璇ュ湴鍧€鍗冲彲銆?
### 5.2 瀹炴椂鏇存柊

鏈湴淇敼 `content` 涓嬬殑鏂囦欢鍚庯紝闇€瑕?*閲嶅惎鏈嶅姟鍣?*鎵嶈兘鐪嬪埌鍙樺寲锛堟寜 `Ctrl+C` 鍋滄锛屽啀閲嶆柊杩愯 `npx quartz build --serve`锛夈€俀uartz 榛樿涓嶇洃鍚枃浠跺彉鍔紝浣嗗彲浠ュ畨瑁?`nodemon` 绛夊伐鍏峰疄鐜拌嚜鍔ㄩ噸鍚紝浣嗛潪蹇呴渶銆?
### 5.3 閫€鍑洪瑙?
鍦ㄧ粓绔腑鎸?`Ctrl+C` 鍗冲彲鍋滄鏈嶅姟鍣ㄣ€?
---

## 6. 甯歌闂

### Q1锛氱綉绔欐洿鏂板悗娌℃湁鍙樺寲锛?
- 妫€鏌?GitHub Actions 鏄惁鎴愬姛锛堢豢鑹?鉁咃級銆傚鏋滃け璐ワ紝鐐瑰嚮鏌ョ湅鏃ュ織銆?- 寮哄埗鍒锋柊娴忚鍣紙`Ctrl + F5` 鎴?`Cmd + Shift + R`锛夈€?- 绛夊緟 1-2 鍒嗛挓锛孏itHub Pages 鏈夋椂鏈夌紦瀛樸€?
### Q2锛氫腑鏂囨枃浠跺悕瀵艰嚧閾炬帴涔辩爜鎴?404锛?
- 绔嬪嵆灏嗘枃浠跺悕鏀逛负鑻辨枃锛堝 `濡備綍瀛︿範.md` 鈫?`how-to-learn.md`锛夛紝骞朵慨鏀规墍鏈夊紩鐢ㄨ鏂囦欢鐨勫弻閾俱€?- 鎻愪氦鏇存敼锛岄噸鏂伴儴缃层€?
### Q3锛氬浘鐗囦笉鏄剧ず锛?
- 妫€鏌ュ浘鐗囪矾寰勬槸鍚︿互 `./` 鎴?`../` 寮€澶达紝骞朵笖鏂囦欢纭疄瀛樺湪銆?- 鍥剧墖鏂囦欢鍚嶄篃寤鸿鐢ㄨ嫳鏂囷紝閬垮厤绌烘牸鍜屼腑鏂囥€?
### Q4锛氭兂闅愯棌鏌愮瘒绗旇锛屼笉璁╁畠鍑虹幇鍦ㄧ綉绔欎笂锛?
- 涓嶈灏嗚绗旇鏀惧叆 `content` 鏂囦欢澶癸紝鎴栬€呮斁鍏?`content` 涓嬬殑涓€涓瓙鏂囦欢澶瑰苟鍦?`ignorePatterns` 涓帓闄ゃ€?- 涔熷彲浠ュ湪 Frontmatter 涓坊鍔?`draft: true`锛堥渶瑕佹彃浠舵敮鎸侊紝Quartz 榛樿涓嶅鐞?draft锛夈€?
### Q5锛氬浣曞浠芥暣涓暟瀛楄姳鍥紵

- 浣犵殑鏈湴 `quartz` 鏂囦欢澶瑰拰 GitHub 浠撳簱宸茬粡鏄畬鏁村浠姐€傚畾鏈?`git push` 鍗冲彲銆?
---

## 7. 杩涢樁鎶€宸?
### 7.1 浠?Obsidian 鑷姩鍚屾绗旇

浣犲彲浠ュ啓涓€涓畝鍗曠殑鑴氭湰锛坄.bat` 鎴?`.sh`锛夛紝灏?Obsidian 浠撳簱涓殑鐗瑰畾鏂囦欢澶瑰鍒跺埌 Quartz 鐨?`content` 鏂囦欢澶癸紝鐒跺悗鑷姩鎻愪氦鎺ㄩ€併€備緥濡?Windows 鎵瑰鐞嗭細

```batch
xcopy "D:\鎴戠殑Obsidian搴揬鍙戝竷\" "C:\鏈夌敤杞欢\obsidian-web\quartz\content\" /E /Y
cd C:\鏈夌敤杞欢\obsidian-web\quartz
git add .
git commit -m "鑷姩鍚屾 %date% %time%"
git push origin v4
```

### 7.2 浣跨敤鏍囩鍜屾悳绱?
Quartz 鍐呯疆鍏ㄦ枃鎼滅储锛屾敮鎸佷腑鏂囷紙浣嗗垎璇嶆晥鏋滀竴鑸級銆傚缓璁负绗旇娣诲姞 `tags` Frontmatter锛屽埄鐢ㄧ粍浠?`TagList` 瀹炵幇鎸夋爣绛捐繃婊ゃ€?
### 7.3 鑷畾涔夊煙鍚?
鍦?GitHub Pages 璁剧疆涓粦瀹氳嚜宸辩殑鍩熷悕锛屽苟鍦ㄤ粨搴撴牴鐩綍娣诲姞 `CNAME` 鏂囦欢锛堝唴瀹逛负浣犵殑鍩熷悕锛夈€傚悓鏃朵慨鏀?`quartz.config.ts` 涓殑 `baseUrl`銆?
---

## 8. 鑾峰彇甯姪

- **瀹樻柟鏂囨。**锛歔quartz.jzhao.xyz](https://quartz.jzhao.xyz/)
- **涓枃绀惧尯**锛歔Obsidian 涓枃璁哄潧](https://forum-zh.obsidian.md/) 鎼滅储 鈥淨uartz鈥?- **GitHub 浠撳簱**锛氭彁浜?[Issues](https://github.com/jackyzha0/quartz/issues)

---

鐜板湪浣犲彲浠ユ剦蹇湴缁存姢鑷繁鐨勬暟瀛楄姳鍥簡锛佸鏋滈亣鍒版枃妗ｆ湭瑕嗙洊鐨勯棶棰橈紝闅忔椂鍥炴潵闂垜銆
