"""
main.py
命令行主入口。
"""

import sys
import os
if __name__ == "__main__" and __package__ is None:
    sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    __package__ = "src"

import argparse
from datetime import datetime
from pathlib import Path
from .audio import download_audio
from .transcribe import transcribe_audio
from .summarize import summarize_text
from .prompts import prompt_templates


def generate_filename(url: str, has_summary: bool = True) -> str:
    """根据URL和是否有总结生成文件名"""
    # 从URL中提取视频ID
    if "bilibili.com" in url:
        # B站视频ID格式：BV1xx411c7mu
        if "BV" in url:
            video_id = url.split("BV")[1].split("?")[0][:10]
            platform = "bilibili"
        else:
            video_id = "unknown"
            platform = "bilibili"
    elif "youtube.com" in url:
        # YouTube视频ID格式：dQw4w9WgXcQ
        if "v=" in url:
            video_id = url.split("v=")[1].split("&")[0][:11]
            platform = "youtube"
        else:
            video_id = "unknown"
            platform = "youtube"
    else:
        video_id = "unknown"
        platform = "other"
    
    # 生成时间戳
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # 生成文件名
    if has_summary:
        filename = f"{platform}_{video_id}_{timestamp}_总结.md"
    else:
        filename = f"{platform}_{video_id}_{timestamp}_转录.txt"
    
    return filename


def main():
    parser = argparse.ArgumentParser(description="视频结构化总结工具")
    parser.add_argument("--url", required=True, help="视频链接（支持B站、YouTube等）")

    parser.add_argument("--output", required=False, help="自定义输出文件名（可选）")
    parser.add_argument("--prompt", required=False, help="自定义摘要提示词")
    parser.add_argument("--prompt_template", required=False, default="default", help="选择摘要提示词模板，可选: default, youtube_全面提取, youtube_结构化提取, youtube_精炼提取, youtube_专业课笔记, 爆款短视频文案, youtube_视频总结")
    args = parser.parse_args()

    # 创建总结内容文件夹
    summaries_dir = Path("summaries")
    summaries_dir.mkdir(exist_ok=True)
    
    # 生成自动文件名
    auto_filename = generate_filename(args.url, has_summary=True)
    
    # 使用自定义文件名或自动生成的文件名
    if args.output:
        output_path = summaries_dir / args.output
    else:
        output_path = summaries_dir / auto_filename

    print("[1/3] 下载并提取音频...")
    audio_path = download_audio(args.url)
    print(f"音频已保存: {audio_path}")

    print("[2/3] 转录音频...")
    transcript = transcribe_audio(audio_path)
    print("转录完成！")

    print("[3/3] 结构化总结...")
    # 优先使用 --prompt，如果没有则用模板
    prompt_to_use = args.prompt if args.prompt else prompt_templates.get(args.prompt_template, prompt_templates["default"])
    summary = summarize_text(transcript, prompt=prompt_to_use)
    print("摘要完成！")

    # 保存到总结文件夹
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(summary)
    print(f"结果已保存到: {output_path}")

if __name__ == "__main__":
    main()