from random import randint

player = 50
i = 1
while(0 < player <= 100):

    coin = randint(1,2)
    print(str(i) + "st")
    print("coin: " + str(coin))

    if coin == 1: 
        player += 9
    elif coin == 2:
        player -= 10

    print("player: " + str(player))
    i += 1
    