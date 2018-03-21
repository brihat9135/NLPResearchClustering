#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 11:15:54 2018

@author: brihat
"""

import pandas as pd
import re
import matplotlib.pyplot as plt
import numpy as np
from prettytable import PrettyTable
#import numpy as np

class DataAnalysis:
    
    def readFileintoDF(self, Filename):
        df = pd.read_csv(Filename, sep = ',')
        return df
    
    def readtxtFileintoDF(self, Filename):
        df = pd.read_csv(Filename, sep = '\t')
        return df    
    
    def checkPatient(self, clusterPatient_df, subjectID):
        patientList = clusterPatient_df["SubjectID"].tolist()
        clusterList = clusterPatient_df["ClusterNumber"].tolist()
        result = []
        for patient in patientList:
            if int(patient) in subjectID:
                a = 1
                result.append(a)
            
            else:
                a = 0
                result.append(a)
        #print(result)
        patient_df = pd.DataFrame({"SubjectID" : patientList, "ClusterNumber" : clusterList, "label" : result})        
        return patient_df
      
    
    def clean_subjectID(self, dataframe):
        directory_List = dataframe['SUBJECT_ID'].tolist()
        clusterList = dataframe['ClusterNumber'].tolist()
        subjectID_List = []
        for di in directory_List:
            a = re.sub(r'/home/cs/NLPResearch/ClusterDataCUI//', "", di)
            b = a[:-4]
            subjectID_List.append(b)
        
        clusterPatient_df = pd.DataFrame({"SubjectID" : subjectID_List, "ClusterNumber" : clusterList})
        
        return clusterPatient_df
        
 
            
    def clusterBar(self, patientList_df):
        
    #def createAbarChart(self, clusterDF):
        cluster0 = patientList_df.loc[patientList_df['ClusterNumber'] == 0]
        cluster_df0 = cluster0['label'].value_counts().to_frame()
        val = pd.Series([0, 0])
        cluster_df0['value'] = val.values
        cluster1 = patientList_df.loc[patientList_df['ClusterNumber'] == 1]
        cluster_df1 = cluster1['label'].value_counts().to_frame()
        val = pd.Series([1, 1])
        cluster_df1['value'] = val.values
        #cluster2 = patientList_df.loc[patientList_df['ClusterNumber'] == 2]
        #cluster_df2 = cluster2['label'].value_counts().to_frame()
        #val = pd.Series([2, 2])
        #cluster_df2['value'] = val.values
        #cluster3 = patientList_df.loc[patientList_df['ClusterNumber'] == 3]
        #cluster_df3 = cluster3['label'].value_counts().to_frame()
        #val = pd.Series([3, 3])
        #cluster_df3['value'] = val.values
        #cluster4 = patientList_df.loc[patientList_df['ClusterNumber'] == 4]
        #cluster_df4 = cluster4['label'].value_counts().to_frame()
        #val = pd.Series([4, 4])
        #cluster_df4['value'] = val.values
        #cluster5 = patientList_df.loc[patientList_df['ClusterNumber'] == 5]
        #cluster_df5 = cluster5['label'].value_counts().to_frame()
        #val = pd.Series([5, 5])
        #cluster_df5['value'] = val.values
        
        
        N = 2
        survived = (cluster_df0['label'].iloc[0], cluster_df1['label'].iloc[0])
        print(survived)
        died = (cluster_df0['label'].iloc[1], cluster_df1['label'].iloc[1])
        
        ind = np.arange(N)
        width = 0.35
        
        fig, ax = plt.subplots()
        
        rects1 = ax.bar(ind, survived, width, color = 'g')
        
        rects2 = ax.bar(ind + width, died, width, color = 'r')
        ax.set_ylabel('Number of patient')
        ax.set_title("Bar plot of clusters")
        ax.set_xticks(ind + width / 2)
        ax.set_xticklabels(('C1', 'C2', 'C3', 'C4', 'C5', 'C6'))
        ax.legend((rects1[0], rects2[0]), ('Survived', 'Died'), loc = 'center left', bbox_to_anchor=(1, 0.5))
        
        concatenateDF = pd.concat([cluster_df0, cluster_df1])
        plt.show()
        return concatenateDF
    
    
    def getTablefortheCluster(self, dataframe):
        y = PrettyTable()
        TotalPatient = dataframe['label'].sum()
        #print(TotalPatient)
        y.field_names = ["ClusterNo.", "CTotal_Patients",  "Patient_Expired", "Expired_Percent(%)", "Cluster_Weight(%)"]
        for x in range(2):
            cluster = dataframe.loc[dataframe['value'] == x]
            Total = cluster['label'].sum()
            PatientDied = cluster['label'].iloc[1]
            patientDiedPercent = round((PatientDied/Total) * 100, 1)
            clusterW = round((Total/TotalPatient) * 100, 1)
            y.add_row([x + 1, Total, PatientDied, patientDiedPercent, clusterW]) 
        print()    
        print("ClusterQuickInfo Table")
        print(y)
            
                
    
    
if __name__ == '__main__':
    DA = DataAnalysis()
    AdmissionDF = DA.readFileintoDF("ADMISSIONS.csv")
    #print(AdmissionDF)
    AdmissionDF1 = AdmissionDF[pd.notnull(AdmissionDF['DEATHTIME'])]
    AdmissionDF2 = AdmissionDF1[['SUBJECT_ID', 'DEATHTIME', 'HOSPITAL_EXPIRE_FLAG']]
    #print(AdmissionDF2)
    subjectIDList = AdmissionDF1['SUBJECT_ID'].values.tolist()
    subjectIDL = AdmissionDF['SUBJECT_ID'].values.tolist()
    #print(subjectIDList)
   
    clusteredP_DF = DA.readtxtFileintoDF("assignCluster42.txt")
    #print(clusteredP_DF)
    clusteredP_DF.columns = ['patient_COUNT', 'ClusterNumber', 'SUBJECT_ID']
    clusteredP_DF = clusteredP_DF.drop('patient_COUNT', axis = 1)
    clusterPatient_df = DA.clean_subjectID(clusteredP_DF)
    #print(clusterPatient_df)
    patientList_df = DA.checkPatient(clusterPatient_df, subjectIDList)
    print(patientList_df)
    patientList_df.to_csv("patientwith42cluster.txt", sep = '\t', index = False)
    #DA.clusterLink(patientList_df)
    concateDF = DA.clusterBar(patientList_df)
    #(concateDF)
    DA.getTablefortheCluster(concateDF)
    
    
    
