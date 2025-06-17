import os
import requests

LLM_API_KEY = os.getenv("LLM_API_KEY")


def generate_alternative_llm(prompt: str, input_text: str) -> str:
    """Generate an alternative LM for an input text."""
    full_prompt = f"""You are a professional content editor. {prompt}

    Original text:
    {input_text}

    Rewrite the text according to the instructions. Return ONLY the final rewritten version without any additional commentary or reasoning.
    """

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {LLM_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost",
        },
        json={
            "model": "anthropic/claude-3-haiku",
            "messages": [{"role": "user", "content": full_prompt}],
            "max_tokens": 500,
            "temperature": 0.7,
        },
        timeout=30,
    )

    try:
        response.raise_for_status()
        data = response.json()
        return data["choices"][0]["message"]["content"].strip()
    except Exception as e:
        raise RuntimeError(f"LLM API error: {e}\nResponse: {response.text}")
