n=input("請輸入一字元為:")
m=reversed(list(n))
if list(m)==list(n):
    print("YES")
else:
    print("NO")