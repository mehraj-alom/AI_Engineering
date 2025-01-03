from collections import deque 
# # class stk:
# #     def __init__(self):
# #        self.stackk = deque()
# class stack:
#     def __init__(self):
#         self.container = deque()
#     def push(self,e):
#         self.container.append(e)
#     def pop(self):
#         if self.container is not None :
#             self.container.pop()
#         else:
#             print("stack_is_empty")
#     def peek (self):
#         return self.container[-1]
#     def size(self):
#         return len(self.container)
#     def isempty(self):
#         return len(self.container) == 0
#     def print(self):
#         if self.isempty():
#             print("Stack_is_empty")
#         else:
#             print(list(self.container))  
              
            
        
    
# st = stack()
# st.push(11)
# st.push(90)
# st.push(22)
# st.print()
# st.pop()
# st.print()
# st.pop()
# st.pop()
# st.print()
# print(st.isempty())


##########################   Exercise **********************
#Write a function in python that can reverse a string using stack data structure. Use Stack class from the tutorial.
#reverse_string("We will conquere COVID-19") should return "91-DIVOC ereuqnoc lliw eW"

# class stack:
#     def __init__(self):
#         self.container = deque()

#     def push(self,e):
#         self.container.append(e)
#     def pop(self):
#         if self.container is not None :
#            return self.container.pop()
#         else:
#             raise IndexError("stack_is_empty")
#     def peek (self):
#         return self.container[-1]
#     def size(self):
#         return len(self.container)
#     def isempty(self):
#         return len(self.container) == 0
# class string(stack):
#     def __init__(self):
#         super().__init__()
#     def revese_string(self,s):
#         for ch in s :
#             self.push(ch)
#         reversed_str = ''
#         while not self.isempty():
#             reversed_str += self.pop()
#         return reversed_str
# st = string()
# print(st.revese_string("We will conquere COVID-19"))
    

# class stack:
#     def __init__(self):
#          self.container = deque()

#     def push(self,item):
#             self.container.append(item)
#     def pop(self):
#         if self.is_empty():
#             raise IndexError("stack_is_empty")
#         else:
#             return self.container.pop()
            
#     def is_empty(self):
#         return len(self.container) == 0
#     def size(self):
#         return len(self.container)
# class string(stack):
#     def __init__(self):
#         super().__init__()
#     def rev_stg(self,s):
#         for ch in s:
#             self.push(ch)
#         strr = ''
#         while self.size() != 0:
#             strr += self.pop()
#         return strr
#     def ptint(self):
#         print(self.size())
# st = string()
# print(st.rev_stg("We will conquere COVID-19"))
# st.ptint()
                    
# Write a function in python that checks if paranthesis in the string are balanced or not. Possible parantheses are "{}',"()" or "[]". Use Stack class from the tutorial.
# is_balanced("({a+b})")     --> True
# is_balanced("))((a+b}{")   --> False
# is_balanced("((a+b))")     --> True
# is_balanced("))")          --> False
# is_balanced("[a+b]*(x+2y)*{gg+kk}") --> True
# class stack :
#     def __init__(self):
#         self.container = deque()
#     def push(self,item):
#         self.container.append(item)
#     def pop(self):
#         if not self.is_empty():
#             return self.container.pop()
#         else:
#             raise IndexError("container is empty")
#     def size(self):
#         return len(self.container)
#     def is_empty(self):
#         return len(self.container)== 0  
#     def print(self):
#         if not self.is_empty():
#             print(list(self.container))
#         else:
#             raise IndexError("container is empty")
# def is_match(ch1,ch2):
#     my_dict = {
#         ")" : "(",
#         "}" : "{",
#         "]" : "["
#     }
#     return my_dict[ch1] == ch2
# def is_balanced(s):
#     st = stack()
#     for ch in s :
#         if ch == '(' or ch == '{' or ch == '[':
#             st.push(ch)
#         elif ch == ')' or ch == '}' or ch == ']':
#             if st.is_empty():
#                 return False
#             elif not is_match(ch,st.pop()):
#                 return False 
#     return st.size() == 0      
    

# print(is_balanced("({a+b})"))    
# print(is_balanced("))((a+b}{"))   
# print(is_balanced("((a+b))"))     
# print(is_balanced("))"))          
# print(is_balanced("[a+b]*(x+2y)*{gg+kk}") )
    
    
#Question to do 
# Question: Validate HTML Tags
# Write a function is_valid_html to check if a given HTML-like string has properly nested and 
# balanced tags. Tags are represented as strings enclosed in < and >. For example:

# <div><p>Hello</p></div> is valid.
# <div><p>Hello</div></p> is invalid.
###########********** refer https://docs.python.org/3/library/collections.html#collections.deque  ************
