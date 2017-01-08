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
        for i in range(self.TreeList.__len__()):
            if self.TreeList[i].nodeName == incommingNodeName:
                return i
        return None
    
         

def doesSumExist(startNode, sumTarget, mytree):
#    print(sumTarget)
    currentSum = 0
    currentDepth = 0
    maxdepth = 10
    treeTotalNodes = mytree.TreeList.__len__()
#    print(treeTotalNodes)
    childrenRemain = True
    trimmedTree = copy.deepcopy(mytree)
#     tempTree.TreeList = sorted(tempTree.TreeList, key=getNodeName)
    print(mytree.TreeList)
    
    while mytree.TreeList:    
        nodeIterator = 0
        currentdepth = 0
        print(nodeIterator)
        print(mytree.TreeList[nodeIterator].nodeName)
        if(mytree.TreeList[nodeIterator].nodeName == startNode):
            print("in if loop")
            print(mytree.TreeList[nodeIterator].nodeName)
            currentSum = mytree.TreeList[nodeIterator].nodeValue
            
            if(mytree.TreeList[nodeIterator].nodeChildren):
                print("all children")
                print(mytree.TreeList[nodeIterator].nodeChildren)
                for childIterator in range(mytree.TreeList[nodeIterator].nodeChildren.__len__()):
                    print("single child")
                    print(mytree.TreeList[nodeIterator].nodeChildren[childIterator])
                    print("child index")
                    childSum = mytree.TreeList[mytree.getIndexOfNodeMember(mytree.TreeList[nodeIterator].nodeChildren[childIterator])].nodeValue + currentSum
                    print("child sum")
                    print(childSum)
            
            mytree.TreeList.pop(nodeIterator) 
            nodeIterator += 1           
            print(mytree.TreeList)
        else:
            mytree.TreeList.pop(nodeIterator)
            nodeIterator += 1
        
        
        
        
#         for nodeIterator in range(mytree.TreeList.__len__()):
#             print("node iterator")
#             print(nodeIterator)
#             if(mytree.TreeList[nodeIterator].nodeName == startNode):
# #                 print(tempTree.TreeList[nodeIterator].nodeName)
# #                 print(tempTree.TreeList[nodeIterator].nodeValue)
#                 currentSum = mytree.TreeList[nodeIterator].nodeValue
#                 mytree.TreeList[nodeIterator].pathSum = currentSum
#                 
#                 if(mytree.TreeList[nodeIterator].nodeChildren):
#                     print("all children")
#                     print(mytree.TreeList[nodeIterator].nodeChildren)
#                     for childIterator in range(mytree.TreeList[nodeIterator].nodeChildren.__len__()):
#                         print("single child")
#                         print(mytree.TreeList[nodeIterator].nodeChildren[childIterator])
#                   #      tempTree.TreeList[nodeIterator].nodeChildren[childIterator].pathSum = currentSum + tempTree.TreeList[nodeIterator].nodeChildren[childIterator].nodeValue
#                  #       print(tempTree.TreeList[nodeIterator].nodeChildren[childIterator].pathSum)
#                     break
#                 else:
#                     print("starting node has no children")
#                     childrenRemain = False
# #                     print(currentSum)
#                     break
#             else:
#                 print("pop")
#                 print(mytree.TreeList.__len__())
#                 trimmedTree.TreeList.pop(nodeIterator)
#                     
#             if(currentSum == sumTarget):
#                 print("FOUND PATH")
#             elif(tempTree.TreeList[nodeIterator].nodeChildren):
#                 for childIterator in range(tempTree.TreeList[nodeIterator].nodeChildren.__len__()):
#                     print(tempTree.TreeList[nodeIterator].nodeChildren)
    print("sum exceeded or equal")
    print(currentSum < sumTarget)
    print("found path")
    print(currentSum == sumTarget)
    print("children remaining?")
    print(childrenRemain)
    print(currentSum)
    print(sumTarget)
    return (childrenRemain and currentSum < sumTarget)

    
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

print(" 4 test ")
print(doesSumExist("a", 4, mytree))
print(" 5 test ")
print(doesSumExist("a", 5, mytree))


    