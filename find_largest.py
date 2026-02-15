# Find the largest number
print("=" * 40)
print("Find the Largest Number")
print("=" * 40)
# Ask user how many numbers they want to enter
count = input("How many numbers do you want to enter? ")
# Check if input is a number
if not count.isdigit():
    print("Please enter a valid number!")
else:
    count = int(count)
    if count <= 0:
        print("Number must be greater than zero!")
    else:
        numbers = []  # List to store numbers
        # Get numbers from user
        for i in range(count):
            num = input(f"Enter number {i+1}: ")
            # Check if it's a valid number (integer or float)
            try:
                numbers.append(float(num))
            except ValueError:
                print("That's not a number!")
                break
        else:
            # Find the largest number
            if numbers:  # If list is not empty
                largest = numbers[0]
                for num in numbers:
                    if num > largest:
                        largest = num
                print("\n" + "-" * 20)
                print(f"Largest number: {largest}")
                print(f"Numbers you entered: {numbers}")
                print("-" * 20)
            else:
                print("No numbers were entered!")

print("\nDone! 🎉")
