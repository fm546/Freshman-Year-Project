import asyncio
import edge_tts

def generate_audio(text: str, voice: str, output_file: str) -> None:
    """
    传入文本、语音及输出文件名，生成语音并保存为音频文件
    :param text: 需要合成的中文文本
    :param voice: 使用的语音类型，如 'zh-CN-XiaoyiNeural'
    :param output_file: 输出的音频文件名
    """
    async def generate_audio_async() -> None:
        """异步生成语音"""
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(output_file)

    # 异步执行生成音频
    asyncio.run(generate_audio_async())

# 示例调用
generate_audio("今天天气不错，适合出门玩耍。", "zh-CN-XiaoyiNeural", "weather.mp3")
