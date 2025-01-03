from itertools import combinations
class Myiterator:
    def __init__(self,data):
        self.data = data
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index <= len(self.data) - 1:
            result = self.data[self.index]
            self.index += 2
            return result
        raise StopIteration
    
if __name__ == "__main__":
    my_list = [10,12,15,20,22,43]
    my_c = Myiterator(my_list)
    for item in my_c:
        print(item)
    items = [1, 2, 3]
    for combo in combinations(my_list, 2):
        print(combo)
