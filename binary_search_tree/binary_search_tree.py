"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if target == self.value:
            return True
        else: 
            if target < self.value:
                if not self.left:
                    return False
                else:
                    return self.left.contains(target)
            else:
                if not self.right:
                    return False
                else:
                    return self.right.contains(target)

    # def contains(self, target):
    #     if self.value == target:
    #         return True
    #     if target < self.value:
    #         if not self.left:
    #             return False
    #         else:
    #             return self.left.contains(target)
    #     else:
    #         if not self.right:
    #             return False
    #         else:
    #             return self.right.contains(target)

    # Return the maximum value found in the tree

    def get_max(self):
        if self.right == None:
            return self.value
        else:
            return self.right.get_max()

    # def get_max(self):
    #     if not self.right:
    #         return self.value
    #     return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # this method wants to traverse every tree node
        # this has to call the fn on self.value
        fn(self.value)

        # how do we propagate to all the other nodes in the tree
        # is there a left child?
        if self.left:
            #if yes call its 'for_each' with the same fn
            self.left.for_each(fn)
        # is there a right child?
        if self.right:
            # if yes call its 'for_each' with the same fn
            self.right.for_each(fn)

    # def iter_depth_first_for_each()
    #     #with depth first traversal there is a certain order to when we visit nodes
    #     # what's that order?
    #     # init a stack to keep track of order of nodes visited
    #     stack = []
    #     # add first node to stack
    #     stack.append(self)
    #     # continue traversing until our stack is empty
    #     while len(stack) > 0:
    #         # pop off the stack
    #         current_node = stack.pop()
    #         # add its children to the stack
    #         # add the right child first and left child second
    #         # to ensure that left is poped off the stack first
    #         if current_node.right:
    #             stack.append(current_node.right)
    #         if current_node.left:
    #             stack.append(current_node.left)
    #         # call the fn function on self.value
    #         fn(self.value)

    # def iter_breadth_first_search(self, fn):
    #     # breadth first traversal follows FIFO ordering of its nodes
    #     # init a deque
    #     q = deque()
    #     # add the first node to our q
    #     q.append(self)

    #     while len(q) > 0:
    #         current_node = q.popleft()
    #         if current_node.left:
    #             q.append(current_node.left)
    #         if current_node.right:
    #             q.append(current_node.right)
    #         fn(self.value)




    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
