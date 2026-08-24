---
---

这是一�?**MarkItDown 的详细使用手�?*。它是一款由微软开源的轻量�?Python 工具，能�?PDF、Word、Excel、PPT、图像、音频等多种文件格式，高效地转换�?LLM（大语言模型）易于理解和处理�?Markdown 格式�?
---

## 📖 快速一�?
| 项目 | 信息 |
| :--- | :--- |
| **项目名称** | MarkItDown |
| **开发�?* | Microsoft |
| **GitHub** | [github.com/microsoft/markitdown](https://github.com/microsoft/markitdown) |
| **核心功能** | 将多种文件格式转换为 LLM 就绪�?Markdown 文本 |
| **主要用�?* | �?AI 工作流、文本分析、文档索引准备高质量数据 |
| **输出特�?* | 保留文档结构（标题、列表、表格等），Token 效率�?|

---

## 🚀 1. 环境准备与安�?
### 环境要求
*   **Python**: 版本 3.10 或更高�?*   **pip**: Python 的包管理工具�?
### 安装步骤

#### 1. 最推荐的方式：一键安装所有功能（`[all]`�?如果希望 MarkItDown 支持尽可能多的文件格式，请执行以下命令：
```bash
pip install markitdown[all]
```
这种方法会安装包�?PDF、Excel、图像、音频等处理所需的所有可选依赖库�?
#### 2. 按需安装（节省空间）
如果你只需要处理特定类型的文件，可以只安装核心库和对应的依赖：
```bash
pip install markitdown[pdf, docx, pptx]
```

#### 3. 从源代码安装（获取最新特性）
如果你想体验最新的开发版功能，可以从 GitHub 克隆并安装：
```bash
git clone git@github.com:microsoft/markitdown.git
cd markitdown
pip install -e packages/markitdown[all]
```

#### 4. 验证安装
安装成功后，可以通过以下命令查看版本信息来验证：
```bash
markitdown --version
```

#### 5. (可�? 使用虚拟环境
为了避免不同 Python 项目间的依赖冲突，建议在虚拟环境中安装：
```bash
# 创建虚拟环境
python -m venv markitdown-env
# 激活虚拟环�?(Windows)
markitdown-env\Scripts\activate
# 激活虚拟环�?(macOS/Linux)
source markitdown-env/bin/activate
# 然后在虚拟环境中安装
pip install markitdown[all]
```

---

## 💻 2. 命令行界�?(CLI) 使用指南

MarkItDown 提供了非常便捷的命令行工具，适合快速转换或集成到脚本中�?
### 基本用法：标准输�?最简单的用法是将转换结果直接打印在终端上�?```bash
markitdown 路径/�?你的文件.pdf
```
你也可以使用重定向操作符 `>` 将内容保存到 `.md` 文件中：
```bash
markitdown 路径/�?你的文件.docx > 输出文档.md
```

### 保存到文件：使用 `-o` 选项
更推荐使�?`-o` �?`--output` 选项，这样可以直接指定输出文件，避免重定向可能带来的编码问题�?```bash
markitdown 路径/�?你的演示文稿.pptx -o 演讲�?md
```
执行后，Markdown 内容会被写入 `演讲�?md` 文件中�?
### 处理标准输入 (stdin)：从管道读取
你可以通过管道将文件内容传递给 `markitdown` 命令，这在处理动态生成的内容时非常有用：
```bash
cat 未知类型文件.bin | markitdown
```
或者通过输入重定向：
```bash
markitdown < 输入文件.txt
```

### 常用命令行选项参�?CLI 提供了多个选项，让你能精确控制转换行为�?
| 选项 | 简�?| 描述 | 示例 |
| :--- | :--- | :--- | :--- |
| `--output` | `-o` | 将结果写入指定文�?| `markitdown -o out.md in.pdf` |
| `--extension` | `-x` | **（重要）** 当从 stdin 输入时，指定文件扩展名以帮助识别格式 | `markitdown -x pdf < input.bin` |
| `--mime-type` | `-m` | 当从 stdin 输入时，指定文件�?MIME 类型 | `markitdown -m application/pdf < input.bin` |
| `--charset` | `-c` | 指定文本输入文件的字符集 | `markitdown -c utf-8 < input.txt` |
| `--version` | `-v` | 显示当前 MarkItDown 的版本号 | `markitdown -v` |

### 💡 实用技巧：使用 `-o` 代替重定�?`>`
当转换包含非英文字符（如中文、法语、德语等）的文件时，使用重定�?`>` 可能会遇�?`UnicodeEncodeError` 错误。此时，使用 `-o` 选项将结果直接写入文件是更可靠的选择，因为它能更好地处理 UTF-8 编码�?
---

## 🐍 3. Python API 使用指南

�?Python 脚本�?Jupyter Notebook 中使�?MarkItDown 可以实现更复杂的集成和自动化�?
### 基础转换
使用 MarkItDown �?API 非常简单，只需三步�?
1.  导入 `MarkItDown` 类�?2.  创建 `MarkItDown` 实例�?3.  调用 `convert()` 方法�?
```python
from markitdown import MarkItDown

# 1. 创建转换器实�?md = MarkItDown()

# 2. 转换文件，支持绝对路径或相对路径
result = md.convert("财务数据.xlsx")

# 3. 打印转换后的 Markdown 文本
print(result.text_content)
```

### 在不同场景中的应�?
#### 场景一：处�?Word 文档
Word 文档中的标题、列表和加粗文本等格式，在转换后会保留为 Markdown 格式�?```python
from markitdown import MarkItDown

md = MarkItDown()
result = md.convert("年度报告.docx")
print(result.text_content)
```

#### 场景二：转换 PowerPoint 幻灯�?MarkItDown 会提取每张幻灯片的标题和项目符号文本，并以幻灯片编号为分隔输出�?```python
result = md.convert("产品介绍.pptx")
print(result.text_content)
```

#### 场景三：解析 Excel 表格
转换器会将电子表格中的结构化数据转换为清晰的 Markdown 表格，非常便�?LLM 理解数据间的列对应关系�?```python
result = md.convert("销售数�?xlsx")
print(result.text_content)
```

#### 场景四：�?ZIP 文件中提取内�?MarkItDown 能够自动遍历 ZIP 压缩包内的文件并逐一转换，然后将所有结果合并输出�?```python
result = md.convert("文档资料�?zip")
print(result.text_content) # 将输出所有内部文件的转换结果
```

---

## 🧠 4. 高级功能

### 🤖 �?LLM 集成：为图片生成描述
MarkItDown 可以与大语言模型（如 GPT-4）结合，为图片生成准确的文本描述�?```python
from markitdown import MarkItDown
from openai import OpenAI

# 初始�?OpenAI 客户端（需要设�?API Key�?client = OpenAI()

# 创建 MarkItDown 实例时，传入 LLM 客户端和模型名称
md = MarkItDown(llm_client=client, llm_model="gpt-4o")

# 转换图片时，会自动调�?LLM 生成描述
result = md.convert("风景照片.jpg")
print(result.text_content)
```
> **注意**: 使用此功能需�?OpenAI API Key 和网络访问权限�?
### 🔧 插件系统
MarkItDown 支持通过插件来扩展功能。第三方转换器可以通过 Python 的入口点系统注册进来�?```python
from markitdown import MarkItDown

md = MarkItDown()

# 启用所有已安装的第三方插件
md.enable_plugins()
```
在命令行中，你可以使�?`--use-plugins` �?`--list-plugins` 选项来管理插件�?
### 🎛�?转换器优先级系统
MarkItDown 内部使用优先级系统来决定使用哪个转换器来处理文件。优先级值越低，转换器越先被尝试�?
*   **特定格式转换�?* (`PRIORITY_SPECIFIC_FILE_FORMAT = 0.0`): 例如 `PdfConverter`、`DocxConverter`，会优先于通用转换器被调用�?*   **通用转换�?* (`PRIORITY_GENERIC_FILE_FORMAT = 10.0`): 例如 `PlainTextConverter`、`ZipConverter`，作为后备方案�?
这个机制确保了系统总是为文件选择最合适的转换器�?
### ☁️ Azure Document Intelligence 集成
MarkItDown 可以集成 Azure 的文档智能服务，用于更高级的文本提取，例如从复杂�?PDF 表单中提取数据�?```bash
markitdown 复杂表单.pdf --use-docintel --endpoint "你的Azure服务端点URL"
```

---

## �?5. 故障排除与常见问�?
### 1. 运行时出�?`UnicodeEncodeError` 错误
*   **问题**: 当转换的文件包含非英文字符（如中文、法语字母）时，�?Windows 命令行中使用重定�?`>` 保存文件时可能出现编码错误�?*   **解决方案**:
    *   **方法一（推荐）**: 使用 `-o` 选项替代重定向。例如：`markitdown 中文文档.pdf -o 输出.md`�?    *   **方法�?*: 在运�?Python 脚本前，先设置环境变�?`PYTHONIOENCODING=utf-8`�?
### 2. 无法转换网络驱动器上的文�?*   **问题**: 当文件位于映射的网络驱动器上时，转换可能因权限问题而失败�?*   **解决方案**: 先将文件复制到本地驱动器（如 `C:\` 盘），然后对本地副本进行转换。转换成功后，再根据需要处理原文件�?
### 3. 如何处理大文件？
*   **问题**: 处理非常大的文件可能会消耗大量内存和时间�?*   **解决方案**: 确保你的计算机有足够的内存。如果可能，考虑将大文件拆分成较小的部分后再进行转换�?
---

## 📚 附录

### 支持的文件格式清�?
| 类型 | 支持的格�?|
| :--- | :--- |
| **📄 办公文档** | PDF (.pdf), Word (.docx), PowerPoint (.pptx), Excel (.xlsx/.xls) |
| **🌐 网页与文�?* | HTML, 纯文�?(.txt), CSV, JSON, XML |
| **🖼�?多媒�?* | 图片 (JPEG, PNG, GIF等，支持OCR), 音频 (MP3, WAV等，支持语音转录) |
| **🗜�?压缩文件** | ZIP 压缩�?(可遍历内部文件并逐一转换) |
| **📚 电子�?* | EPUB 格式 |
| **📧 邮件** | Outlook 邮件文件 (.msg) |
| **💻 代码文件** | 多种编程语言源代码文件，并能保留语法高亮格式 |

### MarkItDown vs. Pandoc

| 特�?| MarkItDown | Pandoc |
| :--- | :--- | :--- |
| **设计目标** | �?LLM �?AI 管道快速转换文�?| 高度保真的文档格式转换，追求视觉布局还原 |
| **输出质量** | 保留文档结构，对机器友好 | 保留复杂布局和格式，对人类阅读友�?|
| **速度** | 快�?| 相对较慢 |
| **适用场景** | AI 训练数据准备、批量文本分�?| 文档出版、格式精确迁�?|
| **总结** | 追求速度�?AI 集成�?| 追求格式完整性和精确�?|

根据任务需求，你可以在 MarkItDown �?**速度�?AI 友好�?* �?Pandoc �?**格式与视觉高保真�?* 之间做出选择�?
### 参考资�?*   **官方 GitHub 仓库**: [https://github.com/microsoft/markitdown](https://github.com/microsoft/markitdown)
*   **PyPI 项目�?*: [https://pypi.org/project/markitdown/](https://pypi.org/project/markitdown/)
*   **问题反馈**: �?GitHub 仓库�?[Issues](https://github.com/microsoft/markitdown/issues) 页面提交�?
---

希望这份手册能帮助你顺利上手 MarkItDown。如果在使用过程中遇到其他问题，随时可以再提问�
