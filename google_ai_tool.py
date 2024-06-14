# google_ai_tool.py
from crewai import Agent, Task, Crew
from crewai_tools import BaseTool
import requests
import json
import os

class GoogleAIAPITool(BaseTool):
    name: str = "GoogleAIAPITool"
    description: str = "A tool to interact with Google AI's LLM API."

    def _run(self, prompt: str) -> str:
        api_key = os.getenv("AIzaSyCmGKPzGU4ovqE1su_GzeVu9joBixoCcOo")
        if not api_key:
            return "API key is missing. Please set the GOOGLE_AI_API_KEY environment variable."

        url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=AIzaSyCmGKPzGU4ovqE1su_GzeVu9joBixoCcOo"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}"
        }
        payload = {
            "prompt": {
                "text": prompt
            },
            "temperature": 0.7,
            "maxOutputTokens": 256
        }

        response = requests.post(url, headers=headers, json=payload)

        if response.status_code == 200:
            response_data = response.json()
            return response_data.get("candidates", [{"output": "No response"}])[0].get("output", "No text in response")
        else:
            return f"Error: {response.status_code} - {response.text}"
