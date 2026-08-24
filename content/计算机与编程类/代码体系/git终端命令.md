---
---

git add .
git commit -m "修改说明"
git push
将现在文件夹里所有的文件更改同步到GitHub远程仓库
克隆到当前目录下的默认文件夹（仓库名）：
    
    bash
    
    git clone https://github.com/用户�?仓库�?git
    
以下�?Git 常用命令的分类整理，涵盖从初始化到远程协作的常见操作。由�?Git 命令众多，这里主要列出实际开发中高频使用的命令，并附简要说明�?
## 一、初始配�?
```bash
git config --global user.name "Your Name"    # 设置全局用户�?git config --global user.email "email@example.com"  # 设置全局邮箱
git config --global core.editor "code --wait"       # 设置默认编辑�?git config --list               # 查看所有配�?git config --global alias.co checkout  # 设置命令别名
```

## 二、仓库创建与克隆

```bash
git init                        # 初始化当前目录为仓库
git clone <url>                 # 克隆远程仓库
git clone --depth 1 <url>       # 浅克隆（只拉取最新一次提交）
```

## 三、基本快照操�?
```bash
git status                      # 查看工作区与暂存区状�?git add <file>                  # 添加指定文件到暂存区
git add .                       # 添加所有变更文�?git add -p                      # 交互式添加（逐块确认�?git rm <file>                   # 删除文件并从暂存区移�?git mv <old> <new>              # 移动/重命名文�?git commit -m "message"         # 提交暂存区内�?git commit -am "message"        # 跳过 add 直接提交已跟踪文�?git commit --amend              # 修改上一次提交（重写历史�?```

## 四、差异与查看历史

```bash
git diff                        # 工作�?vs 暂存�?git diff --staged               # 暂存�?vs 最新提�?git diff HEAD                   # 工作�?vs 最新提�?git diff <commit1> <commit2>    # 比较两个提交
git log                         # 显示提交历史
git log --oneline --graph --all # 简洁图形式历史
git log -p                      # 显示具体改动内容
git reflog                      # 记录所�?HEAD 变动（恢复误删提交）
git show <commit>               # 显示某次提交的详细信�?```

## 五、撤销与重�?
```bash
git restore <file>              # 撤销工作区修改（�?add�?git restore --staged <file>     # 将文件移出暂存区（但保留修改�?git reset <file>                # 同上，旧写法
git reset --soft HEAD~1         # 撤销提交，改动回到暂存区
git reset --mixed HEAD~1        # 撤销提交，改动回到工作区（默认）
git reset --hard HEAD~1         # 完全删除上一次提交（危险�?git revert <commit>             # 生成一个新提交来抵消指定提交的改动
```

## 六、分支管�?
```bash
git branch                      # 列出本地分支（当前带*�?git branch -r                   # 列出远程分支
git branch -a                   # 列出所有分�?git branch <branch-name>        # 创建新分�?git branch -d <branch>          # 删除分支（已合并�?git branch -D <branch>          # 强制删除分支
git branch -m <old> <new>       # 重命名分�?git switch <branch>             # 切换分支（推荐）
git checkout <branch>           # 切换分支（旧命令�?git switch -c <new-branch>      # 创建并切换分�?git checkout -b <new-branch>    # 同上（旧命令�?git merge <branch>              # 将指定分支合并到当前分支
git merge --abort               # 中止合并（解决冲突前�?git rebase <base-branch>        # 变基操作（整理提交历史）
git rebase --continue           # 继续变基
git rebase --abort              # 放弃变基
```

## 七、远程仓库协�?
```bash
git remote -v                   # 查看远程仓库别名及地址
git remote add origin <url>     # 添加远程仓库（命�?origin�?git remote remove <name>        # 删除远程仓库
git remote rename <old> <new>   # 重命名远程别�?git fetch                       # 拉取远程更新（不合并�?git fetch --prune               # 拉取并删除本地已不存在的远程分支引用
git pull                        # fetch + merge （拉取并合并�?git pull --rebase               # fetch + rebase
git push                        # 推送当前分支到远程同名分支
git push -u origin <branch>     # 推送并建立上游跟踪
git push --force                # 强制推送（覆盖远程，谨慎）
git push --force-with-lease     # 更安全的强制推�?git push origin --delete <branch>   # 删除远程分支
git push --tags                 # 推送标签到远程
```

## 八、标签管�?
```bash
git tag                         # 列出所有标�?git tag <tagname>               # 创建轻量标签
git tag -a <tagname> -m "msg"   # 创建附注标签
git show <tagname>              # 查看标签信息
git tag -d <tagname>            # 删除本地标签
git push origin <tagname>       # 推送单个标�?git push origin --tags          # 推送所有标�?git push origin --delete <tagname>  # 删除远程标签
```

## 九、暂存与清理

```bash
git stash                       # 暂存当前未提交的修改
git stash save "message"        # 带说明的暂存
git stash list                  # 查看暂存列表
git stash apply                 # 应用最新暂存但不删�?git stash pop                   # 应用并删除最新暂�?git stash drop                  # 删除指定暂存
git stash clear                 # 清空所有暂�?git clean -n                    # 预览会被删除的未跟踪文件
git clean -f                    # 强制删除未跟踪文�?git clean -fd                   # 同时删除未跟踪目�?```

## 十、调试与高级

```bash
git bisect start                # 开始二分查找定�?bug 引入的提�?git bisect bad                  # 标记当前提交为坏
git bisect good <commit>        # 标记已知好提�?git bisect reset                # 结束二分查找
git grep "pattern"              # 在代码库中搜索字符串
git blame <file>                # 查看文件每一行的最后修改信�?git cherry-pick <commit>        # 拣选某个提交到当前分支
git worktree add <path> <branch>   # 创建新工作树并行开�?```

## 十一、子模块

```bash
git submodule add <url>         # 添加子模�?git submodule update --init     # 初始化并拉取子模�?git submodule update --remote   # 更新子模块到最新提�?git clone --recursive <url>     # 克隆仓库并同时初始化子模�?```

## 十二、常见问题修�?
```bash
# 撤销上一�?push（谨慎使用，需强制推送）
git reset --soft HEAD~1
git push --force-with-lease

# 丢弃本地所有未提交修改（重置到最新提交）
git reset --hard HEAD

# 修改最新提交的 message
git commit --amend -m "new message"

# 将部分文件改动移动到新分�?git stash
git checkout -b new-branch
git stash pop
```

> **提示**：使�?`git <command> --help` 可查看该命令的完整文档（�?`git commit --help`）。以上命令覆盖了日常开�?95% 以上的场景，更多底层命令（如 `git cat-file`、`git fsck` 等）请参考官方文档�?

## 🎯 核心规则（以后就按这个）

|你在哪台电脑上|你的默认分支|要执行的合并操作|
|---|---|---|
|**Windows 系统**|`main`|`git merge origin/ubuntu`（把 Ubuntu 电脑的更新拉过来）|
|**Ubuntu 系统**|`ubuntu`|`git merge origin/main`（把 Windows 电脑的更新拉过来）|

---

## 📝 完整操作流程（以你今天的场景为例�?
假设你今天在 **Windows** 上，想拿到之前在 **Ubuntu** 上写的笔记：

powershell

# 1. 先拉取远程所有最新信息（必须�?git fetch origin
# 2. 切换�?Windows 对应的分支（main�?git checkout main
# 3. �?Ubuntu 的更新合并进�?git merge origin/ubuntu
# 4. 推送到远程，让 Ubuntu 那边也能看到
git push origin main

> 反过来，如果你在 **Ubuntu** 上，想拿 Windows 的更新，就是把上面的 `main` 和 `ubuntu` 互换�?> 
> bash
> 
> git checkout ubuntu
> git merge origin/main
> git push origin ubuntu

---

## ⚠️ 重要提醒：未来的冲突怎么处理

因为两个分支**完全对等**，以后你�?Windows 上写了一些新内容，同�?Ubuntu 上也写了一些新内容�?*互相合并时一定会产生冲突**（因为都有新的提交）�?
### 怎么避免冲突爆炸�?
**黄金习惯：每次开始写笔记前，先拉取对方的最新内容�?*

举个例子�?
- 今天你在 Windows 写完笔记，推送到 `main`�?    
- 晚上你切换到 Ubuntu 系统�?*打开 Obsidian 写笔记之�?*，先执行�?    
    bash
    
    git pull origin main   # �?Windows 的最新笔记拉�?Ubuntu 本地
    
    这样就合并好了，然后再写新笔记，就不会冲突�?    

如果已经产生了冲突（Git 提示 `CONFLICT`），解决方法和今天看到的自动处理不太一样，你需要手动处理。不�?Obsidian �?Markdown 文件大多是追加内容，冲突一般不会太复杂�
