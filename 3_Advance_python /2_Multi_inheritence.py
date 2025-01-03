# Exercise: Raise Exception And Finally
# Create a custom exception AdultException.

# Create a class Person with attributes name and age in it.

# Create a function get_minor_age() in the class. It throws an exception if the person is adult otherwise returns age.

# Create a function display_person() which prints the age and name of a person.

# let us say,

# if age>18 
#     he is major
# else
#     raise exception

# create cusomException named ismajor and raise it if age<18.
class AdultException(Exception):
    def __init__(self, message = "She is minor"):
        self.message = message
        super().__init__(self.message)
class person():
    def __init__(self, name,age):
        self.name = name
        self.age = age 
    def Get_minor_age(self):
        if self.age <= 18:
            raise AdultException()
        else :
            return self.age
    def display_person(self):
        try :
            print("age :",self.Get_minor_age())
        except AdultException as e:
            print(e.message,"and ",end = " ")
        finally:
            print("Name is ", self.name)      
if __name__ == "__main__":
    per = person("Myname",4)
    per.display_person()
