import google.generativeai as genai
import os
import time

genai.configure(api_key=os.environ["API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

while True:
    prompt = input("Enter your prompt: ")
    if prompt != 'exit':
        response = model.generate_content(prompt)

        for char in response.text:
                print(char, end='', flush=True)
                time.sleep(0.004)  
    else:
        response = 'Thank you! for use again run genai.py in terminal with interupter'
        for char in response:
                print(char, end='', flush=True)
                time.sleep(0.004) 
        break
