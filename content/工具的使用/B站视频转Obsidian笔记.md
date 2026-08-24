---
---

# B站视频转Obsidian笔记

一个简单实用的工具，帮助你快速将B站视频信息转换为Obsidian笔记，支持单条和批量处理�?[B站信息提取](file:///C:%5CUsers%5Cc3458%5CDesktop%5C世界%5C学习%5CB站信息提�?
## 功能特�?
- **单条处理**：输入单个B站视频链接或BV号，一键发送到Obsidian
- **批量处理**：支持批量输入多个B站视频链接或BV号，逐行处理并显示结�?- **自动解析**：自动从URL中提取BV�?- **错误处理**：详细的错误提示和异常捕�?- **进度反馈**：批量处理时显示实时进度条和状�?- **美观界面**：现代化的响应式设计，支持移动端

## 技术栈

- **后端**：Python 3 + Flask
- **前端**：HTML + JavaScript + Bootstrap 5
- **依赖**：requests, beautifulsoup4
- **运行**：本地Flask服务�?
## 安装步骤

### 1. 克隆项目

```bash
# 克隆项目到本�?git clone <仓库地址> B站信息提�?cd B站信息提�?```

### 2. 安装依赖

```bash
# 使用pip安装依赖
pip install -r requirements.txt
```

### 3. 配置Obsidian

1. 打开Obsidian
2. 安装并启�?**Local REST API** 插件
3. 在插件设置中生成 **API Key**
4. 将生成的API Key复制�?`obsidian/client.py` 文件中的 `api_key` 变量

### 4. 启动服务�?
```bash
# 启动Flask服务�?python app.py
```

服务器将运行�?`http://localhost:5000`

## 使用方法

### 单条处理

1. 在浏览器中访�?`http://localhost:5000`
2. �?单条处理"输入框中输入B站视频链接或BV�?3. 点击"发送到Obsidian"按钮
4. 等待处理完成，查看结�?
### 批量处理

1. 在浏览器中访�?`http://localhost:5000`
2. �?批量处理"文本框中输入多个B站视频链接或BV号（每行一个）
3. 点击"开始批量发�?按钮
4. 查看实时处理进度和结�?
## 项目结构

```
├── app.py                # Flask应用主文�?├── bilibili/
�?  └── api.py            # B站视频信息获取模�?├── markdown/
�?  └── generator.py      # Markdown笔记生成模块
├── obsidian/
�?  └── client.py         # Obsidian Local REST API客户�?├── templates/
�?  └── index.html        # 前端主页�?├── static/
�?  ├── css/
�?  �?  └── style.css     # 前端样式文件
�?  └── js/
�?      └── main.js       # 前端JavaScript
└── requirements.txt      # 项目依赖文件
```

## 配置说明

### Obsidian配置

- **API Key**：在 `obsidian/client.py` 文件中修�?`api_key` 变量
- **文件夹路�?*：在 `obsidian/client.py` 文件中修�?`vault_path` 变量，默认为 "B站灵�?

### 服务器配�?
- **端口**：在 `app.py` 文件中修�?`app.run()` �?`port` 参数，默认为 5000
- **主机**：在 `app.py` 文件中修�?`app.run()` �?`host` 参数，默认为 "0.0.0.0"

## 注意事项

1. **Obsidian必须打开**：使用前确保Obsidian已打开，并且Local REST API插件已启�?2. **网络连接**：需要网络连接来获取B站视频信�?3. **反爬措施**：已模拟浏览器请求头，避免被B站反�?4. **错误处理**：所有网络请求和处理逻辑都有异常捕获
5. **SSL证书**：开发环境中使用 `verify=False` 忽略SSL证书验证，生产环境建议配置证�?
## 常见问题

### Q: 无法访问 http://localhost:5000

A: 请检查Flask服务器是否正在运行，端口是否被占�?
### Q: 发送到Obsidian失败

A: 请检查：
- Obsidian是否已打开
- Local REST API插件是否已启�?- API Key是否正确
- 网络连接是否正常

### Q: 获取视频信息失败

A: 请检查：
- B站链接或BV号是否正�?- 网络连接是否正常
- 视频是否需要登录才能查看（付费内容无法爬取�?
## 后续优化

- [ ] 添加视频封面提取功能
- [ ] 支持自定义Markdown模板
- [ ] 添加配置页面，允许用户修改API Key和文件夹路径
- [ ] 实现拖拽文件和粘贴URL功能
- [ ] 添加视频信息预览功能

## 许可�?
MIT License

## 版本

1.0.0

