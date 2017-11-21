
#############################
# module: BSTree.py
# Silvia Smith
# A01396094
#############################

from BSTNode import BSTNode

class BSTree:

    def __init__(self, root=None):
        self.__root = root
        if root==None:
            self.__numNodes = 0
        else:
            self.__numNodes = 1

    def getRoot(self):
        return self.__root

    def getNumNodes(self):
        return self.__numNodes

    def isEmpty(self):
        return self.__root == None

    def hasKey(self, key):
        if self.isEmpty():
            return False
        else:
            currNode = self.__root
            while currNode != None:
                if currNode.getKey() == key:
                    return True
                elif key < currNode.getKey():
                    currNode = currNode.getLeftChild()
                elif key > currNode.getKey():
                    currNode = currNode.getRightChild()
                else:
                    raise Exception('hasKey: ' + str(key))
            return False

    def insertKey(self, key):
        if self.isEmpty():
            self.__root = BSTNode(key=key)
            self.__numNodes += 1
            return True
        elif self.hasKey(key):
            return False
        else:
            currNode = self.__root
            parNode = None
            while currNode != None:
                parNode = currNode
                if key < currNode.getKey():
                    currNode = currNode.getLeftChild()
                elif key > currNode.getKey():
                    currNode = currNode.getRightChild()
                else:
                    raise Exception('insertKey: ' + str(key))
            if parNode != None:
                if key < parNode.getKey():
                    parNode.setLeftChild(BSTNode(key=key))
                    self.__numNodes += 1
                    return True
                elif key > parNode.getKey():
                    parNode.setRightChild(BSTNode(key=key))
                    self.__numNodes += 1
                    return True
                else:
                    raise Exception('insertKey: ' + str(key))
            else:
                raise Exception('insertKey: parNode=None; key= ' + str(key))
    

    def heightFromNode(self, node):
        # get height of left subtree, height of right subtree
        # take max, add 1 for root and return
        # call recursively
        if node == None:
            return -1
        if BSTNode.getRightChild(node)==None and BSTNode.getLeftChild(node)==None:
            return 0
        else:
            leftHeight=self.heightFromNode(BSTNode.getLeftChild(node))
            rightHeight=self.heightFromNode(BSTNode.getRightChild(node))
            return 1+max(leftHeight, rightHeight)
        
    def heightOf(self):
        return self.heightFromNode(self.__root)

    def isSideBalanced(self, node):
        ## balanced if difference in height of children is at most 1 for every node
        difference = self.heightFromNode(BSTNode.getLeftChild(node)) - self.heightFromNode(BSTNode.getRightChild(node))
        if abs(difference) > 1:
            return False
        #recurse, once tree has been traversed and no false condition is met
        if BSTNode.getLeftChild(node):
            self.isSideBalanced(BSTNode.getLeftChild(node))
        if BSTNode.getRightChild(node):
            self.isSideBalanced(BSTNode.getRightChild(node))
        return True

    def isBalanced(self):
        return self.isSideBalanced(self.__root)

    def __displayInOrder(self, currnode):
        if currnode == None:
            print('NULL')
        else:
            self.__displayInOrder(currnode.getLeftChild())
            print(str(currnode))
            self.__displayInOrder(currnode.getRightChild())

    def displayInOrder(self):
        self.__displayInOrder(self.__root)

    def isList(self):
        #returns true if number of nodes = height +1
        height=self.heightOf()
        nNodes=self.getNumNodes()
        if height +1 == nNodes:
            return True
        return False
                


    
            

    
   
