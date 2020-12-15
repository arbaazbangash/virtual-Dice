import random

x="yes"

#using while loop for unknown range
while x=="yes":

    #Generate random number between the specific range by using random module
    num=random.randint(1,6)
    

    #using IF condition control statement
    if num==1:
        print("|----------|")
        print("|          |")
        print("|    O     |")
        print("|          |")
        print("|----------|")
    if num==2:
        print("|----------|")
        print("|          |")
        print("|   O  O   |")
        print("|          |")
        print("|----------|")
    if num==3:
        print("|----------|")
        print("|          |")
        print("|  O O O   |")
        print("|          |")
        print("|----------|")
    if num==4:
        print("|----------|")
        print("| O      O |")
        print("|          |")
        print("| O      O |")
        print("|----------|")
    if num==5:
        print("|----------|")
        print("| O      O |")
        print("|     O    |")
        print("| O      O |")
        print("|----------|")
    if num==6:
        print("|----------|")
        print("| O      O |")
        print("| O      O |")
        print("| O      O |")
        print("|----------|")

    x=input("yes to roll again and No to exit")
    
    print("\n")
