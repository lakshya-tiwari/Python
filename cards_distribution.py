from random import shuffle

sp_card= ['jack','queen','king','ace']

spade=[f'spade-{a}' for a in range(2,11)] + [f'spade-{b}' for b in sp_card]


heart=[f'heart-{a}' for a in range(2,11)] + [f'heart-{b}' for b in sp_card]


club=[f'club-{a}' for a in range(2,11)] + [f'club-{b}' for b in sp_card]


dimond=[f'dimond-{a}' for a in range(2,11)] + [f'dimond-{b}' for b in sp_card]


cards= spade + heart + club + dimond

shuffle(cards)
players = input('Players name :').split()
player_no = len(players)
cards_per_player = 52//player_no
index=0
for i in players: 
    a = cards[index:(cards_per_player)+index]
    print(f'{i} : {a}')
    index+=(cards_per_player)
    
