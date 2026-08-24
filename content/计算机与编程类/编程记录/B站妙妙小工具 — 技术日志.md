---
---

# B站妙妙小工具 �?技术日�?
> 2026-07-28
> 记录当前框架状态、已知问题和技术决�?
---

## 一、框架架�?
### 目录结构

```
B站工具框�?
├── __main__.py              # 入口：REPL / _exec 内部命令
├── start.bat                # 双击启动 REPL
├── core/
�?  ├── __init__.py           # 版本�?�?  ├── api.py                # B�?API 工具�?�?  ├── cache.py              # 错误日志缓存系统
�?  ├── cli.py                # 参数解析器（保留备用�?�?  ├── config.py             # 全局配置（data_root, plugin_dir, cache_dir�?�?  ├── registry.py           # 插件发现与重�?�?  └── repl.py               # REPL 主循环（prompt_toolkit�?├── plugins/
�?  ├── demo/                 # 测试插件
�?  ├── transcribe/           # 转文字插�?�?  �?  ├── __init__.py       # 主逻辑（execute + cli_run�?�?  �?  ├── audio_convert.py  # 音频格式转换：librosa �?scipy �?soundfile
�?  �?  ├── audio.py          # whisper.cpp 转录（流�?stdout�?�?  �?  ├── onnx_transcribe.py # ONNX Paraformer 转录（流式子进程�?�?  �?  ├── subtitle.py       # CC 字幕提取
�?  �?  └── onnx_transcribe.py
�?  └── transcribe/
├── scripts/
�?  ├── export_paraformer_onnx.py  # 导出三个 ONNX 模型
�?  └── onnx_infer.py              # ONNX 推理子进�?└── tests/
    ├── test_cli.py           # CLI 参数解析测试�?0 个）
    ├── test_plugins.py       # 插件发现测试�? 个）
    └── test_transcribe.py    # 转录功能测试�?3 个）
```

### 工作�?
```
用户双击 start.bat
  �?REPL 指挥官窗口（prompt_toolkit�?  �?  ├── list          �?列出插件
  ├── run <插件>     �?弹新 cmd 窗口（CREATE_NEW_CONSOLE�?  �?                   �?  �?              _exec 内部命令在新窗口中运�?  �?                   �?  �?              插件 cli_run() �?execute(params, emit)
  �?                   �?  �?              emit("log", ...) �?窗口显示 + 同时写入实时�?  �?              emit("progress", ...) �?进度�?  �?              raise RuntimeError �?触发错误缓存写入
  �?  ├── logs <id>     �?查看错误日志
  ├── reload        �?重新扫描插件目录
  ├── clean         �?清理缓存日志
  └── exit          �?退�?```

### 关键�?
**错误缓存 (`core/cache.py`)**
- 每次 `_exec` 抛异常时写入 `~/.bili_tool/cache/task_N_name_timestamp.json`
- 只写 WARN/ERROR 级日�?+ 完整 traceback + 系统环境
- 自动保留最�?10 个，`clean` 清空全部

---

## 二、转录模块现�?
### 双引擎策�?
```
execute(params, emit)
  �?  ├─ �?audio_path �?ensure_wav() �?_transcribe()
  �?                                    �?  �?                          ┌─────────┴─────────�?  �?                     ONNX 可用?            ONNX 不可�?  �?                          �?                    �?  �?                    transcribe_onnx()     whisper transcribe()
  �?                    （子进程�?              （子进程�?  �?                      失败�?                   �?  �?                   回退 whisper.cpp         结果
  �?  └─ �?url �?fetch_cc() �?有字幕则提取，无字幕则提�?```

### whisper.cpp 路径（当前可�?✅）

| 步骤 | 方法 | 耗时 |
|------|------|------|
| 音频转换 | librosa.load() + scipy.resample + soundfile.write | 较快 |
| 转录 | 子进�?whisper-cli.exe --stdout | GPU 正常 |
| 输出 | 逐行读取 stdout �?emit 到窗�?| 实时 |
| 结果 | 清洗时间戳后返回 text | �?|

### ONNX Paraformer 路径（当前不可用 ❌）

| 步骤 | 状�?| 原因 |
|------|:----:|------|
| 模型文件 | �?已导�?| paraformer(603MB) + predictor(3MB) + decoder(218MB) |
| Python 环境 | �?依赖�?| numpy, torch, soundfile, librosa, onnxruntime-gpu 1.24.1 |
| GPU 环境 | �?cuDNN 缺失 | �?`cudnn64_9.dll`，回退 CPU |
| 编码器推�?| �?模型 bug | dummy 帧数 50 太短，self-attention mask baken 死，输入 2841 帧时报错(1) |

_(1) `onnxruntime::BroadcastIterator::Init axis == 1 || axis == largest was false. Attempting to broadcast an axis by a dimension other than 1. 50 by 2841`_

### 已知问题

| 问题 | 影响 | 状�?|
|------|:----:|------|
| ONNX 编码�?dummy 帧数不足 | ONNX 路径不可�?| 待修：重新导出，dummy 改为 1000 �?|
| cuDNN 9.x 未安�?| ONNX 跑在 CPU �?| 待装 |
| torchcodec + FFmpeg �?DLL | 无法�?torchaudio 读写音频 | 已绕过：改用 librosa + scipy + soundfile |
| whisper 结果只清洗时间戳，未分段 | 输出为连续文�?| 可优化（非阻塞） |
| 插件 render_* 函数已删�?| 不影响功�?| 已完�?|
| TaskManager 已移�?| 改为每任务独立进�?| 已完�?|

---

## 三、关键技术决�?
| 决策 | 说明 |
|------|------|
| **CREATE_NEW_CONSOLE 弹窗** | 不走 `start cmd /k`，避免中文路径编码问�?|
| **subprocess stdout 流式读取** | `asyncio.run_coroutine_threadsafe()` 在线程中每行 emit |
| **PYTHONIOENCODING=utf-8** | 子进程输�?pipe 编码一致�?|
| **错误缓存不存成功任务** | 只有抛出异常才写入，正常完成不留文件 |
| **librosa �?+ scipy 重采�?+ soundfile �?* | 彻底绕开 torchcodec �?FFmpeg 依赖 |
| **onnxruntime-gpu 1.24.1** | 兼容 CUDA 12.0，不要求 CUDA 13.x |
| **28 个测试全部通过** | pytest 覆盖 CLI、插件发现、转录功�?|

---

## 四、环境规�?
| 组件 | 版本 |
|------|------|
| Python | 3.14.6 |
| CUDA | 12.0 |
| onnxruntime-gpu | 1.24.1 |
| torch | 2.13.0+cpu |
| torchaudio | —（未使用） |
| whisper.cpp | 需要用户自行编译或下载 |

