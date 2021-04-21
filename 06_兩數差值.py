p=(input("輸入值為:"))
pp=p.replace(',','')
m=sorted(pp,reverse=True)
n=sorted(pp,reverse=False)
ma=''
mi=''
for i in m:
    ma +=str(i)
for j in n:
    mi +=str(j)

print("最大值數列與最小值數列差值為:"+str(int(ma)-int(mi)))


