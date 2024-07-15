from openai import OpenAI
import os

os.environ.get("OPENAI_API_KEY")


client = OpenAI()


response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Vou viajar para a praia em Peruíbe. Me dê dicas de lugares para visitar.",
        },
    ],
)

print(response.choices[0].message.content)
