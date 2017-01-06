

class Node:
    
    nodeName = None
    nodeValue = None
    parentNode = None
    

    def __init__(self, nodeName, nodeValue, parentNode=None):
        
        self.nodeName = nodeName
        self.nodeValue = nodeValue
        self.parentNode = parentNode
        
        print(self.nodeName)
        print(self.nodeValue)
        print(self.parentNode)



def doesSumExist(startNode, sumTarget):
    print(sumTarget)
    
    
    
    

nodea = Node("a", 5)
nodeb = Node("b", 7, "a")
doesSumExist(nodea, 2)
    