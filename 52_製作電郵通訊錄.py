n=int(input("輸入n值:"))
mail={}
for i in range(n):
    a=input("請輸入姓名:")
    b=input("請輸入電子郵件:")
    mail[a]=b
s=input("請輸入想查詢電子郵件的姓名:")
print(s,"電子郵件帳號為",mail[s])