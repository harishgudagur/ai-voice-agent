from groq import Groq
import json
import re
import os
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
def process_query(text):
    prompt = f"""
You are a healthcare appointment assistant.

Extract structured data from user input.

User: "{text}"

STRICT RULES:
- Choose ONLY ONE intent: book OR cancel OR reschedule
- Return ONLY valid JSON
- No explanation, no markdown, no text

Example:
{{
  "intent": "book",
  "doctor": "dentist",
  "date": "tomorrow",
  "time": null
}}
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        output = response.choices[0].message.content.strip()
        print("RAW OUTPUT:", output)

        # 🔥 Remove markdown ```json ```
        output = re.sub(r"```json|```", "", output).strip()

        # 🔥 Extract JSON safely
        match = re.search(r"\{[\s\S]*\}", output)
        if not match:
            return {"intent": "unknown"}

        result = json.loads(match.group())

        # ✅ Normalize missing fields
        result.setdefault("intent", "book")
        result.setdefault("doctor", None)
        result.setdefault("date", None)
        result.setdefault("time", None)

        # ✅ Fix invalid intent
        if result["intent"] not in ["book", "cancel", "reschedule"]:
            result["intent"] = "book"

        return result

    except Exception as e:
        print("ERROR:", e)
        return {"intent": "unknown"}