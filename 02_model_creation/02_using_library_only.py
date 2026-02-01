import ollama

# Configuration
MODEL_NAME = "my-qwen2"
NAMESPACE = "aman6303"  # Replace with your Ollama username
FINAL_TAG = f"{NAMESPACE}/{MODEL_NAME}"


def create_and_push_model():
    try:

        # 1. Create the model
        print(f"Building '{MODEL_NAME}'...")
        # We use stream=True to see progress, otherwise it hangs silently
        for progress in ollama.create(
            model=MODEL_NAME,
            from_="qwen3:0.6b",  # Note: 'from_' with an underscore
            system="You are a senior DevOps engineer. You answer questions using command-line examples.",
            parameters={"temperature": 0.3},
            stream=True,
        ):
            if "status" in progress:
                print(f"   Status: {progress['status']}", end="\r")
        print(f"\n Model '{MODEL_NAME}' created successfully.")

        # 2. Copy (Tag) the model for the registry
        print(f"Tagging model as '{FINAL_TAG}'...")
        ollama.copy(MODEL_NAME, FINAL_TAG)

        # 3. Push the model
        print(f"DO  Pushing '{FINAL_TAG}' to registry...")
        for progress in ollama.push(FINAL_TAG, stream=True):
            if "status" in progress:
                print(f"   Status: {progress['status']}", end="\r")

        print(f"\nSuccess! Model pushed to https://ollama.com/{FINAL_TAG}")

    except ollama.ResponseError as e:
        print(f"\nError: {e.error}")


if __name__ == "__main__":
    create_and_push_model()
