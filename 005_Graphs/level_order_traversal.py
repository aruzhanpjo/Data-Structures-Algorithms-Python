class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
        

def level_order_traversal(root):
    queue = []
    discovered = set()
    queue.append(root)
    discovered.add(root)
    while queue != []:
        cur = queue.pop(0)
        print(cur.val)
        
        for neighbor in [cur.left, cur.right]:
            if neighbor is not None and neighbor not in discovered:
                queue.append(neighbor)
                discovered.add(neighbor)
        
        
        
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)


level_order_traversal(root)

