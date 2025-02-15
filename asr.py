import os
import json
import pyaudio
from vosk import Model, KaldiRecognizer

class ASR:
    def __init__(self, model_path="vosk-model-cn-kaldi-multicn-0.15"):
        # 加载 Vosk 模型
        if not os.path.exists(model_path):
            raise FileNotFoundError(f"模型未找到: {model_path}")
        self.model = Model(model_path)
        self.recognizer = KaldiRecognizer(self.model, 16000)

    def listen(self):
        # 初始化音频流
        p = pyaudio.PyAudio()
        stream = p.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=16000,
            input=True,
            frames_per_buffer=8192
        )
        stream.start_stream()

        print("正在聆听... (按 Ctrl+C 停止)")
        try:
            while True:
                data = stream.read(4096, exception_on_overflow=False)
                if self.recognizer.AcceptWaveform(data):
                    result = self.recognizer.Result()
                    result_dict = json.loads(result)
                    if "text" in result_dict:
                        yield result_dict["text"].replace(" ", "")  # 返回识别到的文本
        except KeyboardInterrupt:
            print("\n停止聆听...")
        finally:
            stream.stop_stream()
            stream.close()
            p.terminate()