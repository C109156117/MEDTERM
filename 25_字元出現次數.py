while True:
    n=input("檢測的字串(end結束):")
    if n=="end":
        print("檢測結束")
        break
    else:
        m=input("檢測的單一字元:")
        a=n.count(m)
        print("字元",m,"出現次數為:"+str(a))