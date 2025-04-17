import os
import sys

from src.pipeline.Training_Pipeline import Training_Pipeline
from src.components.Regex_Matcher import Regular_Expression
from src.components.LLM_Model import LLMClassifier
from src.components.Logistic_Model import LogisticModel
from src.exception import CustomException
from src.logger import logging

class PredictionPipeline:
    def __init__(self):
        self.regex_matcher=Regular_Expression()
        self.LLM_classifier=LLMClassifier()
        self.Logistic_model=Training_Pipeline()
        self.logisticmodel=LogisticModel()
        logging.info(f"Initialized all the Models")
    
    def prediction_pipeline(self,message):


        try:
            if self.regex_matcher.classify_regex(message)!=None:
                print(self.regex_matcher.classify_regex(message))
                logging.info(f'Identified {self.regex_matcher.classify_regex(message)} through Regex')
                return self.regex_matcher.classify_regex(message)
            elif self.logisticmodel.Classify_log_model(message) !="unknown":
                print(self.logisticmodel.Classify_log_model(message))
                logging.info(f'Identified {self.logisticmodel.Classify_log_model(message)} class through Logistic_Regression')
                return self.logisticmodel.Classify_log_model(message)
            else:
                print(self.LLM_classifier.classify_log_message(message))
                
                logging.info(f'Identified {self.LLM_classifier.classify_log_message(message)} through LLM model llama3-70b-8192')
                return self.LLM_classifier.classify_log_message(message)
        except Exception as e:
            raise CustomException(e,sys)


if __name__=="__main__":
    obj=PredictionPipeline()
    obj.prediction_pipeline('System rebbot initiated by user 12345.')
    obj.prediction_pipeline("Unauthorized access to data was attempted")
    obj.prediction_pipeline("User User494 logged OUT.")
        

         

        
