file = open("Hanzla.txt")
Counter = 0

Content = file.read()

Colist = Content.split("\n")

for i in Colist:
    if i:
        Counter = +1

print("This is the number of lines in the files")
print(Counter)
