from openrouter import OpenRouter
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

match mode:
    case 1:
        print("42")
    case 2:
        result = eval(question)
        print(str(result))

    case 3:
        print("Enter your API key: ")
        API_KEY = input()

        print("Enter your question")

        client = OpenRouter(
            api_key=API_KEY,
            server_url="https://ai.hackclub.com/proxy/v1",
        )

        response = client.chat.send(
            model="openai/gpt-oss-120b",
            messages=[
                {"role": "user", "content": "Tell me a joke."}
            ],
            stream=False,
        )

        print(response.choices[0].message.content)

