answer = input("somthing: ")
file = open("email.txt","w")
file.write(answer)
file.close()

file = open("email.txt","r")
print(file.read())
file.close()