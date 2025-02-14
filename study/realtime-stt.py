from vosk import Model, KaldiRecognizer
import pyaudio
import json

# 加载模型
# model = Model("./study/vosk-model/vosk-model-small-cn-0.22")
# model = Model("./study/vosk-model/vosk-model-cn-0.22")
model = Model("./study/vosk-model/vosk-model-cn-kaldi-multicn-0.15")

# 创建麦克风对象
p = pyaudio.PyAudio()

# 打开麦克风
stream = p.open(
    # 16位深度音频数据
    format=pyaudio.paInt16, 
    # 单声道
    channels=1, 
    # 采样率16000
    rate=16000, 
    # 从麦克风获取数据
    input=True, 
    # 每次获取4000帧数据
    frames_per_buffer=4000
    )

# 初始化识别器
rec = KaldiRecognizer(model, 16000)

print("开始实时识别")
while True:
    # 每次读取4000帧数据
    data = stream.read(4000)
    # 如果读取到数据
    if rec.AcceptWaveform(data):
        # 实时输出识别结果
        text = rec.Result()
        result = json.loads(text)['text'].replace(" ", "")
        print(result)