import bst

class avlnode:
    def __init__(self, val):
        self.height = 1  # distance from leaf, leaf is 1
        self.balance = 0  # left minus right depth
        self.pred = None
        self.succ = None

def PL(parent, left):
    parent.left = left
    left.parent = parent

def PR(parent, right):
    parent.right = right
    right.parent = parent

def updateBalance(node):
    node.balance = node.left.height - node.right.height

dummy = avlnode(-1)
dummy.height = 0
dummy.balance = 0
PL(node, dummy)
PR(node, dummy)

class avl(bst):
    def __init__(self, root=None):
        self.root = root
        self.map = {}  # val to node with val

    def insert(self, node):
        print('\nbefore insert')
        self.out()

        now = self.root
        prev = None
        while now.val != -1:
            prev = now
            if node.val > now.val:
                now = now.right
            else:
                now = now.left
        if node.val > prev.val:
            PR(prev, node)
        else:
            PL(prev, node)
        PL(node, dummy)
        PR(node, dummy)

        print('\nafter')
        self.out()

        while node.parent != self.root:
            if node == node.parent.right and node.height > node.parent.left:
                node.parent.height += 1
                node = node.parent
                updateBalance(node)
                self.rotate(node)
                break
            elif node == node.parent.right and node.height > node.parent.left:
                node.parent.height += 1
                node = node.parent
                updateBalance(node)
                self.rotate(node)
                break
        node.pred = self.predecessor(node)
        node.succ = self.successor(node)
        self.map[node.val] = node

    def rotate(node):
        if node.balance not in [-1, 0, 1]:
            if node.left and node.left.right:
                self.LR(node)
            elif node.left and node.left.left:
                self.LL(node)
            elif node.right and node.right.left:
                self.RL(node)
            elif ndoe.right and node.right.right:
                self.RR(node)

    def LR(self, top):
        middle = top.left
        bottom = top.left.right
        # bottom goes to middle
        middle.right = bottom.left
        PL(top, bottom)
        PL(bottom, middle)
        self.LL(top)

    def LL(self, top):
        # middle goes to top, right rotation
        top.left = middle.right
        PR(middle, top)
        self.updateSubTreeHeightBalance(middle)

    def RL(self, top):
        middle = top.right
        bottom = top.right.left
        middle.left = bottom.right
        PR(top, bottom)
        PR(bottom, middle)
        self.RR(self.top)

    def RR(self, top):
        middle = top.right
        top.right = middle.left
        PL(middle, top)
        self.updateSubTreeHeightBalance(middle)

    def updateSubTreeHeightBalance(node):
        if node.val = -1:
            node.height = 0
            node.balance = 0
        updateSubTreeHeightBalance(node.left)
        updateSubTreeHeightBalance(node.right)
        node.height = max(node.left.height, node.right.height)
        node.balance = node.left.balance - node.right.balance

    def remove(self, node):
        print('\nbefore remove', node.val)
        self.out()

        if not node.right and not node.left:  # no child
            if node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None
            self.rotate(node.parent)

        elif not (node.right and node.left):  # one child
            if node == node.parent.left:
                node.left.parent = node.parent
                node.parent.left = node.left
            else:
                node.right.parent = node.parent
                node.parent.right = node.right
            self.rotate(node.parent)

        else:  # two children
            pre = self.predecessor(node)
            self.remove(pre)
            PL(pre, node.left)
            PR(pre, node.right)
            if node == self.root:
                self.root = pre
            self.rotate(pre)

        delete self.map[node.val]
        print('\nafter remove')
        self.out()
