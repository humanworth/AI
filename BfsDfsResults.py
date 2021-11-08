# -*- coding: utf-8 -*-
"""
Created on Mon Nov  1 21:13:13 2021

@author: Ali
"""
def RunDfs(Source='A', target='T'):
    dfsResult=[]
    visited = set()
    graph = {  'A' : ['B','C','D'],  'B' : ['A'],  'C' : ['A','E'],  'D' : ['A','E'],  'E' : ['G','F'],  'F' : ['H','E','I'],  'G' : ['E','I'],
               'H' : ['F','J','K'],  'I' : ['F','K','L'],  'J' : ['H','M'],  'K' : ['I','N','H'],  'L' : ['S','I','N'],  'M' : ['J','O'],  'N' : ['L','Q','K','O'],
               'O' : ['N','M','R','P'],  'P' : ['O','T'],  'Q' : ['R','N','S'],  'R' : ['T','Q','O'],  'S' : ['L','Q'],  'T' : ['P','R'],
               } 
    def DFS(graph, visited, vertice):
        if vertice not in visited:
            dfsResult.append(vertice)
            visited.add(vertice)
            for neighbour in graph[vertice]:
                DFS(graph,visited, neighbour)

    DFS(graph, visited, 'A')
    return dfsResult


def runBfs(startNode='A',target='T'):
    graph = {  'A' : ['B','C','D'],  'B' : ['A'],  'C' : ['A','E'],  'D' : ['A','E'],  'E' : ['G','F'],  'F' : ['H','E','I'],  'G' : ['E','I'],
               'H' : ['F','J','K'],  'I' : ['F','K','L'],  'J' : ['H','M'],  'K' : ['I','N','H'],  'L' : ['S','I','N'],  'M' : ['J','O'],  'N' : ['L','Q','K','O'],
               'O' : ['N','M','R','P'],  'P' : ['O','T'],  'Q' : ['R','N','S'],  'R' : ['T','Q','O'],  'S' : ['L','Q'],  'T' : ['P','R'],
               }

    visited = [] 
    queue = []   
    result=[]
    
    visited.append(startNode)
    queue.append(startNode)

    while queue:
        s = queue.pop(0) 
        result.append(s)
        if(s==target):
            break
        for adj in graph[s]:
            if adj not in visited:
                visited.append(adj)
                queue.append(adj)
    return result








bfsResult=runBfs('A')

print('Path with BFS ',bfsResult)


print('  ')


dfsResult=RunDfs('T')

print('Path with DFS ',dfsResult)



#root=makeMissionariesCannibalsTree()
