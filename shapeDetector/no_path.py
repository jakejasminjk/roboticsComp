import sys
import cv2
import imutils
import numpy as np
from collections import defaultdict

image = cv2.imread('Path.png')

y, x, d = image.shape
print(x,y)

xVals = []
yVals = []
allVal = {}
for i in range(0, x):
    xVals.append(i)
for i in range(0,y):
    yVals.append(i)
#print(xVals,"\n",yVals)

for i in range(0, x):
    for h in range(0, y):
        b,g,r = image[h,i]
        allVal[i,h] = (i,h,(b,g,r))


# function for adding edge to graph

graph = defaultdict(list)
def addEdge(graph,u,v):
	graph[u].append(v)

# definition of function
def generate_edges(graph):
	edges = []

	# for each node in graph
	for node in graph:

		# for each neighbour node of a single node
		for neighbour in graph[node]:

			# if edge exists then append
			edges.append((node, neighbour))
	return edges

def find_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    for node in graph[start]:
        if node not in path:
            newpath = find_path(graph, node, end, path)
            if newpath:
                return newpath
            return None
# declaration of graph as dictionary
for i in range(0, x):
    for h in range(0, y):
        # addEdge(graph,allVal[i,h],allVal[i+1,h])
        # addEdge(graph,allVal[i,h],allVal[i-1,h])
        # addEdge(graph,allVal[i,h],allVal[i,h+1])
        # addEdge(graph,allVal[i,h],allVal[i,h-1])
        # addEdge(graph,allVal[i,h],allVal[i+1,h+1])
        # addEdge(graph,allVal[i,h],allVal[i-1,h+1])
        # addEdge(graph,allVal[i,h],allVal[i+1,h-1])
        # addEdge(graph,allVal[i,h],allVal[i-1,h-1])
        if(i == 0 and h == 0):
            addEdge(graph,allVal[i,h],allVal[i+1,h+1])
            addEdge(graph,allVal[i,h],allVal[i,h+1])
            addEdge(graph,allVal[i,h],allVal[i+1,h])
        elif(i == 0 and h!=0 and h==len(yVals)-1):
            addEdge(graph,allVal[i,h],allVal[i+1,h])
            #addEdge(graph,allVal[i,h],allVal[i,h+1])
            addEdge(graph,allVal[i,h],allVal[i,h-1])
            #addEdge(graph,allVal[i,h],allVal[i+1,h+1])
            addEdge(graph,allVal[i,h],allVal[i+1,h-1])
        elif(i == 0 and h!=0):
            addEdge(graph,allVal[i,h],allVal[i+1,h])
            addEdge(graph,allVal[i,h],allVal[i,h-1])
            addEdge(graph,allVal[i,h],allVal[i+1,h+1])
            addEdge(graph,allVal[i,h],allVal[i+1,h-1])
        elif(i != 0 and h==0 and i==len(xVals)-1):
            #addEdge(graph,allVal[i,h],allVal[i+1,h])
            addEdge(graph,allVal[i,h],allVal[i-1,h])
            addEdge(graph,allVal[i,h],allVal[i,h+1])
            #addEdge(graph,allVal[i,h],allVal[i+1,h+1])
            addEdge(graph,allVal[i,h],allVal[i-1,h+1])
        elif(i != 0 and h==0):
            addEdge(graph,allVal[i,h],allVal[i+1,h])
            addEdge(graph,allVal[i,h],allVal[i-1,h])
            addEdge(graph,allVal[i,h],allVal[i,h+1])
            addEdge(graph,allVal[i,h],allVal[i+1,h+1])
            addEdge(graph,allVal[i,h],allVal[i-1,h+1])
        elif(i == len(xVals)-1 and h == len(yVals)-1):
            addEdge(graph,allVal[i,h],allVal[i-1,h])
            addEdge(graph,allVal[i,h],allVal[i,h-1])
            addEdge(graph,allVal[i,h],allVal[i-1,h-1])
        elif(i == len(xVals)-1 and h != len(yVals)-1):
            addEdge(graph,allVal[i,h],allVal[i-1,h])
            addEdge(graph,allVal[i,h],allVal[i,h+1])
            addEdge(graph,allVal[i,h],allVal[i,h-1])
            addEdge(graph,allVal[i,h],allVal[i-1,h+1])
            addEdge(graph,allVal[i,h],allVal[i-1,h-1])
        elif(i != len(xVals)-1 and h == len(yVals)-1):
            addEdge(graph,allVal[i,h],allVal[i+1,h])
            addEdge(graph,allVal[i,h],allVal[i-1,h])
            addEdge(graph,allVal[i,h],allVal[i,h-1])
            addEdge(graph,allVal[i,h],allVal[i+1,h-1])
            addEdge(graph,allVal[i,h],allVal[i-1,h-1])


# to print generated graph
#print(generate_edges(graph))
print(allVal)
#print(find_path(graph,(980,554, 'None'),(1432,270, 'None')))
