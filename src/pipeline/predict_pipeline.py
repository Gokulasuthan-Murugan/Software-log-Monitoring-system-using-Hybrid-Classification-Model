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
    
    def prediction_pipeline(self,message):
        if self.regex_matcher.classify_regex(message)!=None:
            print(self.regex_matcher.classify_regex(message))
        elif self.logisticmodel.Classify_log_model(message) !="unknown":
            print(self.logisticmodel.Classify_log_model(message))
        else:
            print(self.LLM_classifier.classify_log_message(message))
        

         

        
