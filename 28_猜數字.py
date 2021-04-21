game=input("猜數字:")
a=0
b=0
game_1=list(game)
while True:
    player=input("玩家的答案:")
    player_1=list(player)
    for i in range(0,4):
        for j in range(0,4):
            if game_1[i]==player_1[j]:
                if i == j:
                    a=a+1
                else:
                    b=b+1
    if player=='0000':
        break
    print(str(a),'A',str(b),'B')
    break