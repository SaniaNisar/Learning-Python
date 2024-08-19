print('Print Statement')
print('Two lines in','one row')

alpha =  'variable-string'
num_variable = 233

print('Printing string', alpha)
print('Printing numeric variable', num_variable)

num = 790
if num > 200:
    print("Number was greater than or equal to 200")
elif num > 150:
    print("Number was equal to or greater than 150")
else:
    print("Number was less than or equal to 150")

print("For Loop implementation")
i=0 
for i in range(10):
    print(i+1)
   
print("While Loop implementation") 
j = 20
while j >= 10:
    print(j)
    j -= 1
    
def add(a, b):
    return a + b

square = lambda x: x * x

num = add(1,2)
print('Function to add numbers',num)

num = square(5)
print('Lambda function', num)

# Using lambda with map
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)

# Using lambda with filter
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

arr = ['alpha','beta','charlie']
print('Data Structures - String Array', arr)

arr = [1,2,'3']
print('Data Structures - Number + String Array', arr)

arr = [1,2,3]
print('Data Structures - Number Array', arr)

squares = [x**2 for x in range(10)]
print('creating iterable lists',squares)

# Dictionaries - Objects
obj = {
    'name': 'John',
    'age': 12,
    'city': 'New York'
}

print("Dictionaries/Objects", obj)

my_set = {1,3,8,10}
print("Sets:", my_set)

my_tuple = (1,2, 3)
print('Tuples:',my_tuple)

# List of tuples
pairs = [(1, 'one'), (2, 'two'), (3, 'three')]

# Sort by the second element in each tuple
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)

# Error and Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("Error: Cannot divide by zero!")
else:
    print("Division successful:", result)
finally:
    print("This block always runs.")
    
#Generators
def countdown(n):
    while n > 0:
        yield n
        n -= 1

for number in countdown(5):
    print(number)
 
#Decorators -  Modify the behavior of a function or class method.   
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello I am a function!")

say_hello()

#Regular Expressions (regex) - Find patterns in strings
import re
pattern = r"\d+"
text = "There are 123 apples"
match = re.findall(pattern, text)
print(match)  # Output: ['123']

