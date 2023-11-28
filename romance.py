# Function to add two numbers
def add_numbers(num1, num2):
    result = num1 + num2
    return result

# Taking input from the user
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Calling the function and printing the result
sum_result = add_numbers(number1, number2)
print(f"The sum of {number1} and {number2} is: {sum_result}")
