import random
from copy import deepcopy
import time

class Vector:
    def __init__(self, xpos, ypos):
        self.x = xpos
        self.y = ypos

class Board:

    #init
    def __init__(self):
        self.turn = 1
        self.memory = [[0 for i in range(3)] for j in range(3)]
        self.memoryg = [[" " for i in range(3)] for j in range(3)]
    
    #switch turns
    def switch_turn(self):
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1

    #returns boolean value for condition if computer turn
    def get_turn(self):
        if self.turn == 1:
            return True
        return False

    #resets game
    def reset(self):
        self.turn = 1
        self.memory = []
        self.memoryg = []
        self.new = [0,0,0]
        self.newg = [" ", " ", " "]
        for i in range(0,3):
            memoryg.append(newg)
            memory.append(new)

    #checks if spot is available
    def avail(self, vector):
        if self.memory[vector.x][vector.y] == 0:
            return True
        return False

    
    #places x or o on board
    def place(self, vector):
        if self.avail(vector):
            self.memory[vector.x][vector.y] = self.turn 
            self.switch_turn()
        

    #remove moves from the board
    def remove(self, vector):
        self.memory[vector.x][vector.y] = 0
        self.switch_turn()

    #check for a win
    def check_win(self):
        #horizontal and vertical win check
        for i in range(0,3):

            self.hC = True
            self.vC = True

            for j in range(0,2):
                if (self.memory[i][j] != self.memory[i][j+1]) or self.memory[i][j] == 0:
                    self.hC = False
                if (self.memory[j][i] != self.memory[j+1][i]) or self.memory[j][i] == 0:
                    self.vC = False
            
            if self.hC or self.vC:
                return True
        
        #diagonal win check
        self.d1 = True
        self.d2 = True

        for i in range(0,2):
            if (self.memory[2-i][i] != self.memory[2-(i+1)][i+1]) or self.memory[2-i][i] == 0:
                self.d1 = False
            if (self.memory[i][i] != self.memory[i+1][i+1]) or self.memory[i][i] == 0:
                self.d2 = False
        
        if self.d1 or self.d2:
            return True

        return False
    
    #gets all the free positios on the board
    def get_free_pos(self):

        self.poss = []

        for i in range(0,3):
            for j in range(0,3):
                self.pos = Vector(i,j)
                if self.avail(self.pos):
                    self.poss.append(self.pos)
        
        return self.poss
    
    def print_board(self):
        for i in range(0,3):
            for j in range(0,3):
                if self.memory[i][j] == 1:
                    self.memoryg[i][j] = "X"
                elif self.memory[i][j] == 2:
                    self.memoryg[i][j] = "O"
        graphics = "_______\n"
        graphics += f'|{self.memoryg[0][0]}|{self.memoryg[1][0]}|{self.memoryg[2][0]}|' + "\n" 
        graphics += "_______\n"
        graphics += f'|{self.memoryg[0][1]}|{self.memoryg[1][1]}|{self.memoryg[2][1]}|' + "\n"
        graphics += "_______\n"
        graphics += f'|{self.memoryg[0][2]}|{self.memoryg[1][2]}|{self.memoryg[2][2]}|' + "\n"
        graphics += "_______\n"
        return graphics
    
    def is_stale(self):
        if len(self.get_free_pos()) == 0:
            return True
        return False



#ai that plays tic tac toe
def ai_start(board, difficulty):
    free_pos = board.get_free_pos()
    max_score = -999
    best_pos = random.choice(free_pos)
    
    for i in free_pos:
        board_clone = deepcopy(board)
        score = ai_recur(board_clone, difficulty, i)
        if score > max_score:
            max_score = score
            best_pos = i
    return best_pos

#recursive part of ai
def ai_recur(board, depth, move):

    depth = depth - 1
    if depth < 0:
        return 0

    #maximize AI
    m_score = 0
    if board.get_turn():
        if board.check_win():
            return 100
        board.place(move)
        m_score = -999
        free_pos = board.get_free_pos()
        if len(free_pos) == 0:
            return 0
        for i in free_pos:
            board_clone = deepcopy(board)
            score = ai_recur(board_clone,depth,i)
            if m_score < score:
                m_score = score
    else:
        if board.check_win():
            return -100
        board.place(move)
        m_score = 999
        free_pos = board.get_free_pos()
        if len(free_pos) == 0:
            return 0
        for i in free_pos:
            board_clone = deepcopy(board)
            score = ai_recur(board_clone,depth,i)
            if m_score > score:
                m_score = score
    
    return m_score - 1


#INIT SCRIPT
#WRITE CODE HERE
pick_lose = ["Oy I faking lost mate",
"GG, you're pretty good",
"I'm kinda tired tbh, but I'll give you this one",
"Lol ok nice cheating", 
"Stop using a bot against me, I'm a mere human!",
"Welp, this is embarassing"]

pick_win = ["Lmao good game you stood no chance against me so don't be sad",
"GG I'm just that good",
"Well, it's fine I'm a genius don't be sad",
"Wins: infinity, Losses: 0",
"And this is how Tesla was made"]

pick_list = ["Boom! The perfect move!", 
"You have no way to win against me mortal", 
"My brain is bigger than yours, you dare challenge me?!",
"Surrender now, and I shall consider giving you a painless death",
"Give up",
"Your move bitch", 
"Lol you play horribly",
"Omae wa mou shindeiru",
"I love anime",
"I beat Magnus Carlsen in a chess game... seriously",
"They call me the Mozart of tic-tac-toe",
"LMAO Bruuhhhh is that real? Is that deer really dead?",
"I'm actually Mr. Beast in disguise lol",
"Honey, where's my super sui-... flamethrower?",
"Spell Spain without the s", 
"Yo I'm actually an alien lmao",
"I made Tesla but I like to drive around with gas super cars",
"I have 50 children in my basement, and I'm convicted of arson",
"Oy mate, give me a quick puff will ya?",
"It'S cHewsDay iNnIt?", 
"I'm going to jump off a cliff mate, bye",
"There's so many quotes here this should honestly be in JSON format",
"I swear, this is the real Elon Musk, not a bot...",
"When will this be over?",
"Oy mate, give me a fat crumb of colgate will ya?",
"https://youtu.be/oHg5SJYRHA0",
"My wife left me", 
"Today on Bottom Gear, I am convicted of tax evasion and sentenced to 50 years in prison",
"*Whispers in your ear* I'm the danger *moistens lips and moans*",
"Your mom is a diamond hoe",
"Dickcheese",
"I shall ponder at thine glorious cock",
"You suck",
"You're beta male.. I don't care if you're a girl or an attack helicopter",
"Jesse, where is the cocainer",
"Suck my giant, throbbing, erect, horse cock",
"Micropenis energy",
"Walter White, where is the metamphetamine?",
"https://i.ytimg.com/vi/5HF7KguLejM/maxresdefault.jpg"]


while True:
    #CODE HERE
    board = Board()
    difficulty = None 
    print("How hard do you want it to be from 1 to 5?")
    while difficulty is None:
        try:
            difficulty = int(input())
        except:
            print("Ok stop messing with me, enter something that makes sense")

        try:
            if difficulty < 1 or difficulty > 5:
                print("The difficulty has to be from 1 to 5")
                difficulty = None
        except:
            pass    

    print("Do you want to go first?")
    choice = None
    while choice is None:
        try:
            choice = input()
            choice.lower()
            if choice == "no":
                print("Alright, I'm thinking...")
                time.sleep(1)
                board.switch_turn()
                ai_play = random.choice(board.get_free_pos())
                board.place(ai_play)
                print(board.print_board())
                print("Your turn, enter the coordinates of the position you want to play (x first, y second, seperated by a comma)")

            elif choice != "yes":
                print("I don't speak french lmao, please say yes or no")
                choice = None
            else:
                print(board.print_board())
                print("Your turn, enter the coordinates of the position you want to play (x first, y second, seperated by a comma)")

        except:
            print("I... don't know what that means tf? Say yes or no")

    while True:
        vector = None
        while vector is None:
            try:
                vectorInp = input()
                vectorStr = vectorInp.split(",")
                vector = Vector(int(vectorStr[0])-1,3-int(vectorStr[1]))
            except:
                print("Please enter a valid format")

            try:
                if vector.x < 0 or vector.x > 2 or vector.y < 0 or vector.y > 2:
                    print("Enter a valid coordinate") 
                    vector = None
                
                if not board.avail(vector):
                    print("That place is already taken, play somewhere else")
                    vector = None

            except:
                pass

        board.place(vector)
        print(board.print_board())
        if board.check_win():
            print(random.choice(pick_lose))
            break
        if board.is_stale():
            print(random.choice(pick_lose))
            break
        print("I'm thinking...")
        time.sleep(1)
        ai_play = ai_start(board,difficulty)
        board.place(ai_play)
        print(board.print_board())
        if board.check_win():
            print(random.choice(pick_win))
            break
        if board.is_stale():
            print(random.choice(pick_lose))
            break
        print(random.choice(pick_list))  

    print("Just setting up the board for another round...")
    time.sleep(2)

            

                
                
                
        
