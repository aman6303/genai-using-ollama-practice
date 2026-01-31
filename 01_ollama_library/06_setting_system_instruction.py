# we can set our models system instruction using system param of genefrate method

import ollama

# without system
response1 = ollama.generate(model="", prompt="Why is the ocean blue")
print(response1.response)

# with system
response2 = ollama.generate(
    model="qwen3:latest",
    prompt="why is the ocean blue",
    system="You are an funny assistant , you explain things in funny way",
)
print(response2.response)
