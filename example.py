# Function to add three numbers
def add_numbers(num1, num2, num3):
    return num1 + num2 + num3

# Get input from the user
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))

# Calculate the sum
sum_result = add_numbers(number1, number2, number3)

# Display the result
print(f"The sum of {number1} and {number2} and {number3} is: {sum_result}")
