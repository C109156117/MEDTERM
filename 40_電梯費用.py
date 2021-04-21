T=int(input("搭了幾次電梯:"))
fee_up=0
fee_down=0
up=0
down=0
s=1
for i in range(T):
    n=int(input(""))
    if n>s:
        up=(n-s)*20
        fee_up=fee_up+up
        s=n
    elif n<s:
        down=(s-n)*10
        fee_down=fee_down+down
        s=n
fee=fee_down+fee_up
print(fee)    
