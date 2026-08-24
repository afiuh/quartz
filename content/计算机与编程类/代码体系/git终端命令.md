---
---

git add .
git commit -m "淇敼璇存槑"
git push
灏嗙幇鍦ㄦ枃浠跺す閲屾墍鏈夌殑鏂囦欢鏇存敼鍚屾鍒癎itHub杩滅▼浠撳簱
鍏嬮殕鍒板綋鍓嶇洰褰曚笅鐨勯粯璁ゆ枃浠跺す锛堜粨搴撳悕锛夛細
    
    bash
    
    git clone https://github.com/鐢ㄦ埛鍚?浠撳簱鍚?git
    
浠ヤ笅鏄?Git 甯哥敤鍛戒护鐨勫垎绫绘暣鐞嗭紝娑电洊浠庡垵濮嬪寲鍒拌繙绋嬪崗浣滅殑甯歌鎿嶄綔銆傜敱浜?Git 鍛戒护浼楀锛岃繖閲屼富瑕佸垪鍑哄疄闄呭紑鍙戜腑楂橀浣跨敤鐨勫懡浠わ紝骞堕檮绠€瑕佽鏄庛€?
## 涓€銆佸垵濮嬮厤缃?
```bash
git config --global user.name "Your Name"    # 璁剧疆鍏ㄥ眬鐢ㄦ埛鍚?git config --global user.email "email@example.com"  # 璁剧疆鍏ㄥ眬閭
git config --global core.editor "code --wait"       # 璁剧疆榛樿缂栬緫鍣?git config --list               # 鏌ョ湅鎵€鏈夐厤缃?git config --global alias.co checkout  # 璁剧疆鍛戒护鍒悕
```

## 浜屻€佷粨搴撳垱寤轰笌鍏嬮殕

```bash
git init                        # 鍒濆鍖栧綋鍓嶇洰褰曚负浠撳簱
git clone <url>                 # 鍏嬮殕杩滅▼浠撳簱
git clone --depth 1 <url>       # 娴呭厠闅嗭紙鍙媺鍙栨渶鏂颁竴娆℃彁浜わ級
```

## 涓夈€佸熀鏈揩鐓ф搷浣?
```bash
git status                      # 鏌ョ湅宸ヤ綔鍖轰笌鏆傚瓨鍖虹姸鎬?git add <file>                  # 娣诲姞鎸囧畾鏂囦欢鍒版殏瀛樺尯
git add .                       # 娣诲姞鎵€鏈夊彉鏇存枃浠?git add -p                      # 浜や簰寮忔坊鍔狅紙閫愬潡纭锛?git rm <file>                   # 鍒犻櫎鏂囦欢骞朵粠鏆傚瓨鍖虹Щ闄?git mv <old> <new>              # 绉诲姩/閲嶅懡鍚嶆枃浠?git commit -m "message"         # 鎻愪氦鏆傚瓨鍖哄唴瀹?git commit -am "message"        # 璺宠繃 add 鐩存帴鎻愪氦宸茶窡韪枃浠?git commit --amend              # 淇敼涓婁竴娆℃彁浜わ紙閲嶅啓鍘嗗彶锛?```

## 鍥涖€佸樊寮備笌鏌ョ湅鍘嗗彶

```bash
git diff                        # 宸ヤ綔鍖?vs 鏆傚瓨鍖?git diff --staged               # 鏆傚瓨鍖?vs 鏈€鏂版彁浜?git diff HEAD                   # 宸ヤ綔鍖?vs 鏈€鏂版彁浜?git diff <commit1> <commit2>    # 姣旇緝涓や釜鎻愪氦
git log                         # 鏄剧ず鎻愪氦鍘嗗彶
git log --oneline --graph --all # 绠€娲佸浘褰㈠紡鍘嗗彶
git log -p                      # 鏄剧ず鍏蜂綋鏀瑰姩鍐呭
git reflog                      # 璁板綍鎵€鏈?HEAD 鍙樺姩锛堟仮澶嶈鍒犳彁浜わ級
git show <commit>               # 鏄剧ず鏌愭鎻愪氦鐨勮缁嗕俊鎭?```

## 浜斻€佹挙閿€涓庨噸缃?
```bash
git restore <file>              # 鎾ら攢宸ヤ綔鍖轰慨鏀癸紙鏈?add锛?git restore --staged <file>     # 灏嗘枃浠剁Щ鍑烘殏瀛樺尯锛堜絾淇濈暀淇敼锛?git reset <file>                # 鍚屼笂锛屾棫鍐欐硶
git reset --soft HEAD~1         # 鎾ら攢鎻愪氦锛屾敼鍔ㄥ洖鍒版殏瀛樺尯
git reset --mixed HEAD~1        # 鎾ら攢鎻愪氦锛屾敼鍔ㄥ洖鍒板伐浣滃尯锛堥粯璁わ級
git reset --hard HEAD~1         # 瀹屽叏鍒犻櫎涓婁竴娆℃彁浜わ紙鍗遍櫓锛?git revert <commit>             # 鐢熸垚涓€涓柊鎻愪氦鏉ユ姷娑堟寚瀹氭彁浜ょ殑鏀瑰姩
```

## 鍏€佸垎鏀鐞?
```bash
git branch                      # 鍒楀嚭鏈湴鍒嗘敮锛堝綋鍓嶅甫*锛?git branch -r                   # 鍒楀嚭杩滅▼鍒嗘敮
git branch -a                   # 鍒楀嚭鎵€鏈夊垎鏀?git branch <branch-name>        # 鍒涘缓鏂板垎鏀?git branch -d <branch>          # 鍒犻櫎鍒嗘敮锛堝凡鍚堝苟锛?git branch -D <branch>          # 寮哄埗鍒犻櫎鍒嗘敮
git branch -m <old> <new>       # 閲嶅懡鍚嶅垎鏀?git switch <branch>             # 鍒囨崲鍒嗘敮锛堟帹鑽愶級
git checkout <branch>           # 鍒囨崲鍒嗘敮锛堟棫鍛戒护锛?git switch -c <new-branch>      # 鍒涘缓骞跺垏鎹㈠垎鏀?git checkout -b <new-branch>    # 鍚屼笂锛堟棫鍛戒护锛?git merge <branch>              # 灏嗘寚瀹氬垎鏀悎骞跺埌褰撳墠鍒嗘敮
git merge --abort               # 涓鍚堝苟锛堣В鍐冲啿绐佸墠锛?git rebase <base-branch>        # 鍙樺熀鎿嶄綔锛堟暣鐞嗘彁浜ゅ巻鍙诧級
git rebase --continue           # 缁х画鍙樺熀
git rebase --abort              # 鏀惧純鍙樺熀
```

## 涓冦€佽繙绋嬩粨搴撳崗浣?
```bash
git remote -v                   # 鏌ョ湅杩滅▼浠撳簱鍒悕鍙婂湴鍧€
git remote add origin <url>     # 娣诲姞杩滅▼浠撳簱锛堝懡鍚?origin锛?git remote remove <name>        # 鍒犻櫎杩滅▼浠撳簱
git remote rename <old> <new>   # 閲嶅懡鍚嶈繙绋嬪埆鍚?git fetch                       # 鎷夊彇杩滅▼鏇存柊锛堜笉鍚堝苟锛?git fetch --prune               # 鎷夊彇骞跺垹闄ゆ湰鍦板凡涓嶅瓨鍦ㄧ殑杩滅▼鍒嗘敮寮曠敤
git pull                        # fetch + merge 锛堟媺鍙栧苟鍚堝苟锛?git pull --rebase               # fetch + rebase
git push                        # 鎺ㄩ€佸綋鍓嶅垎鏀埌杩滅▼鍚屽悕鍒嗘敮
git push -u origin <branch>     # 鎺ㄩ€佸苟寤虹珛涓婃父璺熻釜
git push --force                # 寮哄埗鎺ㄩ€侊紙瑕嗙洊杩滅▼锛岃皑鎱庯級
git push --force-with-lease     # 鏇村畨鍏ㄧ殑寮哄埗鎺ㄩ€?git push origin --delete <branch>   # 鍒犻櫎杩滅▼鍒嗘敮
git push --tags                 # 鎺ㄩ€佹爣绛惧埌杩滅▼
```

## 鍏€佹爣绛剧鐞?
```bash
git tag                         # 鍒楀嚭鎵€鏈夋爣绛?git tag <tagname>               # 鍒涘缓杞婚噺鏍囩
git tag -a <tagname> -m "msg"   # 鍒涘缓闄勬敞鏍囩
git show <tagname>              # 鏌ョ湅鏍囩淇℃伅
git tag -d <tagname>            # 鍒犻櫎鏈湴鏍囩
git push origin <tagname>       # 鎺ㄩ€佸崟涓爣绛?git push origin --tags          # 鎺ㄩ€佹墍鏈夋爣绛?git push origin --delete <tagname>  # 鍒犻櫎杩滅▼鏍囩
```

## 涔濄€佹殏瀛樹笌娓呯悊

```bash
git stash                       # 鏆傚瓨褰撳墠鏈彁浜ょ殑淇敼
git stash save "message"        # 甯﹁鏄庣殑鏆傚瓨
git stash list                  # 鏌ョ湅鏆傚瓨鍒楄〃
git stash apply                 # 搴旂敤鏈€鏂版殏瀛樹絾涓嶅垹闄?git stash pop                   # 搴旂敤骞跺垹闄ゆ渶鏂版殏瀛?git stash drop                  # 鍒犻櫎鎸囧畾鏆傚瓨
git stash clear                 # 娓呯┖鎵€鏈夋殏瀛?git clean -n                    # 棰勮浼氳鍒犻櫎鐨勬湭璺熻釜鏂囦欢
git clean -f                    # 寮哄埗鍒犻櫎鏈窡韪枃浠?git clean -fd                   # 鍚屾椂鍒犻櫎鏈窡韪洰褰?```

## 鍗併€佽皟璇曚笌楂樼骇

```bash
git bisect start                # 寮€濮嬩簩鍒嗘煡鎵惧畾浣?bug 寮曞叆鐨勬彁浜?git bisect bad                  # 鏍囪褰撳墠鎻愪氦涓哄潖
git bisect good <commit>        # 鏍囪宸茬煡濂芥彁浜?git bisect reset                # 缁撴潫浜屽垎鏌ユ壘
git grep "pattern"              # 鍦ㄤ唬鐮佸簱涓悳绱㈠瓧绗︿覆
git blame <file>                # 鏌ョ湅鏂囦欢姣忎竴琛岀殑鏈€鍚庝慨鏀逛俊鎭?git cherry-pick <commit>        # 鎷ｉ€夋煇涓彁浜ゅ埌褰撳墠鍒嗘敮
git worktree add <path> <branch>   # 鍒涘缓鏂板伐浣滄爲骞惰寮€鍙?```

## 鍗佷竴銆佸瓙妯″潡

```bash
git submodule add <url>         # 娣诲姞瀛愭ā鍧?git submodule update --init     # 鍒濆鍖栧苟鎷夊彇瀛愭ā鍧?git submodule update --remote   # 鏇存柊瀛愭ā鍧楀埌鏈€鏂版彁浜?git clone --recursive <url>     # 鍏嬮殕浠撳簱骞跺悓鏃跺垵濮嬪寲瀛愭ā鍧?```

## 鍗佷簩銆佸父瑙侀棶棰樹慨澶?
```bash
# 鎾ら攢涓婁竴娆?push锛堣皑鎱庝娇鐢紝闇€寮哄埗鎺ㄩ€侊級
git reset --soft HEAD~1
git push --force-with-lease

# 涓㈠純鏈湴鎵€鏈夋湭鎻愪氦淇敼锛堥噸缃埌鏈€鏂版彁浜わ級
git reset --hard HEAD

# 淇敼鏈€鏂版彁浜ょ殑 message
git commit --amend -m "new message"

# 灏嗛儴鍒嗘枃浠舵敼鍔ㄧЩ鍔ㄥ埌鏂板垎鏀?git stash
git checkout -b new-branch
git stash pop
```

> **鎻愮ず**锛氫娇鐢?`git <command> --help` 鍙煡鐪嬭鍛戒护鐨勫畬鏁存枃妗ｏ紙濡?`git commit --help`锛夈€備互涓婂懡浠よ鐩栦簡鏃ュ父寮€鍙?95% 浠ヤ笂鐨勫満鏅紝鏇村搴曞眰鍛戒护锛堝 `git cat-file`銆乣git fsck` 绛夛級璇峰弬鑰冨畼鏂规枃妗ｃ€?

## 馃幆 鏍稿績瑙勫垯锛堜互鍚庡氨鎸夎繖涓級

|浣犲湪鍝彴鐢佃剳涓妡浣犵殑榛樿鍒嗘敮|瑕佹墽琛岀殑鍚堝苟鎿嶄綔|
|---|---|---|
|**Windows 绯荤粺**|`main`|`git merge origin/ubuntu`锛堟妸 Ubuntu 鐢佃剳鐨勬洿鏂版媺杩囨潵锛墊
|**Ubuntu 绯荤粺**|`ubuntu`|`git merge origin/main`锛堟妸 Windows 鐢佃剳鐨勬洿鏂版媺杩囨潵锛墊

---

## 馃摑 瀹屾暣鎿嶄綔娴佺▼锛堜互浣犱粖澶╃殑鍦烘櫙涓轰緥锛?
鍋囪浣犱粖澶╁湪聽**Windows**聽涓婏紝鎯虫嬁鍒颁箣鍓嶅湪聽**Ubuntu**聽涓婂啓鐨勭瑪璁帮細

powershell

# 1. 鍏堟媺鍙栬繙绋嬫墍鏈夋渶鏂颁俊鎭紙蹇呴』锛?git fetch origin
# 2. 鍒囨崲鍒?Windows 瀵瑰簲鐨勫垎鏀紙main锛?git checkout main
# 3. 鎶?Ubuntu 鐨勬洿鏂板悎骞惰繘鏉?git merge origin/ubuntu
# 4. 鎺ㄩ€佸埌杩滅▼锛岃 Ubuntu 閭ｈ竟涔熻兘鐪嬪埌
git push origin main

> 鍙嶈繃鏉ワ紝濡傛灉浣犲湪聽**Ubuntu**聽涓婏紝鎯虫嬁 Windows 鐨勬洿鏂帮紝灏辨槸鎶婁笂闈㈢殑聽`main`聽鍜屄燻ubuntu`聽浜掓崲锛?> 
> bash
> 
> git checkout ubuntu
> git merge origin/main
> git push origin ubuntu

---

## 鈿狅笍 閲嶈鎻愰啋锛氭湭鏉ョ殑鍐茬獊鎬庝箞澶勭悊

鍥犱负涓や釜鍒嗘敮**瀹屽叏瀵圭瓑**锛屼互鍚庝綘鍦?Windows 涓婂啓浜嗕竴浜涙柊鍐呭锛屽悓鏃?Ubuntu 涓婁篃鍐欎簡涓€浜涙柊鍐呭锛?*浜掔浉鍚堝苟鏃朵竴瀹氫細浜х敓鍐茬獊**锛堝洜涓洪兘鏈夋柊鐨勬彁浜わ級銆?
### 鎬庝箞閬垮厤鍐茬獊鐖嗙偢锛?
**榛勯噾涔犳儻锛氭瘡娆″紑濮嬪啓绗旇鍓嶏紝鍏堟媺鍙栧鏂圭殑鏈€鏂板唴瀹广€?*

涓句釜渚嬪瓙锛?
- 浠婂ぉ浣犲湪 Windows 鍐欏畬绗旇锛屾帹閫佸埌聽`main`銆?    
- 鏅氫笂浣犲垏鎹㈠埌 Ubuntu 绯荤粺锛?*鎵撳紑 Obsidian 鍐欑瑪璁颁箣鍓?*锛屽厛鎵ц锛?    
    bash
    
    git pull origin main   # 鎶?Windows 鐨勬渶鏂扮瑪璁版媺鍒?Ubuntu 鏈湴
    
    杩欐牱灏卞悎骞跺ソ浜嗭紝鐒跺悗鍐嶅啓鏂扮瑪璁帮紝灏变笉浼氬啿绐併€?    

濡傛灉宸茬粡浜х敓浜嗗啿绐侊紙Git 鎻愮ず聽`CONFLICT`锛夛紝瑙ｅ喅鏂规硶鍜屼粖澶╃湅鍒扮殑鑷姩澶勭悊涓嶅お涓€鏍凤紝浣犻渶瑕佹墜鍔ㄥ鐞嗐€備笉杩?Obsidian 鐨?Markdown 鏂囦欢澶у鏄拷鍔犲唴瀹癸紝鍐茬獊涓€鑸笉浼氬お澶嶆潅銆
