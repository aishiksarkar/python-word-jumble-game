
import random
from datetime import datetime
class wordjumblegame(object):

    def __init__(self, name, level) -> None:
        self.name = name
        self.points = 0
        self.level = level
        self.words = self.loadwords(self.level)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def banner(self):
        print("-------------------------------------------------------")
        print("            WELCOME TO WORD JUMBLE GAME                ")
        print("-------------------------------------------------------")
        print("          The computer presents a jumbled word.        ")
        print("                You need to guess it                   ")
        print("-------------------------------------------------------")
        print("NAME  :", self.name)
        print("LEVEL :", self.level)
        print("*******************************************************")
        print("\n")


    def loadwords(self, level):
        path = str(level) + ".txt"
        with open(path) as file:
            temp = file.readlines()
            return [s.strip() for s in temp]
        
    def jumble(self, word):
        temp = list(word)
        random.shuffle(temp)
        return ''.join(temp)

    def run(self):
        self.banner()
        random.shuffle(self.words)
        for word in self.words:
            jword = self.jumble(word)
            print("Jumbled Word -> ", jword)
            uword = input("Can you guess? ")
            if(uword == word):
                self.points += 1
                print("Correct!")
            else:
                print("Incorrect.")
            print("\n")
        self.printinfo()

    def score(self):
        return self.points

    def printinfo(self):
        print("*******************************************************")
        print("NAME   :", self.name)
        print("LEVEL  :", self.level)
        print("SCORE  :", self.points)
        if(self.points > 6):
            print("RESULT : Excellent Playing")
        elif(3 <= self.points <= 6):
            print("RESULT : Good Playing")
        else:
            print("RESULT : Needs Improvement")
        print("-------------------------------------------------------")
                
class wordjumblegameupdate(wordjumblegame):
    
    def __init__(self, name, level):
        super().__init__(name, level)
        self.time=0

    
    def run(self):
        self.banner()
        random.shuffle(self.words)
        for word in self.words:
            jword = self.jumble(word)
            print("Jumbled Word -> ", jword)
            t1=((datetime.now()).second)
            uword = input("Can you guess? ")
            t2=((datetime.now()).second)
            self.time+=(t2-t1)
            self.time=int(self.time)
            
            if(uword == word):
                self.points += 1
                print("Correct!")

            else:
                print("Incorrect.")
            print("\n")
        self.printinfo()
# --------------------------------------------------------

if __name__ == "__main__":


    # Inital test
    ''' 
    p = wordjumblegame("Anil", 2)
    print(getattr(p, "words"))
    p.run()
    print(p.score())
    '''


    # Multiplayer test
    D = {"Anil": 2, "Sunil": 1, "Ram": 1}
    players = [wordjumblegameupdate(player, level) for player, level in D.items()]
    for player in players:
        player.run()

    results = {}
    for player in players:
        key = getattr(player, "name")
        score = player.score()
        level = getattr(player, "level")
        results[key] = {"score":score, "level":level,"timetaken":player.time}

    sorted_dict = sorted(results.items(), key=lambda x:x[1]['score'],reverse=True)
    sorted_dict=dict(sorted_dict)
    # print(results)
    # print(sorted_dict)
    #l1=list(sorted_dict.keys())[0]#Highest Score!
    #print("Highest Score"  ,sorted_dict[l1]["score"])
    print(sorted_dict)


    # ans_dict=dict({})
    # for key,value in sorted_dict.items():
    #     if sorted_dict[key]["score"]==sorted_dict[l1]["score"]:
    #         ans_dict[key]=sorted_dict[key]
    # ans_dict_sorted=dict(sorted(ans_dict.items(), key=lambda x:x[1]['timetaken']))
    # # print(ans_dict_sorted)

    # for key,value in sorted_dict.items():
    #     if sorted_dict[key]["score"]!=sorted_dict[l1]["score"]:
    #         ans_dict_sorted[key]=sorted_dict[key]

    # print(ans_dict_sorted)

