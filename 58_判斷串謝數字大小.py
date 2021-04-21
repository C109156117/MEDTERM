a=[]
ma=[]
mi=[]
c=0
for i in range(10):
    c=c+1
    u=int(input("請輸入第"+str(c)+"個數字:"))
    a.append(u)
ma=sorted(a,reverse=True)
mi=sorted(a,reverse=False)
print("最大的3個數字為:"+str(ma[0])+",",str(ma[1])+","+str(ma[2]))
print("最小的3個數字為:"+str(mi[2])+","+str(mi[1])+","+str(mi[0]))