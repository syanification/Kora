from openai import OpenAI
from gptConfig import API_KEY
client = OpenAI(api_key=API_KEY)

def getCommand(input):
    completion = client.chat.completions.create(
        model="ft:gpt-4o-mini-2024-07-18:personal::Ar4dngUA",
        messages=[
            {"role": "user", "content": input}
        ]
    )

    return completion.choices[0].message.content


print(getCommand("play the next song please"))