# import in python
import random

#no need to declare variables, start using them
number = random.randint(16,377)

#print in python
print(number)

# Prompt the user to enter their name
name = input("Enter your name: ")

# Greet the user
print("Hello, " + name + "! Welcome to Python.")

#defining function in python
def function(a,b) : 
    return a + b

#calling function 
numberr = function(1,3)
print(numberr)

#if-else statements
if name=="sania":
    print("Hello "+name )
else:
    print("Imposter detected")
    
#TYPES
number1 = 23.334
print(number1)
print(type(number1))
print(type(number))
print(type(name))

#length calculation
print(len(name))

paragraph = """ Download this comprehensive guide to data analytics and embark on your journey towards data-driven success. Don't let valuable insights slip through the cracks—start making informed decisions based on data.
In today's competitive landscape, harnessing the power of data is essential for businesses to stay ahead. By unlocking valuable insights and making informed decisions based on data, you can gain a competitive edge and drive growth. Don't miss out on this opportunity to supercharge your business and maximize its potential. Arm yourself with the knowledge and tools provided in this guide to help your business transform into a data-driven powerhouse."""

print(paragraph)

print(type(False))

x = None
print(x)
print(type(None))

age_as_str = "233"
print(type(age_as_str))

#casting
age = int(age_as_str)
print(type(age))

#functions
def hello():
    return "Helllooooooo Worldddd"

result = hello()
print(result) 

#functions
def empty():
    print("I am not returning anything I am none")

result = empty()
print(result) 

def add(a,b):
    return a+b

result = add(2.4,1)
print(result)

#function accepting variable number of arguments
def summations(*arguments):
    return sum(arguments)

print(summations(1,2,4,3))
print(summations(1))

#operators
print(3*2) #"Multiplication"
print(3**2) #"Exponential"
print(11%7) #"Modulus"
print(6/2) #"Division"
# print(5>"alpha") type error
print(True and True)
print(True and not True)
print(True and not False)
print(False or True)

days = 28
#Control Flow
if(days>=30):
    print("its 30+")
elif(days>=28):
    print("its febrauary")
else:
    print("it could be any month")
    
#loops
#for loop
names = ['sania','zain','fatima','uzma','nisar']
print("Names of my Family Members is as follows")
for name in names:
    print(name)
    
#while loop
count = 0
while count<=10:
    print("Counting....")
    count+=1
    
#collections
#lists
l = [3,'alpha',True]
print(len(l))
print(l[-1]) #accesing last element
print(l[-2]) #accesing second last element

#appending in list
l.append('Python')
print(l[-1])
print(l)
print('Python' in l)

#tuples
t = (2,'BYE WORLD',False)
print(len(t))
print(t[-1]) #accesing last element
print(t[-2]) #accesing second last element
print('Python' in t)
# t.append('Python') not possible in tuples they are immutable - cant be modified

#dictionaries = maps like collections (unorderd,mutable)
