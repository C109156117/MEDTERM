mon,day=input("請輸入月及日為:").split(' ')
mon=int(mon)
day=int(day)
mon=mon*100
date=mon+day
if date <=120:
    print("Capricorn")
elif date <=218:
    print("Aquarius")
elif date <=320:
    print("Pisces")
elif date<=420:
    print("Aries")
elif date <=521:
    print("Taurus")
elif date <=621:
    print("Gemini")
elif date <=722:
    print("Cancer")
elif date <=823:
    print("Leo")
elif date <=923:
    print("Virgo")
elif date <=1023:
    print("Libra")
elif date <=1122:
    print("Scorpio")
elif date <=1221:
    print("Capricorn")