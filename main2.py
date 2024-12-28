file = open("Hanzla.txt",  "r")
print("File is in reading mode")
print(file.read())
file.close()

file = open("Hanzla.txt",  "w")
file.write("File is in writing mode ")
file.write("Hi am Hanzla And I am 11 years old")
file.close()

file = open("Hanzla.txt",  "a")
file.write("\n File is in append mode ")
file.write("Hi am Abuzar And I am 5 years old")
file.close()