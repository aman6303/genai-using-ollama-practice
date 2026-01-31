import ollama
import re

response = ollama.generate(
    model="qwen3:latest", prompt="why is plant leaves green in color"
)

response_text = response.response

# we can hide or remove thinking part as below
actual_response = re.sub(
    r"<think>.*?</think>", "", response_text, flags=re.DOTALL
).strip()
print(actual_response)
