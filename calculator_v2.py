#!/usr/bin/env python3

# Calculator V2 - ACG Intro to Python Scripting Chapter 5

def add(num1, num2):
        return num1 + num2

def subtract(num1, num2):
        return num1 - num2

def multiply(num1, num2):
        return num1 * num2

def divide(num1, num2):
        if num2 == 0:
                print("Can't divide by 0")
                return
        else:
                return num1 / num2

operation = -1
while operation != 0:
        print("CALCULATOR PROGRAM")
        print("Select operation:")
        print("0 - quit, 1 - add, 2 - subtract, 3 - multiply, 4 - divide")
        operation = int(input("What operation do you want to perform? "))
        
        if operation == 0:
                print("Ending program..")
        else:
                num1 = int(input("Enter num1: "))
                num2 = int(input("Enter num2: "))
                if operation == 1:
			result = add(num1, num2)
                        print(result)
                elif operation == 2:
                        result = subtract(num1, num2)
                        print(result)
                elif operation == 3:
                        result = multiply(num1, num2)
                        print(result)
                elif operation == 4:
                        if num2 == 0:
                                print("Can't divide by 0")
                        else:
                                result = divide(num1, num2)
                                print(result)
                else:
                        print("Operation not recognized...")