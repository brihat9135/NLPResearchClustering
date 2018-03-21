# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 14:42:21 2018

@author: cs
"""
import os
import pandas as pd
#import numpy as np
import time
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.cluster import KMeans

class ReadTxtFiles:
    
    def listDirectoryFiles(a):
        txtfilesTrain = []
        count = 0
        for file in os.listdir(a):
            try:
                if file.endswith(".txt"):
                    txtfilesTrain.append(a + "/" + str(file))
                    count = count + 1
                else:
                    print("There is no text file")
            except Exception as e:
                raise e
                print("No files found here!")
        print("Total files found:", count)
        return txtfilesTrain
    
    def convertToDF(a):
        df_train = pd.DataFrame(a, columns = ['filepath'])
        return df_train
        
    def splitData(dataFrame):
        train, test = train_test_split(dataFrame, test_size = 0.98)
        return train, test
        
    def transformData(data):
        
        count_vect = CountVectorizer()
        
        X_train_counts = count_vect.fit_transform(data)
        tf_transformer = TfidfTransformer(norm = 'l2', use_idf=True)
        X_train_tfdif = tf_transformer.fit_transform(X_train_counts)
        #print(X_train_tfdif)
        return X_train_tfdif
        
    
    def elbow_Point_KMeans(transformData):
        clusterRange = range(1, 10)
        clusterErrors = []
        clusterPredict = []
        
        for cluster in clusterRange:
            kmean = KMeans(cluster)
            kmean.fit(transformData)
            clusterErrors.append(kmean.inertia_)
            predictlist = kmean.predict(transformData)
            clusterPredict.append(predictlist)
            print("Cluster K value done: ", cluster)
        #print("Reached Here")    
        clusters_df = pd.DataFrame({"Clusters" : clusterRange, "clusterErrors" : clusterErrors})
        print(clusters_df)
        return(clusters_df, clusterPredict)
       
    def plotElbowPoints(dataframe):
        fig = plt.figure()
        plt.plot(dataframe['Clusters'], dataframe['clusterErrors'])
        fig.suptitle('ClustersErrors vs Cluster')
        plt.xlabel('Number of Clusters')
        plt.ylabel('Cluster_Errors')
        plt.show()
        
    
if __name__ == '__main__':
    start_time = time.time()
    RTF = ReadTxtFiles
    loc = "/home/cs/NLPResearch/ClusterDataCUI/"
    dirlist = RTF.listDirectoryFiles(loc)    
    df_dirTrain = RTF.convertToDF(dirlist)
    #print(df_dirTrain)
    
    small_data = df_dirTrain
    print(small_data['filepath'])
    print(small_data.shape)
    train_data = small_data['filepath']
    print(small_data['filepath'])
    
    train_data = [open(documents, "r").read() for documents in train_data]
    #print()
    #print()
    #print("new document")
    #print(train_data)
    
    transformData = RTF.transformData(train_data)
    elbowPointDF, clusterPredictList = RTF.elbow_Point_KMeans(transformData)
    RTF.plotElbowPoints(elbowPointDF)
    total_time = (time.time() - start_time)
    print("{0:.3f}".format(total_time))
    print(clusterPredictList[1])
    print(small_data)
    #two cluster
    clusterpredict_df = pd.DataFrame({"file" : small_data['filepath'], "clusters" : clusterPredictList[1]})
    clusterpredict_df.to_csv("assignCluster52.txt", sep = '\t')
    #three cluster
    clusterpredict_df = pd.DataFrame({"file" : small_data['filepath'], "clusters" : clusterPredictList[2]})
    clusterpredict_df.to_csv("assignCluster53.txt", sep = '\t')
    #fourCluster
    clusterpredict_df = pd.DataFrame({"file" : small_data['filepath'], "clusters" : clusterPredictList[3]})
    clusterpredict_df.to_csv("assignCluster54.txt", sep = '\t')
    #five cluster
    clusterpredict_df = pd.DataFrame({"file" : small_data['filepath'], "clusters" : clusterPredictList[4]})
    clusterpredict_df.to_csv("assignCluster55.txt", sep = '\t')
    #six cluster
    clusterpredict_df = pd.DataFrame({"file" : small_data['filepath'], "clusters" : clusterPredictList[5]})
    clusterpredict_df.to_csv("assignCluster56.txt", sep = '\t')
    #secven cluster
    clusterpredict_df = pd.DataFrame({"file" : small_data['filepath'], "clusters" : clusterPredictList[6]})
    clusterpredict_df.to_csv("assignCluster57.txt", sep = '\t')
    
    
    
    
    