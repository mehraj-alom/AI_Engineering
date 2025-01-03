import time
# class Tree:
#     def __init__(self,data):
#         self.data = data 
#         self.children = []
#         self.parent = None
#     def add_child(self,child):
#         self.parent = self
#         self.children.append(child)
#     def print_tree(self):
#         print(self.data)
#         for child in self.children:
#             time.sleep(0.2)
#             child.print_tree()
#             time.sleep(0.4)
# def build_pro_tree():
#     root = Tree("Electronics")
#     laptop = Tree("Laptop")
#     smartphone = Tree("Smartphone")
#     tv = Tree("TV")

#     root.add_child(laptop)
#     root.add_child(smartphone)
#     root.add_child(tv)

#     # Second level
#     laptop.add_child(Tree("Acer"))
#     laptop.add_child(Tree("Lenovo"))
#     laptop.add_child(Tree("Chromebook"))

#     smartphone.add_child(Tree("Micromax"))
#     smartphone.add_child(Tree("Redmi"))
#     smartphone.add_child(Tree("Samsung"))

#     tv.add_child(Tree("LG"))
#     tv.add_child(Tree("Motorola"))

#     root.print_tree()

# build_pro_tree()

# class Tree:
#     def __init__(self,data = None):
#         self.data = data
#         self.children = []
#         self.parent = None
#     def add_child(self,child):
#         child.parent = self
#         self.children.append(child)
#     def Get_level(self):
#         level = 0 
#         current = self
#         while current.parent:
#             level += 1
#             current = current.parent
#         return level
#     def print_tree(self):
#         level = self.Get_level()
#         prefix = "  " * level * 2 + " !--" if level>0 else ""
#         time.sleep(1)
#         print(prefix + self.data)
#         for child in self.children:
#             child.print_tree()
# def Build_product_tree():         
#     root = Tree("Electronics")
#     laptop = Tree("Laptop")
#     Smart_phones = Tree("Smart_phones")
#     Tv = Tree("TV")
#     root.add_child(laptop)
#     root.add_child(Smart_phones)
#     root.add_child(Tv)   
#     laptop.add_child(Tree("ACer"))        
#     laptop.add_child(Tree("Lenevo"))  
#     laptop.add_child(Tree("Chromebook"))  
#     laptop.add_child(Tree("TEchno"))  
#     Smart_phones.add_child(Tree("Nokia"))
#     Smart_phones.add_child(Tree("Motorola"))
#     Smart_phones.add_child(Tree("Samsung"))
#     Smart_phones.add_child(Tree("Realme"))
#     Tv.add_child(Tree("LG"))
#     Tv.add_child(Tree("TCL"))
#     root.print_tree()
# Build_product_tree()


# class Tree:
#     def __init__(self,name = None,des = None):
#         self.name = name 
#         self.des = des
#         self.down_line = []
#         self.up = None 
#     def add_downLine(self,name):
#         name.up = self
#         self.down_line.append(name)
#     def print_by_name(self):
#         level = self.get_level()
#         prefix = " " * level * 2 + "!__" if level > 0 else ""
#         time.sleep(3)
#         print(prefix + self.name)
#         for name in self.down_line:
#             name.print_by_name()
#     def print_by_designation(self):
#         level = self.get_level()
#         prefix = " " * level * 2 + "!__" if level > 0 else ""
#         print(prefix + self.des)
#         time.sleep(0.8)
#         for des in self.down_line:
#             des.print_by_designation()
#     def print_by_all(self):
#         level = self.get_level()
#         prefix = " " * level * 2 + "!__" if level > 0 else ""
#         time.sleep(0.9)
#         print(prefix + self.name + "(" + self.des + ")")
#         for down in self.down_line:
#             down.print_by_all()
#     def get_level(self):
#         level = 0 
#         current = self
#         while current.up:
#             level += 1
#             current = current.up
#         return level
# def build_the_tree():
#     Ceo = Tree("Nilupal","CEO")
#     Cto = Tree("Chinmay","CTO")
#     Insf_Head = Tree("Vishwa","Insfrastucture_Head")
#     Cloud_manager = Tree("Dhaval","Cloud_manager")
#     App_manager = Tree("Abhijit","App_manager")
#     Apl_head = Tree("Amir","Application Head")
#     Hr_Head = Tree("Gels","HR HEAD")
#     Rec_Manager = Tree("Peter","Recruit Manager")
#     Policy_manager = Tree("Waqar","Policy_manager")
#     Ceo.add_downLine(Cto)
#     Ceo.add_downLine(Hr_Head)
#     Cto.add_downLine(Insf_Head)
#     Cto.add_downLine(Apl_head)
#     Insf_Head.add_downLine(Cloud_manager)
#     Insf_Head.add_downLine(App_manager)
#     Hr_Head.add_downLine(Rec_Manager)
#     Hr_Head.add_downLine(Policy_manager)
    
#     Ceo.print_by_designation()
#     print("\n")
#     Ceo.print_by_name()
#     print("\n")
#     Ceo.print_by_all()


# build_the_tree()

class Tree:
    def __init__(self,name = None):
        self.name = name
        self.sub_location = []
        self.mainn_loc = None 
    def add_Sub_location(self,name):
        name.mainn_loc = self
        self.sub_location.append(name)
    def print_by_level(self,level):
        if self.get_level() > level:
            return
        prefix = " " * self.get_level() * 2 + "!__" if self.get_level() > 0 else ""
        time.sleep(0.7)
        print(prefix + self.name)
        if self.sub_location:
            for loc in self.sub_location:
                loc.print_by_level(level)        
    def get_level(self):
        level = 0
        current  = self
        while current.mainn_loc:
            level += 1
            current = current.mainn_loc
        return level


def build_product_tree():
    Global = Tree("Global")
    India = Tree("India")
    Gujrat = Tree("Gujrat")
    Ahmedabad = Tree("Ahmedabad")
    Baroda = Tree("Baroda")
    Karnataka = Tree("Karnataka")
    Bengaluru = Tree("Bengaluru")
    Mysore = Tree("Mysore")
    Usa = Tree("USA")
    New_Jersey = Tree("New_Jersey")
    princeton = Tree("princeton")
    trenton = Tree("Trenton")
    California = Tree("California")
    San_Francisco = Tree("San_francisco")
    mountain_view = Tree("Mountain view")
    palo_alto = Tree("Palo Alto")
    Global.add_Sub_location(India)
    Global.add_Sub_location(Usa)
    India.add_Sub_location(Gujrat)
    India.add_Sub_location(Karnataka)
    Usa.add_Sub_location(New_Jersey)
    Usa.add_Sub_location(California)
    Gujrat.add_Sub_location(Ahmedabad)
    Gujrat.add_Sub_location(Baroda)
    Karnataka.add_Sub_location(Bengaluru)
    Karnataka.add_Sub_location(Mysore)
    New_Jersey.add_Sub_location(princeton)
    New_Jersey.add_Sub_location(trenton)
    California.add_Sub_location(San_Francisco)
    California.add_Sub_location(mountain_view)
    California.add_Sub_location(palo_alto)
    
    Global.print_by_level(1)
    time.sleep(0.4)
    print("\n")
    Global.print_by_level(2)
    time.sleep(0.4)
    print("\n")
    Global.print_by_level(3)
build_product_tree()