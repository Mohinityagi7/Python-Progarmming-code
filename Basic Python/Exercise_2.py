# Ask user to input 3 numbers and you have to print average of three numbers using string formatting
# Bonus :- try to take all three comma separated inputs inone line.

name1 = input("Enter first number :")
name2 = input("Enter Second number :")
name3 = input("Enter Third number :")
name1,name2,name3 = input("Enter three numbers comma separated: ").split(",")
#(int(name1)+int(name2)+int(name3))/3
print(f"average of three numbers :{( int(name1) + int(name2) + int(name3)) / 3}")