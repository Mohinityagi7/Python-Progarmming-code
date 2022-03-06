#take two comma separated input from user
# 1.) User's name, example, "Harshit"
# 2.) a single character, "H"

# Output:- 2 print lines
# 1.) user's name length
# 2.) count the character that user inputed (bouns : case insensitive count)
# name = input("Enter the comma separated name : ").split(",")
# char = input("Enter the comma separated character: ").split(",")
# print(f"length of your name is {len(name)}")
# print(f"character count :{name.count(char)}") #Case senstive

# print(len(name))
# print(name.count(char))

name = input("Enter the comma separated name and character : ").split(",")
char = input("Enter the comma separated name and character : ").split(",")
print(f"length of your name is {len(name)}")
print(f"character count :{name.lower().count(char.lower())}") #Case senstive