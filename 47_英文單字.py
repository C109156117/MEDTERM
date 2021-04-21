n=int(input("輸入筆數n:"))
d={}
for i in range(n):
    a,b=input("請輸入對應的中、英文:").split(" ")
    d[a]=b
s=input("輸入欲查詢單字:")
print(s,"中文意思為",d[s])