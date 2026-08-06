import os
from pathlib import Path
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
my_api_key=os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable is not set. Please set it in your .env file.")

client = Groq(api_key=my_api_key)

model ="llama-3.3-70b-versatile"
role="user"
prompt="Suggest a name for my clothes company."
message_system={
    "role": "system",
    #"content": "You are my loving girlfriend"
    #"content": "You are my strictoffice colleague and also my manager"
    "content": "You are a brand manager and you have to suggest me a name for my clothes company. name should be of one word"
}
#message me role and content

message = {
    "role": role,
    "content": prompt
}
messages = [message_system,message]
#Temperature by default is 0 meaning safe. range is[0,2].
response = client.chat.completions.create(model=model, messages=messages, temperature=2)
#print(response)

print("#######################")

answer = response.choices[0].message.content
print(answer)