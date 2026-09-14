# Initialize empty list
number = []

# Collect 10 integers from user
print("Enter 10 integers:")
for i in range(10):
    val = int(input(f"Enter integer {i+1}: "))
    number.append(val)

# Calculate sum and average
total_sum = 0
for num in number:
    total_sum += num

average = total_sum / len(number)

# Display results
print("List:", number)
print("Sum:", total_sum)
print("Average:", average)
