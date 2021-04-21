n=int(input("整數n:"))
i=1
s=''
while True:
    s+=str(round(n))+" "
    if n==1:
        break
    if (n%2)!=0:
        n=3*n+1
    else:
        n=n/2
    i=i+1
print("數列:",s)
print("cycle length:",str(i))
