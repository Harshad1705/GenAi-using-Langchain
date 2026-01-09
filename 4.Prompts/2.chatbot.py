from langchain_openai import ChatOpenAI


model = ChatOpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1",
    model="openai/gpt-4o-mini",
    temperature=0.5
)

chat_history = []

while True:
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input == 'exit' :
        break
    result = model.invoke(chat_history)
    chat_history.append(result.content)
    print("AI: ",result.content)
print(chat_history)