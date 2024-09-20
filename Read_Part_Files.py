file = open("test.txt", "r")

ply = file.read()

andrew = ply.split()

print(len(andrew))

file.close()