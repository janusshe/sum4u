#!/bin/bash

# 视频总结工具快速启动脚本
# 使用方法: ./start.sh "视频URL"

echo "🎥 视频总结工具快速启动"
echo "================================"

# 检查参数
if [ $# -lt 1 ]; then
    echo "❌ 错误: 请提供视频URL"
    echo "使用方法: ./start.sh \"视频URL\""
    echo ""
    echo "示例:"
    echo "  ./start.sh \"https://www.youtube.com/watch?v=VIDEO_ID\""
    echo "  ./start.sh \"https://www.bilibili.com/video/BV1xxx\""
    exit 1
fi

URL=$1

# 新增：提示用户选择prompt模板
TEMPLATES=("youtube_全面提取" "youtube_结构化提取" "youtube_精炼提取" "youtube_专业课笔记" "爆款短视频文案" "youtube_视频总结")
echo "可选的摘要模板："
for i in "${!TEMPLATES[@]}"; do
    echo "  $((i+1)). ${TEMPLATES[$i]}"
done
read -p "请选择模板编号（直接回车默认default）：" TEMPLATE_IDX

# 新增：提示用户输入自定义prompt
read -p "请输入本次总结的自定义提示词（直接回车则使用模板）：" PROMPT

echo "📹 视频URL: $URL"

# 检查虚拟环境
if [ ! -d ".venv" ]; then
    echo "⚠️  未找到虚拟环境，正在创建..."
    uv venv
fi

# 激活虚拟环境
echo "🔧 激活虚拟环境..."
source .venv/bin/activate

# 检查依赖
echo "📦 检查依赖包..."
uv pip install -r requirements.txt

# 创建必要的文件夹
echo "📁 创建输出文件夹..."
mkdir -p downloads summaries transcriptions

# 运行主程序
echo "🚀 开始处理视频..."
echo "================================"
if [ -n "$PROMPT" ]; then
    python3 src/main.py --url "$URL" --prompt "$PROMPT"
else
    if [ -n "$TEMPLATE_IDX" ] && [[ "$TEMPLATE_IDX" =~ ^[1-6]$ ]]; then
        TEMPLATE_NAME="${TEMPLATES[$((TEMPLATE_IDX-1))]}"
        python3 src/main.py --url "$URL" --prompt_template "$TEMPLATE_NAME"
    else
        python3 src/main.py --url "$URL"
    fi
fi

echo ""
echo "✅ 处理完成！"
echo "📁 请查看 summaries/ 文件夹中的结果文件"