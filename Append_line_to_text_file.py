#r = read mode (shows code without modifacations)
#a = append mode (adds new text to the end of whats already there)
#w = wrote mode(next lesson)
file = open("report.txt","a")
file.write("Quote was said by Gandhi")
file.close() 

file = open("report.txt","r")
print(file.read())
file.close()