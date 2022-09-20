from asyncio.windows_events import NULL


def Busca_retorcesso(G,inicial,objetivo):
    LE= [inicial]
    LNE= [inicial]
    BSS=[]
    EC=inicial
    while LNE!=[]:
        if EC==objetivo:
            return LE
        if G.get(EC) == NULL:
            while LE!=[] and EC==LE[0]:
                BSS.append(EC) 
                LE.pop(0)
                LNE.pop(0)
                EC= LNE[1]
            LE.append(EC)
        else:
            for i in range(len(G.get(EC))):
                LNE.append(G.get(EC)[i])
            EC=LNE[0]
            LE.append(EC)
            print(LNE)
        return "falha"    

graph = {'A':['B','C','D','E'],
        'B':['A','C','D','E'],
        'C':['A','B','D','E'],
        'D':['A','B','C','E'],
        'E':['A','B','C','D']}

g= Busca_retorcesso(graph,"A","")
print(g)
