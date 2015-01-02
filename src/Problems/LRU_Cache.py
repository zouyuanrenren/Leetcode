'''
Created on 2 Jan 2015

@author: Yuan
'''
class LRUCache:

    dict = None
    cap = None
    head = None
    tail = None
    # @param capacity, an integer
    def __init__(self, capacity):
        self.dict = {}
        self.cap = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.pre = self.head

    # @return an integer
    def get(self, key):
        if key in self.dict:
            node = self.dict[key]
            self.use(node)
            return node.val
        else:
            return -1

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key in self.dict:
            node = self.dict[key]
            node.val = value
            self.use(node)
        else:
            node = Node(key, value)
            if len(self.dict) == self.cap:
                pre = self.tail.pre
                del self.dict[pre.key]
                pre.pre.next = self.tail
                self.tail.pre = pre.pre
            self.add(node)
                

    def use(self, node):
        node.pre.next = node.next
        node.next.pre = node.pre
        node.next = self.head.next
        node.next.pre = node
        self.head.next = node
        node.pre = self.head
    
    def add(self, node):
        self.dict[node.key] = node
        node.next = self.head.next
        node.next.pre = node
        node.pre = self.head
        self.head.next = node

class Node:
    
    key = -1
    val = -1
    pre = None
    next = None
    
    def __init__(self, key, val):
        self.key = key
        self.val = val
        pre = None
        next = None
        

key = [3,2,4,5,6,4]
val = [1,2,3,4,5,6,7,8,9,0]


cache = LRUCache(2)
cache.set(2,1)
cache.set(1,1)
cache.get(2)
cache.set(4,1)
cache.get(1)
cache.get(2)
# [set(2,1),set(1,1),get(2),set(4,1),get(1),get(2)]

2, 4
1, 1

node = cache.head
while node != None:
    print node.val,
    node = node.next