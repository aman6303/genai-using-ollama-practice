import ollama

messages = [{"role": "user", "content": "Tell me short story about dragons"}]


response = ollama.chat(
    model="gemma3:latest",
    messages=messages,
    options={
        "temperature": 1.0,
        "top_p": 0.9,
        "num_predict": 100,
        "repeat_penalty": 1.2,
    },
)


print(response["message"]["content"])

# similarly we can use all of other params just like generate
