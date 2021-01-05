n = int(input("Enter the nmumber:"))
num = n
sq = n*n
t = 10
equal = False
print("Square of", n , "is", sq)
while(n>0):
    r = sq % t
    if (num==r):
        equal = True
        break
    n = n//10
    t = t*10
if (equal):
    print(num, "is an Automorphic Number")
else:
    print(num, "is NOT an Automorphic Number")
    
#OUTPUT:-

#Enter a number : 25
#Square of 25 is 625
#25 is an Automorphic Number
