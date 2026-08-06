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
# 3 prompts
prompt1= "Hi!"
prompt2= "Explain the theory of relativity in simple terms."
prompt3= "Write a 1000 words essay about the beauty of nature."

prompts = [prompt1, prompt2, prompt3]
for prompt in prompts:
    message = {
        "role": role,
        "content": prompt
    }
    messages = [message]
    #max_tokens=500 means the model will generate a response with a maximum of 500 tokens. You can adjust this value based on your needs.
    response = client.chat.completions.create(model=model, messages=messages, max_tokens=500)
    usage = response.usage
    print(f"Prompt: {prompt} --> Tokens used: {usage.total_tokens}, Prompt tokens: {usage.prompt_tokens}, Completion tokens: {usage.completion_tokens} Finish Reason: {response.choices[0].finish_reason}")



#prompt="Do you know Virat Kohli?"

#message = {
#    "role": role,
#    "content": prompt
#}
#messages = [message]
#response = client.chat.completions.create(model=model, messages=messages)
#print(response)
#print(response)

#print("#######################")

#answer = response.choices[0].message.content
#print(answer)