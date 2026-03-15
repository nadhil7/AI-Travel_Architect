def build_itinerary_prompt(destination: str, style: str, days: int):
    return f"""
Generate a {days}-day travel itinerary.

Destination: {destination}
Travel style: {style}

Return ONLY JSON in this format:

{{
  "days": [
    {{
      "day": number,
      "activities": [string]
    }}
  ]
}}

Rules:
- Exactly {days} days
- 3 to 5 activities per day
- No explanations
- JSON only
"""