import ollama

# getting response using .generate method of ollama

response = ollama.generate(
    model="tinyllama:latest", prompt="Who is the prime minister of India"
)

print(response)
print(type(response))
print(response.response)
print(response.model_dump().keys())  # converting to dict and then getting the keys
