import requests
import os

def generate_workout_program():
    api_key = os.getenv('CHATGPT_API_KEY')
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json',
    }
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role': 'user',
                      'content': 
                        """
                        ГЕНЕРАЦИЯ
                        """}],
    }
    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
    return response.json().get('choices')[0]['message']['content']