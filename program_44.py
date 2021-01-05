n = int(input("Enter the nmumber:"))
t = n
r = 0
while(n>0):
    a = n % 10
    r =r+a*a*a
    n = n//10
if (r == t):
    print("Armstrong Number")
else:
    print("NOT an Armstrong Number")
    
#OUTPUT:-

#Enter a number : 153
#Armstrong Number
