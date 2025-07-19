from typing import Any, Dict
import openai

class AIService:
    def __init__(self, api_key: str):
        openai.api_key = api_key

    def generate_response(self, user_input: str) -> str:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "user", "content": user_input}
            ]
        )
        return response['choices'][0]['message']['content']

    def process_input(self, user_input: str) -> Dict[str, Any]:
        # Here you can add logic to process the input and determine the type of response needed
        response = self.generate_response(user_input)
        return {
            "input": user_input,
            "response": response
        }