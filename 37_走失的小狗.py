n=int(input("小狗可能跑的n個點:"))
for i in range(n):
    i=i+1
    k=int(input("猜想點與家的距離:"))
    if (k%9)==0 or (k%11)==0:
        print("第",str(i),"個點",str(k))     