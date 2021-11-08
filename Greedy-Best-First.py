# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 20:14:11 2021

@author: Ali
"""
 


def generateEdges(graph1):
    def addedge(x, y):
        graph1[x].append(y)
 
    addedge('A', 'B')
    addedge('A', 'C')
    addedge('A', 'D')
    addedge('C', 'E')
    addedge('D','E')
    addedge('E', 'F')
    addedge('E', 'G')
    addedge('G', 'I')
    addedge('F', 'H')
    addedge('F','I')
    addedge('H', 'K')
    addedge('H', 'J')
    addedge('I', 'L')
    addedge('I','K')

    addedge('J', 'M')
    addedge('K', 'N')
    addedge('L', 'N')
    addedge('L', 'S')
    addedge('N','Q')
    addedge('N', 'O')
    addedge('O', 'P')
    addedge('Q', 'R')
    addedge('Q','S')
    addedge('R','T')
    addedge('P','T')


def generateGraph():
    graph2 = {
  'A' : [],  'B' : [],  'C' : [],  'D' : [],  'E' : [],  'F' : [],
  'G' : [],  'H' : [],  'I' : [],  'J' : [],  'K' : [],  'L' : [],
  'M' : [],  'N' : [],  'O' : [],  'P' : [],  'Q' : [],  'R' : [],
  'S' : [],  'T' : []}
    visited =  {  'A' : False,  'B' : False,  'C' : False,  'D' : False,  'E' : False,  'F' : False,
                'G' : False,  'H' : False,  'I' : False,  'J' : False,  'K' : False,  'L' : False,
                'M' : False,  'N' : False,  'O' : False,  'P' : False,  'Q' : False,  'R' : False,
                'S' : False,  'T' : False}
    h_n_cost = {  'A' : 30/2, 'B' : 35/2,  'C' : 24/2,  'D' : 24/2,  'E' : 20/2,  'F' : 15/2,  'G' : 15/2,  'H' : 12/2,  'I' : 12/2,  'J' : 8/2,  'K' : 8/2,  'L' : 8/2,  'M' : 6/2,  'N' : 6/2,
                'O' : 3/2,  'P' : 2/2,  'Q' : 3/2,  'R' : 2/2,  'S' : 6/2,  'T' : 0/2}
    generateEdges(graph2)
    return graph2, visited, h_n_cost

def GreedyBestFirst(graph=None,source='A',target='T',h_cost=None,visited=None):
    q1=[]
    result=[source]
    q1.append(source)
    totalCost=0 
    while len(q1) !=0:
        u = q1.pop()
        print(u)
        visited[u] = True
        totalCost+=h_cost[u]
        # Displaying the path having lowest cost
        
        if u==target:
            break
        mini=h_cost[u]
        minimum=u
        for node in graph[u]:
            if(h_cost[node]<=mini):
                mini=h_cost[node]
                minimum=node
        q1.append(minimum)
        result.append(minimum)     
    return result , totalCost






graph3, visited, h_cost=generateGraph()  

res,costs=GreedyBestFirst(graph=graph3,source='A',target='T',h_cost=h_cost,visited=visited)

    
    