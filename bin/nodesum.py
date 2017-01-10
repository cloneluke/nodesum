import copy

class Node:

    nodeValue = None
    nodeChildren = []
    
    def __init__(self, nodeName, nodeValue, nodeChildren=None):       
        self.nodeName = nodeName
        self.nodeValue = nodeValue
        self.nodeChildren = nodeChildren
        self.pathSum = None
#        print(self.nodeName)
#        print(self.nodeValue)
    def __repr__(self):
        return "<name: %s, value: %s, pathsum %s>" % (self.nodeName, self.nodeValue, self.pathSum)

def getNodeName(incomingNode):
    return incomingNode.nodeName

class Tree:
    
    TreeList = []    
    def add(self, nodeToAdd):
        self.TreeList.append(nodeToAdd) 
    def sortTree(self):
        sorted(self.TreeList, key=getNodeName)
    def getIndexOfNodeMember(self, incommingNodeName):
#         print(self.TreeList)
        for i in range(self.TreeList.__len__()):
            if self.TreeList[i].nodeName == incommingNodeName:
                return i
        return None
    
def doesSumExist(startNode, sumTarget, mytree):

    currentSum = 0
    pastStartPoint = False
    trimmedTree = copy.deepcopy(mytree)
    
    #while tree list is not totally popped
    while trimmedTree.TreeList:    
        nodeIterator = 0
        #checking for start point
        if(trimmedTree.TreeList[nodeIterator].nodeName == startNode):
            pastStartPoint = True
            currentSum = trimmedTree.TreeList[nodeIterator].pathSum = trimmedTree.TreeList[nodeIterator].nodeValue   
            if(trimmedTree.TreeList[nodeIterator].pathSum == sumTarget):
                return True
        
        elif(pastStartPoint):

            if(trimmedTree.TreeList[nodeIterator].pathSum == sumTarget):
                return True
   
        if(pastStartPoint and trimmedTree.TreeList[nodeIterator].nodeChildren):
            if(CheckChildrenForSum(trimmedTree, nodeIterator, currentSum, sumTarget)):
                return True
        #skip any node before start point or advance to next node
        trimmedTree.TreeList.pop(nodeIterator)
        nodeIterator += 1       
    return False

def CheckChildrenForSum(trimmedTree, nodeIterator, currentSum, sumTarget):
    for childIterator in range(trimmedTree.TreeList[nodeIterator].nodeChildren.__len__()):
#                     print("single child")
#                     print(mytree.TreeList[nodeIterator].nodeChildren[childIterator])
#                     print("child index")
        childIndex = trimmedTree.getIndexOfNodeMember(trimmedTree.TreeList[nodeIterator].nodeChildren[childIterator])
        trimmedTree.TreeList[childIndex].pathSum = trimmedTree.TreeList[childIndex].nodeValue + trimmedTree.TreeList[nodeIterator].pathSum
        if(trimmedTree.TreeList[childIndex].pathSum == sumTarget):
#             print(trimmedTree.TreeList[childIndex].nodeName)
            return childIndex   
    return False

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
mytree.TreeList = sorted(mytree.TreeList, key=getNodeName)
 
print("a4 test ")
print(doesSumExist("a", 4, mytree))
print("d2 test ")
print(doesSumExist("d", 2, mytree))
print("d3 test ")
print(doesSumExist("d", 3, mytree))
print("a5 test ")
print(doesSumExist("a", 5, mytree))
print("a12 test ")
print(doesSumExist("a", 12, mytree))
print("a21 test ")
print(doesSumExist("a", 21, mytree))
print("c3 test ")
print(doesSumExist("c", 3, mytree))
print("d16 test ")
print(doesSumExist("d", 16, mytree))


    