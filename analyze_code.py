import google.generativeai as genai
import sys

# Configure the API key
genai.configure(api_key='AIzaSyCLY3okKHz7qZUfW-Q8Q0GDjsvwmnIYaKs')

# Start a new chat session
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

def analyze_code(code):
    prompt = (
        "You are an AI skilled in analyzing code. Analyze the following C++ code "
        "and provide its time complexity, space complexity, and any potential "
        "optimizations.\n\n"
        f"{code}"
    )

    try:
        response = chat.send_message(prompt)
        analysis = "".join(chunk.text for chunk in response if chunk.text)
        return analysis
    except Exception as e:
        print(f"Error during code analysis: {e}", file=sys.stderr)
        return f"Error during code analysis: {str(e)}"

if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            code_file = sys.argv[1]
            with open(code_file, 'r') as f:
                code = f.read()
            analysis = analyze_code(code)
            print(analysis)
        else:
            print("No code file provided", file=sys.stderr)
            sys.exit(1)
    except Exception as e:
        print(f"Error in main execution: {e}", file=sys.stderr)
        sys.exit(1)
