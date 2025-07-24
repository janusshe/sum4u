"""
transcribe.py
Whisper 转录模块 - 使用本地 whisper 进行音频转录。
"""

import os
from typing import Optional
import tempfile
from moviepy.audio.io.AudioFileClip import AudioFileClip

def transcribe_audio(audio_path: str, api_key: Optional[str] = None, model: str = "medium") -> str:
    """
    将音频文件转为文本，使用本地 whisper 进行转录。
    当文件大于100M时自动分段（每600秒一段）转录。
    :param audio_path: 音频文件路径
    :param api_key: 保留参数以兼容接口（实际不使用）
    :param model: whisper模型大小（tiny, base, small, medium, large），默认small
    :return: 转录文本
    """
    try:
        import whisper
        file_size = os.path.getsize(audio_path)
        MB = 1024 * 1024
        if file_size <= 100 * MB:
            print(f"使用本地 whisper ({model}) 进行转录...")
            whisper_model = whisper.load_model(model)
            result = whisper_model.transcribe(audio_path)
            print("转录完成！")
            return result["text"]
        else:
            print(f"音频文件较大（{file_size/MB:.1f}MB），自动分段转录...")
            audio = AudioFileClip(audio_path)
            duration = int(audio.duration)  # 秒
            chunk_sec = 600  # 每段10分钟
            texts = []
            whisper_model = whisper.load_model(model)
            for start in range(0, duration, chunk_sec):
                end = min(start + chunk_sec, duration)
                print(f"转录分段: {start//60:02d}:{start%60:02d} - {end//60:02d}:{end%60:02d}")
                with tempfile.NamedTemporaryFile(suffix='.mp3', delete=True) as tmp:
                    # 兼容moviepy 1.x和2.x的分段方法
                    try:
                        segment = audio.subclip(start, end)
                    except AttributeError:
                        segment = audio.subclipped(start, end)
                    try:
                        segment.write_audiofile(tmp.name, codec='mp3')
                    except TypeError:
                        segment.write_audiofile(tmp.name, codec='mp3', verbose=False, logger=None)
                    result = whisper_model.transcribe(tmp.name)
                    texts.append(result["text"])
            audio.close()
            print("所有分段转录完成！")
            return '\n'.join(texts)
    except ImportError:
        raise RuntimeError("未安装 whisper 库，请运行: pip install openai-whisper")
    except Exception as e:
        raise RuntimeError(f"本地 whisper 转录失败: {e}") 