# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 13:18:38 2018

@author: cs
"""

import pandas as pd
import string
class DataProcess:
    
    def NoteEventFileintoDF(self, Filename):
        df = pd.read_csv(Filename, sep = ',')
        return df  
    
    def readFileintoDF(self, Filename):
        df = pd.read_csv(Filename)
        return df
    
    def getSIDwithHID(self, filename1, filename2):
        new_df = pd.merge(filename1, filename2, how = 'inner', on = ['SUBJECT_ID', 'HADM_ID']) 
        return new_df
        
    def writeeachrowToText(self, dataframe):
        path = '/home/cs/NLPResearch/ClusterData/'
        NoteEventsDict = zip(dataframe.patientID, dataframe.TEXT)
        for k, v in NoteEventsDict:
            printable = ''.join(c for c in v if c in string.printable)
            outfile = open('%s%s.txt' % (path, k), 'a')
            outfile.write(printable + '\n')
            
        
if __name__ == '__main__':
    DP = DataProcess()
    data_df = DP.readFileintoDF('mimic_respfailure_cohort.csv')
    print(data_df.shape)
    #duplicate_data = data_df[data_df.duplicated(['SUBJECT_ID'], keep = False)]
    #print(duplicate_data)
    NoteEventsDF = DP.NoteEventFileintoDF('NOTEEVENTS.csv')
    print(NoteEventsDF.head())
    merged_df = DP.getSIDwithHID(NoteEventsDF, data_df)
    new_merged_df = merged_df[['SUBJECT_ID', 'HADM_ID', 'TEXT']]
    
    print(new_merged_df.loc[new_merged_df['SUBJECT_ID'] == 505])
    print(new_merged_df.shape)
    #group_merge_df = new_merged_df.groupby(['SUBJECT_ID', 'HADM_ID'])['TEXT'].apply(' '.join).reset_index()
    #print(group_merge_df)
    new_merged_df['patientID'] = new_merged_df['SUBJECT_ID'].astype(str)+'-'+ new_merged_df['HADM_ID'].astype(int).astype(str)
    #group_merge_df['patientID'] = group_merge_df['SUBJECT_ID'].astype(str)+'-'+ group_merge_df['HADM_ID'].astype(int).astype(str)
    new_merged_df = new_merged_df[['patientID', 'TEXT']]
    print(new_merged_df)
    DP.writeeachrowToText(new_merged_df)
    