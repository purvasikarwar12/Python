
bill_amt = int(input("Enter Bill Amount : "))
if bill_amt >= 5000:
     bill_amt = bill_amt - 500
 
elif bill_amt >= 4000 and bill_amt <= 4999:
     bill_amt = bill_amt - 400
 
elif bill_amt >= 3000 and bill_amt <= 3999:
     bill_amt = bill_amt - 300
 
elif bill_amt >= 2000 and bill_amt <= 2999:
     bill_amt = bill_amt - 200
 
elif bill_amt >= 1000 and bill_amt <= 1999:
     bill_amt = bill_amt - 100
 
print("Final bill amount after discount is ", bill_amt)


#OUTPUT:-

 #Enter BilI Amount : 3900
 #Final bill amount after discount is 3600
