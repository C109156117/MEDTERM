n=int(input("輸入一個度數(正整數):"))
a=n*2.10
aa=n*2.10
b=((n-120)*3.02)+120*2.1
bb=((n-120)*2.68)+120*2.1
c=((n-330)*4.39)+120*2.1+210*3.02
cc=((n-330)*3.61)+120*2.1+210*2.68
d=((n-500)*4.97)+120*2.1+210*3.02+170*4.39
dd=((n-500)*4.01)+120*2.1+210*2.68+170*3.61
e=((n-700)*5.63)+120*2.1+210*3.02+170*4.39+200*4.97
ee=((n-700)*4.50)+120*2.1+210*2.68+170*3.61+200*4.01
if n <= 120:
    print("Summer months:"+str(a))
    print("Non-Summer months:"+str(aa))
elif n >120 and n <=330:
    print("Summer months:"+str(b))
    print("Non-Summer months:"+str(bb))
elif n >330 and n <=500:
    print("Summer months:"+str(c))
    print("Non-Summer months:"+str(cc))
elif n >500 and n <=700:
    print("Summer months:"+str(d))
    print("Non-Summer months:"+str(dd))
elif n > 700:
    print("Summer months:"+str(e))
    print("Non-Summer months:"+str(ee))
