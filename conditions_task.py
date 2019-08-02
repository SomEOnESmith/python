#this program creats a simple calc

def is_valid():
	number = input("Enter a number:   ")
	while (not number.isdigit()):
		number = input("invalid operand, Enter a number:   ")
	return int(number)

print("\t\t\t Welcome to the simple calculator program")

first_number = is_valid()
print ("the first number is " + str(first_number))
second_number = is_valid()
print ("the second number is " + str(second_number))
operator = input ("choose the operation (+, -, /, *):   ")


if operator == "+":
	result = first_number + second_number
elif operator == "-":
	result = first_number - second_number
elif operator == "*":
	result = first_number * second_number
elif operator == "/":
	if second_number == 0:
		result = "cannot devide by zero"
	else:
		result = first_number / second_number
else:
	print ("invalid operator ")


print ("Result = " + str(result))

