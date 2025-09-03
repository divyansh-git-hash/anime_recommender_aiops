import requests

headers = {
    "Authorization": "Bearer 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",
    "Content-Type": "application/json"
}

data = {
    "model": "llama-3.1-8b-instant",  # or whatever model you're using
    "messages": [{"role": "user", "content": "Hello"}]
}

response = requests.post("https://api.groq.com/openai/v1/chat/completions", headers=headers, json=data)
print(response.status_code)
print(response.json())
