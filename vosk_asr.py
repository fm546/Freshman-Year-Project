import os
import sys
import json
import pyaudio
from vosk import Model, KaldiRecognizer

# 加载 Vosk 模型
model_path = "vosk-model-cn-kaldi-multicn-0.15"
if not os.path.exists(model_path):
    print(f"Error: Model not found at {model_path}")
    sys.exit(1)

model = Model(model_path)
recognizer = KaldiRecognizer(model, 16000)

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

print("Listening... (Press Ctrl+C to stop)")

try:
    while True:
        data = stream.read(4096, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            result = recognizer.Result()
            result_dict = json.loads(result)
            if "text" in result_dict:
                print("Recognized:", result_dict["text"].replace(" ", ""))
except KeyboardInterrupt:
    print("\nStopping...")

# 释放资源
stream.stop_stream()
stream.close()
p.terminate()