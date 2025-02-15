import ollama

class LLM:
    def __init__(self, model_name="qwen:1.8b"):
        self.model_name = model_name

    def generate_response(self, prompt):
        # 调用 Ollama 生成回复
        response = ollama.generate(model=self.model_name, prompt=prompt)
        return response["response"]