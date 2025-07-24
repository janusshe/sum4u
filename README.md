# 视频总结工具 (Video Summarizer CLI)

一个强大的Python命令行工具，用于自动下载视频、提取音频、转录音频内容并生成结构化总结。

## 🚀 功能特性

- **多平台支持**: 支持YouTube和Bilibili视频下载
- **智能音频提取**: 自动提取视频音频并转换为MP3格式
- **高质量转录**: 使用OpenAI Whisper进行本地音频转录，支持99种语言自动检测
- **AI智能总结**: 使用DeepSeek或OpenAI GPT API生成结构化总结
- **自动文件管理**: 智能命名和保存结果文件
- **中文友好**: 完全支持中文界面和内容处理

## 📋 系统要求

- Python 3.8+
- macOS/Linux/Windows
- 稳定的网络连接
- 足够的磁盘空间用于音频文件存储

## 🛠️ 安装步骤

### 1. 克隆项目
```bash
git clone <项目地址>
cd video_summarizer_cli
```

### 2. 创建虚拟环境
```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# 或
venv\Scripts\activate  # Windows
```

### 3. 安装依赖
```bash
pip install -r requirements.txt
```

### 4. 安装额外工具
```bash
# 安装 yt-dlp (用于视频下载)
pip install yt-dlp

# 安装 ffmpeg (用于音频处理)
# macOS
brew install ffmpeg

# Ubuntu/Debian
sudo apt update && sudo apt install ffmpeg

# Windows (下载并添加到PATH)
# 从 https://ffmpeg.org/download.html 下载
```

## 🔑 API密钥配置

本工具已内置API密钥，无需用户手动配置。

## 📖 使用方法

### 1. 使用快速启动脚本 (推荐)

为了简化操作，项目提供了 `start.sh` 脚本，可以交互式地选择总结模板。

```bash
./start.sh "视频URL"
```

脚本会自动激活虚拟环境、运行主程序，并引导您选择一个预设的总结模板。

### 2. 直接运行主程序

您也可以直接运行 `main.py` 并通过参数指定总结模板或自定义提示词。

```bash
# 使用预设模板
python3 src/main.py --url "视频URL" --prompt_template "模板名称"

# 使用自定义提示词
python3 src/main.py --url "视频URL" --prompt "你的自定义提示词"
```

可用的模板名称请参考 `src/prompts.py` 文件。



## 📁 输出文件

### 文件结构
```
video_summarizer_cli/
├── downloads/           # 下载的音频文件
│   ├── youtube_output.mp3
│   └── bilibili_output.mp3
├── summaries/          # 生成的总结文件
│   ├── youtube_VIDEO_ID_TIMESTAMP_总结.md
│   └── bilibili_VIDEO_ID_TIMESTAMP_总结.md
└── transcriptions/     # 转录文本文件
    ├── youtube_VIDEO_ID_TIMESTAMP_转录.txt
    └── bilibili_VIDEO_ID_TIMESTAMP_转录.txt
```

### 文件命名规则
- **总结文件**: `平台_视频ID_时间戳_总结.md`
- **转录文件**: `平台_视频ID_时间戳_转录.txt`
- **音频文件**: `平台_output.mp3`

## 🔧 项目结构

```
video_summarizer_cli/
├── main.py              # 主程序入口
├── audio.py             # 音频下载和提取模块
├── transcribe.py        # 音频转录模块
├── summarize.py         # AI总结模块
├── utils.py             # 工具函数模块
├── requirements.txt     # 依赖包列表
├── README.md           # 项目说明文档
└── summaries/          # 输出文件夹
```

## 🆕 使用uv管理与项目结构

本项目已采用 [uv](https://github.com/astral-sh/uv) 进行依赖和虚拟环境管理，推荐使用 uv 替代 pip。

### 目录结构
```
video_summarizer_cli/
├── src/                  # 主要源代码
│   ├── main.py
│   ├── audio.py
│   ├── transcribe.py
│   ├── summarize.py
│   ├── prompts.py         # 新增：存储所有提示词模板
│   ├── utils.py
├── summaries/            # 输出总结文件
├── downloads/            # 下载的音频文件
├── transcriptions/       # 转录文本文件
├── requirements.txt      # 依赖包列表
├── README.md             # 项目说明文档
└── ...
```

### uv 常用命令
```bash
# 安装 uv
pip install uv

# 创建虚拟环境并安装依赖
uv venv
uv pip install -r requirements.txt

# 激活虚拟环境
source .venv/bin/activate  # macOS/Linux
# 或
.venv\Scripts\activate    # Windows

# 安装新依赖
uv pip install 包名

# 运行主程序
python src/main.py --url "视频URL"
```

## ⚙️ 配置选项

### 转录选项
- **模型大小**: 默认使用Whisper small模型，平衡速度和准确性
- **语言检测**: 自动检测音频语言，支持99种语言
- **输出格式**: 转录结果保存为UTF-8编码的文本文件

### 总结选项
- **结构化输出**: 包含关键概念、主要观点、实用建议等部分
- **多语言支持**: 根据转录内容自动选择总结语言
- **Markdown格式**: 便于阅读和分享

## 🐛 常见问题

### Q: 下载失败怎么办？
A: 
- 检查网络连接
- 确认视频URL有效
- 某些视频可能需要登录，尝试使用浏览器cookies

### Q: 转录速度慢？
A: 
- Whisper small模型需要一定处理时间
- 长视频处理时间更长，请耐心等待
- 确保有足够的CPU资源

### Q: API调用失败？
A: 
- 检查API密钥是否正确
- 确认API账户有足够余额
- 检查网络连接是否正常

### Q: 音频文件损坏？
A: 
- 确保ffmpeg正确安装
- 检查磁盘空间是否充足
- 重新下载视频

## 📝 使用建议

1. **选择合适的API**: DeepSeek API通常更稳定且价格更优惠
2. **批量处理**: 可以编写脚本批量处理多个视频
3. **定期清理**: 定期清理downloads文件夹中的音频文件
4. **备份重要总结**: 重要的总结文件建议备份到其他位置

## 🤝 贡献

欢迎提交Issue和Pull Request来改进这个项目！

## 📄 许可证

本项目采用MIT许可证，详见LICENSE文件。

## 🙏 致谢

- [yt-dlp](https://github.com/yt-dlp/yt-dlp) - 强大的视频下载工具
- [OpenAI Whisper](https://github.com/openai/whisper) - 优秀的语音识别模型
- [DeepSeek](https://platform.deepseek.com/) - 提供AI总结服务
- [OpenAI](https://openai.com/) - 提供GPT API服务

---

**注意**: 请遵守相关平台的使用条款和版权法律，仅用于个人学习和研究目的。