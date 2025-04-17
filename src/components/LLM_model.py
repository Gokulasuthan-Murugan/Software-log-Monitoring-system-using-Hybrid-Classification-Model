import os
import sys

from groq import Groq # type: ignore

from src.exception import CustomException
from src.logger import logging

class LLMClassifier:
    def __init__(self):
        os.environ["GROQ_API_KEY"] = ""  
        self.client = Groq(api_key=os.getenv("GROQ_API_KEY"))

    def classify_log_message(self, log_message: str):
        try:
            prompt = (
                f"Classify the log message into one of these categories: (1) workflow,(2) Deprication Warning. "
                f" If you can't figure out a category, return 'unclassified'. "
                f"Only return the category name. No preamble.\nLog message: {log_message}"
            )

            response = self.client.chat.completions.create(
                model="llama3-70b-8192",
                messages=[{"role": "user", "content": prompt}]
            )

            label = response.choices[0].message.content.strip()
            logging.info(f"Log classified as: {label}")
            return label

        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    classifier = LLMClassifier()
    example_log = "System reboot initiated by user 12345."
    print(classifier.classify_log_message(example_log))