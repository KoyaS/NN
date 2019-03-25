import random
import math
import os

INPUTS = 5

HIDDEN_LAYERS = 2
HIDDEN_LEN = 4

OUTPUTS = 4

def createLayer(length):
	layer = []
	for x in range(0,length):
		holding = []
		for x in range(0,3):
			holding.append(random.uniform(-1,1))
		holding.append([])
		layer.append(holding)
	return(layer)

	"""
	layer = []
	for x in range(0, 4):
		holding = []
		for i in range(0, length):
			holding.append(random.uniform(-1,1))
		layer.append(holding)
	return(layer)
	"""


def createNet(inputs,hidden_layers,hidden_len,outputs):
	NET = []
	NET.append(createLayer(inputs))
	for x in range(0,hidden_layers):
		NET.append(createLayer(hidden_len))
	NET.append(createLayer(outputs))
	return(NET)

def calcNode(v1,w1,b1):
	return((v1*w1)-b1)

def sigmoid(x):
	#For values between 0 and 1: 1/(1+e^-x)
	#For values between -1 and 1: 2/(1+e^-x)-1
	return(1/(1+math.exp(-1*x)))

def nodeIndex(net, layer, position, part):
	if part == 'v':
		index = 0
	elif part == 'w':
		index = 1
	elif part == 'b':
		index = 2
	elif part == 'holding':
		index = 3

	return(net[layer-1][position-1][index])

def calcNetOutput(net, inputs):
	outputs = []
	layerNo = 0
	nodeNo = 0

	for layer in net:
		
		for node in layer:

			#Check if first layer, if so take inputs
			if layerNo == 0:
				v = sigmoid(inputs[nodeNo])
			else:
				v = sigmoid(sum(node[3]))

			w = node[1]
			b = node[2]

			nodeOut = calcNode(v,w,b)

			if layerNo < len(net)-1:
				#Append calculated value to the valueHolding list
				for nextNode in net[layerNo+1]:
					nextNode[3].append(nodeOut)
			else:
				outputs.append(nodeOut)
			nodeNo+=1

		layerNo+=1

	return(outputs)

	"""
	for layerNo in range(0,len(net)):
		layerNo += 1

		for nodeNo in range(0,len(layer)):
			nodeNo += 1

			if layerNo == 1:
				v1 = sum(index(net, layerNo, nodeNo, 'holding'))
			else:
				v1 = index(net, layerNo, nodeNo, 'v')
			w1 = index(net, layerNo, nodeNo, 'w')
			b1 = index(net, layerNo, nodeNo, 'b')

			output = calcNode(v1,w1,b1)
			for nextNode in net[layerNo]:
				print(nextNode)

	return(outputs)
	"""

def saveNet(net, name, write):
	path = path.join(path.abspath(path.dirname(__file__)), "savedNetworks")
	files = [f for f in listdir(path) if f != ".DS_Store"]

	if name in files:
		if write:
			
		print("")
		return('')

network = createNet(INPUTS,HIDDEN_LAYERS,HIDDEN_LEN,OUTPUTS)
#print(nodeIndex(network, 1, 2, 'v'))

#print(createLayer(4))
print(calcNetOutput(network,[7,3,6,5,8]))



