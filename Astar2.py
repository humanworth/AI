# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 12:46:20 2021

@author: Ali
"""


class missionariesCannibalsGraph:
    def __init__(self,lst={}):
        self.adjac_lis=lst
        self.graph=self.generateGraph()
 
    def get_neighbors(self, v):
        return self.adjac_lis[v]
    
    def generateGraph(self):
        graph2 = {
  'A' : [],  'B' : [],  'C' : [],  'D' : [],  'E' : [],  'F' : [],
  'G' : [],  'H' : [],  'I' : [],  'J' : [],  'K' : [],  'L' : [],
  'M' : [],  'N' : [],  'O' : [],  'P' : [],  'Q' : [],  'R' : [],
  'S' : [],  'T' : []}
        self.adjac_lis=graph2
        self.generateEdges(graph2)
        return graph2
    
    def getGraph(self):
        return self.adjac_lis 
    
    def addedge(self,x, y,missionaries,cannibals):
        if abs(missionaries+cannibals-2)==0:
            cost=10
        else:
            cost=(missionaries+cannibals)/(abs(missionaries+cannibals-2))
        self.adjac_lis[x].append((y,cost))
        self.adjac_lis[y].append((x,cost))
      
        
    def generateEdges(self,graph1):
        self.addedge('A', 'B',0,1)
        self.addedge('A', 'C',0,2)
        self.addedge('A', 'D',1,1)
        self.addedge('C', 'E',1,1)
        self.addedge('D','E',1,0)
        self.addedge('E', 'F',1,1)
        self.addedge('E', 'G',0,2)
        self.addedge('G', 'I',0,1)
        self.addedge('F', 'H',0,1)
        self.addedge('F','I',1,0)
        self.addedge('H', 'K',1,1)
        self.addedge('H', 'J',2,0)
        self.addedge('I', 'L',1,1)
        self.addedge('I','K',2,0)

        self.addedge('J', 'M',1,1)
        self.addedge('K', 'N',1,0)
        self.addedge('L', 'N',0,1)
        self.addedge('L', 'S',1,0)
        self.addedge('N','Q',1,1)
        self.addedge('N', 'O',2,0)
        self.addedge('O', 'P',0,1)
        self.addedge('Q', 'R',0,1)
        self.addedge('Q','S',2,0)
        self.addedge('R','T',1,1)
        self.addedge('P','T',0,2)
        
 
    def h(self, n):
        h_n_cost = {  'A' : 30/2, 'B' : 35/2,  'C' : 24/2,  'D' : 24/2,  'E' : 20/2,  'F' : 15/2,  'G' : 15/2,  'H' : 12/2,  'I' : 12/2,  'J' : 8/2,  'K' : 8/2,  'L' : 8/2,  'M' : 6/2,  'N' : 6/2,
                'O' : 3/2,  'P' : 2/2,  'Q' : 3/2,  'R' : 2/2,  'S' : 6/2,  'T' : 0/2}
 
        return h_n_cost[n]
 
    def aStar(self, source, target):
        openedList = set([source])
        closedList = set([])
 
        #the distance dictionary provides the distance from beggining to the current node
        
        distance = {}
        distance[source] = 0
 
        # Here we initialized adjacent mapping for all nodes
        adjMapping = {}
        adjMapping[source] = source
 
        while len(openedList) > 0:
            n = None
 
            # finding minimum f(n)=g(n)+h(n) node
            for v in openedList:
                if n == None or distance[v] + self.h(v) < distance[n] + self.h(n):
                    n = v;
 
            if n == None:
                print('No path found')
                return None
 
            # if the current node is the target
            # then we start again from source
            if n == target:
                buildPath = []
 
                while adjMapping[n] != n:
                    buildPath.append(n)
                    n = adjMapping[n]
 
                buildPath.append(source)
 
                buildPath.reverse()
 
                print('Minimum Path: ',buildPath)
                return buildPath
 
            # consider all neighbors
            for (m, weight) in self.get_neighbors(n):
                if m not in openedList and m not in closedList:
                    openedList.add(m)
                    adjMapping[m] = n
                    distance[m] = distance[n] + weight
                else:
                    if distance[m] > distance[n] + weight:
                        distance[m] = distance[n] + weight
                        adjMapping[m] = n
 
                        if m in closedList:
                            closedList.remove(m)
                            openedList.add(m)
            openedList.remove(n)
            closedList.add(n)
 
        print('Path does not exist!')
        return None
    
graph=missionariesCannibalsGraph()

outputGraph = graph.generateGraph()

graph.aStar('A', 'T')

