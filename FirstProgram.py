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
    
# Python
def add(a, b):
    return a + b

# Python
square = lambda x: x * x

num = add(1,2)
print('Function to add numbers',num)

num = square(5)
print('Lambda function', num)

arr = ['alpha','beta','charlie']
print('Data Structures - String Array', arr)

arr = [1,2,'3']
print('Data Structures - Number + String Array', arr)

arr = [1,2,3]
print('Data Structures - Number Array', arr)

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