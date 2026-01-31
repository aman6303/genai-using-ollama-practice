# similar to generate but has extra param called messages which act as a history manager for current session

import ollama

# lets understand the difference by comparinng it with generate method

# chatbot using generate method

print("Chatbot using Generate")
while True:
    input_text = input("User: ")

    if input_text.lower() == "quit":
        print("Assistant : Goodbye")
        break
    response = ollama.generate(model="gemma3:latest", prompt=input_text)

    print("Assistant:", response.response)

# we can do the same using chat method (by mantainng the memory as messages)
print("Chatbot using chat")
messages = []

messages.append(
    {
        "role": "system",
        "content": "You are a funny assistant, you tell joke in every output",
    }
)  # we need to pass each compement as single dict

while True:
    input_text = input("User: ")

    if input_text.lower() == "quit":
        print("Assistant: Goodbye")
        break
    messages.append({"role": "user", "content": input_text})
    response = ollama.chat(model="gemma3:latest", messages=messages)
    print("Assistant:", response["message"]["content"])
    messages.append({"role": "Assistant", "content": response["message"]["content"]})
