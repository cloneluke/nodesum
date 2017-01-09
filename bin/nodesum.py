import copy

class Node:

    nodeValue = None
    nodeChildren = []
    
    def __init__(self, nodeName, nodeValue, nodeChildren=None):       
        self.nodeName = nodeName
        self.nodeValue = nodeValue
        self.nodeChildren = nodeChildren
        self.pathSum = 0
#        print(self.nodeName)
#        print(self.nodeValue)
    def __repr__(self):
        return "<name: %s, value: %s>" % (self.nodeName, self.nodeValue)

def getNodeName(incomingNode):
    return incomingNode.nodeName

class Tree:
    
    TreeList = []
    
    def add(self, nodeToAdd):
        self.TreeList.append(nodeToAdd) 
#        print(self.TreeList)
    def sortTree(self):
        sorted(self.TreeList, key=getNodeName)
    def getIndexOfNodeMember(self, incommingNodeName):
        print("Tree list inside get index")
        print(self.TreeList)
        for i in range(self.TreeList.__len__()):
            if self.TreeList[i].nodeName == incommingNodeName:
                return i
        return None
    
def doesSumExist(startNode, sumTarget, mytree):
#    print(sumTarget)
    currentSum = 0
    pastStartPoint = False
#     currentDepth = 0
#     maxdepth = 10
#     treeTotalNodes = mytree.TreeList.__len__()
#    print(treeTotalNodes)
    childrenRemain = True
    trimmedTree = copy.deepcopy(mytree)
#     tempTree.TreeList = sorted(tempTree.TreeList, key=getNodeName)
    print(trimmedTree.TreeList)
    
    #while tree list is not totally popped
    while trimmedTree.TreeList:    
        nodeIterator = 0
        #checking for start point
        if(trimmedTree.TreeList[nodeIterator].nodeName == startNode):
            pastStartPoint = True
            currentSum = trimmedTree.TreeList[nodeIterator].pathSum = trimmedTree.TreeList[nodeIterator].nodeValue   
            if(trimmedTree.TreeList[nodeIterator].pathSum == sumTarget):
                break
            if(trimmedTree.TreeList[nodeIterator].nodeChildren):
                if(CheckChildrenForSum(trimmedTree, nodeIterator, currentSum, sumTarget)):
                    print("FOUND PATH!!!")
                    break
            trimmedTree.TreeList.pop(nodeIterator) 
            nodeIterator += 1           
            print(trimmedTree.TreeList)
            
        elif(pastStartPoint):
            print(trimmedTree.TreeList[nodeIterator].nodeName)
            currentSum = trimmedTree.TreeList[nodeIterator].pathSum = trimmedTree.TreeList[nodeIterator].nodeValue + currentSum
            print("current sum past start")
            print(currentSum)
            if(currentSum == sumTarget):
                break
            if(trimmedTree.TreeList[nodeIterator].nodeChildren):
                if(CheckChildrenForSum(trimmedTree, nodeIterator, currentSum, sumTarget)):
                    print("FOUND PATH!!!")
                    return True
            trimmedTree.TreeList.pop(nodeIterator)
            nodeIterator += 1
            print(trimmedTree.TreeList)
        else:
            #skip any node before start point
            trimmedTree.TreeList.pop(nodeIterator)
            nodeIterator += 1
            print(trimmedTree.TreeList)                   

    return (currentSum == sumTarget)

def CheckChildrenForSum(trimmedTree, nodeIterator, currentSum, sumTarget):
    for childIterator in range(trimmedTree.TreeList[nodeIterator].nodeChildren.__len__()):
#                     print("single child")
#                     print(mytree.TreeList[nodeIterator].nodeChildren[childIterator])
#                     print("child index")
        childIndex = trimmedTree.getIndexOfNodeMember(trimmedTree.TreeList[nodeIterator].nodeChildren[childIterator])
        trimmedTree.TreeList[childIndex].pathSum = trimmedTree.TreeList[childIndex].nodeValue + currentSum
        if(trimmedTree.TreeList[childIndex].pathSum == sumTarget):
            print(trimmedTree.TreeList[childIndex].nodeName)
            print("FOUND PATH INSIDE CHILDREN SUM!!!!!!!!")
            return trimmedTree.TreeList[childIndex].pathSum     
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

# print(" 4 test ")
# print(doesSumExist("a", 4, mytree))
# print(" 5 test ")
# print(doesSumExist("a", 5, mytree))
print(" 12 test ")
print(doesSumExist("a", 12, mytree))
# 
# print(" 21 test ")
# print(doesSumExist("a", 21, mytree))


    