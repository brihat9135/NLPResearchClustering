# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 02:32:37 2018

@author: cs
"""

import pandas as pd

class ClustersCUI:
    
    def readFileintoDF(self, Filename):
        df = pd.read_csv(Filename, sep = '\t')
        return df
        
if __name__ == '__main__':
    Clus = ClustersCUI()
    clusterList = ['cluster1TopWords.txt', 'cluster2TopWords.txt', 
                   'cluster3TopWords.txt', 'cluster4TopWords.txt',
                   'cluster5TopWords.txt', 'cluster6TopWords.txt']
            
    cluster = 0        
    for x in clusterList:
        df_cluster0 = Clus.readFileintoDF(x)
        print()
        print()
        print(df_cluster0)
        
    
           