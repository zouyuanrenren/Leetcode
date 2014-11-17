'''
Created on 17 Nov 2014

@author: zouyuanrenren
'''

'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
'''

'''
This problem can be solved by different approaches:
1. merge all the lists the same time: always append with the one with least head
To find the smallest one among k ones, time complexity is O(k)
Do this for n times, time complexity is O(kn)
Requies k head pointers and other constant space pointers.
Space complexity is O(k)

2. merge the first two and then the third, then the fourth, ..., repeat until all k lists are merged.
To merge the first two, time complexity is O(n1+n2).
To merge with the thrid one, time complexity is O(n1+n2+n3).
To merge with the 4th one, time complexity is O(n1+n2+n3+n4).
...
To merge with the last one, time compelxity is O(n1+...+nk).
Overall time complexity is still O(kn), but avoids some redundant comparisons.
Space compleixty is O(2+3+...+k) = O(k^2)

3. merge every two lists. Obtain k/2 merged lists. Then merge every two lists again, etc.
To merge each round, time complxity is O(n)
There are in total log(k) rounds.
The total time complexity is O(log(k)n)
Space complexity is O(k/2 + k/4 + ...) = O(k)

4. Heap sort all the lists. The basic idea is:
    a. construct a min-heap of k element from the heads of all lists. Time complexity O(k)
    b. pop the top node. The compleixty O(1)
    c. if the top node is not the end of the corresponding list, add the next element into the heap and adjust.
        Time complexity O(logk)
    d. repeat b-c for n-k times.
    Total time complexity is O(log(k)n)
    
    
In this solution, we use the heap-sort approach
Note that when building heap and adjusting heap, one should swap the actual nodes instead of node values
to make sure that each list is still sorted.
When adjust heap, should adjust along the smaller child.
Need also consider empty list.
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    heap = []
    def mergeKLists(self, lists):
        if lists == None or len(lists) == 0:
            return None
        self.makeHeap(lists)
        newhead = ListNode(0)
        tail = newhead
        size = len(self.heap)
        while size > 0:
            tail.next = self.heap[0]
            tail = tail.next
            if self.heap[0].next != None:
                self.heap[0] = self.heap[0].next
                self.adjustHeap(size)
            else:
                self.heap[0] = self.heap[size-1]
                size -=1
                self.adjustHeap(size)
        return newhead.next
    
    def makeHeap(self, lists):
        self.heap = []
        for i in range(len(lists)):
            if lists[i] != None:
                self.heap.append(lists[i])
                current = len(self.heap)-1
                while (current-1)/2 >=0 and self.heap[(current-1)/2].val > self.heap[current].val:
                    self.swap((current -1)/2,current)
                    current = (current-1)/2
    
    def adjustHeap(self,size):
        current = 0
        while current < size:
            left = current * 2+1
            right = current *2 +2           
            if left < size and self.heap[current].val > self.heap[left].val:
                if right < size and self.heap[right].val < self.heap[left].val:
                    self.swap(right, current)
                    current = right
                else:
                    self.swap(current, left)
                    current = left
            elif right < size and self.heap[current].val > self.heap[right].val:
                self.swap(current, right)
                current = right
            else:
                return
    
    def swap(self,i,j):
        temp = self.heap[i]
        self.heap[i] = self.heap[j]
        self.heap[j] = temp


list1 = [-8,-7,-6,-3,-2,-2,0,3]
list2 = [-10,-6,-4,-4,-4,-2,-1,4]
list3 = [-10,-9,-8,-8,-6]
list4 = [-10,0,4]

head1 = ListNode(0)
tail1 = head1
for item in list1:
    tail1.next = ListNode(item)
    tail1 = tail1.next

head2 = ListNode(0)
tail2 = head2
for item in list2:
    tail2.next = ListNode(item)
    tail2 = tail2.next
    
head3 = ListNode(0)
tail3 = head3
for item in list3:
    tail3.next = ListNode(item)
    tail3 = tail3.next

head4 = ListNode(0)
tail4 = head4
for item in list4:
    tail4.next = ListNode(item)
    tail4 = tail4.next

lists = [head1.next, head2.next, head3.next, head4.next]

sol = Solution()
head = sol.mergeKLists(lists)
while head != None:
    print head.val,
    head = head.next
print

        