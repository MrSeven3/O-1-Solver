def solve(mode, question, api_key=None):
    import requests
    import time
    match mode:
        case 1:
            return "42"
        case 2:
            expected_run_time = 5
            start_time = time.time()
            try:
                result = eval(question)
                end_time = time.time()
                run_time = end_time-start_time

                if run_time < expected_run_time:
                    time.sleep(expected_run_time-run_time)

                return str(result)
            except Exception as e:
                end_time = time.time()
                run_time = end_time - start_time

                if run_time < expected_run_time:
                    time.sleep(expected_run_time - run_time)
                return str(e)

        case 3:
            expected_run_time = 15
            start_time = time.time()
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

                if response.status_code == 200:
                    texts = []

                    # unfortunately, because json and python together are annoying, I had to get AI (the irony) to help with this parser.
                    # its probably not great, but it works
                    for item in response.json()["output"]:
                        if item.get("type") == "message" and item.get("role") == "assistant":
                            for part in item.get("content", []):
                                if part.get("type") == "output_text":
                                    texts.append(part["text"])

                    end_time = time.time()
                    run_time = end_time - start_time

                    if run_time < expected_run_time:
                        time.sleep(expected_run_time - run_time)

                    return "".join(texts)
                else:
                    return response.json()
            except Exception as e:
                end_time = time.time()
                run_time = end_time - start_time

                if run_time < expected_run_time:
                    time.sleep(expected_run_time - run_time)
                return str(e)
    return "Complete Solving Failure"