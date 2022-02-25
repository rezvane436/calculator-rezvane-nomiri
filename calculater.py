from math import *
print ("Hello welcome to calculator...")
def options():
    print("------------------------------------------------------------------")
    print("Options: ")
    print ("------------------------------------------------------------------")
    print("Enter '+' to add two numbers")
    print("Enter '-' to subtract two numbers")
    print("Enter '*' to multiply two numbers")
    print("Enter '/' to divide two numbers")
    print("Enter '**' to power two numbers")
    print("Enter '&' to square root ")
    print("Enter 'exit' to exit the calculator")
    print("------------------------------------------------------------------")

#divide function
def divide():
    try:
      num1, num2 = float(input("Enter first number: ")), float(input("Enter second number: "))
      result = num1 / num2
      print("The answer: ", result,"\n")
    except ZeroDivisionError:
      print ("Error: division by zero is not possible!")
      divide()
    finally:
        x = input ("wanna continue? (y/n) ")
        if x == "y" or x == "Y":
            divide()
        else:
            exit

#Add function
def add():
    try:
        num1,num2 = float(input("Enter first number: ")),float(input("Enter second number: "))
        result = num1 + num2
        print ("The answer: ",result,"\n")
    except:
        print ("An error ooccured!")
    finally:
        r = input ("wanna continue? (y/n) ")
        if r == "y" or r == "Y":
            add()
        else:
            exit
#Subtract function
def subtract():
    try:
        num1, num2 = float(input("Enter first number: ")), float(input("Enter second number: "))
        result = num1 - num2
        print("The answer: ", result,"\n")
    except:
        print ("An error ooccured!")
    finally:
        z = input ("wanna continue? (y/n) ")
        if z == "y" or z == "Y":
            subtract()
        else:
            exit

#Multiply function
def multiply():
    try:
        num1, num2 = float(input("Enter first number: ")), float(input("Enter second number: "))
        result = num1 * num2
        print("The answer: ", result,"\n")
    except:
        print ("An error ooccured!")
    finally:
        y = input ("wanna continue? (y/n) ")
        if y == "y" or y == "Y":
            multiply()
        else:
            exit

#Power function
def power():
    try:
        num1, num2 = float(input("Enter first number: ")), float(input("Enter second number: "))
        result = num1 ** num2
        print("The answer: ", result, "\n")
        del (result)
    except:
        print ("An error ooccured!")
    finally:
        a = input ("wanna continue? (y/n) ")
        if a == "y" or a == "Y":
            power()
        else:
            exit
#Square root function
def square_root():
    try:
        num1 = float(input("Enter Your number: "))
        result = sqrt(num1)
        print("The answer: ",result)
    except:
        print ("An error ooccured!")
    finally:
        b = input ("wanna continue? (y/n) ")
        if b == "y" or b == "Y":
            square_root()
        else:
            exit
#Base codes
while True:
    options()
    try:
        u_in = input("Enter Your command: ")
        if u_in == "exit" or u_in == "Exit" or u_in == "quit" or u_in == "Quit":
            print("Good bye!\n------------------------------------------------------------------")
            break
        elif u_in == "+":
            add()
        elif u_in == "-":
            subtract()
        elif u_in == "*":
            multiply()
        elif u_in == "/":
            divide()
        elif u_in == "**":
            power()
        elif u_in == "&":
            square_root()
        else:
            print ("check your input!\n")
    except:
        print ("An error ooccured!")

        #Show all errors
        raise