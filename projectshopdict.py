amount= int(input("enter the amount"))
d = {}
n = int(input("enter the number"))
for i in range(n):
    item = input("enter the item name : ")
    price = int(input("enter the price of item : "))
    d.update({item:price})
if(amount>0):
     print(d)
     buy = input("enter what u want to buy")
    
for i in d:
        if(buy==i):
            hm = int(input("enter the quantity of things"))
            tp = hm*d[i]
            balance = amount - tp
print(balance)            
            
            
        
        