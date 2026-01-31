# we can set the params of a model using option parameter of generate method

import ollama

response1 = ollama.generate(model="gemma3:latest", prompt="what is the color of sky")

# giving the same prmpt by changing the params of the same model

response2 = ollama.generate(
    model="",
    prompt="what is the color of sky",
    options={"temperature": 1, "top_k": 0.3, "top_p": 0.5},
)
