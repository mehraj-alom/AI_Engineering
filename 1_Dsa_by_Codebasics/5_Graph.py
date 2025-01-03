import time
class graph:
    def __init__(self,listt):
        self.list = listt
        self.dict = {}
        for key , value in self.list :
            if key in self.dict:
                self.dict[key].append(value)
            else:
                self.dict[key] = [value]
    def get_path(self,start,end,path = []):
        path = path + [start]
        if start == end :
            return [path] 
        if  start not in self.dict:
            return []
        paths = []
        for city in self.dict[start]:
            print("path: ",path)
            time.sleep(0.6)
            if city not in path :
                new_city = self.get_path(city,end,path)
                
                for new_path in new_city:
                    paths.append(new_path)
                time.sleep(0.8)
                print(paths)   
        return paths     
    def Shortest_path(self,start,end):
        a = self.get_path(start,end)
        if not a:
            return "no path"
        ret_path = a[0]
        for path in a :
            if len(path) < len(ret_path):
                ret_path = path
        return ret_path
    
# Define edges of the graph
edges = [
    ("Mumbai", "Pune"),
    ("Mumbai", "Delhi"),
    ("Pune", "Goa"),
    ("Delhi", "Goa"),
    ("Goa", "Bangalore"),
]

# Create a graph instance
g = graph(edges)

# Print all paths from Mumbai to Bangalore
print("All paths:", g.get_path("Mumbai", "Bangalore"))

# Print the shortest path from Mumbai to Bangalore
print("Shortest path:", g.Shortest_path("Mumbai", "Goa"))
