import ollama

class LLM:
    def __init__(self, model_name="short-qwen:latest"):
        self.model_name = model_name

    def generate_response(self, prompt):
        # 调用 Ollama API 生成回复
        response = ollama.generate(
            model=self.model_name,
            prompt=prompt,
            max_tokens=100
        )
        return response["response"]

# 测试 LLM 模块
if __name__ == "__main__":
    llm = LLM()
    prompt = "你好，请问你能帮我做什么？"
    response = llm.generate_response(prompt)
    print("LLM Response:", response)