class Node:
    def __init__(self, val):
        self.v = val
        self.left = None
        self.right = None

    def add(self, val):
        if val < self.v:
            if self.left:
                self.left.add(val)
            else:
                self.left = Node(val)
        elif val > self.v:
            if self.right:
                self.right.add(val)
            else:
                self.right = Node(val)
    
    def _reprl(self):
        if self.left is None:
            return '.'
        else:
            return '(' + repr(self.left) + ')'

    def _reprr(self):
        if self.right is None:
            return '.'
        else:
            return '(' + repr(self.right) + ')'

    def __repr__(self):
        return self._reprl() + repr(self.v) + self._reprr()

class Tree:
    def __init__(self):
        self.head = None

    def add(self, val):
        if self.head:
            self.head.add(val)
        else:
            self.head = Node(val)

    def add_sorted_list(self, l):
        if len(l) == 1:
            self.add(l[0])
        else:
            p = len(l) // 2
            self.add(l[p])
            self.add_sorted_list(l[:p])
            if len(l) > 2:
                self.add_sorted_list(l[p+1:])
    
    def __repr__(self):
        return 'Tree(' + repr(self.head) + ')'
    
if __name__ == '__main__':
    t = Tree()
    t.add_sorted_list([0, 1, 2, 3, 4, 5, 6])
    print(t)

