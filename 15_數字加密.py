n=input("輸入一組四位數字為:")
m=list(n)
a=(int(m[0])+7)%10
b=(int(m[1])+7)%10
c=(int(m[2])+7)%10
d=(int(m[3])+7)%10
print("加密後的數字為:",str(c)+str(d)+str(a)+str(b))
