import os
import sys

from src.pipeline.Training_Pipeline import Training_Pipeline
from src.components.Regex_Matcher import Regular_Expression
from src.components.LLM_Model import LLMClassifier
from src.exception import CustomException
from src.logger import logging

class PredictionPipeline:
    def __init__(self):
        self.regex_matcher=Regular_Expression()
        self.LLM_classifier=LLMClassifier()
        self.Logistic_model=Training_Pipeline()
    
    def prediction_pipeline(self):
        pass