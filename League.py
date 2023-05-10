import os
def cls():
    os.system('cls')
name=list()
match=list()
versus=list()
temp_name=list()
player_data=dict()
name_list=list()

while True:
    try:
        number=input('Enter the number of players: ')
        number=number.strip()
        number=int(number)
        break
    except:
        print('Invalid Input')


for a in range(0,number):
    cls()
    print('Player',a+1,'name: ')
    name.append(input())
    name[a]=name[a].strip()
    name[a]=name[a].upper()
x=0
match_count=0

while x<number-1:
    for a in range(x,number-1):
        versus.append(name[x]+' VS '+name[1+a])
        match_count=match_count+1
    match.append(versus)
    versus=[]
    x=x+1

for pname in name:
    player_data[pname]=dict()
    player_data[pname]['GF']=0
    player_data[pname]['GA']=0
    player_data[pname]['GD']=0
    player_data[pname]['WIN']=0
    player_data[pname]['LOSE']=0
    player_data[pname]['DRAW']=0
    player_data[pname]['POINTS']=0

for a in range(0,number-1):
    for b in range(0,number-1):
        arranged_name=list()
        for pname in name:
            name_list=[player_data[pname]['POINTS'],player_data[pname]['GD'],player_data[pname]['GF'],pname]
            arranged_name.append(name_list)

        arranged_name.sort(reverse=True)
        arr_name=list()
        for i in range(0,len(arranged_name)):
            arr_name.append(arranged_name[i][3])

        cls()
        print('----------------------------------------------------------------------------')
        print('|    Player Name                       |  W|  D|  L|  GF|  GA|  GD|  POINTS|')
        print('----------------------------------------------------------------------------')
        for pname in arr_name:
            nlen=len(pname)
            wlen=len(str(player_data[pname]['WIN']))
            dlen=len(str(player_data[pname]['DRAW']))
            llen=len(str(player_data[pname]['LOSE']))
            gflen=len(str(player_data[pname]['GF']))
            galen=len(str(player_data[pname]['GA']))
            gdlen=len(str(player_data[pname]['GD']))
            plen=len(str(player_data[pname]['POINTS']))
            space=' '*(34-nlen)
            print('|    '+pname+space+'|'+' '*(3-wlen)+str(player_data[pname]['WIN'])+'|'+' '*(3-dlen)+str(player_data[pname]['DRAW'])+'|'+' '*(3-llen)+str(player_data[pname]['LOSE'])+'|'+' '*(4-gflen)+str(player_data[pname]['GF'])+'|'+' '*(4-galen)+str(player_data[pname]['GA'])+'|'+' '*(4-gdlen)+str(player_data[pname]['GD'])+'|'+' '*(8-plen)+str(player_data[pname]['POINTS'])+'|')

        print('----------------------------------------------------------------------------\n')
        try:
            print(match[b][a])
            temp_name=match[b][a].split(' VS ')
            name1=temp_name[0]
            name2=temp_name[1]
            while True:
                try:
                    player1_goal=(input(name1+' Goal Score: '))
                    player1_goal=player1_goal.strip()
                    player1_goal=int(player1_goal)
                    break
                except:
                    print('Invalid Input')
            player_data[name1]['GF']=player_data[name1].get('GF',0)+player1_goal
            player_data[name2]['GA']=player_data[name2].get('GA',0)+player1_goal
            while True:
                try:
                    player2_goal=(input(name2+' Goal Score: '))
                    player2_goal=player2_goal.strip()
                    player2_goal=int(player2_goal)
                    break
                except:
                    print('Invalid Input')
            player_data[name2]['GF']=player_data[name2].get('GF',0)+player2_goal
            player_data[name1]['GA']=player_data[name1].get('GA',0)+player2_goal
            if player1_goal>player2_goal:
                player_data[name1]['WIN']=player_data[name1].get('WIN',0)+1
                player_data[name2]['LOSE']=player_data[name2].get('LOSE',0)+1
            elif player2_goal>player1_goal:
                player_data[name2]['WIN']=player_data[name2].get('WIN',0)+1
                player_data[name1]['LOSE']=player_data[name1].get('LOSE',0)+1
            else:
                player_data[name1]['DRAW']=player_data[name1].get('DRAW',0)+1
                player_data[name2]['DRAW']=player_data[name2].get('DRAW',0)+1
            for pname in name:
                player_data[pname]['GD']=player_data[pname]['GF']-player_data[pname]['GA']
                player_data[pname]['POINTS']=player_data[pname]['WIN']*3+player_data[pname]['DRAW']
        except:
            continue

arranged_name=list()
for pname in name:
    name_list=[player_data[pname]['POINTS'],player_data[pname]['GD'],player_data[pname]['GF'],pname]
    arranged_name.append(name_list)

arranged_name.sort(reverse=True)
arr_name=list()
for i in range(0,len(arranged_name)):
    arr_name.append(arranged_name[i][3])

cls()
print('----------------------------------------------------------------------------')
print('|    Player Name                       |  W|  D|  L|  GF|  GA|  GD|  POINTS|')
print('----------------------------------------------------------------------------')
for pname in arr_name:
    nlen=len(pname)
    wlen=len(str(player_data[pname]['WIN']))
    dlen=len(str(player_data[pname]['DRAW']))
    llen=len(str(player_data[pname]['LOSE']))
    gflen=len(str(player_data[pname]['GF']))
    galen=len(str(player_data[pname]['GA']))
    gdlen=len(str(player_data[pname]['GD']))
    plen=len(str(player_data[pname]['POINTS']))
    space=' '*(34-nlen)
    print('|    '+pname+space+'|'+' '*(3-wlen)+str(player_data[pname]['WIN'])+'|'+' '*(3-dlen)+str(player_data[pname]['DRAW'])+'|'+' '*(3-llen)+str(player_data[pname]['LOSE'])+'|'+' '*(4-gflen)+str(player_data[pname]['GF'])+'|'+' '*(4-galen)+str(player_data[pname]['GA'])+'|'+' '*(4-gdlen)+str(player_data[pname]['GD'])+'|'+' '*(8-plen)+str(player_data[pname]['POINTS'])+'|')

print('----------------------------------------------------------------------------\n\n')
print('\t\t\tThe Winner is '+arr_name[0]+'.')
end=input()
