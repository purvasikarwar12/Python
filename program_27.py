while (1):
    print("\nEnter a number (<=100) to find its Square.")
    print("Press 0 to exit : ")
    num =int(input())
    if num == 0:
        print("Program's End. Thank You")
        break
    elif num > 100:
        print("Number is greater that 100. Try again.")
        continue
    print("\nSquare of ", num, "is", num * num)


#OUTPUT:-

 #Enter a number (<=100) to find its Square.
 #Press 0 to exit : 
 #3
 
 #Square of 3 is 9
 
 #Enter a number (<=100) to find its Square.
 #Press 0 to exit : 
 #0
 #Program's End. Thank You