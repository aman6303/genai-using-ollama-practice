import ollama

# we can achieve stream output using stream param
response = ollama.generate(
    model="qwen3:latest", prompt="What is the color of sky?", stream=True
)

print(response)  # we get iter object

# for i in response:
#     print(i)
#     print("**")

for i in response:
    print(i["response"], end="")
