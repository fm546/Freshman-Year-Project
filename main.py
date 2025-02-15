from asr import ASR
from llm import LLM
from tts import ChineseTTS


def main():
    # 初始化 ASR 和 LLM
    asr = ASR()
    llm = LLM()
    tts = ChineseTTS()

    # 开始流式语音识别
    for text in asr.listen():
        if text.strip():  # 如果识别到非空文本
            print(f"识别到的文本: {text}")
            # 调用 LLM 生成回复
            response = llm.generate_response(text)
            print(f"LLM 回复: {response}")
            # 调用 TTS 生成语音并播放
            tts.synthesize_speech(response)
            tts.play_audio("output_wav/output.wav")
if __name__ == "__main__":
    main()