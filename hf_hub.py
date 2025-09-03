import os
from huggingface_hub import InferenceClient

client = InferenceClient(
    provider="cerebras",
    api_key="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",
)

completion = client.chat.completions.create(
    model="meta-llama/Llama-3.1-8B-Instruct",
    messages=[
        {
            "role": "user",
            "content": "What is the capital of France?"
        }
    ],
)

print(completion.choices[0].message)