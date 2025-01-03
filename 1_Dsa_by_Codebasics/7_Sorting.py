class Sort:
    def __init__(self,lis):
        self.lis = lis
    def Bubble_sort(self):
        length = len(self.lis)
        for i in range (length - 1):
            swap  = False
            for j in range(length - 1 - i):
                if self.lis[j] > self.lis[j+1]:
                    # temp = self.lis[j]
                    # self.lis[j] = self.lis[j+1]
                    # self.lis[j+1] = temp
                    (self.lis[j]),(self.lis[j+1]) = (self.lis[j+1]), (self.lis[j])
                    swap = True
            if not swap:
                break
        return self.lis
    
    def lis_size(self):                          #Helper Function
        return len(self.lis)
    
    def Bubble_sort_exer(self,key):
        for i in range(self.lis_size() - 1):
            swap = False
            for j in range (self.lis_size()-1-i):
                if self.lis[j][key] > self.lis[j+1][key]:
                    (self.lis[j]),(self.lis[j+1]) = (self.lis[j+1]),(self.lis[j])
                    swap = True
            if not swap:
                break 
        return self.lis    
        
    def selection_sort(self):
        for i in range(self.lis_size() - 1):
            for j in range(i+1,self.lis_size()):
                if self.lis[i] > self.lis[j]:
                    (self.lis[i]),(self.lis[j]) = (self.lis[j]),(self.lis[i])
        return self.lis
    def selection_sort_exer(self,key):
        for i in range (self.lis_size() - 1):
            for j in range(i+1,self.lis_size()):
                if self.lis[j][key] < self.lis[i][key]:
                    (self.lis[i]),(self.lis[j]) = (self.lis[j]),(self.lis[i])
        return self.lis
                
    def quick_sort(self):
        if self.lis_size() <= 1:
            return self.lis
        else:
            pivot = self.lis[0]
            low = [x for x in self.lis[1:] if x<= pivot]
            high = [x for x in self.lis[1:] if x > pivot]
            # return self.quick_sort(low) + [pivot] + self.quick_sort(high)
            sorted_low = Sort(low).quick_sort()
            sorted_high = Sort(high).quick_sort()
            return sorted_low + [pivot] + sorted_high
    def quick_sort_exer(self):
        if self.lis_size() <= 1:
            return self.lis
        else:
            pivot = self.lis[self.lis_size() - 1]
            low = [x for x in self.lis[ :self.lis_size() - 1] if x <= pivot]
            high = [x for x in self.lis[ :self.lis_size() - 1] if x > pivot]  
            low_sorted = Sort(low).quick_sort_exer()
            high_sorted = Sort(high).quick_sort()
            return low_sorted + [pivot] + high_sorted  
    def insertion_sort(self):
        if self.lis_size() <= 0:
            return self.lis
        for i in range (1,self.lis_size()):
            key = self.lis[i]
            j = i -1 
            while j >= 0 and self.lis[j] > key:
                self.lis[j + 1] = self.lis[j]
                j -= 1
            self.lis[j + 1] = key
        return self.lis
    def merge_two_sorted(self,arr1,arr2, arr): # Merge_sort helper Function 
        i = j = k = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                arr[k] = arr1[i]
                i += 1
            else :
                arr[k] = arr2[j]
                j += 1
            k += 1
        while i < len(arr1):
            arr[k] = arr1[i]
            i += 1
            k += 1
        while j < len(arr2):
            arr[k] = arr2[j]
            j += 1
            k+= 1
    def merge_sort(self):
        #base case
        if len(self.lis) <= 1:
            return self.lis
        mid = len(self.lis) // 2
        a = Sort(self.lis[ :mid]).merge_sort()
        b = Sort(self.lis[mid : ]).merge_sort()
        self.merge_two_sorted(a,b,self.lis)
        return self.lis
    def merge_two_sorted_exer(self,arr1,arr2,arr,key,dessending):
        i = j = k = 0
        if not dessending:
            while i < len(arr1) and j < len(arr2):
                if arr1[i][key] < arr2[j][key]:
                    arr[k] = arr1[i]
                    i += 1
                else :
                    arr[k] = arr2[j]
                    j += 1
                k += 1
            while i < len(arr1):
                arr[k] = arr1[i]
                i += 1
                k += 1
            while j < len(arr2):
                arr[k] = arr2[j]
                j += 1
                k += 1
        else:
            while i < len(arr1) and j < len(arr2):
                if arr1[i][key] > arr2[j][key]:
                    arr[k] = arr1[i]
                    i += 1
                else :
                    arr[k] = arr2[j]
                    j += 1
                k += 1
            while i < len(arr1):
                arr[k] = arr1[i]
                i += 1
                k += 1
            while j < len(arr2):
                arr[k] = arr2[j]
                j += 1
                k += 1
            
    def merge_sort_exer(self,key,dessending):
        if len(self.lis) <= 1:
            return self.lis
        mid = len(self.lis) // 2
        a = Sort(self.lis[ :mid]).merge_sort_exer(key,dessending)
        b = Sort(self.lis[mid : ]).merge_sort_exer(key,dessending)
        self.merge_two_sorted_exer(a,b,self.lis,key,dessending)
        return self.lis
    def shell_sort(self):
        gap = self.lis_size() // 2
        while gap > 0:
            for i in range(gap, self.lis_size()):
                anchor = self.lis[i]
                j = i
                while j >= 0  and self.lis[j - gap] > anchor:
                    self.lis[j] = self.lis[j - gap]
                    j -= gap 
                self.lis[j] = anchor
            gap //= 2
        return self.lis
    def shell_sort_exer_helper(self,arr): #removes duplicates 
        new_lis = []
        i = 0
        
        while i < len(arr):
            j = i -1
            if arr[i] == arr[j]:
                i += 1
            else:
                new_lis.append(arr[i])
                i += 1
        return new_lis
        
    def shell_sort_exercise(self):
        if len(self.lis) <= 1:
            return self.lis
        gap = self.lis_size() // 2
        while gap > 0:
            for i in range(gap, self.lis_size()):
                anchor = self.lis[i]
                j = i
                while j >= 0  and self.lis[j - gap] > anchor:
                    self.lis[j] = self.lis[j - gap]
                    j -= gap 
                self.lis[j] = anchor
            gap //= 2
        return self.shell_sort_exer_helper(self.lis)
s = Sort([2,4,6,9,0,3,50,45,67,0,0,0,0,0,9,9,9,2,2,2])
print(s.Bubble_sort())
print(s.selection_sort())
print(s.quick_sort())
print(s.quick_sort_exer())
print(s.insertion_sort())
print(s.merge_sort())
print(s.shell_sort())
p = Sort([3])
print(p.shell_sort_exercise())
print("************** \n")

# Bubble Sort Exercise
# Modify bubble_sort function such that it can sort following list of transactions happening in an electronic store,

# elements = [
#         { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
#         { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
#         { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
#         { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
#     ]
# bubble_sort function should take key from a transaction record and sort the list as per that key. For example,

# bubble_sort(elements, key='transaction_amount')
# This will sort elements by transaction_amount and your sorted list will look like,

# elements = [
#         { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
#         { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
#         { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
#         { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
#     ]
# But if you call it like this,

# bubble_sort(elements, key='name')
# output will be,

# elements = [
#         { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
#         { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
#         { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
#         { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
#     ]
elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
s = Sort(elements)
print(s.Bubble_sort_exer('name'))
print("\n")

# Implement a Multi-Level Sort of a given list of dictionaries based on a given sorting order. If user wants to sort dictionary based on First Key 'A', Then Key 'B', they shall pass list of keys in the order of preference as a list ['A','B']. Your code should be able to sort list of dictionaries for any number of keys in sorting order list.

# Using this multi-level sort, you should be able to sort any list of dictionaries based on sorting order preference

# Example: A single dictionary entry contains two keys 'First Name' and 'Last Name'. the list should be sorted first based on 'First Name', then based on 'Last Name', w.r.t. common/same 'First Name' entries.

# for this, one shall past sorting order of preference list [ 'First Name' , 'Last Name' ]

# For this, Given the following sequence List:

# [
#     {'First Name': 'Raj', 'Last Name': 'Nayyar'},
#     {'First Name': 'Suraj', 'Last Name': 'Sharma'},
#     {'First Name': 'Karan', 'Last Name': 'Kumar'},
#     {'First Name': 'Jade', 'Last Name': 'Canary'},
#     {'First Name': 'Raj', 'Last Name': 'Thakur'},
#     {'First Name': 'Raj', 'Last Name': 'Sharma'},
#     {'First Name': 'Kiran', 'Last Name': 'Kamla'},
#     {'First Name': 'Armaan', 'Last Name': 'Kumar'},
#     {'First Name': 'Jaya', 'Last Name': 'Sharma'},
#     {'First Name': 'Ingrid', 'Last Name': 'Galore'},
#     {'First Name': 'Jaya', 'Last Name': 'Seth'},
#     {'First Name': 'Armaan', 'Last Name': 'Dadra'},
#     {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
#     {'First Name': 'Aahana', 'Last Name': 'Arora'}
# ]
# Your algorithm should generate sorted list:

# [
#     {'First Name': 'Aahana', 'Last Name': 'Arora'}
#     {'First Name': 'Armaan', 'Last Name': 'Dadra'}
#     {'First Name': 'Armaan', 'Last Name': 'Kumar'}
#     {'First Name': 'Ingrid', 'Last Name': 'Galore'}
#     {'First Name': 'Ingrid', 'Last Name': 'Maverick'}
#     {'First Name': 'Jade', 'Last Name': 'Canary'}
#     {'First Name': 'Jaya', 'Last Name': 'Seth'}
#     {'First Name': 'Jaya', 'Last Name': 'Sharma'}
#     {'First Name': 'Karan', 'Last Name': 'Kumar'}
#     {'First Name': 'Kiran', 'Last Name': 'Kamla'}
#     {'First Name': 'Raj', 'Last Name': 'Nayyar'}
#     {'First Name': 'Raj', 'Last Name': 'Sharma'}
#     {'First Name': 'Raj', 'Last Name': 'Thakur'}
#     {'First Name': 'Suraj', 'Last Name': 'Sharma'}
# ]

eleme = [
    {'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    {'First Name': 'Jaya', 'Last Name': 'Seth'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    {'First Name': 'Aahana', 'Last Name': 'Arora'}
]
s = Sort(eleme)
print(s.selection_sort_exer('First Name'))
# output =[{'First Name': 'Aahana', 'Last Name': 'Arora'},
#          {'First Name': 'Armaan', 'Last Name': 'Dadra'},
#          {'First Name': 'Armaan', 'Last Name': 'Kumar'},
#          {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
#          {'First Name': 'Ingrid', 'Last Name': 'Galore'},
#          {'First Name': 'Jade', 'Last Name': 'Canary'},
#          {'First Name': 'Jaya', 'Last Name': 'Seth'},
#          {'First Name': 'Jaya', 'Last Name': 'Sharma'}, 
#          {'First Name': 'Karan', 'Last Name': 'Kumar'}, 
#          {'First Name': 'Kiran', 'Last Name': 'Kamla'}, 
#          {'First Name': 'Raj', 'Last Name': 'Sharma'},
#          {'First Name': 'Raj', 'Last Name': 'Nayyar'},
#          {'First Name': 'Raj', 'Last Name': 'Thakur'},
#          {'First Name': 'Suraj', 'Last Name': 'Sharma'}]

# Merge sort exercise 
# Merge Sort Exercise
# Modify merge_sort function such that it can sort following list of athletes as per the time taken by them in the marathon,

elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]
print(" ## ")
print("\n")
S = Sort(elements)
print(S.merge_sort_exer("time_hours",dessending = True))
# merge_sort function should take key from an athlete's marathon log and sort the list as per that key. For example,

# merge_sort(elements, key='time_hours', descending=True)
# This will sort elements by time_hours and your sorted list will look like,

# elements = [
#         {'name': 'rajab', 'age': 12, 'time_hours': 3},
#         {'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
#         {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
#         {'name': 'vedanth', 'age': 17, 'time_hours': 1},
#     ]
# But if you call it like this,

# merge_sort(elements, key='name')
# output will be,

# elements = [
#         { 'name': 'chinmay',   'age': 24, 'time_hours': 1.5},
#         { 'name': 'rajab', 'age': 12,  'time_hours': 3},
#         { 'name': 'vedanth',  'age': 17,  'time_hours': 1},
#         { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
#     ]

#Q  Exercise: Shell Sort
# Sort the elements of a given list using shell sort, but with a slight 
# modification. Remove all the repeating occurances of elements while sorting.
# Traditionally, when comparing two elements in shell sort, we swap if
# first element is bigger than second, and do nothing otherwise.
# In this modified shell sort with duplicate removal, we will swap 
# if first element is bigger than second, and do nothing if element is smaller, 
# but if values are same, we will delete one of the two elements we are comparing before
# starting the next pass for the reduced gap.
# For example, given the unsorted list [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3], 
# after sorting using shell sort without duplicates, the sorted list would be:

# [0, 1, 2, 3, 5, 7, 8, 9]