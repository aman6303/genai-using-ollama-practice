# we can also add the images also
# load the image and convert to to base64 encode
import base64

import ollama

image_path = "img.png"
with open(image_path, "rb") as f:
    image_bytes = f.read()
    image_64 = base64.b64encode(image_bytes).decode("utf-8")

print("Chatbot using chat regarding an image")
messages = []

messages.append(
    {
        "role": "system",
        "content": "You are a funny assistant, you tell joke in every output",
        "image": [image_64],  # we can attach image at the begin
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
