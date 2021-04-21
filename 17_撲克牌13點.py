l,m,n,o,p=input("輸入五張牌:").split(" ")
poker={"A":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":11,"Q":12,"K":13}
ans=int(poker[l])+int(poker[m])+int(poker[n]+int(poker[o])+int(poker[p]))
print("加總值:"+str(ans))