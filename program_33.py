number = int(input("Enter any number: "))
if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
             print(number, "is not a prime number")
             break
    else:
        print(number, "is a prime number")
else:
     print(number, "is not a prime number")


#OUTPUT:-

 #Enter any number: 3
 #3 is a prime number