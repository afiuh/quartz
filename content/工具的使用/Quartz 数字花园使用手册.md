---
---


## 1. 核心工作流程

你的数字花园是一�?Git 仓库 + GitHub Actions 自动构建的静态网站。日常使用只需要三步：

1. **编辑内容**：在 `content` 文件夹中添加、修改或删除 `.md` 文件�?2. **提交变更**：使�?Git 命令提交本地更改�?3. **推送上�?*：将提交推送到 GitHub，Actions 自动构建并更新网站�?
> 整个流程�?1 分钟生效，无需手动触发构建（除非你关闭了自动部署）�?
---

## 2. 管理笔记内容

### 2.1 添加新笔�?
- **位置**：所有笔记必须放�?[content](file:///C:%5C有用软件%5Cobsidian-web%5Cquartz%5Ccontent) 文件夹内（可以创建子文件夹分类）�?- **文件格式**：`.md`（Markdown）�?- **命名规范**�?*强烈建议使用英文**，如 `my-article.md`。避免空格、中文、特殊符号（`@#$%` 等）�?  - �?`obsidian-tips.md`
  - �?`Obsidian技�?md`
  - �?`how-to-use-git.md`
- **内容模板**（可选）：在文件开头添�?YAML Frontmatter 可以控制页面标题、日期、标签等�?
```markdown
---
title: 我的文章标题（会显示在浏览器标签页和页面顶部�?date: 2026-04-20
tags:
  - obsidian
  - quartz
---

正文使用标准 Markdown 语法...
```

### 2.2 设置标题和日�?
- **标题**：如果写�?`title`，网页会使用它；否则使用文件名（去除扩展名）�?- **日期**：Quartz 默认会从 Git 提交历史中读取创建和修改时间。也可以手动指定�?  ```yaml
  date: 2026-04-20
  updated: 2026-04-21
  ```

### 2.3 插入图片和附�?
- 将图片（`.png`, `.jpg` 等）�?PDF 等文件放�?`content` 文件夹内的任意位置（建议建立 `assets` �?`images` 子文件夹）�?- �?Markdown 中使�?*相对路径**引用�?
```markdown
![图片说明](./images/example.png)
[下载 PDF](./files/manual.pdf)
```

> 注意：不支持 Obsidian �?`![[attachment]]` 语法，必须使用标�?Markdown 图片链接�?
### 2.4 内部双链

Quartz 完美支持 `[[双链]]` 语法，就像在 Obsidian 中一样�?
- 链接到另一篇笔记：`[[另一篇笔记的文件名]]`
- 带别名：`[[另一篇笔记|显示的文字]]`
- 链接到标题：`[[另一篇笔�?小标题]]`

> 双链的文件名**不需要加 `.md`**，且注意大小写（建议统一使用小写+连字符）�?
### 2.5 删除笔记

- 直接删除 `content` 中的对应 `.md` 文件�?- 提交并推送，网站会自动移除该页面�?
---

## 3. 提交与发�?
### 3.1 使用 Git 命令（推荐）

打开终端（PowerShell、CMD �?Git Bash），进入你的 Quartz 项目根目录（即包�?`content` 文件夹和 `quartz.config.ts` 的目录）�?
```bash
# 1. 查看当前变更
git status

# 2. 添加所有更改（新增、修改、删除）
git add .

# 3. 提交并写描述
git commit -m "更新内容：添加了关于XXX的笔�?

# 4. 推送到 GitHub
git push origin v4
```

> 如果你的默认分支不是 `v4`，请将最后的 `v4` 替换为你的主分支名（�?`main`）�?
### 3.2 �?GitHub 网页上直接操作（适合少量快速修改）

- 进入仓库 �?`content` 文件�?�?点击文件进行编辑，或点击 **Add file** 上传新文件�?- 提交后会自动触发构建�?
### 3.3 注意事项

- **避免文件占用错误**：如果在 Windows 上遇�?`EBUSY` 错误，说明有程序（如 Obsidian、文件资源管理器）正在占�?`content` 文件夹。关闭这些程序后重新 `git add .` 即可�?- **不要�?Obsidian 直接打开 Quartz 项目文件�?*，否�?Obsidian 会锁定文件。建议将 Obsidian 笔记库放在另一个目录，只把需要发布的笔记复制�?`content`�?
---

## 4. 自定义网站外观与行为

Quartz 的配置集中在两个 TypeScript 文件：`quartz.config.ts` �?`quartz.layout.ts`。修改后需要重新构建并推送�?
### 4.1 基本配置 (`quartz.config.ts`)

| 配置�?| 说明 | 示例 |
|--------|------|------|
| `pageTitle` | 网站标题（显示在浏览器标签页�?| `"我的数字花园"` |
| `pageTitleSuffix` | 标题后缀（可选） | `" | Obsidian"` |
| `enableSPA` | 是否启用单页应用模式（平滑切换） | `true` / `false` |
| `enablePopovers` | 鼠标悬停时显示链接预�?| `true` / `false` |
| `locale` | 界面语言 | `"zh-CN"` 中文，`"en-US"` 英文 |
| `baseUrl` | 你的网站域名（不包含 `https://`�?| `"yourname.github.io/quartz"` |
| `ignorePatterns` | 忽略的文�?文件夹（正则�?| `["private", "drafts/*"]` |

### 4.2 布局配置 (`quartz.layout.ts`)

控制页面各个区域（页眉、页脚、侧边栏）显示哪些组件�?
```typescript
export const defaultLayout: Layout = {
  pageBody: "Page",           // 主体内容
  header: [
    { type: "Component", name: "Header" },
    { type: "Search", name: "Search" },     // 搜索�?  ],
  left: [
    { type: "PageList", name: "PageList" }, // 文件列表
    { type: "RecentNotes", name: "Recent" },// 最近笔�?    { type: "DesktopOnly", name: "TableOfContents" }, // 目录（仅桌面�?  ],
  right: [
    { type: "Graph", name: "Graph" },       // 局部关系图�?    { type: "Backlinks", name: "Backlinks" }, // 反向链接
  ],
  footer: [
    { type: "Links", name: "Links" },       // 页脚链接
  ],
}
```

你可以注释掉不需要的组件，或调整顺序�?
### 4.3 更换主题颜色

编辑 `quartz/styles/custom.scss`（如果没有就新建）。例如：

```scss
:root {
  --primary: #2e6e9e;      // 主色调（链接、按钮）
  --background: #f5f5f5;   // 背景�?  --gray: #4a5568;         // 文字�?}
```

修改后需要重新构建（`npx quartz build`）并推送�?
### 4.4 添加自定义页面（如“关于”）

�?`content` 目录下创建一�?`.md` 文件，例�?`about.md`。然后在 `quartz.layout.ts` 的页眉组件中添加导航链接�?
```typescript
header: [
  { type: "Component", name: "Header" },
  { type: "PageList", name: "PageList" },
  { type: "Links", name: "CustomLinks", links: [
    { title: "关于", link: "/about" },
    { title: "GitHub", link: "https://github.com/你的用户�? },
  ]},
]
```

### 4.5 启用评论功能

推荐使用 **Giscus**（基�?GitHub Discussions）。配置方法：

1. 安装 Giscus 插件（在 `quartz.config.ts` �?`plugins` 数组中添加）�?2. 获取你的 Giscus 仓库配置（需�?GitHub 仓库公开）�?3. �?`quartz.layout.ts` �?`footer` 区域添加 `{ type: "Giscus", name: "Giscus" }`�?
具体参�?[Giscus 官网](https://giscus.app/)�?
---

## 5. 本地预览（可选）

在推送前，你可以在本地预览网站效果，避免反复提交�?
### 5.1 启动本地服务�?
确保已安�?Node.js�?=22）。在项目根目录执行：

```bash
npx quartz build --serve
```

终端会显�?`Started a Quartz server listening at http://localhost:8080`，用浏览器打开该地址即可�?
### 5.2 实时更新

本地修改 `content` 下的文件后，需�?*重启服务�?*才能看到变化（按 `Ctrl+C` 停止，再重新运行 `npx quartz build --serve`）。Quartz 默认不监听文件变动，但可以安�?`nodemon` 等工具实现自动重启，但非必需�?
### 5.3 退出预�?
在终端中�?`Ctrl+C` 即可停止服务器�?
---

## 6. 常见问题

### Q1：网站更新后没有变化�?
- 检�?GitHub Actions 是否成功（绿�?✅）。如果失败，点击查看日志�?- 强制刷新浏览器（`Ctrl + F5` �?`Cmd + Shift + R`）�?- 等待 1-2 分钟，GitHub Pages 有时有缓存�?
### Q2：中文文件名导致链接乱码�?404�?
- 立即将文件名改为英文（如 `如何学习.md` �?`how-to-learn.md`），并修改所有引用该文件的双链�?- 提交更改，重新部署�?
### Q3：图片不显示�?
- 检查图片路径是否以 `./` �?`../` 开头，并且文件确实存在�?- 图片文件名也建议用英文，避免空格和中文�?
### Q4：想隐藏某篇笔记，不让它出现在网站上�?
- 不要将该笔记放入 `content` 文件夹，或者放�?`content` 下的一个子文件夹并�?`ignorePatterns` 中排除�?- 也可以在 Frontmatter 中添�?`draft: true`（需要插件支持，Quartz 默认不处�?draft）�?
### Q5：如何备份整个数字花园？

- 你的本地 `quartz` 文件夹和 GitHub 仓库已经是完整备份。定�?`git push` 即可�?
---

## 7. 进阶技�?
### 7.1 �?Obsidian 自动同步笔记

你可以写一个简单的脚本（`.bat` �?`.sh`），�?Obsidian 仓库中的特定文件夹复制到 Quartz �?`content` 文件夹，然后自动提交推送。例�?Windows 批处理：

```batch
xcopy "D:\我的Obsidian库\发布\" "C:\有用软件\obsidian-web\quartz\content\" /E /Y
cd C:\有用软件\obsidian-web\quartz
git add .
git commit -m "自动同步 %date% %time%"
git push origin v4
```

### 7.2 使用标签和搜�?
Quartz 内置全文搜索，支持中文（但分词效果一般）。建议为笔记添加 `tags` Frontmatter，利用组�?`TagList` 实现按标签过滤�?
### 7.3 自定义域�?
�?GitHub Pages 设置中绑定自己的域名，并在仓库根目录添加 `CNAME` 文件（内容为你的域名）。同时修�?`quartz.config.ts` 中的 `baseUrl`�?
---

## 8. 获取帮助

- **官方文档**：[quartz.jzhao.xyz](https://quartz.jzhao.xyz/)
- **中文社区**：[Obsidian 中文论坛](https://forum-zh.obsidian.md/) 搜索 “Quartz�?- **GitHub 仓库**：提�?[Issues](https://github.com/jackyzha0/quartz/issues)

---

现在你可以愉快地维护自己的数字花园了！如果遇到文档未覆盖的问题，随时回来问我�
