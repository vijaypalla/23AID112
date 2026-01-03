import random
numbers = [random.randint(1, 100) for _ in range(8)] # Create a list of 8 random integers between 1 and 100
print("List:", numbers)

# Find biggest number using loop
biggest = numbers[0]
for num in numbers:
    if num > biggest:
        biggest = num

# Find smallest number using loop
smallest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num

print("Biggest number:", biggest)
print("Smallest number:", smallest)