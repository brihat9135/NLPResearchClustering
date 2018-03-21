# -*- coding: utf-8 -*-
"""
Created on Sat Mar 17 20:15:21 2018

@author: cs
"""

import pandas as pd
import re
import matplotlib.pyplot as plt
import numpy as np
from nltk.tokenize import word_tokenize
from collections import Counter
from UMLSCUI import UMLSClient


class ExtractCUIs:
    
    
    def extractfromTxt(self, listofPatient, clusternumber):
        df = pd.read_csv(listofPatient, sep = '\t')
        patientList = df.loc[df['ClusterNumber'] == clusternumber]
        patientList = patientList['SubjectID'].tolist()
        #print(patientList)
        return patientList
    
    def readAndconverttodict(self, patientList):
        loc = "/home/cs/NLPResearch/ClusterDataCUI/"
        filePathList = []
        for patient in patientList:
            filepath = loc + str(patient) + ".txt"
            filePathList.append(filepath)
        #print (filePathList)
        listCUIs = []
        for filePath in filePathList:
            with open (filePath) as fin:
                for line in fin:
                    listCUIs.extend(word_tokenize(line))
                    
        patientCUIsDict = Counter(listCUIs)
        
        return patientCUIsDict
        
    def getCUIsList(self, patientCUIsDict):
        APIKey = 'c24cc91f-0c2f-4380-aa36-3f375cc78030'
        UMLSCUIs = UMLSClient(APIKey)
        getTd = UMLSCUIs.getst()
        print(getTd)
        cui = []
        nameofCUI = []
        countCUI = []
        for k, v in patientCUIsDict:
            #print(k)
            cui_name = k.lstrip('-').upper()
            if cui_name.startswith('NEG'):
                cui_name = cui_name[3:]
            if not len(cui_name) == 8:
                raise ValueError('CUI must be formatted C#######')
            real_name = UMLSCUIs.query_umls(cui_name)['name']
            #print(k, real_name, v)
            cui.append(k)
            nameofCUI.append(real_name)
            countCUI.append(v)
         
        df_listofCUI = pd.DataFrame({"CUI" : cui, "CUI_name" : nameofCUI, "CUI_count": countCUI})
        print(df_listofCUI)
        return (df_listofCUI)
            
                
        
        
        
        
        
if __name__ == '__main__':
    EC = ExtractCUIs()
    for x in range(6):    
        patientList = EC.extractfromTxt("patientwith46cluster.txt", x)
        patientCUIsDict = EC.readAndconverttodict(patientList)
        most_common_c = patientCUIsDict.most_common(25)
        df_cluster = EC.getCUIsList(most_common_c)
        filename = "cluster" + str(x + 1) + "TopWords.txt"
        df_cluster.to_csv(filename, sep = '\t', index = False)
        
    