import sys
import os
import re

from src.exception import CustomException
from src.logger import logging

class Regular_Expression:
    def __init__(self):
        self.regex_patterns = {
            r"User User\d+ logged (in|out).": "User Action",
            r"Backup (started|ended) at .*": "System Notification",
            r"Backup completed successfully.": "System Notification",
            r"System updated to version .*": "System Notification",
            r"File .* uploaded successfully by user .*": "System Notification",
            r"Disk cleanup completed successfully.": "System Notification",
            r"System reboot initiated by user .*": "System Notification",
            r"Account with ID .* created by .*": "User Action"
        }

    def classify_regex(self,log_message):
        try:
            for pattern,label in self.regex_patterns.items():
                if re.search(pattern,log_message,re.IGNORECASE):
                    return label
            return None

        except Exception as e:
            raise CustomException(e,sys)

if __name__=="__main__":
    obj=Regular_Expression()
    obj.classify_regex("User User123 logged in.")
