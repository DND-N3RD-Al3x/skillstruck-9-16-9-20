cols = [2, 5, 10, 100]

rows = [int(n) for n in input("Input a list of numbers: ").split()]

result = [[row - col for col in cols] for row in rows]

print(result)
