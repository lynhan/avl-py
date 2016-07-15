class node:
    def __init__(self, val=None, parent=None, left=None, right=None):
        self.val = val
        self.parent = parent
        self.left = left
        self.right = right
    def __gt__(self, other):
        return self.val > other.val

def PL(parent, left):
    parent.left = left
    left.parent = parent

def PR(parent, right):
    parent.right = right
    right.parent = parent

class bst:
    def __init__(self, root=None):
        self.root = root

    def insert(self, node):
        print('\nbefore insert')
        self.out()

        now = self.root
        prev = None
        while now:
            prev = now
            if node.val > now.val:
                now = now.right
            else:
                now = now.left
        if node.val > prev.val:
            prev.right = node
        else:
            prev.left = node
        node.parent = prev

        print('\nafter')
        self.out()

    def remove(self, node):
        print('\nbefore remove', node.val)
        self.out()

        if not node.right and not node.left:  # no child
            if node == node.parent.left:
                node.parent.left = None
            else:
                node.parent.right = None

        elif not (node.right and node.left):  # one child
            if node == node.parent.left:
                node.left.parent = node.parent
                node.parent.left = node.left
            else:
                node.right.parent = node.parent
                node.parent.right = node.right

        else:  # two children
            pre = self.predecessor(node)
            self.remove(pre)
            PL(pre, node.left)
            PR(pre, node.right)
            if node == self.root:
                self.root = pre

        print('\nafter remove')
        self.out()

    def find(self, node):
        now = root
        while now:
            if now == node:
                return True
            if now > parent:
                now = now.right
            else:
                now = now.left
        return False

    def update(self, node):
        self.remove(node)
        self.insert(node)

    def successor(self, node):
        if node.right:
            now = node.right
            while now.left:
                now = now.left
            return now
        while node == node.parent.right:
            node = node.parent
        return node

    def predecessor(self, node):
        original = node.val
        if node.left:
            now = node.left
            while now.right:
                now = now.right
            return now
        while node == node.parent.left:
            node = node.parent
        return node

    def out(self):
        self.traverse(self.root)

    def traverse(self, node):
        if not node: return
        self.traverse(node.left)
        print(node.val)
        self.traverse(node.right)


# test

one = node(1)
two = node(2)
three = node(3)
four = node(4)
five = node(5)
six = node(6)
seven = node(7)

PL(four, two)
PL(two, one)
PR(two, three)
PR(four, six)
PL(six, five)

b = bst(four)
b.successor(four)
