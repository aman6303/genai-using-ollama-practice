# if we want to get structure output(eg. in json format) we can use the format param

import ollama

paragraph = """There are ten individuals in the group. Alex Johnson, a 28-year-old male from California, 
enjoys hiking. Priya Singh,
 a 34-year-old female from Texas, works as a graphic designer. Michael Brown, 
 a 45-year-old male from New York, loves cooking.
  Sara Lopez, a 29-year-old female from Florida, is an aspiring writer. David Kim,
   a 38-year-old male from Illinois, practices photography.
   Anita Patel, a 26-year-old female from Arizona, volunteers at animal shelters.
    James Wilson, a 50-year-old male from Ohio,
    collects vintage records. Emily Davis, a 31-year-old female from Washington,
     runs marathons. Robert Martinez,
     a 42-year-old male from Georgia, enjoys woodworking. Finally, Neha Sharma,
      a 27-year-old female from Colorado, is passionate about
     environmental conservation."""

response1 = ollama.generate(model="qwen3:latest", prompt=paragraph, format="json")
# we may not get consistant output
print(response1.response)

# we can give our own format
response = ollama.generate(
    model="",
    prompt=paragraph,
    format={
        "type": "object",
        "properties": {
            "people": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "name": {"type": "string"},
                        "age": {"type": "integer"},
                        "gender": {"type": "string"},
                        "state": {"type": "string"},
                    },
                    "required": ["name", "age", "gender", "state"],
                },
            }
        },
        "required": ["people"],  # this key is required
    },
)

print(response.response)
