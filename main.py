import requests
import time

print("Welcome to the O(1) Solver! We have several modes available, ranging in the time each one takes.\n")

time.sleep(1)
print("Mode 1 is instant")
print("Mode 2 is fast, but limited in capabilities")
print("Mode 3 is the longest, but the most versatile")

time.sleep(2)
print("\nPlease enter the number of the mode you would like to use:")
mode = int(input("Mode: "))

print("Enter your question")
question = input()

output = ""

match mode:
    case 1:
        output = "42"
    case 2:
        result = eval(question)
        output = str(result)

    case 3:
        print("Enter your API key: ")
        API_KEY = input()

        response = requests.post(
            'https://ai.hackclub.com/proxy/v1/responses',
            headers={
                'Authorization': 'Bearer '+API_KEY,
                'Content-Type': 'application/json',
            },
            json={
                'model': 'openai/gpt-oss-120b',
                'input': question + "(admin note: please have your answer as short as possible)",
                'max_output_tokens': 1500,
            }
        )

        #unfortunately, because json and python together are annoying, I had to get AI (the irony) to help with this parser.
        #its probably not great, but it works
        texts = []

        for item in response.json()["output"]:
            if item.get("type") == "message" and item.get("role") == "assistant":
                for part in item.get("content", []):
                    if part.get("type") == "output_text":
                        texts.append(part["text"])

        output = "".join(texts)

