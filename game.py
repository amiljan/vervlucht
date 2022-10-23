import random

lives = 5
monsters = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]
weapons = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40]

field = []
player1 = []
player2 = []
player3 = []
player4 = []
player5 = []

players = [player1,player2,player3,player4,player5]


#monsters = ["m1","m2"]
#weapons = ["w1","w2"]

def draw(player):
    cards = [monsters,weapons]
    if len(monsters) == 0:
        card_type = weapons
    elif len(weapons) == 0:
        card_type = monsters
    else:
        card_type = random.choice(cards)
    card = random.choice(card_type)
    if card_type == monsters:
        field.append(card)
    if card_type == weapons:
        player.append(card)
    card_type.remove(card)


while len(monsters) > 0 and len(weapons) > 0:
    for player in players:
        draw(player)
        field.sort()

        if len(field) > 1:
            for monster in range(len(field)-1):
                monster_power = field[monster]
                if monster_power + 1 == field[monster + 1]:
                    try:
                        if field[monster + 1] + 1 == field[monster + 2]:
                            print("double attack!")
                    except:
                        continue
                    print(field)
                    print("attack!")




