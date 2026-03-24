import os

def extract(text):
    try:
        from openai import OpenAI
        client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

        prompt = f"""
        Extract entities and relationships from:
        "{text}"
        Return JSON format.
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return eval(response.choices[0].message.content)

    except Exception as e:
        print("⚠️ Using fallback mock LLM:", e)

        # fallback mock
        return {
    "entities": [
        {"name": "Addis Ababa", "type": "City"},
        {"name": "Ethiopia", "type": "Country"}
    ],
    "relations": [
        {
            "subject": "Addis Ababa",
            "predicate": "capitalOf",
            "object": "Ethiopia",
            "confidence": 0.95
        },
        {
            "subject": "Ethiopia",
            "predicate": "locatedIn",
            "object": "Africa",
            "confidence": 0.9
        }
    ]
}
