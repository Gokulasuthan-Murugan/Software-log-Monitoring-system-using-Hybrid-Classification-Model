import os
import sys
import pandas as pd
import numpy as np
import pickle
from sklearn.cluster import DBSCAN
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass

@dataclass 
class ClusteringConfig:
    clustering_model_path:str=os.path.join('Saved_Models','DBSCAN_Model.pkl')
    clustered_data_path:str=os.path.join('artifacts','clustered_data.csv')

class Clustering:
    def __init__(self):
        self.clustering_config=ClusteringConfig()
    
    def initiate_clustering(self,Data_Path):
        try:
            os.makedirs(os.path.dirname(self.clustering_config.clustered_data_path),exist_ok=True)
            os.makedirs(os.path.dirname(self.clustering_config.clustering_model_path),exist_ok=True)
            logging.info('Initiate Column_Transformer')
            with open('Saved_Models/Column_Transformer.pkl','rb') as f:
                embedding_model=pickle.load(f)
            logging.info('Column_Transformer initiated_successfully')
            logging.info('Load Data...')
            self.input_path=Data_Path or 'artifacts\\data.csv'
            df=pd.read_csv(self.input_path)
            logging.info("Data Loaded Successfully")
            # Perform Embedding using Column Transformer
            logging.info('Initiated Embeddings')
            embeddings=embedding_model.encode(df['log_message'].tolist())
            logging.info('Embedding Completed Successfully')

            # DBSCAN Clustering
            DBSCAN_model=DBSCAN(eps=0.2,min_samples=1,metric='euclidean')
            clusters=DBSCAN_model.fit_predict(embeddings)
            df['clusters']=clusters
            logging.info(f"Clustered Data Saved Successfully in {self.clustering_config.clustered_data_path}")

            with open(self.clustering_config.clustering_model_path,'wb') as f:
                pickle.dump(DBSCAN_model,f)
            logging.info(f"Dbscan Model Saved Successfully in {self.clustering_config.clustering_model_path}")

            df.to_csv(self.clustering_config.clustered_data_path,index=False,header=True)
            logging.info('clustered_data_added succesfully')
            return self.clustering_config.clustered_data_path,self.clustering_config.clustering_model_path

        except Exception as e:
            raise CustomException(e,sys)

if __name__=="__main__":
    obj=Clustering()
    obj.initiate_clustering('artifacts\\data.csv')




