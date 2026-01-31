# giving multi model input to a model

import base64  # we need to encode the image

import ollama

image_path = "img.png"

with open(image_path, "rb") as f:
    image_bytes = f.read()
    image_64 = base64.b64encode(image_bytes).decode("utf-8")

# ensure model has vision capabilties
response = ollama.generate(
    model="gemma3:latest", images=[image_64], prompt="Describe image in short format"
)

print(response.response)


# if we want to multiple images as input -- we need to pass them as list

images_path = ["img1.png", "img2.png", "img3.png"]

# coverting the image in 64 bit encoding
final_images = []

for image in images_path:
    with open(image, "rb") as f:
        image_bytes = f.read()
        image_64 = base64.b64encode(image_bytes).decode("utf-8")
        final_images.append(image_64)

response2 = ollama.generate(
    model="gemma3:latest",
    images=final_images,
    prompt="Generate an story based on these images, make sure you take context from each and every image in sequential order.",
)

print(response2.response)
