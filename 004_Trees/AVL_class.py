########################################################################################
###############################  Node class for AVL TREE  ##############################
########################################################################################

class Node:
    # Constructor with a key parameter creates the Node object.
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.height = 0
        
    # Method to calculate the current nodes's balance factor node, 
    # defined as height(left subtree) - height(right subtree)
    def get_balance(self):
        # Get current height of subtree, or -1 if None
        # return the balance factor.
        
        leftHeight = -1 if self.left == None else self.left.height
        rightHeight = -1 if self.right == None else self.right.height
        return leftHeight - rightHeight

    # Recalculates the current height of the subtree rooted at
    # the node, usually called after a subtree has been 
    # modified.
    def update_height(self):
        # Get current height of subtree, or -1 if None
        # Assign self.height with calculated node height.
        
        leftHeight = -1 if self.left == None else self.left.height
        rightHeight = -1 if self.right == None else self.right.height
        self.height = max(leftHeight, rightHeight) + 1

        
    # Assign either the left or right data member with a new
    # child. The parameter which_child is expected to be the
    # string "left" or the string "right". Returns True if
    # the new child is successfully assigned to this node, False
    # otherwise.
    def set_child(self, which_child, child):
        # Ensure which_child is either left or right.
        # Assign the left or right data member.
        # Assign the new child's parent data member,
        # if the child is not None.
        # Update the node's height, since the structure
        # of the subtree may have changed.
        
        if which_child not in ("left", "right"):
            return False
        if (which_child == "left"):
            self.left = child
        else:
            self.right = child
        
        if (child is not None):
            child.parent = self
            
        self.update_height()
        return True
        

    # Replace a current child with a new child. Determines if
    # the current child is on the left or right, and calls
    # set_child() with the new node appropriately.
    # Returns True if the new child is assigned, False otherwise.
    def replace_child(self, current_child, new_child):
        # Determine if current_child is a left or right child and 
        # assign properly
        # If neither of the above cases applied, then the new child
        # could not be attached to this node.
        
        if self.left == current_child:
            return self.set_child('left', new_child)
        elif self.right == current_child:
            return self.set_child('right', new_child)
        return False
        

########################################################################################
#################################  Class for AVL TREE  #################################
########################################################################################
        
class AVLTree:
    def __init__(self):
        # Constructor to create an empty AVLTree. There is only
        # one data member, the tree's root Node, and it starts
        # out as None.
        self.root = None

    # Performs a left rotation at the given node. Returns the
    # subtree's new root.
    def rotate_left(self, node):
        # Define a convenience pointer to the right child of the 
        # left child.
        rightLeftChild = self.right.left
        
        # Step 1 - the right child moves up to the node's position.
        # This detaches node from the tree, but it will be reattached
        # later.
        if node.parent == None:
            self.root = node.right
        
        # Step 2 - the node becomes the left child of what used
        # to be its right child, but is now its parent. This will
        # detach right_left_child from the tree.
        
        
        # Step 3 - reattach right_left_child as the right child of node.
        
        
        

            
        
        pass

    # Performs a right rotation at the given node. Returns the
    # subtree's new root.
    def rotate_right(self, node):
        # Define a convenience pointer to the left child of the 
        # right child.
        leftRightChild = node.left.right
        
        # Step 1 - the left child moves up to the node's position.
        # This detaches node from the tree, but it will be reattached
        # later.
        if node.parent == None:
            self.root = node.left
            node.left.parent = None
        else:
            node.parent.replace_child(node, node.left)

        # Step 2 - the node becomes the right child of what used
        # to be its left child, but is now its parent. This will
        # detach left_right_child from the tree.
        node.left.replace_child(leftRightChild, node)
        # Step 3 - reattach left_right_child as the left child of node.
        node.set_child("left", leftRightChild)
        

    # Updates the given node's height and rebalances the subtree if
    # the balancing factor is now -2 or +2. Rebalancing is done by
    # performing a rotation. Returns the subtree's new root if
    # a rotation occurred, or the node if no rebalancing was required.
    def rebalance(self, node):
    
        # First update the height of this node. This is because after 
        # each insertion and deletion this is called.
        # This ensures that the height is updated after each insertion/deletion
          
        
        # Check for a right skew.    
            # The subtree is too big to the right.
                # Double rotation case. First do a right rotation
                # on the right child.

                
            # A left rotation will now make the subtree balanced.
        
        # Check for a left skew.                          
            # The subtree is too big to the left
                # Double rotation case. First do a left rotation
                # on the left child.
                
            # A right rotation will now make the subtree balanced.
            
        # No imbalance, so just return the original node.
        pass

    # Insert a new node into the AVLTree. When insert() is complete,
    # the AVL tree will be balanced.
    def insert(self, node):
        
        # Special case: if the tree is empty, just set the root to
        # the new node.

        # else
            # Step 1 - do a regular binary search tree insert.
            
            # Step 2 - Rebalance along a path from the new node's parent up
            # to the root.
        pass            

    # Searches for a node with a matching key. Does a regular
    # binary search tree search operation. Returns the node with the
    # matching key if it exists in the tree, or None if there is no
    # matching key in the tree.
    def search(self, key):
            # Compare the current node's key with the target key.
            # If it is a match, return the current key; otherwise go
            # either to the left or right, depending on whether the 
            # current node's key is smaller or larger than the target key.
            pass
    
    # Attempts to remove a node with a matching key. If no node has a matching key
    # then nothing is done and False is returned; otherwise the node is removed and
    # True is returned.
    def remove_key(self, key):
        node = self.search(key)
        if node is None:
            return False
        else:
            return self.remove_node(node)
            
    # Removes the given node from the tree. The left and right subtrees,
    # if they exist, will be reattached to the tree such that no imbalances
    # exist, and the binary search tree property is maintained. Returns True
    # if the node is found and removed, or False if the node is not found in
    # the tree.
    def remove_node(self, node):
        # Base case: 
                
        # Parent needed for rebalancing.
                    
        # Case 1: Internal node with 2 children
        
        
        # Case 2: Root node (with 1 or 0 children)
        
        # Case 3: Internal with left child only
                    
        # Case 4: Internal with right child only OR leaf
            
        # node is gone. Anything that was below node that has persisted is already correctly
        # balanced, but ancestors of node may need rebalancing.
        pass            