# Program to find the largest of 5 numbers

def find_largest_number():
    # Taking 5 numbers as input from the user
    numbers = []
    for i in range(1, 6):
        num = float(input(f"Enter number {i}: "))
        numbers.append(num)
    
    # Finding the largest number using the max() function
    largest = max(numbers)
    
    # Displaying the result
    print(f"The largest number among the entered numbers is: {largest}")

# Call the function to execute
find_largest_number()

