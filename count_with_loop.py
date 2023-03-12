#create variable and remove whitespaces
str = input("What is the input string? ").strip()

#count length of string
count = 0
for x in str:
    count += 1

#print how many characters are in string
if str == "":
    print("You have to write something")
else:
    print(f"{str} has {count} characters")
