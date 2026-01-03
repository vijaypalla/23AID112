# Create list of numbers from 1 to 20
numbers = list(range(1, 21))
for num in numbers: 
    if num %3 == 0:   # Print numbers divisible by 3
        print(num)