import datetime

class Player:
    def __init__(self,firstname,lastname,team=None):
        self.first_name = firstname
        self.last_name = lastname
        self.scores = []
        self.team = team

    def add_score(self,date,scores):
        """
        take = 
        date=datetime.date(take)
        """
        self.scores.append(scores)
        


    def total_score(self):
        return sum(self.scores)        

    def average_score(self):
        return int(sum(self.scores)/len(self.scores))
    

   

class Team:
    def __init__(self,name,league=None,manager_name=None,points=None):
        self.name=name
        self.league=league
        self.manager_name=manager_name
        self.points=points
        self.players=[]

    def add_player(self,player):
        firstname=str(input('enter first name: '))
        secondname =str(input('enter second name: '))
        team = str(input('enter team: '))
        squad=Player(firstname,secondname,team)
        where=team
        team=Team(where)
        team.players.append(secondname)        
        print( team.players)

    def __str__(self):
        cname = self.name
        inner = ' is playing in the '
        where = self.league
        info = cname + inner + where
        return (info)
        
        



'''
Portugal = Team('portugal','euros','pilas')
spain = Team('spain','euros','nana')
torres = Player('fernando','torres',spain)
ronaldo = Player('christiano','ronaldo',Portugal)
print (ronaldo.team)
print (torres.team)


spain.add_player('torres')

#spain.self.player.append('torres')


while True:
    try:
        date = datetime.datetime.strptime(raw_input("Enter the date checked out in YYYY-MM-DD format: "), "%Y-%m-%d")

    except ValueError:
        print "The date was not inserted in the following format: YYYY-MM-DD"
    else:
        break
~                 


'''    
        


class Match:
    def __init__(self,home_team,away_team,date=None,home_score=None,away_scores=None):
        self.home_team=home_team
        self.away_team=away_team
        #self.date=datetime.date(date)
        self.home_scores={'pilas':0} 
        self.away_scores={'sam':0}

        while True:
            try:
                self.date = datetime.datetime.strptime(input("Enter the date checked out in YYYY-MM-DD format: "), "%Y-%m-%d")

            except ValueError:
                print ("The date was not inserted in the following format: YYYY-MM-DD")
            else:
                break
                 
        

    def home_score(self):
             summer=0
             for i in self.home_scores:
                 summer+=self.home_scores[i]
             return summer
            


    def away_score(self):
        summer=0
        for i in self.away_scores:
            summer+=self.away_scores[i]
        return summer


    def winner(self):
        homeget=self.home_score()
        print(homeget)
        awayget=self.away_score()
        print(awayget)
        if homeget>awayget:
            return self.home_team
        elif awayget>homeget:
            return self.away_team
        elif homeget==awayget:
            return 'it is a draw game'

    def add_score(self,player=None,score=None):
        
        firstname=str(input('enter first name: '))
        secondname =str(input('enter second name: '))
        team = str(input('enter team: '))
        self.score = int(input('enter goals: '))
        scorer=Player(firstname,secondname,team)
        self.player=scorer      
        print(team)
        print(self.home_team)
         
        if str(team) == str(self.home_team):
            
            for i in self.home_scores:               
                
                if str(i) == str(secondname):
                    self.home_scores[str(secondname)]= self.score + self.home_scores[str(secondname)]
                    print ('here')
                    
                else:
                    self.home_scores[str(secondname)]= self.score
                    
                    
            return self.home_team
        
        elif str(team)==str(self.away_team):
            for i in self.home_scores:
                if str(i)==str(secondname):
                    self.away_scores[str(secondname)]= self.score + self.away_scores[str(secondname)]
                    break
                else:
                    self.away_scores[str(secondname)]= self.score
                    break
            return self.away_team
        else:
            return 'invalid team'
       

        
        


        






















    
