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

@dataclass
class LogisticModelConfig:
    logistic_model_path:str=os.path.join('Saved_Models','Logistic_Model.pkl')
    train_data_path:str=os.path.join('artifacts',"train_clusterd_data.csv")
    test_data_path:str=os.path.join('artifacts',"test_clustered_data.csv")

class LogisticModel:
    def __init__(self):
        self.model_path=LogisticModelConfig()

    def train_logistic_model(self,Data_Path):
        try:
            os.makedirs(os.path.dirname(self.model_path.logistic_model_path),exist_ok=True)
            logisticmodel=LogisticRegression()
            logging.info("Read Data...")
            self.input_path=Data_Path or 'artifacts\\clustered_data.csv'
            data=pd.read_csv(self.input_path)
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
            embeddings=model_embeddings.encode(train_data['log_message'].tolist(),show_progress_bar=False)

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
            return self.model_path.logistic_model_path
    
        except Exception as e:
            raise CustomException(e,sys)
        
    def Classify_log_model(self,log_message):
        try:
            with open(self.model_path.logistic_model_path,'rb') as f:
                log_model=pickle.load(f)

            with open('Saved_Models/Column_Transformer.pkl','rb') as f:
                Column_Transformer=pickle.load(f)

            embeddings=Column_Transformer.encode(log_message,show_progress_bar=False).reshape(1,-1)
            predict_probability=log_model.predict_proba(embeddings).reshape(-1)
            if max(predict_probability)>0.5:

                return log_model.predict(embeddings)[0]
            else:
                return "unknown"
                

        except Exception as e:
            raise CustomException(e,sys)
        
    

        
if __name__=="__main__":
    obj=LogisticModel()
    #obj.train_logistic_model('artifacts\\clustered_data.csv')
    obj.Classify_log_model("Unauthorized access to data was attempted")


        









        



        


