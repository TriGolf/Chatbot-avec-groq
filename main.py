from groq import Groq


client = Groq(api_key='clé api ici')

messages=[
    {
        "role": "system",
        "content": "Tu est un assistant utile qui parle en français, tu parles sur un terminal donc essaie de faire des paragraphes."
    }
]


while 1 :

    prompt = input("\033[94m"+'Vous : ')#+"\033[0m")
    print("\n")

    messages.append({"role":"user","content":prompt})
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="llama3-8b-8192",
    )

    print("\033[92m"+"Chat Bot : ",chat_completion.choices[0].message.content,"\n"+"\033[0m")
    print("---------------------------------------------\n")
    messages.append({"role" : "assistant", "content" : chat_completion.choices[0].message.content})
