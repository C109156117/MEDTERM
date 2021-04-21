T=int(input("班級數:"))
s=[]
ma=[]
for i in range(T):
    c=input("每班人數:")
    s.append(c)
ma=sorted(s,reverse=True)
print("要購買"+str(ma[0])+"台電腦")