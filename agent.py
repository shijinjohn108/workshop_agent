from openai import OpenAI
import os
client = OpenAI(
    api_key="",
    base_url="https://api.groq.com/openai/v1",
)

response = client.responses.create(
    input="what is 2+2, give me a very short answer",
    model="openai/gpt-oss-20b",
)
print(response.output_text)
