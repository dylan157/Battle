from random import randint
from sys import platform

import os
import time
global health_icon
global bandit_icon
global fight_timer


if platform == "linux" or platform == "linux2":
    clear = lambda: os.system('clear')
elif platform == "darwin":
    clear = lambda: os.system('clear')
elif platform == "win32":
    clear = lambda: os.system('cls')

#------------------------------------------------------------------------------------------------------- Classes
class Player(object):
    def __init__(self, name, health, attack, weapon, life):
        self.level = 1
        self.name = name
        self.health = 100
        self.attack = 100
        self.weapon = 0
        self.life = True
    def health_check(self):
        if self.health > self.level * 10:
            return False
        else:
            return True

    def level_check(self):
        if self.attack % ((self.level + 1) * 100) <= 0:
            self.level = int(attack * .1) 

    def stat_check(self):
        self.level_check()
        self.health_check()





class Enemy(object):
    def __init__(self):
        self.name = "Scary fucking monster"
        self.health = randint(int(player.health * 0.5), int(player.health * 1.2))
        self.attack = randint(int(player.attack * 0.5), int(player.attack * 1.2))
        self.life = True
#------------------------------------------------------------------------------------------------------- Varibles
player = Player(raw_input("Name?"), 1000, 1000, 0, True)

#boring varibles
player_score = 0
error_message = ""
ran = randint 
won = False

#other varibles
win = 300
gold_count = 3
enemy_count = 60
Map_Size_X_Y = 8


#bot varibles
d3bug = False
bot_speed = 0.1
bot_memory = 2
max_step = 2

#Icons
land_icon = ' '
bandit_icon = 'X'
health_icon = '+'
player_icon = "##"
wall_icon = "-"
body_icon = "*"
#------------------------------------------------------------------------------------------------------- Map gen/icon length/Object placer/player start location
icon_length = len(player_icon)
bandit_icon = bandit_icon*icon_length
health_icon = health_icon*icon_length
land_icon = land_icon*icon_length
wall_icon = wall_icon*icon_length
body_icon = body_icon*icon_length



object_board = []
memory_board = []
playerboard = []

for click in range(Map_Size_X_Y):
    object_board.append([land_icon] * Map_Size_X_Y)
    playerboard.append([land_icon] * Map_Size_X_Y)
    memory_board.append([0] * Map_Size_X_Y)


Used_coordinates = []
player_xy = [(len(object_board)-2), 0, 0]
Used_coordinates.append(str(player_xy[0]) + str(player_xy[1]))

def Object_Placement(object_count, object_to_be_placed):
    spot = []
    for x in range(object_count): # How many random numbers?
        x, z = 0, 0        
        def baker():
            global x
            global z
            x, z = randint(0, (len(object_board)-1)), randint(0, (len(object_board)-1))            
            if (str(x) + str(z)) in Used_coordinates: # or (str(x) + str(z)) in Used_coordinates:
                #print "XZ FOUND IN SPOT", (str(x) + str(z))
                baker()
            elif (str(x) + str(z)) in spot:
                #print "XZ FOUND IN USED COORDINATES", (str(x) + str(z))
                baker()
            else:
                object_board[x][z] = object_to_be_placed
                Used_coordinates.append(str(x) + str(z))
                spot.append(str(x) + str(z))
                           
        baker()

    if len(spot) > object_count:
        print "OVERFLOW!"
    return spot
    Used_coordinates.append(spot)
Object_Placement(gold_count, health_icon)
Object_Placement(enemy_count, bandit_icon)
tick = 0
for block in range(len(playerboard)):
    playerboard[len(playerboard)/2][tick] = wall_icon
    tick += 1
#------------------------------------------------------------------------------------------------------- print board
def print_board(board):
    for row in board:
        for x in range(icon_length):
            print " ".join(row)
        #print ""

print_board(playerboard)
#print_board(object_board)
#------------------------------------------------------------------------------------------------------- Board Transport
def board_transport(move_choice, em, who):
    #Board transport determins if the move it has been ordered to process is legal or not (valid input and on-map) 
    #Once the move has been validated, the players current location is re-written and returned to be further processed by the game loop.
    global error_message
    global player_score
    global clear


    if move_choice == "d3bug":
        player.level, player.attack, player.health = 15766, 15766, 15766
    em = move_choice
    if move_choice == "RESET":
        who[0] = 0
        who[1] = 0

    if len(move_choice) == 2 and move_choice[0] in ('u', 'd', 'l', 'r') and move_choice[1] in str(range(0, len(object_board))): 
        if move_choice[0] == "u":
            if who[0] - int(move_choice[1]) >= 0: #UP
                if playerboard[(who[0] - int(move_choice[1]))][who[1]] not in (wall_icon):
                    who[0] -= int(move_choice[1]) 
                else:
                    em = "You can't move there!"
            else:
                em = "You can't move there!"

        elif move_choice[0] == "d":
            if (who[0] + int(move_choice[1])) <= (len(object_board)-1): #DOWN
                if playerboard[(who[0] + int(move_choice[1]))][who[1]] not in (wall_icon):
                    who[0] += int(move_choice[1])
                else:
                    em = "You can't move there!"
            else:
                em = "You can't move there!"

        elif move_choice[0] == "r":
            if who[1] + int(move_choice[1]) <= (len(object_board)-1): #RIGHT
                if playerboard[who[0]][(who[1] + int(move_choice[1]))] not in (wall_icon):
                    who[1] += int(move_choice[1])
                else:
                    em = "You can't move there!"
            else:
                em = "You can't move there!"

        elif move_choice[0] == "l":
            if who[1] - int(move_choice[1]) >= 0: #LEFT
                if playerboard[who[0]][(who[1] - int(move_choice[1]))] not in (wall_icon):
                    who[1] -= int(move_choice[1])
                else:
                    em = "You can't move there!"
            else:
                em = "You can't move there!"
        else:
            em = "What?"
    else:
        em = "Unreadable input"
    error_message = em
    return who

#------------------------------------------------------------------------------------------------------- Battle loop
def fight(enemy):
    global fight_timer
    time.sleep(1)
    clear()
    print "A", enemy.name ,"appears!"
    time.sleep(1)
    if enemy.health > player.health:
        print "He looks Tough!"
    else:
        print "You should be able to kill him!"
    time.sleep(1)
    fight_timer = True

    while fight_timer:
        def battle(fighter, opponent):
            global fight_timer
            def hit(attack, enattack):
                chance = attack - enattack + 5 * ran(1, (int(fighter.attack)) / 2) # all the comments are written in opponent attack.
                enchance = attack - enattack + 4 * ran(1, (int(opponent.attack)) / 2)
                if chance > enchance:
                    return True
                else:
                    return False

            def attack(attack):
                damage = attack / ran(1, 10)
                return damage


            clear()
            print fighter.name, "throws a punch!" #add more items!!!!
            time.sleep(2)
            if hit(fighter.attack, opponent.attack):
                hit = attack(fighter.attack)
                opponent.health -= hit
                if opponent.health <= 0:
                    opponent.health = 0
                        
                clear()
                print fighter.name, "hit", opponent.name
                time.sleep(1)
                clear()
                print opponent.name, "Takes",  str(hit), "Damage!"
                time.sleep(1)
                clear()
                print opponent.name, "has", str(opponent.health) + " HP Remaining"
                time.sleep(1)
            else:
                clear()
                print fighter.name, "missed!"
                time.sleep(1)
            if opponent.health <= 0:
                opponent.life = False
                print opponent.name, "is dead!"
                fight_timer = False
                
                

        who = ran(1, 2)# 50/50 turn chance despite attack level.
        if who == 1:
            battle(player, enemy)
        else:
            battle(enemy, player)
        print fight_timer
        time.sleep(1)


#------------------------------------------------------------------------------------------------------- game loop
while player.life == True:
    icon_length = len(player_icon)
    bandit_icon = bandit_icon
    health_icon = health_icon
    #print_board(object_board)
    #time.sleep(1)
    while True:

        clear()
        #os.system('clear') #FOR LINUX  




        print error_message
        error_message = ""
        oldposision = player_xy
        playerboard[player_xy[0]][player_xy[1]] = player_icon # Make me Multiple choice!
        print_board(playerboard)
        print ""

        playerboard[oldposision[0]][oldposision[1]] = object_board[oldposision[0]][oldposision[1]] # Make old posision == object
        memory_board[oldposision[0]][oldposision[1]] += 1 #Block usage counter (You have stepped on this square x times)



        if object_board[oldposision[0]][oldposision[1]] == bandit_icon:
            enemy = Enemy()
            fight(enemy)
            if player.life == True:
                player.attack += int(enemy.attack*.2)
                playerboard[oldposision[0]][oldposision[1]], object_board[oldposision[0]][oldposision[1]] = body_icon, body_icon
                clear()
                won = True
            else:
                break

        if object_board[oldposision[0]][oldposision[1]] == health_icon:
            if player.health_check():
                if memory_board[oldposision[0]][oldposision[1]] <= 3:
                    player.health += player.level *.25
            else:
                memory_board[oldposision[0]][oldposision[1]] -= 1
            if memory_board[oldposision[0]][oldposision[1]] == 3:
                playerboard[oldposision[0]][oldposision[1]], object_board[oldposision[0]][oldposision[1]] = land_icon, land_icon # Make chest_icon into bandit_icon

            



        print "HP:", player.health
        print "Level: ", player.level
        print "Xp: ", player.attack




        player.stat_check()
        print ""
        if won != True:
            W = raw_input("Where to move?")
        else:
            W = "u0"
            won = False

        '''else:
            W = d3bug_bot(bot_speed)'''
        board_transport(W, error_message, player_xy)
    break
else:
    print "You have died!"
    time.sleep(22)