# # Please install OpenAI SDK first: `pip3 install openai`
#
# from openai import OpenAI
#
# client = OpenAI(api_key="sk-d201e8b15c9d4f9f92d8268025f25a26", base_url="https://api.deepseek.com")
#
# response = client.chat.completions.create(
#     model="deepseek-chat",
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant"},
#         {"role": "user", "content": "Hello"},
#     ],
#     stream=True
# )
#
# print(response.choices[0].message.content)
from openai import OpenAI

client = OpenAI(api_key="sk-d201e8b15c9d4f9f92d8268025f25a26", base_url="https://api.deepseek.com")

# 创建流式响应
stream = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=True,
)

# 逐块处理响应
for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")