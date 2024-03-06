import random

number = random.randint(0,10)

threshold = 6
threshold2 = 4

if number < threshold:
    print("small number")
elif number > 4:
    print("Big Number")
else:
    print("Number is 7")
    
if number < threshold2:
    print("really small number")
    
print("dedented")
print(number)
    