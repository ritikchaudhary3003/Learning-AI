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



#Structure it
from pydantic import BaseModel

class Ticket(BaseModel):
    name: str
    #address: str
    phone_number: int
    email: str
    issue: str

schema = Ticket.model_json_schema()
response_format={
    "type": "json_object"
}
system_prompt = f"""
Extract the personal information strictly based on this schema and return the result in JSON format.
{schema}
"""

message_system ={
    
    "role": "system",
    "content": system_prompt
}



text ="Hello My name is Ritik and I have purchased a iphone and it stopped working after 2 days. My adress is 123 abd gfr, and my phone number is 223344. My email is abc@gmail.com"
prompt=f"""
This is a customer ticket. Please extract the personal information from this.
{text} 
"""

message = {
    "role": role,
    "content": prompt
}
messages = [message_system, message]
response = client.chat.completions.create(model=model, messages=messages, response_format=response_format)
answer = response.choices[0].message.content
print(answer)

#To read it 
import json
raw_json=answer
data_files=json.loads(raw_json)
ticket = Ticket(**data_files)

print(ticket.name)
print(ticket.phone_number)
print(ticket.email)
print(ticket.issue)