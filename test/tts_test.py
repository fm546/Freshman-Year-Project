from TTS.api import TTS
import torch
from TTS.utils.radam import RAdam
from collections import defaultdict

# 添加 RAdam, defaultdict 和 dict 到安全全局列表
torch.serialization.add_safe_globals([RAdam, defaultdict, dict])

# 初始化 Tacotron 2 + WaveGlow 模型
tts = TTS(model_name="tts_models/zh-CN/baker/tacotron2-DDC-GST", progress_bar=False, gpu=False)