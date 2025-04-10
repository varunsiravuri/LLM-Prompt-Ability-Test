import os
import json
import re
import requests
from dotenv import load_dotenv

from utils.prompts import (
    JD_PARSE_SYSTEM_PROMPT,
    RESUME_PARSE_SYSTEM_PROMPT,
    JD_RESUME_MATCH_SYSTEM_PROMPT,
    jd_parse_user_prompt,
    resume_parse_user_prompt,
    jd_resume_match_user_prompt
)

# Load Environment Variables
load_dotenv()
deepseek_api_key = os.getenv("DEEPSEEK_API_KEY")
model = "deepseek-chat"  # Confirm the model name from DeepSeek Docs

# Cleaning LLM Output
def clean_llm_output(llm_text: str) -> dict:
    try:
        llm_text = llm_text.strip()
        llm_text = re.search(r'\{.*\}', llm_text, re.DOTALL).group()
        data = json.loads(llm_text)
    except Exception as e:
        print("Error loading LLM Output JSON:", e)
        data = {}
    return data


# JD Parsing Function (DeepSeek API)
def parse_jd(jd_text, api_key, model) -> dict:
    url = "https://api.deepseek.com/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": JD_PARSE_SYSTEM_PROMPT},
            {"role": "user", "content": jd_parse_user_prompt(jd_text)},
        ],
    }

    response = requests.post(url, headers=headers, json=payload)
    result_json = response.json()

    # Debug print response to see what's coming
    print("Response from DeepSeek API:")
    print(json.dumps(result_json, indent=2))

    if "choices" in result_json:
        llm_output = result_json["choices"][0]["message"]["content"]
        result = clean_llm_output(llm_output)
    else:
        print("API Error:", result_json)
        result = {}

    return result



# Main Function
def main():
    print("Running Main Function...")  # Debug print

    jd_text = """We are looking for a Software Engineer with experience in Python, Django, and REST API development.

Qualifications:
- Bachelor's Degree in Computer Science
- 3+ years of Software Development Experience
- Knowledge of Cloud Technologies (AWS or Azure)
- Good communication skills"""

    print("=== Parsing JD ===")

    jd_info = parse_jd(jd_text, deepseek_api_key, model)

    print("=== JD Info Parsed ===")
    print(json.dumps(jd_info, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()

