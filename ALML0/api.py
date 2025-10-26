from groq import Groq
import json
f=open("text.txt",'r')
lines=f.readlines()
f.close()
D = {}
client = Groq(api_key="NOPE",)
for l in lines:
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": l,
            }
        ],
        model="llama-3.3-70b-versatile",
    )
    D[l] = chat_completion.choices[0].message.content

json_str = json.dumps(D, indent=4)
with open("sample.json", "w") as f:
    f.write(json_str)
