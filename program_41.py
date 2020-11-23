def fact(n):
    f = 1
    i = 1
    while i <= n:
        f = f * i
        i += 1
    return f
# taking input 
nLines = int(input("Enter the no. of lines : "))
for x in range(nLines):
    for y in range(x + 1):
        print(fact(x) // (fact(y) * fact(x - y))," ", end="")
    print()

#OUTPUT:-
#Enter the no. of lines : 6 
#1 
#1   1 
#1   2   1 
#1   3   3   1 
#1   4   6   4   1
#1  5  10  10  5  1