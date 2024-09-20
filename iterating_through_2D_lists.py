x = int(input("What is the first number?"))

y = int(input("What is the second number?"))

z = int(input("What is the third number?"))

my_list = [[0, 1, x], [10, 15, y], [100, 200, 300], [5, 6, z]]
largest_number = my_list[0][0]

for row in my_list:
    for element in row:
        if element > largest_number:
            largest_number = element
print(largest_number)