M=int(input("小明身上有幾元(<=100):"))
N=int(input("販賣機有幾種飲料(<=30):"))
a=0
for i in range(0,N):
    d=int(input(""))
    if M>=d:
        a=a+1
print("小明可買",str(a),"種飲料")