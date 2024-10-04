from openai import OpenAI
from datauri import DataURI
from datetime import datetime as DateTime
from os import path as Path
import json as JSON


# Encodes an image file into a data URI.
def encode_image(path: str) -> str:
    uri = DataURI.from_file(path)
    return str(uri)


# Gets the current date and time formatted as a string.
def current_time() -> str:
    now = DateTime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S")


# Reads the contents of a text file and returns it as a string.
# Note: the path is relative to this script file.
def read_file(rel_path: str) -> str:
    script_dir = Path.dirname(Path.abspath(__file__))
    file_path = Path.join(script_dir, rel_path)
    with open(file_path, "r") as file:
        return file.read()


# Returns a formatted prompt for the system based on the provided information.
def make_prompt(
    address: str = "Not Provided",
    users: list[str] = ["Not Provided"],
    comment: str = "Not Provided",
) -> str:
    # Prepare the required values
    country = "Australia"
    address = str(address)
    time = current_time()
    users_str = ", ".join(users)
    comment = str(comment)
    # Load the prompt template from a file
    prompt = read_file("prompt.md")
    # Substitute placeholders in the template with actual values
    prompt = prompt.replace("__COUNTRY__", country)
    prompt = prompt.replace("__ADDRESS__", address)
    prompt = prompt.replace("__TIME__", time)
    prompt = prompt.replace("__USERS__", users_str)
    prompt = prompt.replace("__COMMENT__", comment)
    return prompt


# Removes the surrounding code fences and parses the JSON content.
def parse_json(content: str):
    lines = content.splitlines()
    left, right = 0, len(lines)
    # Find the starting point (the first line with ```).
    while left < right:
        line = lines[left]
        line = line.strip()
        left += 1
        if line.startswith("```"):
            break
    # Find the ending point (the last line with ```).
    while right > left:
        right -= 1
        line = lines[right]
        line = line.strip()
        if line.startswith("```"):
            break
    # Extract the lines between the code fences
    lines = lines[left:right]
    json_str = "".join(lines)
    # Parse the JSON string into a Python object
    json_obj = JSON.loads(json_str)
    return json_obj


# Returns a json object containing details about the mail cover.
# You must pass a prompt formatted by make_prompt() or the function will not work.
def analyze_mail_cover(prompt: str, image: str) -> dict:
    key = read_file("apikey.txt")
    client = OpenAI(api_key=key)
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
                        "image_url": {"url": encode_image("image.png")},
                    }
                ],
            },
        ],
        max_tokens=300,
    )
    text = response.choices[0].message.content
    return parse_json(text)
