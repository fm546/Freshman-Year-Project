from langchain_community.chat_models import ChatSparkLLM
from langchain_core.messages import HumanMessage


chat = ChatSparkLLM(
spark_app_id="a199a1e3", spark_api_key="10c1cfa455bad18ead3608f4a1c06bb3", spark_api_secret="ODUzOGNjMWNmYjliZWRjYTQ1NWY4Yjc1"
)
a = input("请输入：")
message = HumanMessage(content = a)

print(chat([message]).content)