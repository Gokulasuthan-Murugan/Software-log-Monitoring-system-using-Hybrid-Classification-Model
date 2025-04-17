import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m-%d-%Y-%H-%M-%S')}.log"
logs_path=os.path.join(os.getcwd(),'logs',LOG_FILE)
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH=os.path.join(logs_path,LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__=="__main__":
    logging.info("initialized logging file logger.py")


"""
%(asctime)s==> returns the time in readable format
%(lineno)d==> Source line number where the logging call was issued (if available).
%(name)s==> Name of the logger used to log the call.
%(levelname)s==>returns the level like info,warnings,debug...
%(message)s==>Actual log messsge 

"""