data=int(input("測試的資料量:"))
for i in range(0,data):
    f,m,c=input("父、母、子的血型:").split(" ")
    if f=='O' and m=='O' and c=='O':
        print("YES")
    elif f=='O' and m=='A' and (c=='A' or c=='O'):
        print("YES")
    elif f=='O' and m=='B' and (c=='B' or c=='O'):
        print("YES")
    elif f=='O' and m=='AB' and (c=='A' or c=='B'):
        print("YES")
    elif f=='A' and m=='A' and (c=='A' or c=='O'):
        print("YES")
    elif f=='A' and m=='B' and (c=='A' or c=='O' or c=='B' or c=='AB'):
        print("YES")
    elif f=='A' and m=='AB' and (c=='A' or c=='B' or c=='AB'):
        print("YES")
    elif f=='B' and m=='B' and (c=='B' or c=='O'):
        print("YES")
    elif f=='B' and m=='AB' and (c=='A' or c=='B' or c=='AB'):
        print("YES")
    elif f=='AB' and m=='AB' and (c=='A' or c=='B' or c=='AB'):
        print("YES")
    else:
        print("IMPOSSIBLE")