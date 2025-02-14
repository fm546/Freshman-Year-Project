import ollama

# 调用 DeepSeek-V1.5B 模型生成回复
def generate_response(prompt):
    response = ollama.generate(
        model="deepseek-r1:1.5b",
        prompt=prompt
    )
    return response["response"]

# 测试生成回复
prompt = "你好，请问你能帮我做什么？"
response = generate_response(prompt)
print(response)