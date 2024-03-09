import random

var = []

print(var)

print(type(var))

var2 = [151, 125, 251, 386, 493, 65, "beth"]

print(var2)

var2.append(721)

print(var2)

print(dir(var2))

print(dir("string"))

var3 = [0,1,2,3,4]

numbers = range(10)

print(numbers)
print(type(numbers))

numbers = list(numbers)

print(numbers)
print(numbers[4])

numbers.reverse()

print(numbers[4])

print(numbers.index(4))

print(numbers[5])

numbers.reverse()
print(numbers)

print(len(numbers))

for number in numbers:
    print(number**2)
    
for i in range(10):
    print(i**3)
    
list_of_lists = []
list_of_lists.append([0,1,2])
list_of_lists.append([0,1,2])
list_of_lists.append([0,1,2])
list_of_lists.append([0,1,2])

print(list_of_lists)

for list_element in list_of_lists:
    print(list_element)
    for element in list_element:
        print(element)
        

            


