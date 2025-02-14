from vosk import Model, KaldiRecognizer
import wave
import json

# 加载模型
# model = Model("./study/vosk-model/vosk-model-small-cn-0.22")
# model = Model("./study/vosk-model/vosk-model-cn-0.22")
model = Model("./study/vosk-model/vosk-model-cn-kaldi-multicn-0.15")

# 打开音频文件
wf = wave.open("./study/test.mp3")

# 初始化识别器
rec = KaldiRecognizer(model, 16000)

print("开始识别")
while True:
    # 每次读取4000帧数据
    data = wf.readframes(4000)
    # 读取不到数据则退出
    if len(data) == 0:
        break
    # 识别数据
    rec.AcceptWaveform(data)

# 获取识别结果
result = json.loads(rec.FinalResult())['text'].replace(" ", "")
print(result)