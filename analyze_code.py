import os
import google.generativeai as genai
import sys

genai.configure(api_key='AIzaSyCLY3okKHz7qZUfW-Q8Q0GDjsvwmnIYaKs')

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def analyze_code(code):
    prompt = (
        "You are an AI skilled in analyzing code. Analyze the following C++ code "
        "and provide its time complexity, space complexity, and any potential "
        "optimizations.\n\n"
        f"{code}"
    )

    response = chat.send_message(prompt)
    analysis = "".join(chunk.text for chunk in response if chunk.text)

    return analysis

if __name__ == "__main__":
    if len(sys.argv) > 1:
        code_file = sys.argv[1]
        with open(code_file, 'r') as f:
            code = f.read()
        analysis = analyze_code(code)
        print(analysis)
