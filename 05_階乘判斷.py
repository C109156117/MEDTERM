m=int(input("請輸入階乘值M:"))
total=1
n=1
while total <m:
    total=total*n
    if total>m:
        break
    n=n+1
print("超過M值為"+str(m)+"的最小階乘N值為:"+str(n))