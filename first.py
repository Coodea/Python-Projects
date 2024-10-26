name = input("Please Enter Your Name: ")
print("Hello "+name)

birth_year = input("Please Enter Your Birth Year: ")

'''
The following code will product an error due to attempting to subtract a int from a string
age = 2024-birth_year
print(age)
'''
#to fix this we must convert the birth year to an int
age = 2024-int(birth_year)
print(age)

#below is all the built in conversion commands
'''
int()
float()
bool()
str()
'''




#simple sum calc
Num1 = input("FirstNum: ")
Num2 = input("SecondNum: ")
sum = float(Num1)+float(Num2)
print("sum: ", sum)




#Strings
course = 'Python for beginneers'
#Each letter has an index starting a 0
print(course.upper())
print(course)
print(course.lower())
print(course.find('y'))
#If the letter isnt present it will print -1
print(course.find('Y'))

#When using the find command on a string of chars the index giving will be when the first char is found
print(course.find('for'))

print(course.replace('for','4'))
#if you try to replace a character/string that isnt present nothing happens
print(course.replace('x','4'))

#in will either display True or False
print('Python' in course)




#Arithmetic OPS
print(13+3)
print(13-3)
print(13*3)
# / will give float number
print(13/3)
# // will give an int
print(13//3)
# % will give the remainder, its known as modulos
print(13%3)
# ** will be exponential op
print(13**3)

x=10
x = x+3
x += 3 # this will do the same thing as the pervious line and can be done with all the arithmetic ops
#This follows Pemdas so it can be changed via parenthesis
y = 10+3*2
y2 = (10+3)*2




#Comparison OPS
x = 3<1
print(x)
x = 3>1
print(x)
x = 3==1
print(x)
x = 3!=1
print(x)




#Logical OPS
price = 25
# The 'and' operator will produce true if both boolean expressions are true
print(price >10 and price<30)
# The 'or' operator will produce true if either one of the boolean expressions are true
print(price >10 or price < 5)
#You can also have a one way expression
print(price >10)
# The 'not' operator will provide true when the boolean expression is false
print(not price<10)




# If statements
temp = 35
if temp > 35:
    print("Its a hot day")
    print("Drink plenty of water")
elif temp>20:
    print("Its a nice day")
elif temp>10:
    print("Its a bit cold")
else:
    print("Its cold")
print("Done")




#Exercise
weight = input("Please Enter weight: ")
weight_Unit = input("(K)g or (L)bs: ")
if weight_Unit == 'l' or weight_Unit == 'L':
    kg = float(weight)*.45
    print("Weight in Kg", kg)
elif weight_Unit == 'k' or weight_Unit == 'K':
    lbs = float(weight)/.45
    print("Weight in Lbs", lbs)
else:
    print("ERROR, wrong weight unit input")




# While Loops

i = 1
while i <= 5:
    print(i)
    i += 1
#This will print out the symbol on the line for the amount of time being whatever number i is at
y = 1
while i <= 5:
    print(i*'*')
    i = i +1




# List
#print(names[-1]) the index -1 will go reverse so it will print mary
names = ["John", "Bob", "Mosh", "Sam", "Mary"]
name[0]="jon"
print(names)
print(names[0])
print(names[-2])
print(names[0:3])




# List Methods

numberList = [1, 2, 3, 4, 5]
numberList.append(6)
# Append will add the number at the end of the list 
print(numberList)

numberList.insert(0, -1)
# Insert at a index which in this case is 0 and the number to insert which was -1

numberList.remove(3)
# Remove will do this obvious and remove the item

numberList.clear()
# clear will remove the items in the list

# To check for a num in the list you can do Ex for 1; print(1 in numberList)
print(1 in numberList)

# To find the length of a list you can us len()
print(len(numberList))



# For Loops

numberList2 = [1, 2, 3, 4, 5]
print(numberList2)

# For Loop that uses the num of items in the list to loop through the list and print each item
for item in numberList2:
    print(item)

i = 0
while i < len(numberList2):
    print(numberList2[i])
    i = i+1




# Range() Function

numbers = range(5)
print(numbers)

for number in numbers:
    print(number)

number = 0
numbers2 = range(5, 10)
for number in numbers2:
    print(numbers2)

number = 0
# the 3rd variable in range(x,y,z) is the amount to jump like 2 would be 5 7 9
numbers3 = range(5, 10, 2)
for number in numbers3:
    print(number)

number = 0

# You can use Range in th for loop
for number in range(5):
    print(number)



# Tuples

numbers4 = (1, 2, 3, 3)
#tuples use () instead of [] so trying to reassign numbers[0] = 10 wont work as tuples are unchangable 
numbers4.count(3)# this will check the list and count the amount of 3's in the list and in this instance will produce 2

