# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 23:25:09 2018

@author: brihat
"""

#ReadZipFile

import pandas as pd
import gzip
import string


class DataFile:
    
    def printNLines(Filename, N):
        from itertools import islice
        with gzip.open(Filename, 'rb') as myfile:
            for line in islice(myfile, N):
                print(line)
                
    def NoteEventFileintoDF(self, Filename):
        df = pd.read_csv(Filename, sep = ',')
        return df  
    
    def readFileintoDF(self, Filename):
        df = pd.read_csv(Filename)
        return df
     
    def dumptoTxt(pandasDataFrame):
        for index, row in pandasDataFrame.iterrows():
            S_ID = str(row['SUBJECT_ID'])
            path = '/home/cs/NLPResearch/SamplePatientData/'
            filename = path + S_ID + '.txt'
            #print(filename)
            #print(row['TEXT'])
            text = row.drop('SUBJECT_ID')
            printable = ''.join(c for c in text if c in string.printable)
            printable.to_csv(filename, header=False, index = False)
    
    def writetoTxt(self, pandasDataFrame):
        path = '/home/cs/NLPResearch/SamplePatientData/'
        NoteEventsDict = zip(pandasDataFrame.SUBJECT_ID, pandasDataFrame.TEXT)
        for k, v in NoteEventsDict:
            printable = ''.join(c for c in v if c in string.printable)
            outfile = open('%s%s.txt' % (path, k), 'a')
            outfile.write(printable + '\n')
     
    
    def writeSelectedIDToTxt(self, pandasDataFrame, SubjectIDDF):
        SubjectIDDF['HADM_ID'] = SubjectIDDF['HADM_ID'].astype(str)
        groupedDF = SubjectIDDF.groupby('SUBJECT_ID').agg({'HADM_ID': ', '.join}).reset_index()
        #print(groupedDF.shape)
        """
        dfSubjectIDList = groupedDF['SUBJECT_ID'].tolist()
        #print(len(dfSubjectIDList))
        #NoteEventsDict = dict(NoteEventsDict) 
        #print(NoteEventsDict)
        pandasDataF = pandasDataFrame[['SUBJECT_ID', 'TEXT']]
        selectedDF = pandasDataF.loc[pandasDataF['SUBJECT_ID'].isin(dfSubjectIDList)]
        #print(selectedDF.shape)
        
        NoteEventsZip = zip(selectedDF.SUBJECT_ID, selectedDF.TEXT)
        
        path = '/home/cs/NLPResearch/ClusterDataWithHamID/'

        for k, v in NoteEventsZip:

            printable = ''.join(c for c in v if c in string.printable)
            outfile = open('%s%s.txt' % (path, k), 'a')
            outfile.write(printable + '\n')
        """
        return groupedDF
        
        
if __name__ == '__main__':
    DF = DataFile()
   
    NoteEventsDF = DF.NoteEventFileintoDF('NOTEEVENTS.csv')
    
    print(NoteEventsDF.loc[NoteEventsDF['SUBJECT_ID'] == 93031])
    #print(NoteEventsDF)
    
    #NoteEventsDict = DF.createDict(NoteEventsDF)
    #SubjectIDDF = DF.readFileintoDF('mimic_respfailure_cohort.csv')
    #print(SubjectIDDF.shape)
    
    #groupedDF = DF.writeSelectedIDToTxt(NoteEventsDF, SubjectIDDF)  
    #print(groupedDF)
    #groupedDF.SUBJECT_ID.to_csv("clusterdata.csv")
    
    #DF.writetoTxt(NoteEventsDict)
    #patientIDsDF = DF.readFileintoDF('mimic_respfailure_cohort.csv')
    #print(patientIDsDF)
    
    