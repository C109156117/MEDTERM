data=int(input("組數為:"))
for i in range(0,data):
    i=i+1
    a,b=input("第"+str(i)+"組為:").split(" ")
    a=int(a)
    b=int(b)
    fee=(a*250)+(b*175)
    print("第"+str(i)+"組應收費用:"+str(fee))
    