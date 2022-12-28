class Node:
    def __init__(self, Data, Parent):
        self.data = Data
        self.left = None
        self.right = None
        self.parent = Parent

    def insert(self, val):
        if val <= self.data:
            if self.left != None:
                self.left.insert(val)
            else:
                self.left = Node(val, self)
        else:
            if self.right != None:
                self.right.insert(val)
            else:
                self.right = Node(val, self)

    def prev(self):
        if self.left != None:
            cur = self.left
            while cur.right != None:
                cur = cur.right
            return cur

        if self.parent == None:
            return None
        
        if self == self.parent.right:
            return self.parent

        if self == self.parent.left:
            cur = self
            par = self.parent
            grand = self.parent.parent
            while grand != None:
                if par == grand.right:
                    return grand
                cur = cur.parent
                par = par.parent
                grand = grand.parent
            return None

    def next(self):
        if self.right != None:
            cur = self.right
            while cur.left != None:
                cur = cur.left
            return cur

        if self.parent == None:
            return None
        
        if self == self.parent.left:
            return self.parent

        if self == self.parent.right:
            cur = self
            par = self.parent
            grand = self.parent.parent
            while grand != None:
                if par == grand.left:
                    return grand
                cur = cur.parent
                par = par.parent
                grand = grand.parent
            return None

    def getMaxDepth(self):
        if self.left == None and self.right == None:
            return 1

        leftDepth = 0
        if self.left != None:
            leftDepth = self.left.getMaxDepth()
        rightDepth = 0
        if self.right != None:
            rightDepth = self.right.getMaxDepth()
        return max([leftDepth, rightDepth] + 1)

    def delete(self):
        if self.left.getMaxDepth() > self.right.getMaxDepth():
            self.data = self.left.data
            self.left.delete()
        else:
            self.data = self.right.data
            self.right.delete()

    def printSpaced(self, level):
        if self.right != None:
            self.right.printSpaced(level + 1)

        for i in range(level):
            print("      ", end = '')
        print(self.data, end = '')

        if self.right != None and self.left != None:
            print("<")
        elif self.right != None:
            print("/")
        elif self.left != None:
            print("\\")
        print('')
            
        if self.left != None:
            self.left.printSpaced(level + 1)

    def PreOrder(self):
        print(self.data, end = " ")
        if self.left != None:
            self.left.PreOrder()        
        if self.right != None:
            self.right.PreOrder()

    def InOrder(self):
        if self.left != None:
            self.left.InOrder()
        print(self.data, end = " ")      
        if self.right != None:
            self.right.InOrder()

    def PostOrder(self):
        if self.left != None:
            self.left.PostOrder()      
        if self.right != None:
            self.right.PostOrder()
        print(self.data, end = " ")

    def InfixPrint(self):
        if self.data == '+' or self.data == '-':
            print("(", end = ' ')

        if self.left != None:
            self.left.InfixPrint()
        print(self.data, end = " ")      
        if self.right != None:
            self.right.InfixPrint()
            
        if self.data == '+' or self.data == '-':
            print(")", end = ' ')

    def PostfixTree(self, data):
        item = data[0][data[1]]
        data[1] -= 1
        self.data = item
        if str(item) in '+-*/':
            self.left = Node(0, self)
            self.left.PostfixTree(data)
            self.right = Node(0, self)
            self.right.PostfixTree(data)

    def PrefixTree(self, data):
        item = data[0][data[1]]
        data[1] += 1
        self.data = item
        if str(item) in '+-*/':
            self.left = Node(0, self)
            self.left.PrefixTree(data)
            self.right = Node(0, self)
            self.right.PrefixTree(data)

    
class Tree:
    def __init__(self, Root):
        self.root = Root
        
    def WidthPrint(self):
        queue = []
        queue.append(self.root)
        while len(queue) > 0:            
            curNode = queue[0]
            print(curNode.data, end = ' ')

            if curNode.left != None:
                queue.append(curNode.left)
            if curNode.right != None:
                queue.append(curNode.right)
            queue.pop(0)

    def insert(self, val):
        self.root.insert(val)

    def min(self):
        cur = self.root
        while cur.left != None:
            cur = cur.left
        return cur.data

    def max(self):
        cur = self.root
        while cur.right != None:
            cur = cur.right
        return cur.data

    def find(self, val):
        cur = self.root
        while cur != None:
            if val == cur.data:
                return cur

            if val < cur.data:
                if cur.left != None:
                    cur = cur.left
                else:
                    return None
            else:
                if cur.right != None:
                    cur = cur.right
                else:
                    return None
        return cur
    
    def ShowHorizontally(self):
        halfConsole = 50
        queue = []
        queue.append([self.root, halfConsole, 0, halfConsole // 2])

        for i in range(halfConsole):
            print(" ", sep = "", end = "")

        while len(queue) > 0:
            cur = queue.pop(0)
            data = cur[0].data
            step = cur[3]
            line = cur[2]
            col = cur[1]


            if cur[0].left != None:
                queue.append([cur[0].left, col - step, line + 1, step // 2])
                print("/", end = '')

            print(data, end = "")

            if cur[0].right != None:
                queue.append([cur[0].right, col + step, line + 1, step // 2])
                print("\\", end = '')

            if len(queue) == 0:
                print("")
                return

            nextItemLine = queue[0][2]
            nextItemCol = queue[0][1]

            if line == nextItemLine:
                for i in range(nextItemCol - col):
                    print(" ", end = "")
            else:
                print("")
                print("")
                for i in range(nextItemCol):
                    print(" ", end = "")

    def ShowVertically(self):
        self.root.printSpaced(0)
        print()

    def PreOrderPrint(self):
        self.root.PreOrder()
        print()
    
    def InOrderPrint(self):
        self.root.InOrder()
        print()
        
    def PostOrderPrint(self):
        self.root.PostOrder()
        print()

    def InfixPrint(self):
        self.root.InfixPrint()
        print()

def ParceFormula(string):
    res = []
    curNumber = 0
    for item in string:
        if item in '0123456789':
            curNumber = curNumber * 10 + int(item)
        else:
            if curNumber != 0:
                res.append(curNumber)
                curNumber = 0
            if item in "()+-*/":
                res.append(item)
                
    if curNumber != 0:
        res.append(curNumber)
    return res

def InfixToPostfix(formula):
    stack = []
    queue = []
    for item in formula:
        if type(item) is int:
            queue.append(item)

        elif item in '+-*/':

            if len(stack) > 0:
                topStack = stack[len(stack) - 1]
            if len(stack) == 0 or topStack == '(':
                stack.append(item)
            elif item in '*/' and topStack in '+-':
                stack.append(item)
            else:
                while True:
                    top = stack.pop()
                    queue.append(top)
                    if len(stack) == 0:
                        break
                    newTop = stack[len(stack) - 1]
                    if top in '*/' and newTop in '+-' or newTop == '(':
                        break;
                stack.append(item)

        elif item == '(':
            stack.append(item)

        elif item == ')':
            while True:
                top = stack.pop()
                if top == '(':
                    break
                else:
                    queue.append(top)
                    
    while len(stack) > 0:
        queue.append(stack.pop())
    return queue

def PostfixToTree(formula):
   tree = Tree(Node(0, None))
   pointer = len(formula) - 1
   tree.root.PostfixTree([formula, pointer])
   return tree

def PrefixToTree(formula):
   tree = Tree(Node(0, None))
   pointer = 0
   tree.root.PrefixTree([formula, pointer])
   return tree



tree = Tree(Node(21, None))
t = [7, 32, 5, 14, 27, 37, 4, 6, 12, 18, 25, 30, 34, 39, 2, 9, 24, 33]

for item in t:
    tree.insert(item)
    
text = '(4-2)+6*9'
print(['Formula:', text])
formula = (ParceFormula(text))
formula = InfixToPostfix(formula)
t2 = PostfixToTree(formula)
t2.ShowHorizontally()
print('Infix:', end = " ")
t2.InfixPrint()
print('Postfix:', end = " ")
t2.PostOrderPrint()
print('Prefix:', end = " ")
t2.PreOrderPrint()
print()
