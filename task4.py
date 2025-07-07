#1. Write a Python program to create a basic calculator that performs the following 
#operations: 
#• Addition 
#• Subtraction 
#• Multiplication 
#• Division 
#Requirements: 
#The program should take two numbers as input from the user. 
#The program should ask the user to choose the operation (+, -, *, /). 
#Based on the user’s choice, perform the corresponding arithmetic operation. 
#Handle division by zero error gracefully with a proper message. 
#The program should display the result clearly.num1 = float(input("Enter the first number: "))
num1=float(input("Enter the first number:"))
num2 = float(input("Enter the second number:"))
print("Choose the operation: + for addition, - for subtraction, * for multiplication, / for division")
operation = input("Enter operation (+, -, *, /): ")
if operation == '+':
    result = num1 + num2
    print("Result:", result)
elif operation == '-':
    result = num1 - num2
    print("Result:", result)
elif operation == '*':
    result = num1 * num2
    print("Result:", result)
elif operation == '/':
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        print("Result:", result)
else:
    print("Invalid operation selected.")

#2. Write a Python program to print the first N terms of the Fibonacci series using a while loop.
n=int(input())
a,b=0,1
count=0
while count<n:
    print(a,end=" ")
    a,b= b,a+b
    count+=1

#3. Write a program to check whether a number is an Armstrong number using a while loop. 
#Example: 153 → 1³ + 5³ + 3³ = 153 
n=int(input())
num=n
res=0
res1=len(str(n))
while n>0:
    digit=n%10
    res+=digit**res1
    n//=10
if res==num:
    print(num,"is an Armstrong number.")
else:
    print(num,"is not an Armstrong number.")

#4. Write a program to find the greatest digit in a given number using a while loop.
n=int(input("Enter a number: "))
max_digit=0
while n>0:
    digit=n%10
    if digit>max_digit:
        max_digit=digit
    n//=10
print("The greatest digit is:",max_digit)

#5. Write a program to find  greatest(a, b, c) to find the greatest of three numbers.
a=float(input("Enter first number:"))
b=float(input("Enter second number:"))
c=float(input("Enter third number:"))
if a>=b and a>=c:
    greatest=a
elif b>=a and b>=c:
    greatest=b
else:
    greatest=c
print("The greatest number is:",greatest)

#6. Write a function sum_numbers(*args) that accepts any number of arguments and returns their sum. 
def sum_numbers(*args):
    return sum(args)
print(sum_numbers(10,20,30))
print(sum_numbers(15,25,35,40))
print(sum_numbers())

#7. Write a function display_info(**kwargs) that prints all key-value pairs passed as arguments.
def display_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
display_info(name="Pooji",age=23,city="Hyderabad")

#8. Write a Python program to calculate the sum of elements present at even indices and odd indices separately 
def sum_even_odd_indices(lst):
    even_sum=0
    odd_sum=0

    for i in range(len(lst)):
        if i%2==0:
            even_sum+=lst[i]
        else:
            odd_sum+=lst[i]

    print("Sum of elements at even indices:",even_sum)
    print("Sum of elements at odd indices:",odd_sum)

#9. Write a Python program to double all even numbers in the same list without creating a new list. 
#Conditions: 
#You must modify the list in-place. 
#Odd numbers should remain unchanged.
lst=[1,2,5,8,10,14,17,20]
for i in range(len(lst)):
    if lst[i]%2==0:
        lst[i]*=2
print("Modified list:",lst)

#10. Modify the list such that all even numbers are halved, odd numbers remain unchanged. 
#Example: 
#Input: [4, 7, 8, 3] → Output: [2, 7, 4, 3] 
lst=[10,20,30,40]
for i in range(len(lst)):
    if lst[i]%2==0:
        lst[i]=lst[i]//2
print("Modified list:",lst)

#11. Check given number is perfect number or not ? 
n=int(input())
total=0
for x in range(1,n):
    if n%x==0:
        total+=x
if n==total:
    print('Perfect number')
else:
    print('Not Perfect number')

#12. Write a Python program that takes a sentence as input and separates the uppercase and lowercase letters from the sentence. 
sentence=input("Enter a sentence: ")
uppercase_letters=""
lowercase_letters=""
for char in sentence:
    if char.isupper():
        uppercase_letters+=char
    elif char.islower():
        lowercase_letters+=char
print("Uppercase letters:",uppercase_letters)
print("Lowercase letters:",lowercase_letters)
