import graphes as gr
from numpy import inf

def voisins(graph, s):
    l=[]
    if s in graph[0]:
        for i in range(0,len(graph[0])):
            elt = graph[1][graph[0].index(s)][i]
            if elt not in (0,inf):
                l.append(graph[0][i])
    return l