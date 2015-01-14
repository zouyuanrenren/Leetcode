'''
Created on 17 Nov 2014

@author: zouyuanrenren
'''

'''
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.
'''

'''
A deep copy copies the data instead of the pointer.
To avoid redundant copies, use a hashmap.
Also note that the list may have cycles so one can not simply iterate through the list.

One solution1 is to use a queue to maintian the processed nodes.
The basic idea is:
1. put the head node into the hashmap.
2. put the head node into the queue.
2. going through each node in the queue;
3. if the copy's next node has not been copied, create a copy of the original's next and put into the hashmap and queue;
4. if the copy's random node has not been copied, reate a copy of the original's random and put into the hashmap and queue.


The other solution2 is to design an additional stop condition for the loop.
The basic idea is:
1. put the head node into the hashmap.
2. for each node in the list, we find its copy and start to add its next and random node.
3. if the copy's next and random do not exist or have already been added, then quit the loop.
4. otherwise, create copies for the next and random node and add them into the hashmap.
'''

# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution1:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head == None:
            return None
        current = head
        newhead = RandomListNode(current.label)
        nodemap = {current:newhead}
        while current:
            copied = nodemap[current]
            if (current.next == None or copied.next) and (current.random == None or copied.random):
                break
            if current.next:
                if current.next not in nodemap:
                    nodemap[current.next] = RandomListNode(current.next.label)
                copied.next = nodemap[current.next]
            if current.random:
                if current.random not in nodemap:
                    nodemap[current.random] = RandomListNode(current.random.label)
                copied.random = nodemap[current.random]
            current = current.next
        return newhead


class Solution2:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        if head == None:
            return None
        current = head
        newhead = RandomListNode(current.label)
        nodemap = {current:newhead}
        queue = [current]
        i = 0
        while i < len(queue):
            current = queue[i]
            copied = nodemap[current]
            if current.next:
                if current.next not in nodemap:
                    nodemap[current.next] = RandomListNode(current.next.label)
                    queue.append(current.next)
                copied.next = nodemap[current.next]
            if current.random:
                if current.random not in nodemap:
                    nodemap[current.random] = RandomListNode(current.random.label)
                    queue.append(current.random)
                copied.random = nodemap[current.random]
            i += 1
        return newhead
    
    
list = [1,2,3,4,5]
head = RandomListNode(0)
tail = head
for item in list:
    tail.next = RandomListNode(item)
    tail.random = tail.next
    tail = tail.next
tail.next = head

sol = Solution2()
head = sol.copyRandomList(head)
while head != None:
    print head.label,
    head = head.random
print
        
