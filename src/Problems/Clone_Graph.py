'''
Created on 30 Dec 2014

@author: Yuan
'''
'''
This is a typical search problem. Either depth-first search or breadth-first search will work.
When using breadth-first search, one can emply a queue to maintain the nodes to be processed.
Another hashmap is needed to maintain the clone of all nodes.
'''
# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node == None:
            return None
        head = UndirectedGraphNode(node.label)
        dict = {node.label:head}
        queue = [node]
        index = 0
        while index < len(queue):
            current = queue[index]
            index += 1
            for neighbor in current.neighbors:
                if neighbor.label not in dict:
                    dict[neighbor.label] = UndirectedGraphNode(neighbor.label)
                    queue.append(neighbor)
                dict[current.label].neighbors.append(dict[neighbor.label])
        return head

node0 = UndirectedGraphNode(0)
node1 = UndirectedGraphNode(1)
node2 = UndirectedGraphNode(2)
node0.neighbors.append(node1)
node0.neighbors.append(node2)
node1.neighbors.append(node0)
node1.neighbors.append(node2)
node2.neighbors.append(node0)
node2.neighbors.append(node1)
node2.neighbors.append(node2)

sol = Solution()
node = sol.cloneGraph(node0)
print node.label           