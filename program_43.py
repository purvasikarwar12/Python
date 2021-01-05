
i = 1
sum = 0
n = int(input("Enter a number : "))
while i < n:
    if(n % i == 0):
        sum = sum + i
    i += 1
if sum == n:
    print(i, "is a perfect number")
else:
    print(i, "is NOT a perfect number")
    

#OUTPUT:-

#Enter a number : 6
#6 is a perfect number
