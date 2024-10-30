from openai import OpenAI
from dotenv import load_dotenv
import os

class Optimizator:
    def __init__(self):
        try:
            if not load_dotenv('/config/.env'):
                raise FileNotFoundError()
        except FileNotFoundError as e:
            # 기본 경로에서 다시 시도
            load_dotenv()
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def optimize_code(self, code_snippet):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are an expert software engineer specializing in code optimization and refactoring. "
                        "Please refactor the given code to be as time-efficient and memory-efficient as possible, "
                        "while maintaining functionality. "
                        "Provide only the optimized and refactored code without any formatting or markdown syntax (such as ```). "
                        "Use comments in Korean to explain the changes, focusing on how they improve performance and memory usage."
                    )
                },
                {
                    "role": "user",
                    "content": (
                        f"Here is some code to optimize and refactor:\n\n{code_snippet}\n\n"
                        "Please return only the refactored code with correct indentation and Korean comments, "
                        "focusing on time and memory efficiency. Avoid any markdown syntax such as ```."
                    )
                }
            ]
        )

        return completion.choices[0].message.content

