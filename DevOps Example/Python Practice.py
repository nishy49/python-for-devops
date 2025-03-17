#Print numbers from 1 to 10
#for i in range(1,121):
#print(i)

#Print even numbers from 1 to 20
#for i in range(2,21,2):
   # print(i)

#3)Sum of numbers
"""
sum_numbers =0
for i in range(1,11):
    sum_numbers += i
    print("Sum:", sum_numbers)
"""
from pycparser.ply.yacc import resultlimit

#4)Print numbers untilcondiiton is met
"""
x = 12
while x>1 :
    print(x)
    x += 1
"""
#5)While Loop: Reverse Counting
"""
x = 10
while x > 0:
     print(x)
     x -= 1
     """
#6) Loop Control: break Statement
"""
for i in range (1,10):
     if i == 5:
         break
     print(i)
"""
#7) Loop control :continuestatemtn
"""
for i in range (1,10):
    if i ==5:
        continue
    print(i)
"""
#8)Basic If Statement
"""
num =int(input("Enter a number: "))
if num > 5 :
    print("less tha five ")
else :
    print("the number is 5 or less")
"""
#9



    



""""
     
n=int(input("Enter a number:"))
if n%2==0:
    print("Number is even")
else:
    print("Number isodd")
    def addition(a,b):
    return (a+b)

result = addition(5,6)

if result ==11 :
    print("result is write")
else :
    print("result is wrong")

#Question: Write a Python program to check if a number is positive, negative, or zero using nested if statements.

n=int(input("Enter a number:"))
if n<0 :
    print("{n} is negative")
elif n==0:
    print("n is positive")
else:
 print("n is zero")

"""

"""
for i in range(10):
    print(i)

    num = 1  # Initialize the starting number

    while num <= 10:  # Loop runs while num is less than or equal to 10
        print(num)  # Print the current number
        num += 1
"""
"""
#Write a function that takes a number as input and returns whether it is even or odd.
def number(n):
    if n%2==0 :
        print("Number is even")
    else :
        print("Number is odd")
n =int(input("Enter a number :"))
number(n)

"""
#Write a function that takes a string and returns it in reverse order.
"""
def primenumber(n):
    if n<2 :
        print("Number is notprime")
        return
    for i in range (2,int(n ** 0.5) + 1):
        if n % i ==0:
            print("Number is not prime")
            return

n= int(input("Enter a number :").replace(",",""))
primenumber(n)
"""
"""
# Write a function that takes a list of numbers and returns the sum of all elements.
def addition_of_all_elements(df):
    df =["1","2","3","4","5"]
    print("sum of all numbers")
    addition_of_all_elements(df)
"""
"""
def sum_of_elements (numbers):
    return sum(int(num) for num in numbers)
numbers_list =[1,2,3,4,5,]
result = sum_of_elements(numbers_list)
print(result)
"""
"""
def sum_of_elements (numbers):
    return sum(int(num) for num in numbers)

user_input =input("Enter 5 numbers separted by spaces :")
numbers_list =user_input.split()

result =sum_of_elements(numbers_list)
print(result)
"""
"""
#Write a function that takes a string and returns it in reverse order.
def reverse_string(rs):
    return rs[::-1] #using slicing to reverse the string

user_input =input("Enter a string to reverse: ")
reversed_str =reverse_string(user_input)
print("rEVERSED STRING" ,reversed_str)
"""
"""
#FactorialFunctio
def factorial (n):
    result = 1
    for i in range (2, n+1):
        result *= i
    return result

num =int(input("Enter a number:"))


print(f"Factorial of {num} is {factorial(num)}")
"""
"""
def count_words(sentence):
    words =sentence.split()
    return len(words)
user_input =input("Enter a sentence ")

lengthis=count_words(user_input)
"""

"""
def largest_number(num):
    if not num:
     return None
    return max(num)

user_input =input("Enter a number separted by spaces =")
numbers_list =[int(num) for num in user_input.split(",")]

biggest_number =largest_number(numbers_list)

if biggest_number is not None:
    print(f"The largest number is :{biggest_number}")
else:
    print("The list is empty")
"""
"""
def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is even")
    else :
        print(f"{number} is odd")
num=int(input("Enter a number :"))
check_even_odd(num)
"""
"""
def divide_numbers (a,b):
    try:
        result=a/b
        print(f"Result :{result}")
    except ZeroDivisionError:
                print(f"Eror :Cannot divide by zero")
    except ValueError:
               print("Error inavlid input")

try:
  num1 = int(input("Enter a numerator:"))
  num2 = int(input("Enter a denominator "))
  divide_numbers(num1, num2)

except ValueError:
    print("Error :InvalidInput")
"""

"""
def open_file(filename):
    try:
        with open (filename,"r") as file:
         print(file.read())
    except FileNotFoundError:
        print("Error : File not found")
    finally:
        print("Execution completed")

open_file("example.txt")
"""
"""
def read_and_write (filename,content):
    try:
        with open(filename,"w") as file:
            file.write(content)
        print("File written successfully:")
    except Exception as e:
        print(f"Error : {e}")
    finally:
        print("Exectution Completed")
read_and_write("example.txt","Hello DeVops!,This is a test file")
"""
def append_to_file(filename,content):
    try:
        with open(filename,"a") as file:
         file.write("\n" + content)
        print("Content appended")
    except Exception as e:
        print(f"Error:{e}")
    finally:
        print("Exection completed")
append_to_file("exampless.txt","Hi new file created")



