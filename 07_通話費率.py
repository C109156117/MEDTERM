ty,time=input("請輸入月租費型式及通話時間為:").split(',')
ty=int(ty)
time=int(time)
fee=0
fee_1=0
if ty == 186:
    fee=time*0.09
    if fee/186 >1:
        fee_1=fee*0.8
    elif fee/186 <=1:
        fee_1=fee*0.9
elif ty ==386:
    fee=time*0.08
    if fee/386 >1:
        fee_1=fee*0.7
    elif fee/386<=1:
        fee=fee*0.8
elif ty ==586:
    fee=time*0.07
    if fee/586 >1:
        fee_1=fee*0.6
    elif fee/586<=1:
        fee_1=fee*0.7
elif ty ==986:
    fee=time*0.06
    if fee/986 >1:
        fee_1=fee*0.5
    elif fee/986 <=1:
        fee_1=fee*0.6
print(str(round(fee_1)))
