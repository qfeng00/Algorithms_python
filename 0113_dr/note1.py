list()

class Array(object):
    def __init__(self,size = 25):
        self._size = size
        self._item = [None] * size


class Node(object):
    def __init__(self,value = None,next = None):
        self.value, self.next = value,next

class LinkedList(object):
    def __init__(self,maxsize = None):
        self.maxsize = maxsize
        self.root = Node()
        self.length = 0
        self.tailnode = None

    def __len__(self):
        return self.length
    def append(self,value):
        if self.maxsize is not None and len(self) > self.maxsize:
            raise Exception('full')
        node =Node(value)
        tailnode = self.tailnode
        if tailnode is None:
            self.root.next = node
        else:
            tailnode.next = node
        tailnode = node
        self.length +=1

    def appendleft (self,value):
        headnode = self.root.next
        node = Node(value)
        self.root.next = node
        node.next = headnode
        self.length +=1

    def iter_node(self):
        currnode = self.root.next
        while currnode is not self.tailnode:




