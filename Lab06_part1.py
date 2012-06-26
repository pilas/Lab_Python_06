"""
Lab_Python_06
Part 1
"""

"""
Whatever the datastructure you choose,
it should represent the following data:

player		| date		| score
_______________________________________
rooney		| 6/23/2012	| 2
rooney		| 6/25/2012	| 2
ronaldo		| 6/19/2012	| 0
ronaldo		| 6/20/2012	| 3
torres		| 6/22/2012	| 0
torres		| 6/21/2012	| 1
"""

import datetime
## create the player_stats data structure

player_stats = {'rooney':([datetime.date(2012,6,23),2],[datetime.date(2012,6,25),2]),
                'ronaldo':([datetime.date(2012,6,19),7],[datetime.date(2012,6,20),3]),
                'torres':([datetime.date(2012,6,21),0],[datetime.date(2012,6,21),1])
               }

#print (player_stats)

"""
i chose to use a dictionary as the data type with the name of the player as key
because like associative arrays its better to have the name of the player as the index or key
"""

## implement highest_score

def highest_score(player_stats):
    c=0
    counter1=0
    counter2=0
    highs=0
    for i in player_stats:
            get=i              
            get= player_stats[i]
            
            
            if get[0][1]>counter1:
                counter1=get[0][1]
            if get[1][1]>counter2:
                counter2=get[1][1]
            if counter1>counter2:
                highs=counter1
            elif counter2>counter1:
                highs=counter2
            else:
                highs=counter2
            

            if player_stats[i][c][1]==highs:
                final= (print(i,player_stats[i][1][0],highs))
                c+=1
                if c==2:
                    c=0
    

    score=(highs,)
   


                
            
            



## implement highest_score_for_player
def highest_score_for_player(player_stats,player):
    inside=True
    for i in player_stats:
            get=i              
            get= player_stats[i]
            if player==i:
                print('in list')
                
                if player_stats[player][0][1]>player_stats[player][1][1]:
                    print(player_stats[player][0][1])
                if player_stats[player][0][1]<player_stats[player][1][1]:
                    print(player_stats[player][1][1])
                elif player_stats[player][0][1]==player_stats[player][1][1]:
                    print('he has a tie score at: ',player_stats[player][0][1])
                 
                break


def highest_scorer(player_stats):
    highever=0
    player =''
    for i in player_stats:
        get=i
        get=player_stats[i]
        one=get[0][1]+get[1][1]
        two=get[0][1]+get[1][1]
        three=get[0][1]+get[1][1]
        if one>highever:
            highever = get[0][1]+get[1][1]
            player= i
        if two>highever:
            highever = get[0][1]+get[1][1]
            player=i
        if three>highever:
            highever = get[0][1]+get[1][1]
            player=i
            
    print(player,'scored the highest goals witha total of ',highever)
            
        
        
        
    
                
            
    
                
    












































## implement highest_scorer
