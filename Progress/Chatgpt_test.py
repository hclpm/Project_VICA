from openai import OpenAI
import keys

client = OpenAI(
    # defaults to os.environ.get("OPENAI_API_KEY")
    api_key=keys.ChatGPT_key(),
)

request = input("input question: ")

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "summarize the following content in Korean: " + request,
        }
    ],
    model="gpt-3.5-turbo",
)
print(chat_completion.choices[0].message.content)
print("hello world")