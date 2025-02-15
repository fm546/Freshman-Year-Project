from TTS.api import TTS
import torch
from TTS.utils.radam import RAdam
from collections import defaultdict
import pyaudio
import wave

# 添加 RAdam, defaultdict 和 dict 到安全全局列表
torch.serialization.add_safe_globals([RAdam, defaultdict, dict])

class ChineseTTS:
    def __init__(self, model_name="tts_models/zh-CN/baker/tacotron2-DDC-GST"):
        # 初始化 TTS 模型
        self.tts = TTS(model_name=model_name, progress_bar=False, gpu=False)

    def synthesize_speech(self, text, output_file="output_wav/output.wav"):
        # 生成语音
        self.tts.tts_to_file(text=text, file_path=output_file)
        print(f"语音已保存到 {output_file}")

    def play_audio(self, file_path):
        # 打开音频文件
        wf = wave.open(file_path, 'rb')
        p = pyaudio.PyAudio()

        # 打开音频流
        stream = p.open(
            format=p.get_format_from_width(wf.getsampwidth()),
            channels=wf.getnchannels(),
            rate=wf.getframerate(),
            output=True
        )

        # 播放音频
        data = wf.readframes(1024)
        while data:
            stream.write(data)
            data = wf.readframes(1024)

        # 关闭音频流
        stream.stop_stream()
        stream.close()
        p.terminate()

# 测试语音合成功能
if __name__ == "__main__":
    chinese_tts = ChineseTTS()
    text = "你好，请问有什么可以帮你的吗？"
    chinese_tts.synthesize_speech(text)
    chinese_tts.play_audio("output_wav/output.wav")