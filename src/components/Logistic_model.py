import os
import sys
import pandas as pd
import numpy as np
import pickle
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

from src.exception import CustomException
from src.logger import logging

class LogisticModelConfig:
    logistic_model_path:str=os.path.join('Saved_Models','Logistic_Model.pkl')
    train_data_path:str=os.path.join('artifacts',"train_clusterd_data.csv")
    test_data_path:str=os.path.join('artifacts',"test_clustered_data.csv")

class LogisticModel:
    def __init__(self):
        self.model_path=LogisticModelConfig()

    def train_logistic_model(self):
        try:
            os.makedirs(os.path.dirname(self.model_path.logistic_model_path),exist_ok=True)
            logisticmodel=LogisticRegression()
            logging.info("Read Data...")
            data=pd.read_csv(r'artifacts/clustered_data.csv')
            logging.info("Data Loaded Successfully")

            data_final=data[data['source']!='LegacyCRM']
            logging.info("Initiate Train Test Split")
            train_data,test_data=train_test_split(data_final,test_size=0.2)
            train_data.to_csv(self.model_path.train_data_path,header=True,index=False)
            logging.info(f"Train Data saved in {self.model_path.train_data_path}")
            test_data.to_csv(self.model_path.test_data_path,header=True,index=False)
            logging.info(f"Test Data saved in {self.model_path.test_data_path}")

            # Load Saved Model Column Transformer
            with open('Saved_Models/Column_Transformer.pkl','rb') as f:
                model_embeddings=pickle.load(f)

            # Embeddings
            embeddings=model_embeddings.encode(train_data['log_message'].tolist())

            #Initialize X and y 

            X=embeddings
            y=train_data['target_label']

            logging.info('Train Test Split')
            X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
            logging.info(f"Split completed with X_train:{X_train.shape} X_test:{X_test.shape} y_train:{y_train.shape} y_test{y_test.shape}")
        
            log_model=LogisticRegression()
            log_model.fit(X_train,y_train)

            with open(self.model_path.logistic_model_path,'wb') as f:
                pickle.dump(log_model,f)
            logging.info(f'Model saved successfully in {self.model_path.logistic_model_path}')
    
        except Exception as e:
            raise CustomException(e,sys)
        
    def Classify_log_model(self,log_message):
        try:
            with open(self.model_path.logistic_model_path,'rb') as f:
                log_model=pickle.load(f)
            predict_probability=log_model.predict_prob
            
        except Exception as e:
            raise CustomException(e,sys)
        
    

        
if __name__=="__main__":
    obj=LogisticModel()
    obj.initiate_logistic_model()


        









        



        


