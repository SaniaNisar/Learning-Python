class Dog:
    def __init__(self, name):
        self.name = name
        
    def bark(self): 
        print(f"{self.name} says Woof!") 

my_dog = Dog('Dobbie')

# Print the class name
print(Dog.__name__) 

# Call the `bark` method on the instance
my_dog.bark() 
