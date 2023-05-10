string = "laxman menam"
output = ""

for i in range(len(string)):
    if i % 2 == 0:
        output += "@"
    else:
        output += string[i]

print(output)


