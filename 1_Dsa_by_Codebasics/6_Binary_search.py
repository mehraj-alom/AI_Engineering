class binary_search:
    def __init__(self,listt):
        self.listt = listt
    def bn_search(self,value):
        if not self.listt :
            return "Empty list"
        low = 0
        high = len(self.listt) - 1
        
        while low <= high:
            mid = (low + high) // 2
            if value == self.listt[mid]:
                return mid 
            elif value < self.listt[mid]:
                high = mid - 1 
            else:
                low = mid + 1
        return -1  
        
bs = binary_search([10, 20, 30, 40, 50, 60])
bs = binary_search([20,30,40,45,78,100,112])
print(bs.bn_search(40))  # Output: 3
print(bs.bn_search(25))  # Output: -1
print(bs.bn_search(60))  # Output: 5
print(bs.bn_search(100))