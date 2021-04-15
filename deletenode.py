'''
Delete node when pointer to the specific node is given not head is given
'''

def delteNode(self,node):
    node.val = node.next.val
    node.next = node.next.next