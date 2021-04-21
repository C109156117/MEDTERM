n=int(input("請輸入查詢組數:"))
atm=[['123','456','9000'],['456','789','5000'],['789','888','6000'],
['336','558','10000'],['775','666','12000'],['566','221','7000']]
for i in range(0,n):
    ac,psw=input("帳號密碼:").split(' ')
    if ac==atm[0][0] and psw==atm[0][1]:
        print(atm[0][2])
    elif ac==atm[1][0] and psw==atm[1][1]:
        print(atm[1][2])
    elif ac==atm[2][0] and psw==atm[2][1]:
        print(atm[2][2])
    elif ac==atm[3][0] and psw==atm[3][1]:
        print(atm[3][2])
    elif ac==atm[4][0] and psw==atm[4][1]:
        print(atm[4][2])
    elif ac==atm[5][0] and psw==atm[5][1]:
        print(atm[5][2])
    else:
        print("error")