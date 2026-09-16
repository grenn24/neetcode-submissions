
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        new_old_node_mappings = {}

        if not head:
            return None

        curr = head
        while curr != None:
            new_node = Node(x = curr.val, next = curr.next, random = curr.random)
            new_old_node_mappings[curr] = new_node
            curr = curr.next

        curr = head
        while curr != None:
            new_node = new_old_node_mappings[curr]
            if curr.random:
                new_node.random = new_old_node_mappings[curr.random]
            if curr.next:
                new_node.next = new_old_node_mappings[curr.next]
            curr = curr.next

        return new_old_node_mappings[head]