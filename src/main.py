import time
from random import choice
from random import shuffle
from random import randint
from math import ceil, floor, sqrt, log
BASE_NAME = ["Health","Attack","Defense","Speed","Luck"]
MONSTER_LUCK = 11
MONSTERS_KILLED = 0
class Monster:
    name = "default"
    adj = ""
    def __init__(self,lis=[]):
        self.base = [0 for x in range(5)]
        for i in range(len(lis)):
            self.base[i] = lis[i]
    def set_name(self,name):
        self.name = name
    def get_name(self):
        return self.name
    def generate_name(self):
        lines = None
        with open("monsters.txt","r") as f:
            lines = [x.strip() for x in f.readlines()]
        self.name = choice(lines)
        if (len(self.adj) > 0):
            self.name = f"{self.adj} {self.name}"
    def generate_stats(self,luck,slow=False):
        tmp = [0 for i in range(5)]
        if (slow and FLOOR_NUM <=2):
            luck *= 0.5
        if (slow == False):
            k = randint(1,10)
            if (k <= 1):
                #Item names have smoother distribution, and higher weight attached to names.
                xx = randint(0,4)
                listmp =['Legendary','Divine','Cursed','Strong','Metal']
                self.adj = listmp[xx]
                luck *= (1.1 + (4-xx)/10)
        if (N == 3):
            luck *= .8
        x = 10 +randint(floor(luck * sqrt(luck) * 0.5), ceil(luck * sqrt(luck) * 0.7))
        self.base[0] = x
        if (slow):
            self.base[0] *= sqrt(FLOOR_NUM) * 1.1
        x = randint(floor(luck* sqrt(luck) * 0.16),ceil(luck * sqrt(luck) * 0.4))
        self.base[1] = x
        if (slow):
            self.base[1] *= 0.8
            self.base[1] -= 10
            self.base[1] = max(0,self.base[1])
        x = randint(floor(luck*0.10),floor(luck*0.15))
        self.base[2] = min(x,50)
        x = 7 + randint(ceil(sqrt(luck) * 0.3),ceil(sqrt(luck) * (1-1/luck) * 0.6))
        self.base[3] = x
        if (slow):
            self.base[3] //=3.5
        x = randint(max(floor(log(luck) * 0.55),1),max(ceil(0.1 * log(luck) * log(luck)),1))
        self.base[4] = x
    def printm(self):
        print("Monster: "+ self.name)
        for i in range(5):
            print(f"{BASE_NAME[i]} {self.base[i]}")
op = 'x'


def SHOW_CURRENT():
    print(f"YOUR CURRENT HEALTH: {CURR_HP}/{BASE_HP}")
    print(f"YOUR CURRENT POINTS: {SCORE:.0f}")
    print(f"MONSTERS SLAIN: {MONSTERS_KILLED}")
def GETYN():
    """Get Y/N answer into 'op'"""
    while(1):
        global op 
        op = input().lower()
        if (op not in "yn"): print("> Please enter the letter 'y' or 'n'")
        else: break
def PRINT():
    """Print the board"""
    for i in range(N):
        for j in range(N):
            print(BOARD[i][j],end=' ')
        print()
def STATE():
    """Print the current floor and board state"""
    print(f"== Floor {FLOOR_NUM} ==")
    PRINT()
    SHOW_CURRENT()
def INIT():
    """ Initialize BOARD and VIS to empty"""
    global BOARD, VIS
    BOARD = [['.' for j in range(N)] for i in range(N)]
    global CURR_ROW, CURR_COL
    CURR_ROW = N//2
    CURR_COL = N//2
    BOARD[N//2][N//2] = 'P'
    VIS = [[False for j in range(N)] for i in range(N)]
    VIS[N//2][N//2] = True
def GENERATE():
    global BOARD
    for i in range(N):
        for j in range(N):
            if (i == N//2 and j == N//2): continue
            BOARD[i][j] = choice(BOARD_STATES)
def UPDATE_BOARD():
    for i in range(N):
        for j in range(N):
            if (VIS[i][j] or BOARD[i][j] == 'P'): BOARD[i][j] ='.'
    ret = BOARD[CURR_ROW][CURR_COL]
    BOARD[CURR_ROW][CURR_COL] = 'P'
    VIS[CURR_ROW][CURR_COL] = True
    return ret
def CHECK_FLOOR_CLEAR():
    cnt = 0
    for i in range(N):
        for j in range(N):
            if (VIS[i][j]):
                cnt+=1
    if (cnt == N*N):
        return True
    else:
        return False

def UPDATE_STATS():
    global BASE_HP, BASE_ATK, BASE_DEF, BASE_SPEED, BASE_LUCK
    BASE_HP     = BASE[0]
    BASE_ATK    = BASE[1]
    BASE[2] = min(75,BASE[2])
    BASE_DEF    = BASE[2]
    BASE_SPEED  = BASE[3]
    BASE_LUCK   = BASE[4]
    #IF FULL, THEN RESTORE HP?
def SHOW_INVENTORY():
    """Show Two Tables"""
    UPDATE_STATS()
    print("{:^10}|{:>9}".format("STAT","VALUE"))
    print("-" * 20)
    for i in range(len(BASE)):
        print(f"{BASE_NAME[i]:^10}|{BASE[i]:>9}")
    print("=" * 20)
    print("{:^30}|{:^9}|{:^13}".format("ITEM","BOOST","STAT"))
    print("-" * 55)
    for i in range(len(ITEMS)):
        print(f"{ITEMS[i][0]:^30}|{ITEMS[i][1]:>9}|{BASE_NAME[i]:^13}")
    print("=" * 55)
    SHOW_CURRENT()
def PRINT_STAT_INCREASE(op,x):
    time.sleep(TM)
    print(f"{BASE_NAME[op]} increased by {x}!",end= ' ')
    old = BASE[op]
    BASE[op] += x 
    print(f"({old} --> {BASE[op]})")
def POWERUP():
    # luck = BASE_LUCK * 0.5 * FLOOR_NUM
    luck = BASE_LUCK * 0.68 * sqrt(FLOOR_NUM)
    if (N == 3):
        luck *= 2.5
    op = randint(0,4)
    #0 health
    #1 atk
    #2 DEF
    #3 SPEED
    #4 LUCK
    #LOG DECAY FOR LUCK
    # SQRT DECAY FOR SPEED
    x = 0
    if (op == 0):
        x = randint(floor(luck * sqrt(luck) * 1), ceil(luck * sqrt(luck) * 1.4))
    elif (op == 1):
        x = randint(floor(luck* sqrt(luck) * 0.32),ceil(luck * sqrt(luck) * 0.8))
    elif (op == 2):
        x = randint(floor(luck*0.20),floor(luck*0.30))
    elif (op == 3):
        x = randint(ceil(sqrt(luck) * 0.2),ceil(sqrt(luck) * (1-1/luck) * 0.5))
    elif (op == 4):
        x = randint(max(floor(log(luck) * 0.55),1),max(ceil(0.1 * log(luck) * log(luck)),1))
    PRINT_STAT_INCREASE(op,x)
    UPDATE_STATS()
def CHOOSE_RANDOM_ITEM():
    #0 health
    #1 atk
    #2 DEF
    #3 SPEED
    #4 LUCK
    #read from file
    #RANDOM ITEM (STATS 3)
    op = randint(0,4)
    # op = 0
    luck = BASE_LUCK * 0.68 * sqrt(FLOOR_NUM)
    if (N == 3):
        luck *= 2.2
    name = "-"
    with open(f"items{op}.txt","r") as f:
        lines = f.readlines()
        gett = choice(lines).strip()
    adj = choice(ADJ_SEQ)
    k = ADJ_MAP[adj]+1
    name = f"{adj} " +gett
    x = 0
    luck *= k/6.5
    coin = randint(1,2)
    if (op == 0):
        x = randint(floor(luck * luck * 0.8), ceil(luck * luck * 2.5)) + randint(1,3)
    elif (op == 1):
        x = randint(floor(luck* sqrt(luck) * 0.72),ceil(luck * sqrt(luck) * 1.2))+ randint(1,3)
    elif (op == 2):
        x = randint(floor(luck*0.30),floor(luck*1.50))
    elif (op == 3):
        x = randint(ceil(sqrt(luck) * 0.3),ceil(sqrt(luck) * (1-1/luck) * 5))
    elif (op == 4):
        x = randint(max(floor(log(luck) * 0.95),1),max(ceil(0.7 * sqrt(luck) * log(luck) * log(luck)),1))
    
    print(f"You got {name}!",end=' ')
    print(f"(+{x} {BASE_NAME[op]})")
    

    time.sleep(TM)
    if (ITEMS[op][0] == '-'):
        print("REPLACING <empty slot> with ",end='')
        ITEMS[op][0] = name
        ITEMS[op][1] = x
        with open("log.txt","a") as f: f.write(f"{name:<30} +{x} {BASE_NAME[op]}\n")
        print(f"{ITEMS[op][0]} (+{ITEMS[op][1]})")
        PRINT_STAT_INCREASE(op,x)
    elif (x > ITEMS[op][1]):
        print(f"REPLACING {ITEMS[op][0]} (+{ITEMS[op][1]}) with ",end='')
        ITEMS[op][0] = name
        diff = x-ITEMS[op][1]
        ITEMS[op][1] = x
        with open("log.txt","a") as f: f.write(f"{name:<30} +{x} {BASE_NAME[op]}\n")
        print(f"{ITEMS[op][0]} (+{ITEMS[op][1]})")
        PRINT_STAT_INCREASE(op,diff)
    else:
        print(f"Your current item is better! (+{ITEMS[op][1]} {BASE_NAME[op]})")
        print(f"{name} will be scrapped for 3-5% of its stats!")
        with open("log.txt","a") as f: f.write(f"{name:<50} ({x} {BASE_NAME[op]})\n")
        x = floor(x * randint(3,5)/100)
        PRINT_STAT_INCREASE(op,x)
    print("<><><>")
def GEN_RANDOM_ADJ():
    #RANDOMIZED PROBABILITY
    for i in range(len(ADJ_FREQ)):
        x = 10 * 1/(i+1)
        if (x > 7): x = 7
        if (i >= 5):
            x *= randint(10,23)/10
        ADJ_FREQ[i] = ceil(x)
    # WRITE TO ADJACENCY PROBABILITY
    with open("adj.txt","r") as f:
        lines = f.readlines()
        with open("adjfreq.txt","w") as outt:
            for x in range(len(lines)):       
                for i in range(ADJ_FREQ[x]):
                    outt.write(lines[x].strip())
                    if (x != 14):
                        outt.write('\n')
                    else:
                        if (i + 1!=ADJ_FREQ[x]):
                            outt.write('\n')
def FIGHT_SEQ(monster=Monster()):
    print(f"Fighting against {monster.name}!")
    print("=" * 23)
    print("{:^12}|{:>10}".format("MONSTER STAT","VALUE"))
    print("-" * 23)
    for i in range(len(BASE)):
        print(f"{BASE_NAME[i]:^12}|{monster.base[i]:>10.0f}")
    print("=" * 23)
    # print("Turn sequence:")
    PLAYER_SPEED_X = 5/(BASE[3]/monster.base[3])
    MONSTER_SPEED_Y = 5/1
    # print(f"{PLAYER_SPEED_X} {MONSTER_SPEED_Y}")
    CURR_X = PLAYER_SPEED_X
    CURR_Y = MONSTER_SPEED_Y
    turn_count = 0
    turn_limit = 200
    global CURR_HP, SCORE, GAME_END, MONSTERS_KILLED
    while(1):
        turn_count+=1
        if (turn_count == turn_limit):
            break
        if (CURR_X <= CURR_Y):
            print(f"You attack {monster.name}!")
            DAMAGE = BASE_ATK * (100-monster.base[2])/100
            NEW_HP = round(max(monster.base[0]-DAMAGE,0),0)
            print(f"{monster.name}: {monster.base[0]:.0f} HP --> {NEW_HP:.0f} HP")
            time.sleep(TM)
            CURR_X+=PLAYER_SPEED_X
            monster.base[0] = NEW_HP
            if (monster.base[0] <= 0):
                print(f"{monster.name} has died!")
                SCORE += round((ceil(FLOOR_NUM * sqrt(N)) * 10) * (1 - PENALTY_PERCENT/100),0)
                MONSTERS_KILLED+=1
                break
        else:
            print(f"{monster.name} attacks you!")
            DODGE_CHANCE = ceil((BASE_LUCK/monster.base[4])/100 * 3)
            k = randint(1,100)
            if (k <= DODGE_CHANCE):
                print("Luckily, you dodged the attack!")
                CURR_Y+=MONSTER_SPEED_Y
                continue
            DAMAGE = monster.base[1] * (100-BASE_DEF)/100
            NEW_HP = max(round(ceil(CURR_HP-DAMAGE),0),0)
            print(f"Player: {CURR_HP:.0f} HP --> {NEW_HP:.0f} HP")
            time.sleep(TM)
            CURR_Y+=MONSTER_SPEED_Y
            CURR_HP = NEW_HP
            if (CURR_HP <= 0):
                print(f"<><><><><><>")
                print(f"Player (you) has died!")
                print(f"<><><><><><>")
                GAME_END = True
                break
    if (turn_count == turn_limit):
        print(f"{monster.name} has fatigued!")
    if (not GAME_END):
        CURR_HP += floor(BASE_HP * 0.035 * 3/N)
        CURR_HP = min(CURR_HP,BASE_HP) 
def REGEN_HP_AFTER_CELL():
    global CURR_HP
    CURR_HP += floor(BASE_HP * 0.015 * 3/N)
    CURR_HP = min(CURR_HP,BASE_HP)

# 2D Rogue game
#
## GAMEPLAY
# items
# monsters
## BOARD
# 2d grid
# different floors
## STORE FILES
# STORE HIGH SCORE
# STORE ITEM NAMES
## RULE EXPLANATION

SKIP_SEQ = 0
## INIT RULES
ORG_BOARD_STATES =  ['&','I','^','?']
BOARD_STATE_WEIGHTS = [14,5,4,4]
BOARD_STATES =[]
for i in range(4):
    BOARD_STATES.extend([ORG_BOARD_STATES[i] for x in range(BOARD_STATE_WEIGHTS[i])])
#DEFAULT TABLE
ADJ_FREQ = [
    10,9,7,6,5,
    5,5,5,4,3,
    2,1,1,1,1
]
ADJ_NAME = None
ADJ_MAP = dict()
ADJ_SEQ = None
with open("adj.txt","r") as f:
    ADJ_NAME = [x.strip() for x in f.readlines()]
for i in range(len(ADJ_NAME)):
    ADJ_MAP[ADJ_NAME[i]] = i
with open("adjfreq.txt","r") as f:
    ADJ_SEQ = [x.strip() for x in f.readlines()]
GEN_RANDOM_ADJ()

with open("log.txt","w") as f:
    f.write("ITEM LOG FOR PREVIOUS GAME\n")
    f.write('='*65 + '\n')
    f.write(f"{'ITEM':<30} {'EQUIPPED':<20}{'SCRAPPED'}\n")
    f.write('='*65 + '\n')
    
## BOARD
BOARD   = None
VIS     = None
TM      = 100/1000
TM = 0
# TM = 500/1000
N = 3
N = 3
FLOOR_NUM = 1
CURR_ROW = 0
CURR_COL = 0
## BOOL AND SCORE
SCORE = 0
PENALTY_PERCENT = 0
FLOOR_CLEAR = False
GAME_END    = False
AUTO        = False
## PLAYER STATS
BASE_HP = 300; CURR_HP = BASE_HP
BASE_ATK = 17
BASE_DEF = 1 #reduce incoming dmg by x%
BASE_SPEED = 10 #10/SPEED = wait time
BASE_LUCK = 10
BASE = [300,17,1,10,10]
# BASE_NAME = ["Health","Attack","Defense","Speed","Luck"]
BASE_REGEN = 2
ITEMS = [['-',0] for x in range(5)]
print("<><><> Welcome to 2D Rogue Game! <><><>")
print("<><><> By: Aaron Wang (2021)     <><><>")
print("""OVERVIEW (more details in rules)
Traverse an n by n grid using 'wasd'. Fight monsters, gain items and powerups. 

Press 'I' to see your inventory and stats. Fights are automated, and results of monster fights, item and powerup collections are shown in the console. 

Everything is randomized, with items and powerups scaled according to your "luck", and monsters scaled according to the floor number and grid size.

You must clear each floor before going to the next one. At the end of each floor you must defeat a boss.

Points are given per monster and boss kill, and are scaled based on the size of your grid and what floor you are on.
""")
if (not SKIP_SEQ):
    print("> How fast do you want text to scroll? (in milliseconds)\n* as a guideline: 400 for slow speed (immersive), 250 for moderate, 100 for fast, 0 for instant text")
    while(1):
        try:
            TM = float(input())/1000
            if (TM < 0):
                print("Error: Please enter a positive number")
                continue
            break
        except:
            print("Error: Please input an integer")

    print("> Do you want an in-depth explanation of the rules? (y/n)"); GETYN()
    if (op == 'y'):
        with open("rules.txt","r") as rules_file:
            for x in rules_file:
                print(x,end='')
                time.sleep(TM)
    else: print("> Rules skipped!")    

    print("> How large do you want the n by n grid to be? (n must be at least 3 and less than 21)")
    print("\tAs a guideline: 3 easy, 5 medium, 10 hard, 20 near-impossible")
    print("\tnote: larger boards take a very long time to clear manually.")
    print("\tStart with a small board size first (3-5)")
    while (1):
        try:
            N = int(input())
            if (N >= 30): print("> Grid is too big. Please enter an integer less than 21")
            elif (N < 3): print("> Grid is too small. Please enter an integer at least 3")
            else: break
        except:
            print("Error: please enter an integer")

    print(f"> Ok! You have a {N} x {N} grid, with {N*N} cells to traverse")
    ##
INIT()
# STATE()
# print("Do you want to auto traverse? (y/n)"); GETYN()
# if (op=='y'): AUTO = 1
# else: AUTO = 0

print("Do you want to start with some item/powerups (make the game easier)? (y/n)"); 
print("\t(You will receive a significant score penalty accordingly).")
print(f"\t(E.g., as it gets easier, your score reduction % grows like a cubic function).")
print(f"\t(You can also use this to test the random generation for large numbers, looking at the log.txt file for all items).")
GETYN()
if (op=='y'):
    print("How many items AND powerups? (e.g. 3 items and 3 powerups)")
    print("(1-5 is slight boost; 5-10 is medium; >10 is high boost; >50 gives you an idea on how item generation works (look at log.txt)")
    n = 0
    while(1):
        try:
            n = int(input())
            for i in range(n):
                CHOOSE_RANDOM_ITEM()
                POWERUP()
                print("<><><>")
            break
        except:
            print("Please enter an integer.")
    PENALTY = round(n * n * n * N * sqrt(N) + randint(3,10),0)
    PENALTY_PERCENT = min(ceil(n * sqrt(n) * 1.0 *sqrt(N)),100)
    if (n <= 0):
        PENALTY = 0
    print(f"PENALTIES APPLIED:")
    print(f"-{PENALTY:.0f} points initially")
    print(f"-{PENALTY_PERCENT}% overall")
    SCORE -= PENALTY

GENERATE()
STATE()
print("> Make sure to check your inventory/stats ('i') every now and then!")

while (not GAME_END):
    while(not FLOOR_CLEAR):
        while (1):
            if (not AUTO):
                print("> Input move (wasd or 'i' for inventory/stats OR 'x' for END GAME IMMEDIATELY):")
                while (1):
                    op = input().lower()
                    if (op not in "wasdix"):
                        print("error: must be letter from 'wasdix'")
                    elif (op =='i'):
                        print("SHOWING INVENTORY")
                        SHOW_INVENTORY()
                        STATE()
                        print("> Input move (wasd or 'i' for inventory/stats OR 'x' for END GAME IMMEDIATELY):")
                    elif (op == 'x'):
                        print("**Please enter 'x' again to confirm. If not, enter any other character")
                        op= input().lower()
                        if (op == 'x'):
                            GAME_END = True
                            break
                        else:
                            STATE()
                            print("> Input move (wasd or 'i' for inventory and stats OR 'x' for END GAME IMMEDIATELY):")
                    else: break
                if (GAME_END): break
                TMP_ROW = CURR_ROW
                TMP_COL = CURR_COL
                if (op == 'w'): CURR_ROW-=1
                elif (op == 's'): CURR_ROW+=1
                elif (op == 'd'): CURR_COL+=1
                elif (op == 'a'): CURR_COL-=1
                if (CURR_ROW < 0 or CURR_COL < 0 or CURR_ROW >= N or CURR_COL >= N):
                    print("Out of bounds!")
                    CURR_ROW = TMP_ROW
                    CURR_COL = TMP_COL
                    STATE()
                else:
                    break
            else:
                pass
        if (GAME_END): break
        COLLIDE = UPDATE_BOARD()
        # pygame.display.update()
        if (COLLIDE == '?'):
            COLLIDE = choice(['&','I','^'])
        if (COLLIDE == 'I'):
            print("<><> ITEM <><>")
            CHOOSE_RANDOM_ITEM()
        elif (COLLIDE == '&'):
            print("<><> MONSTER <><>")
            m1 = Monster()
            m1.generate_stats(MONSTER_LUCK)
            m1.generate_name()
            FIGHT_SEQ(m1)
            #NOT DONE
            #ENTER MONSTER FIGHT PHASE
            #IF DEAD THEN BREAK
        elif (COLLIDE == '^'):
            print("<><> POWERUP <><>")
            POWERUP()
        elif (COLLIDE == '.'):
            print("<><> EMPTY <><>")
        time.sleep(TM)
        #DO ACTION WITH COLLIDED
        if(GAME_END):
            break
        if (COLLIDE != '.'):
            REGEN_HP_AFTER_CELL()
        FLOOR_CLEAR = CHECK_FLOOR_CLEAR()
        STATE()
    if not GAME_END:
        print(f"Floor {FLOOR_NUM} has been cleared!!")
        print(f"Boss time!")
        # print("BOSS FIGHT SEQUENCE")
        lines_boss = None
        with open("boss.txt") as f:
            lines_boss = [x.strip() for x in f.readlines()]
        boss1 = Monster()
        boss1.set_name(choice(lines_boss))
        boss1.generate_stats(5 + N/5 * FLOOR_NUM * MONSTER_LUCK * sqrt(FLOOR_NUM),slow=True)
        FIGHT_SEQ(boss1)
        if (GAME_END):
            print(f"Boss has defeated you! You remain on FLOOR {FLOOR_NUM}!")
            break
        # IF BOSS LOSE THEN LEAVE THIS LOOP
        # IF BOSS WIN THEN CONTINUE WITH BELOW
        FLOOR_CLEAR = 0
        FLOOR_NUM += 1
        print(f"<><><> You have reached FLOOR {FLOOR_NUM} <><><>")
        MONSTER_LUCK += 4*FLOOR_NUM *sqrt(FLOOR_NUM) * N/4
        CURR_HP = BASE_HP
        INIT()
        GENERATE()
        STATE()
    else:
        break
print(f"<--> GAME OVER <-->")
print(f"Showing your final inventory and stats below:")
SHOW_INVENTORY()
print(f"<--> GAME OVER <-->")
print(f"Your final inventory and stats are shown above:")
print(f"Your final results are shown above:")
FLOOR_NUM-=1
if (FLOOR_NUM == 1):
    print(f"You passed {FLOOR_NUM} floor on the {N} x {N} grid")
else:
    print(f"You passed {FLOOR_NUM} floors on the {N} x {N} grid")
SHOW_CURRENT()
print("Check log.txt to see what items you acquired and scrapped along the way!")