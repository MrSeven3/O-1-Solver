def solve(mode, question, api_key=None):
    import requests
    output = ""
    match mode:
        case 1:
            return "42"
        case 2:
            try:
                result = eval(question)
                return str(result)
            except Exception as e:
                return str(e)

        case 3:
            try:
                response = requests.post(
                    'https://ai.hackclub.com/proxy/v1/responses',
                    headers={
                        'Authorization': 'Bearer ' + str(api_key),
                        'Content-Type': 'application/json',
                    },
                    json={
                        'model': 'openai/gpt-oss-120b',
                        'input': question + "(admin note: please have your answer as short as possible)",
                        'max_output_tokens': 1500,
                    }
                )

                # unfortunately, because json and python together are annoying, I had to get AI (the irony) to help with this parser.
                # its probably not great, but it works
                if response.status_code == 200:
                    texts = []

                    for item in response.json()["output"]:
                        if item.get("type") == "message" and item.get("role") == "assistant":
                            for part in item.get("content", []):
                                if part.get("type") == "output_text":
                                    texts.append(part["text"])

                    return "".join(texts)
                else:
                    return response.json()
            except Exception as e:
                return str(e)
    return "Complete Solving Failure"