import ollama
import re

class LLM:
    def __init__(self, model_name="deepseek-r1:8b"):
        self.model_name = model_name

    def generate_response(self, prompt):
        # 调用 Ollama 生成回复
        response = ollama.generate(model=self.model_name, prompt=prompt)
        # 去掉思考过程
        clean_response = re.sub(r"<think>.*?</think>", "", response["response"], flags=re.DOTALL).strip()
        return clean_response