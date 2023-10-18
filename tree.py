#Author Name - Aryan Sahni
#Date -05/12/2023
#file - tree.py
#Description - calculator that will convert a command from infix to postfix

from stack import Stack


class BinaryTree:
    def __init__(self, rootObj=None):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
        if isinstance(self.key, BinaryTree):
            self.setRootVal(rootObj.getRootVal())
            self.leftChild = rootObj.getLeftChild()
            self.rightChild = rootObj.getRightChild()

    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key

    def __str__(self):
        s = f"{self.key}"
        s += '('
        if self.leftChild != None:
            s += str(self.leftChild)
        s += ')('
        if self.rightChild != None:
            s += str(self.rightChild)
        s += ')'
        return s


class ExpTree(BinaryTree):

    
    def make_tree(postfix):
        opStack = Stack()
        opsp = opStack.pop
        oper = "+-*/^()"
        for value in postfix:
            if value in oper:
                ntree = ExpTree(value)
                ntree.insertRight(opsp())
                ntree.insertLeft(opsp())
                opStack.push(ntree)
            else:
                opStack.push(value)
        returnval = opsp()
        return returnval

    
    def preorder(tree):
        s = ''
        if not tree == None:
            s += tree.getRootVal()
            s += ExpTree.preorder(tree.getLeftChild())
            s += ExpTree.preorder(tree.getRightChild())
            # print(s)
        return s

    
    def inorder(tree):
        s = ''
        if not tree == None:

            if not tree.getLeftChild() == None:
                s += "("  # adds parathese to the beginning
            lc = str(ExpTree.inorder(tree.getLeftChild()))  # left child
            rv = str(tree.getRootVal())
            rc = str(ExpTree.inorder(tree.getRightChild()))
            # print(lc, rv, rc)
            s += lc
            s += rv
            s += rc
            if not tree.getLeftChild() == None:
                s += ")"  # adds parathese to the end

        return s

    
    def postorder(tree):
        s = ''
        if not tree == None:
            s += ExpTree.postorder(tree.getLeftChild())
            s += ExpTree.postorder(tree.getRightChild())
            s += tree.getRootVal()

        return s

    
    def evaluate(tree):
        oper = ['+', '-', '*', '/', '(', ')', '^']  # operators
        if not tree == None:
            if tree.key in oper:  # checks if tree.key is an operator
                ExpTree.evaluate(tree.getLeftChild())
                ExpTree.evaluate(tree.getRightChild())
                flckey = float(tree.getLeftChild().key)
                frckey = float(tree.getRightChild().key)
                tree.key = ExpTree.doMath(tree.key, flckey, frckey)
        tk = float(tree.key)  # converts tree.key to float
        return tk

    def doMath(op, op1, op2):  # does math
        if op == "*":
            return op1 * op2
        elif op == "/":
            return op1 / op2
        elif op == "+":
            return op1 + op2
        elif op == "^":
            return op1 ** op2
        else:
            return op1 - op2

    def __str__(self):
        return ExpTree.inorder(self)  # returns the inorder of the tree


# a driver for testing BinaryTree and ExpTree
if __name__ == '__main__':
    # test a BinaryTree

    r = BinaryTree('a')
    assert r.getRootVal() == 'a'
    assert r.getLeftChild() == None
    assert r.getRightChild() == None
    assert str(r) == 'a()()'

    r.insertLeft('b')
    assert r.getLeftChild().getRootVal() == 'b'
    assert str(r) == 'a(b()())()'

    r.insertRight('c')
    assert r.getRightChild().getRootVal() == 'c'
    assert str(r) == 'a(b()())(c()())'

    r.getLeftChild().insertLeft('d')
    r.getLeftChild().insertRight('e')
    r.getRightChild().insertLeft('f')
    assert str(r) == 'a(b(d()())(e()()))(c(f()())())'

    assert str(r.getRightChild()) == 'c(f()())()'
    assert r.getRightChild().getLeftChild().getRootVal() == 'f'

    # print("binary tree works properly!")
    # test an ExpTree

    postfix = '5 2 3 * +'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '(5+(2*3))'
    assert ExpTree.inorder(tree) == '(5+(2*3))'
    assert ExpTree.postorder(tree) == '523*+'
    assert ExpTree.preorder(tree) == '+5*23'
    assert ExpTree.evaluate(tree) == 11.0

    postfix = '5 2 + 3 *'.split()
    tree = ExpTree.make_tree(postfix)
    assert str(tree) == '((5+2)*3)'
    assert ExpTree.inorder(tree) == '((5+2)*3)'
    assert ExpTree.postorder(tree) == '52+3*'
    assert ExpTree.preorder(tree) == '*+523'
    assert ExpTree.evaluate(tree) == 21.0
    


