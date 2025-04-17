import os
import sys 
import pandas as pd
import pickle
from src.components.DataIngestion import DataIngestion
from src.components.DBClustering import Clustering
from src.components.Feature_Engineering import FeatureEngineering
from src.components.Logistic_Model import LogisticModel



from src.logger import logging
from src.exception import CustomException

class Training_Pipeline:
    def __init__(self):
        self.data_ingestion=DataIngestion()
        self.clustering=Clustering()
        self.feature_engineering=FeatureEngineering()
        self.logistic_model=LogisticModel()
        
    
    def training_pipeline(self):
        try:
            df=pd.read_csv(self.data_ingestion.initiate_data_ingestion(r'E:\Software-log-Monitoring-system-using-Hybrid-Classification-Model\notebook\synthetic_logs.csv'))
            clustered_data_path,Clustered_model_path=self.clustering.initiate_clustering(r'E:\Software-log-Monitoring-system-using-Hybrid-Classification-Model\notebook\synthetic_logs.csv')
            df_cluster=pd.read_csv(clustered_data_path)
            embeddings_model_path=self.feature_engineering.initiate_feature_engineering()
            with open(embeddings_model_path,'rb') as f:
                embedding_model=pickle.load(f)

            self.logistic_model_path=self.logistic_model.train_logistic_model(clustered_data_path)
            with open(self.logistic_model_path,'rb') as f:
                Logistic_Model=pickle.load(f)

            return Logistic_Model
        except Exception as e:
            raise CustomException(e,sys)

        
        


        





