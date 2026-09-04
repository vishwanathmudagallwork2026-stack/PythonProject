#Operators in Python
#1) Arithmetic Operator
#2) Comparison Operator
#3) Assignment Operator
#4) logical Operator
#5) bitwise Operator
#6) -----


#1) Arithmetic Operators
#(+, -, *, /, //, **, %)
a = 10
b = 2
print("a + b: ", a + b)
print("a - b: ", a - b)
print("a * b: ", a * b)
print("a / b: ", a / b)
print("a // b: ", a // b)
print("a % b: ", a % b)
print("a ** b: ", a ** b)
print("----------------")


#2) Comparison Operators
print("a > b: ", a > b)
print("a < b: ", a < b)
print("a >= b: ", a >= b)
print("a <= b: ", a <= b)
print("a == b: ", a == b)
print("a != b: ", a != b)

#Logical Operators
#(and, or,  not)
#and --> it returns True, if the both statements/oeprands are True
#or ---> it returns True, if any of the statement is True
#not ---> It reverses the False, when both statements are False

#and
# age = 20
# income = 85000
# if age >= 18 and income > 60000:
#     print("You are good")
# else:
#     print("You are bad")

# has_id = True
# has_ticket = True
# can_enter = has_id and has_ticket
# print("It returns: ", can_enter)
# print("It returns: ", can_enter)
#
# print(3 and 5) #it returns the last value
#
#
# has_premium = True
# cart = 45
#
# has_id = True
#
#
# if (has_premium and cart > 50) or (has_id):
#     print("You are eligible for subscription")
# else:
#     print("You are not eligible for subscription")
#
#
# is_raining = True
# temperature = 25
# is_weekend = True
#
# result1 = ((is_raining and temperature > 20) and is_weekend)
# if result1:
#     print("today is good day for outdoor activities")
# else:
#     print("today is not good day for outdoor activities")

#Assignment Operators
x = 5
x += 6
print(x)

#(+=) --> add and assign
#suppose i have 5000 in my bank account. and i need to add the 2000
balance = 5000
balance += 2000
print("The total amount after added to bank account will be: ", balance) #7000

#(-=) --> subtract and assign
#if i have 10000 in my bank account, i need to withdraw the 3000
balance1 = 10000
withdraw = 3000
balance1 -= withdraw
print("the total amount after the withdrawl will be: ", balance1) #remaining balance will be 7000

#(*=) ---> multiply and assign
#the employee has a salary of 30000 per month. the salary will increases 4.5 times the old salary.
salary = 30000
salary *= 4.5
print("the updated salary is: ", salary)

#(/=)---> divide and assign
#the teacher distribute the 100 question paper to students.
# for each student getting atleast 2 papers. the total number of student
#is 25. what is the total question papers will be left?

# total_papers = 100
# students = 25
# total_papers -= (students* 2)
#
# print("The question paper left is: ", total_papers)
#

#(%=) --> Modulus and Assign

#Initialize the  number
number = 20

#Apply modulus and assign
number %= 10
print("the modulus of the given number is: ", number)













