from nexa.gguf import NexaVLMInference
import tempfile

def test_image_generation():
    with tempfile.TemporaryDirectory() as temp_dir:
        model = NexaVLMInference(
            model_path="nanollava",
        )
        output = model.create_chat_completion(
            messages=[
                {
                    "role": "system",
                    "content": "You are an assistant who perfectly describes images.",
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "What's in this image?"},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": "https://www.wikipedia.org/portal/wikipedia.org/assets/img/Wikipedia-logo-v2.png"
                            },
                        },
                    ],
                },
            ],
            stream=True,
        )
        for chunk in output:
            delta = chunk["choices"][0]["delta"]
            if "role" in delta:
                print(delta["role"], end=": ")
            elif "content" in delta:
                print(delta["content"], end="")


# if __name__ == "__main__":
#     print("=== Testing 1 ===")
#     test1()
