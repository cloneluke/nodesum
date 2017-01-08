import copy

class Node:

    nodeValue = None
    nodeChildren = []
    

    def __init__(self, nodeName, nodeValue, nodeChildren=None):
        
        self.nodeName = nodeName
        self.nodeValue = nodeValue
        self.nodeChildren = nodeChildren
#        print(self.nodeName)
#        print(self.nodeValue)



class Tree:
    
    TreeList = []
    
    def add(self, nodeToAdd):
        self.TreeList.append(nodeToAdd) 
#        print(self.TreeList)


def doesSumExist(startNode, sumTarget, mytree):
#    print(sumTarget)
    currentSum = 0
    treeTotalNodes = mytree.TreeList.__len__()
    print(treeTotalNodes)
    childrenRemain = True
    tempTree = copy.deepcopy(mytree)
    
    while childrenRemain and currentSum < sumTarget:    
        nodeIterator = 0
        for nodeIterator in range(tempTree.TreeList.__len__()):
            print(nodeIterator)
            if(tempTree.TreeList[nodeIterator].nodeName == startNode):
                currentSum = tempTree.TreeList[nodeIterator].nodeValue + currentSum
            if(tempTree.TreeList[nodeIterator].nodeChildren == None):
                print("starting node has no children")
                childrenRemain = False
                print(currentSum)
                break
            elif(tempTree.TreeList[nodeIterator].nodeChildren):
                for childIterator in range(tempTree.TreeList[nodeIterator].nodeChildren.__len__()):
                    print(tempTree.TreeList[nodeIterator].nodeChildren)
            
            

    
mytree = Tree()
    


nodeb = Node("b", 7)
mytree.add(nodeb)
nodec = Node("c", 3)
mytree.add(nodec)
noded = Node("d", 2, ["e", "f"])
mytree.add(noded)
nodee = Node("e", 6, ["g"])
mytree.add(nodee)
nodef = Node("f", 1)
mytree.add(nodef)
nodef = Node("g", 8)
mytree.add(nodef)
nodea = Node("a", 5, ["b", "c", "d"])
mytree.add(nodea)



doesSumExist("a", 4, mytree)

    