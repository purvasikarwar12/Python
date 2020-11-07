a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
a.sort()
print("Largest element is:",a[n-1])


#OUTPUT:-

 #Enter number of elements:4
 #Enter element:34
 #Enter element:92
 #Enter element:65
 #Enter element:43
 #Largest element is: 92