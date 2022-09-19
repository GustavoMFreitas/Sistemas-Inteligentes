import struct
import numpy as np


graph = {'A': set(['B', 'C','D','E']),
         'B': set(['A', 'C','D', 'E']),
         'C': set(['A','B','D','E']),
         'D': set(['A','B', 'C','E']),
         'E': set(['A','B', 'C','D'])}

def Busca_retorcesso(G,inicial,objetivo):
    LE= [inicial]
    LNE= [inicial]
    BSS=[]
    EC=inicial
    while LNE!=[]:
        if EC==objetivo:
            return LE
        if EC!=0:
            while LE!=[] and EC==LE[0]:
                BSS.append(EC) 
                LE.pop(0)
                LNE.pop(0)
                EC= LNE[1]
            LE.append(EC)
        else:
        