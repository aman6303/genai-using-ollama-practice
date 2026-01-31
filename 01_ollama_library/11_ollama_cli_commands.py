# we can also perform all possible cli commands using ollama library also

import ollama

# OLLAMA LIST
local_models = ollama.list()
print(local_models)


for i in local_models["models"]:
    print(i["model"])
    print(i["size"])


# OLLAMA PULL
model_name = "tinyllama:latest"
progess = ollama.pull(model_name, stream=True)

for i in progess:
    print(i)


# OLLAMA SHOW
models_details = ollama.show("llama3.2:1b")
print(models_details)

model_dict = models_details.dict()
print(model_dict["capabilities"])
print(model_dict["parameters"])


# OLLAMA DELETE
ollama.delete("embeddinggemma:latest")
