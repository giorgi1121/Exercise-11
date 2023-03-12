#create variable and remove whitespaces
str = input("What is the input string? ").strip()

#count length of string
chars = len(str)

#print how many characters are in string
if str == "":
    print("You have to write something")
else:
    print(f"{str} has {chars} characters")
