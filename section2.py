

''' Multi-Line Statements and Strings '''

#Multi-Line Strings
#You can create multi-line strings by using triple delimiters

#Multi Line Comment
# this is
# a multi-line
# comment

''' Conditionals'''
a = int(input("please enter your age"))
if a >= 18:
    print('you are an adult and you can have driving licence')
else:
    print('you are under 18 so you can not have an license')

#use of elif
a = int(input("please enter your age"))
if a >= 18:
    print('College Student')
elif a >= 13:
    print('Highschool Student')
else:
    print('Primary Student')

#if nested
a = int(input("please enter your order value"))

if a >= 100:
    print('you can have 20% discount if your order size is more than 100')
else:
    if a < 75:
        print('you can have 15% discount if your order size is more than 75')
    else:
        print('you can have 10% discount if your order size is less than 75')

''' functions and while loop'''
# Program of a simple calculator

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y


print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter choice(1/2/3/4): ")

    # Check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        break
    else:
        print("Invalid Input")

# Use of break statement 
for val in "Section":
    if val == "o":
        break
    print(val)

print("The end")

# Use of continue statement
for val in "section":
    if val == "o":
        continue
    print(val)

print("The end")

'''Try Statement'''
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

a = int(input("enter number"))
b = int(input("enter number"))
try:
    a / b
except ZeroDivisionError:
    print('division by 0')
finally:
    print("you have given number in correct way")
    print(a/b)

'''for loop'''
for i in range(5):
    print(i)

for x in 'hello':
    print(x)

