
### 📖 Pandoc 是什么？

你可以把 Pandoc 理解为一本万能词典，它能在超过 40 种文档格式间进行精确转换，是真正的“文档格式转换瑞士军刀”。

*   **格式支持广泛**：小到 Markdown、HTML，大到 Word（.docx）、PPT、PDF，甚至电子书（EPUB），它都能轻松搞定。
*   **质量高**：转换的核心是解析文档的“结构”（如标题、段落、表格），而非样式，因此能最大程度保证内容的准确性。

### 💻 第一步：安装

Pandoc 支持 Windows、macOS 和 Linux，安装很简单。

*   **Windows 用户**
    *   **推荐方法**：从官网下载 `.msi` 安装程序，双击按提示操作即可，安装程序会自动配置好环境。
    *   **包管理器**：使用 `winget install --id JohnMacFarlane.Pandoc` 或 `choco install pandoc`。

*   **macOS 用户**
    *   同样推荐从官网下载 `.pkg` 安装程序。习惯用 Homebrew 的开发者，可执行 `brew install pandoc`。

*   **Linux 用户**
    *   以 Ubuntu/Debian 为例，在终端执行 `sudo apt-get install pandoc` 即可。

安装完成后，打开终端（命令提示符或 PowerShell），输入 `pandoc --version`，如果能看到版本信息，就表示安装成功啦。

### ✨ 第二步：核心语法

Pandoc 的核心命令只有一个简单公式：`pandoc [输入文件] -o [输出文件]`。

它的智能之处在于，会自动根据文件后缀名判断格式。比如，要把 Markdown 笔记转成 Word 报告，只需：

```bash
pandoc my_note.md -o my_report.docx
```

*   若想精确控制，也可用 `-f`（输入格式）和 `-t`（输出格式）来指定。
*   为生成完整文档，建议加上 `-s` 或 `--standalone`。

### 🚀 第三步：高频转换场景

**1. Word 转 Markdown**
这是你构建知识库的关键一步，命令同样很简单：

```bash
pandoc "你的文档.docx" -f docx -t markdown -o "输出文件.md"
```

*   `-f docx`：指定输入格式是 Word。
*   `-t markdown`：指定输出格式是 Markdown。
*   `-o "输出文件.md"`：指定输出文件名。

**2. Markdown 转 Word**
如果你的文章是 Markdown 格式，想转成 Word 格式保存，可以用这个命令：

```bash
pandoc report.md -o final_report.docx
```

**3. Markdown 转 PDF**
如果你的 Markdown 笔记包含表格或代码，想要打印或分享，PDF 是很好的选择。

```bash
pandoc paper.md -s -o paper.pdf
```

> ⚠️ **注意事项**：PDF 转换需要依赖 LaTeX 引擎，如果你的电脑是首次运行此命令，Pandoc 可能会自动下载必要的组件。
>
> **中文支持**：默认引擎可能不支持中文，需要指定 `xelatex` 引擎和中文字体：
> ```bash
> pandoc paper.md -o paper.pdf --pdf-engine=xelatex -V mainfont="SimSun"
> ```

**4. 多文件合并**
写长文或电子书时，可以将多个 Markdown 文件合并成一个。

*   **合并为 EPUB 电子书**
    ```bash
    pandoc title.md ch1.md ch2.md -o mybook.epub
    ```

*   **合并为 Word 长报告**
    ```bash
    pandoc *.md -o full_report.docx
    ```

**5. 批量转换（Windows）**
为了批量处理 `.md` 文件，你可以使用 PowerShell 脚本。这里提供两种常用场景：

*   **场景一：批量将当前目录下所有 `.md` 文件转换为 `.docx`**
    ```powershell
    Get-ChildItem -Path . -Filter *.md | ForEach-Object {
        pandoc $_.FullName -o "$($_.BaseName).docx"
        Write-Host "已转换: $($_.Name)"
    }
    Write-Host "批量转换完成！"
    ```

*   **场景二：批量将当前目录下所有 `.docx` 文件转换为 `.md`**
    ```powershell
    Get-ChildItem -Path . -Filter *.docx | ForEach-Object {
        pandoc $_.FullName -f docx -t markdown -o "$($_.BaseName).md"
        Write-Host "已转换: $($_.Name)"
    }
    Write-Host "批量转换完成！"
    ```
    > 你可以把脚本保存为 `.ps1` 文件（如 `convert.ps1`），放在需要转换的文件夹中，右键选择“使用 PowerShell 运行”即可。

### 🔧 第四步：常用选项

| 选项 | 功能 | 示例 |
| :--- | :--- | :--- |
| `-f` / `--from` | 指定输入格式 | `-f markdown` |
| `-t` / `--to` | 指定输出格式 | `-t html` |
| `-o` / `--output` | 指定输出文件名 | `-o output.docx` |
| `-s` / `--standalone` | 生成完整文档 | `pandoc -s file.md -o out.html` |
| `--toc` | 生成目录 | `pandoc --toc file.md -o out.pdf` |
| `--template` | 使用自定义模板 | `pandoc --template=mytemplate.tex file.md -o out.pdf` |
| `--pdf-engine` | 指定 PDF 引擎 | `--pdf-engine=xelatex` |
| `-V` / `--variable` | 设置变量 | `-V mainfont="SimSun"` |

### 🔥 第五步：高级玩法

**1. 自定义 Word 模板**
想拥有完全符合心意的 Word 样式？可以这样做：

1.  **获取默认模板**：在终端输入 `pandoc -o custom-reference.docx --print-default-data-file reference.docx`，就会生成一个 `custom-reference.docx` 文件。
2.  **修改样式**：用 Word 打开，尽情修改其中的字体、段落、页边距等一切样式。
3.  **应用模板**：转换时，通过 `--reference-doc` 参数指定你改好的模板文件即可，如 `pandoc input.md -o output.docx --reference-doc=custom-reference.docx`。

**2. 管理元数据**
在 Markdown 文件最顶部添加以 `---` 包裹的 YAML 格式信息，可以方便地定义文档的标题、作者、日期等。

```yaml
---
title: 这是标题
author: 张三
date: 2023-10-20
---
```

### ❓ 第六步：常见问题与解决方案

*   **中文 PDF 乱码或空白**
    默认引擎 `pdflatex` 不支持中文。需要指定引擎和中文字体：
    ```bash
    pandoc input.md -o output.pdf --pdf-engine=xelatex -V mainfont="SimSun"
    ```
*   **Word 转 Markdown 后格式混乱**
    可以尝试输出更纯净的 Markdown 格式：
    ```bash
    pandoc input.docx -f docx -t markdown-strict -o output.md
    ```
*   **转换出的文件无法打开**
    如果转换的是 RTF 等格式，记得加上 `-s` 参数，以确保生成完整的文档结构，而非内容片段。

### 💎 总结

掌握 Pandoc，就如同为自己配备了一位文档格式的万能转换大师。无论是构建个人知识库，还是处理日常的学术和工作文档，它都能让你事半功倍。

希望这份指南对你有所帮助。