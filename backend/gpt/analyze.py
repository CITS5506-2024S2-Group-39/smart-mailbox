import openai
from datauri import DataURI
from datetime import datetime as DateTime
from os import path as Path
import json as JSON

def encode_image(path: str) -> str:
    uri = DataURI.from_file(path)
    return str(uri)

def current_time() -> str:
    now = DateTime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")

def read_file(rel_path: str) -> str:
    script_dir = Path.dirname(Path.abspath(__file__))
    file_path = Path.join(script_dir, rel_path)
    with open(file_path, "r") as file:
        return file.read()

def make_prompt(
    address: str = "Not Provided",
    users: list[str] = ["Not Provided"],
    comment: str = "Not Provided",
) -> str:
    country = "Australia"
    address = str(address)
    time = current_time()
    users_str = ", ".join(users)
    comment = str(comment)
    prompt = read_file("prompt.md")
    prompt = prompt.replace("__COUNTRY__", country)
    prompt = prompt.replace("__ADDRESS__", address)
    prompt = prompt.replace("__TIME__", time)
    prompt = prompt.replace("__USERS__", users_str)
    prompt = prompt.replace("__COMMENT__", comment)
    return prompt

def parse_json(content: str):
    lines = content.splitlines()
    left, right = 0, len(lines)
    while left < right:
        line = lines[left].strip()
        left += 1
        if line.startswith("```"):
            break
    while right > left:
        right -= 1
        line = lines[right].strip()
        if line.startswith("```"):
            break
    lines = lines[left:right]
    json_str = "".join(lines)
    json_obj = JSON.loads(json_str)
    return json_obj

def gpt_analyze_image(prompt: str, image: str) -> dict:
    key = read_file("apikey.txt")
    client = openai.OpenAI(api_key=key)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content": [{"type": "text", "text": prompt}],
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {"url": encode_image(image)},
                    }
                ],
            },
        ],
        max_tokens=300,
    )
    text = response.choices[0].message.content
    return parse_json(text)