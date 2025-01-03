import time
class Electronic:
    def __init__(self,Pro_name,Year_of_launch,size,warrenty):
        self.pro_name = Pro_name
        self.year_of_launch = Year_of_launch
        self.size = size
        self.warrenty = warrenty
class Laptop(Electronic):
    def __init__(self, Pro_name, Year_of_launch, size, warrenty):
        super().__init__(Pro_name, Year_of_launch, size, warrenty)
    def more_details(self):
        pass
    def insert(self,list):
        a = Laptop()
        
    def print(self):
        print("Product Name ",self.pro_name,",YOL ",self.year_of_launch,",Size ",self.size,",warrenty ",self.warrenty)
class Mobile(Electronic):
    def __init__(self, Pro_name, Year_of_launch, size, warrenty):
        super().__init__(Pro_name, Year_of_launch, size, warrenty)
    def more_details(self):
        pass
    def print(self):
        print("Product Name ",self.pro_name,",YOL ",self.year_of_launch,",Size ",self.size,",warrenty ",self.warrenty)
class vehicle(Electronic):
    def __init__(self, Pro_name, Year_of_launch, size, warrenty):
        super().__init__(Pro_name, Year_of_launch, size, warrenty)
    def more_details(self):
        pass
    def print(self):
        print("Product Name ",self.pro_name,",YOL ",self.year_of_launch,",Size ",self.size,",warrenty ",self.warrenty)
# Exercise: Inheritance
# create inheritance using animal Dog relation.
# for example, 
#     Animal and Dog both has same habitat so create a method for habitat 
# use super() constructor for calling parent constructor.
# class Animal:
#     #code

# class Dog(Animal):
#     super()-it refers Animal class,now you can call Animal's methods.  
class Animal:
    def __init__(self,habitat):
        self.habitat = habitat
    def ret_habitat(self):
        return self.habitat
class Dog(Animal):
    def __init__(self):
        super().__init__("Street")
    def sound(self):
        self.sound = "Bow"
        return self.sound
class Cat(Animal):
    def __init__(self):
        super().__init__("street 2 ")
    def sound(self):
        self.sound = "Meow"
        return self.sound 
            
      
    
if __name__ == "__main__":
    # M = Mobile()
    # V = vehicle()
    listt = [["Asus","2021","14 inch","5 year"],["Lenevo","2023","15.5 inch","1 year"],["Infinix","2018","14 inch","6 year"],["Nokia","2024","16 inch","8 year"]
            ,["Samsung","2016","14 inch","5 year"],["Acer","2024","14 inch","2 year"]]
    laptops = []
    for item in listt:
        laptops.append(Laptop(*item))
    for laptop in laptops :
        laptop.print()
        # time.sleep(0.6)
    print("\n")
    mobiles = [
        ["iPhone 13", "2021", "6.1 inch", "1 year"],
        ["Samsung Galaxy S22", "2022", "6.6 inch", "1 year"],
        ["OnePlus 9", "2021", "6.55 inch", "1 year"],
        ["Google Pixel 7", "2022", "6.3 inch", "1 year"],
        ["Redmi Note 12", "2023", "6.4 inch", "1 year"],
        ["Vivo X80", "2022", "6.78 inch", "2 year"],
        ["Oppo Reno 8", "2022", "6.5 inch", "1 year"],
        ["Realme GT", "2023", "6.4 inch", "1 year"],
        ["Motorola Edge 30", "2022", "6.7 inch", "1 year"],
        ["Sony Xperia 1 IV", "2022", "6.5 inch", "1 year"],
        ["iPhone 14", "2023", "6.1 inch", "1 year"],
        ["Samsung Galaxy Z Flip", "2023", "6.7 inch", "1 year"],
        ["Huawei Mate 50", "2022", "6.7 inch", "1 year"],
        ["Asus ROG Phone 6", "2023", "6.78 inch", "1 year"],
        ["Nokia XR20", "2021", "6.67 inch", "2 year"]
    ]
    Mobile_list = []
    for item in mobiles:
        Mobile_list.append(Mobile(*item))
    for mobile in Mobile_list:
        mobile.print()
        # time.sleep(0.8)
    print("\n")
    vehicles = [
        ["Tesla Model 3", "2023", "Compact", "8 year"],
        ["Toyota Corolla", "2022", "Sedan", "3 year"],
        ["Honda Civic", "2021", "Sedan", "3 year"],
        ["Ford Mustang", "2023", "Sports", "5 year"],
        ["Chevrolet Bolt", "2022", "Hatchback", "8 year"],
        ["BMW X5", "2023", "SUV", "4 year"],
        ["Audi Q7", "2023", "SUV", "4 year"],
        ["Mercedes-Benz C-Class", "2023", "Sedan", "4 year"],
        ["Volkswagen Passat", "2022", "Sedan", "3 year"],
        ["Hyundai Sonata", "2023", "Sedan", "3 year"],
        ["Jeep Wrangler", "2023", "SUV", "5 year"],
        ["Nissan Leaf", "2021", "Hatchback", "8 year"],
        ["Porsche Taycan", "2023", "Sports", "5 year"],
        ["Range Rover Evoque", "2023", "SUV", "4 year"],
        ["Subaru Outback", "2022", "Wagon", "3 year"]
    ]
        
    vehicle_list = []
    for item in vehicles:
        vehicle_list.append(vehicle(*item))
    for item in vehicle_list:
        item.print()
        time.sleep(0.3)  
        
c = Cat()
d = Dog()
print(c.ret_habitat())
print(c.sound())
print(d.ret_habitat())
print(d.sound())

