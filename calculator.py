#!/usr/bin/env python3

def calculate(num1, num2, OP):
	if OP == 1:
		RESULT = num1 + num2
	elif OP == 2:
		RESULT = num1 * num2
	elif OP == 3:
		RESULT = num1 - num2
	elif OP == 4:
		if num2 == 0:
			print("Can't divide by 0")
		else:
			RESULT = num1 / num2
	else:
		print("Operation not recognized")
	print(RESULT)

print("Calculator program")
number1 = int(input("Enter num1: "))
number2 = int(input("Enter num2: "))
print("Operations: 1 - add, 2 - multiply, 3 - subtract, 4 - divide")
operation = int(input("What operation to perform: "))

calculate(number1, number2, operation)