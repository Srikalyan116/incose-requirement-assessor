import os
from openai import OpenAI
import json

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_analysis(text, context):

    system_prompt = """
You are an INCOSE-certified systems engineering expert.

Evaluate requirements based on ISO/IEC/IEEE 29148.

Return STRICT JSON ONLY.
"""

    user_prompt = f"""
Requirement:
{text}

Retrieved Examples:
{context}

Evaluate:
- Clarity
- Unambiguity
- Verifiability
- Atomicity
- Completeness

Return:
{{
 "compliance_score": 0-100,
 "compliance_level": "High | Medium | Low",
 "issues": [],
 "risk_level": "Low | Medium | High",
 "improvements": [],
 "rewritten_requirement": ""
}}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.2,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )

    content = response.choices[0].message.content

    try:
        return json.loads(content)
    except:
        return {"error": content}
