n=int(input("輸入一正整數:"))
if (n %2)==0 and (n%11)==0:
    if (n%5)!=0 and (n%7)!=0:
        print(str(n),"為新公倍數?:YES")
else:
    print(str(n),"為新公倍數?:NO")