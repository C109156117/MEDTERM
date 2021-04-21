km=float(input("請輸入路程公里數:"))
r=(km-1.5)%0.25
n=int((km-1.5)/0.25)
fee=0
if km<1.5:
    print("所需車資為:75")
elif km>1.5:
    if r!=0:
        n=n+1
        fee=75+n*5
    else:
        fee=75+n*5
    print("所需車資為",str(fee))