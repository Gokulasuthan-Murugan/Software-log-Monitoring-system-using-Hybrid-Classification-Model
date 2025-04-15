import os 
import sys 
import pickle

from sentence_transformers import SentenceTransformer
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass 

@dataclass
class FeatureEngineeringConfig:
    Column_Transformer_path:str=os.path.join('Saved_Models','Column_Transformer.pkl')

class FeatureEngineering:
    def __init__(self):
        self.feature_engineering_config=FeatureEngineeringConfig()
    
    def initiate_feature_engineering(self):
        logging.info('FeatureEngineering initiated')
        try:
            os.makedirs(os.path.dirname(self.feature_engineering_config.Column_Transformer_path),exist_ok=True)
            logging.info('Directory created')
            model_encoder=SentenceTransformer('all-MiniLM-L6-v2')
            with open(self.feature_engineering_config.Column_Transformer_path,'wb') as f:
                pickle.dump(model_encoder,f)
            logging.info(f'Model SentenceTransformer saved successfully in {self.feature_engineering_config.Column_Transformer_path}')
            return self.feature_engineering_config.Column_Transformer_path

        except Exception as e:
            raise CustomException(e,sys)

if __name__=="__main__":
    obj=FeatureEngineering()
    obj.initiate_feature_engineering()


