#Seraching in Bst is O(log n)
#8->4->2->1
#Insert Complexity ias also O(log n)
import time
# class Tree:
#     def __init__(self,val):
#         self.val = val 
#         self.left = None
#         self.right = None 
#     def add_value(self,value):
#         if value == self.val:
#               return 
#         elif value < self.val:
#               #value should go left 
#             if self.left:
#                 self.left.add_value(value)
#             else:
#                 self.left = Tree(value)
#         else:
#             #value should go right 
#             if self.right:
#                 self.right.add_value(value)
#             else:
#                 self.right = Tree(value)
#     def in_order_traversal(self):
#         lis = []
#         if self.left:
#             lis += self.left.in_order_traversal()
#         lis.append(self.val)
#         if self.right:
#             lis += self.right.in_order_traversal()
#         return lis
#     def search_by_value(self,value):
        
#         current = self
#         while current :
#             if value == current.val:
#                 return True
#             elif value > current.val:
#                 #go to right
#                 current = current.right
#             else:
#                 #go to left 
#                 current  = current.left
#         return False
            
# def Build_tree(listt):
#     Root = Tree(listt[0])
#     for i in range(1,len(listt)):
#         #time.sleep(0.6)
#         Root.add_value(listt[i])
#     return Root
# listt = [17,4,1,20,9,23,18,34]
# Root = Build_tree(listt)
# print(Root.in_order_traversal())
# print(Root.search_by_value(34))

# ****************************************************************khckdshshkdshkjnndjsdjnjksdnkjn****************************
# Binary Tree Part 1 Exercise
# Add following methods to BinarySearchTreeNode class created in main video tutorial

# 1. find_min(): finds minimum element in entire binary tree
# 2. find_max(): finds maximum element in entire binary tree
# 3. calculate_sum(): calcualtes sum of all elements
# 4. post_order_traversal(): performs post order traversal of a binary tree
# 5. pre_order_traversal(): perofrms pre order traversal of a binary tree

class Tree:
    def __init__(self,value):
        self.value = value
        self.left = None 
        self.right = None
    def add_child(self,child_value):
        if child_value == self.value:
            return
        elif child_value < self.value:
            if self.left:
                self.left.add_child(child_value)
            else :
                self.left = Tree(child_value)
        else:#child value is greater than node value , it should go right 
            if self.right:
                self.right.add_child(child_value)
            else:
                self.right = Tree(child_value)
    def in_order_traversal(self):
        list = []
        if self.left :
            list += self.left.in_order_traversal()
        list.append(self.value)
        if self.right:
            list += self.right.in_order_traversal()
        return list
    def find_min(self):
        current = self 
        while current.left:
            current = current.left
        return current.value
    def find_max(self):
        current = self
        while current.right:
            current = current.right
        return current.value
    def calc_sum(self):
        sum = self.value
        if self.left:
            sum += self.left.calc_sum()
        if self.right:
            sum += self.right.calc_sum()
        return sum
    def pre_order_traversal(self):
        list = [self.value]
        if self.left:
           list += self.left.pre_order_traversal()
        if self.right:
           list += self.right.pre_order_traversal()
        return list
    def post_order_traversal(self):
        list = []
        if self.left:
            list += self.left.post_order_traversal()
        if self.right:
            list += self.right.post_order_traversal()
        list.append(self.value)
        return list
    # def delete_a_node(self,node_val):
    #     if node_val < self.value:
    #         if self.left :
    #             self.left = self.left.delete_a_node(node_val)
        # elif node_val > self.value:
        #     if self.right :
        #         self.right = self.right.delete_a_node(node_val)
        # else :
        #     if self.left is None and self.right is None:
        #         return None
        #     if not self.right:
        #         return self.left
        #     if not self.left:
        #         return self.right
        #     #Now find the minimum from the right subtree
        #     # current = self.right 
        #     # while current.right :
        #     #     current = current.right
            
        #     # min_value = self.right.find_min()
        #     # self.data = min_value
        #     # self.right.delete_a_node(min_value)
        #     #find the maximum from the right subtree
        #     current = self.left
        #     while current.left:
        #         current = current.left
        #     max_val = self.left.find_max()
        #     self.data = max_val
        #     self.left.delete_a_node(max_val)
        # return self
    def delete_a_node(self,node_value):
        if node_value > self.value:
            self.right = self.right.delete_a_node(node_value)
        elif node_value < self.value:
            self.left = self.left.delete_a_node(node_value)
        else:
            if self.right is None and self.left is None :
                return None 
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            current = self.left 
            while current.left :
                current = current.left
            max_value = self.left.find_max()
            self.data = current.data
            self.left.delete_a_node(max_value)
        return self
        
                
def build_tree(elements):
    if not elements:
        return None
    root = Tree(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])
    return root
elem = [1,7,9,4,65,87,13,56,54,12,10,15]
root = build_tree(elem)
a = root.in_order_traversal()
print(a)
time.sleep(3)
# root.add_child(0)
print(root.in_order_traversal())
time.sleep(4)
b = root.find_max()
c = root.find_min()
print("Min =", c, "Max = ",b)
time.sleep(5)
print(root.calc_sum())
time.sleep(6)
print(root.pre_order_traversal())
time.sleep(7)
print(root.post_order_traversal())
time.sleep(8)
root.delete_a_node(10)

print("After deleting a node :",root.post_order_traversal())
