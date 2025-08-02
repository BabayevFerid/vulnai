import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_services_with_openai(xml_summary: str):
    prompt = f"""
You are a cybersecurity analyst. Analyze the following scan result and identify potential vulnerabilities, CVEs, and risk levels.

Scan summary:
{xml_summary}

Respond in this JSON format:
{{
  "vulnerabilities": [
    {{
      "service": "service_name",
      "risk": "low | medium | high | critical",
      "cve": "CVE-XXXX-XXXX",
      "explanation": "Why this is a risk"
    }}
  ],
  "summary": "brief human-readable summary"
}}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a professional vulnerability analyst."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    # Extract and parse the response
    try:
        output_text = response.choices[0].message.content.strip()
        return eval(output_text)  # ⚠️ Real-world projects should use json.loads instead
    except Exception as e:
        return {"error": f"Failed to parse OpenAI response: {str(e)}"}
