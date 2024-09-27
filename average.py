def calculate_average():
    # Prompt the user to input numbers separated by spaces
    numbers = input("Enter numbers separated by spaces: ").split()

    # Convert the input into a list of floats
    numbers = [float(num) for num in numbers]

    # Calculate the average
    average = sum(numbers) / len(numbers)

    maxNum = max(num in numbers)
    minNum = min(num in numbers)
    return average

# Call the function and print the result
print("The average is:", calculate_average())

