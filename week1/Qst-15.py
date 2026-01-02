# Given list
numbers = [12, 45, 3, 98, 7, 34, 21]

# a) Print each number
print("All numbers:")
for num in numbers:
    print(num,end=' ')

# b) Print only numbers greater than 30
print("\nNumbers greater than 30:")
count = 0
for num in numbers:
    if num > 30:
        print(num,end=' ')
        count += 1
print(f"\nCount of numbers greater than 30: {count}")  # c) Count how many numbers are greater than 30


