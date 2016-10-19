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
        self.xp = 0
        self.name = name
        self.health = 100
        self.max_health = 100
        self.attack = 100
        self.defence = 100
        self.weapon = 1
        self.life = True
    def health_check(self):
        if self.health >= self.max_health:
            self.health = self.max_health
            return False
        else:
            return True

    def level_check(self):
        if self.xp >= self.level*100:
            self.level += 1
            clear()
            print "Level up!"
            time.sleep(1)
            print "What would you like to add 50 skill points too?"
            print "1. Attack", "    ", "Attack lv currently: ", self.attack
            print "2. Defence", "    ", "Defence lv currently: ", self.defence
            print "3. Health", "    ", "Max Health currently: ", self.max_health
            skill = ""
            while skill not in ("1", "2", "3"):
                skill = raw_input("enter: 1/2/3  -")
                if skill == "1":
                    self.attack += 50
                elif skill == "2":
                    self.defence += 50
                elif skill == "3":
                    self.max_health += 50
                else:
                    print "Please re-enter  -"
            self.health = self.max_health
    def stat_check(self):
        self.level_check()
        self.health_check()





class Enemy(object):
    def __init__(self):
        self.name = "Scary fucking monster"
        self.health = randint(int(player.health * 0.9), int(player.health * 1.1))
        self.attack = randint(int(player.attack * 0.9), int(player.attack * 1.1))
        self.defence = randint(int(player.defence * 0.9), int(player.defence * 1.1))
        self.life = True
        self.weapon = randint(0, 1)
#------------------------------------------------------------------------------------------------------- Varibles
player = Player(raw_input("Name?"), 100, 100, 0, True)

#boring varibles
player_score = 0
error_message = ""
ran = randint 
Still_alive = True

#other varibles
win = 300
gold_count = 10
enemy_count = 15
Map_Size_X_Y = 16


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
                if object_to_be_placed == bandit_icon:
                    playerboard[x][z] = object_to_be_placed
                Used_coordinates.append(str(x) + str(z))
                spot.append(str(x) + str(z))
                           
        baker()

    if len(spot) > object_count:
        print "OVERFLOW!"
    return spot
    Used_coordinates.append(spot)
Object_Placement(gold_count, health_icon)
Object_Placement(enemy_count, bandit_icon)
#Object_Placement(weapon_count, weapon_icon) ########## add me in!!!

tick = 0
for block in range(len(playerboard)):
    playerboard[len(playerboard)/2][tick] = wall_icon
    tick += 1#wall placer
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
    if move_choice == "XP!":
        player.xp += 10
    if move_choice == "RESET":
        who[0] = 0
        who[1] = 0

    if len(move_choice) == 1 and move_choice[0] in ('w', 'a', 's', 'd'):
        if move_choice[0] == "w":
            if who[0] - int(1) >= 0: #UP
                if playerboard[(who[0] - int(1))][who[1]] not in (wall_icon):
                    who[0] -= int(1) 
                else:
                    em = "You can't move there!"
            else:
                em = "You can't move there!"

        elif move_choice[0] == "s":
            if (who[0] + int(1)) <= (len(object_board)-1): #DOWN
                if playerboard[(who[0] + int(1))][who[1]] not in (wall_icon):
                    who[0] += int(1)
                else:
                    em = "You can't move there!"
            else:
                em = "You can't move there!"

        elif move_choice[0] == "d":
            if who[1] + int(1) <= (len(object_board)-1): #RIGHT
                if playerboard[who[0]][(who[1] + int(1))] not in (wall_icon):
                    who[1] += int(1)
                else:
                    em = "You can't move there!"
            else:
                em = "You can't move there!"

        elif move_choice[0] == "a":
            if who[1] - int(1) >= 0: #LEFT
                if playerboard[who[0]][(who[1] - int(1))] not in (wall_icon):
                    who[1] -= int(1)
                else:
                    em = "You can't move there!"
            else:
                em = "You can't move there!"
        else:
            em = "What?"
    else:
        em = "Controls: Enter "
    error_message = em
    return who

#------------------------------------------------------------------------------------------------------- Battle loop
def fight(enemy):
    global fight_timer
    time.sleep(1)
    clear()
    print "A", enemy.name ,"appears!"
    time.sleep(1)
    weapon_check = ""
    if (enemy.health + enemy.attack + enemy.defence) > (player.health + player.attack + player.defence):
        if enemy.weapon > 0:
            weapon_check = " and has a weapon"
        print "He looks tough" + weapon_check + "!"
    else:
        print "He looks weak" + weapon_check
    time.sleep(1)
    fight_timer = True

    while fight_timer:
        class attack_style(object):
            def __init__(self, ch_attack_style, who):
                self.ch_attack_style = ch_attack_style
                if self.ch_attack_style == "o":
                    self.style = "Attacks"
                    self.defence = 1
                    self.attack = 1.5 + who.weapon
                    self.speed = 1
                elif self.ch_attack_style in ("d", "b"):
                    self.style = "Block!"
                    self.defence = 4
                    self.attack = 0.5 + who.weapon
                    self.speed = 0
                elif self.ch_attack_style == "p":
                    self.style = "Throws a power attack!"
                    self.defence = 0.5
                    self.attack = 3 + who.weapon
                    self.speed = 2
                elif self.ch_attack_style == "r":
                    self.style = "Retreat!"
                    self.defence = 1.5
                    self.attack = 0.5
                    self.speed = 1
                else:
                    self.style = "panic!"
                    self.defence = 0.5
                    self.attack = 0.5
                    self.speed = 0
        class temp_stats(object):
            def __init__(self, who, who_move):
                self.style = who_move.style
                self.attack = who.attack * (who_move.attack)
                self.defence = who.defence * (who_move.defence)


        def battle(fighter, opponent, fighter_stat, opponent_stat):

            global fight_timer

            def attack(attack, defence):
                damage = int(attack / ran(2, int(defence*0.1)))
                if damage < (defence*0.1):
                    damage = 0

                return damage

            
            time.sleep(1)
            hit = attack(fighter_stat.attack, (opponent_stat.defence))
            if hit > 0:
                opponent.health -= hit
                print ""
                print fighter.name, "hit", opponent.name
                time.sleep(1)
                print ""
                print opponent.name, "Takes",  str(hit), "Damage!"
                time.sleep(1)
                print ""
                if opponent.health <= 0:
                    opponent.health = 0
                print opponent.name, "has", str(opponent.health) + " HP Remaining"
                time.sleep(1)
            else:
                print ""
                print opponent.name, "Blocked", fighter.name
                time.sleep(1)
            if opponent.health <= 0:
                opponent.health = 0
                opponent.life = False
                print ""
                print opponent.name, "is dead!"
                fight_timer = False


        player_move = attack_style(raw_input("Enter attack o/d/p/r"), player)
        enemy_rand = randint(0, 2)
        if enemy_rand == 0:
            enemy_move = attack_style("o", enemy)
        elif enemy_rand == 1:
            enemy_move = attack_style("d", enemy)
        else:
            enemy_move = attack_style("p", enemy)

        temp_player = temp_stats(player, player_move)
        temp_enemy = temp_stats(enemy, enemy_move)

        def who(enemy_move, player_move):
            player_speed = player.attack * player_move.speed
            enemy_speed = enemy.attack * enemy_move.speed
            if player_move.style == "Block!":
                player_speed = 0
            if player_move.style == "Retreats!" :
                player_speed = 0
                return "run"
            elif player_speed > enemy_speed:
                return 1
            elif player_speed < enemy_speed:
                return 0
            else:
                return randint(0,1)

        clear()
        print player.name, "prepares to", player_move.style
        time.sleep(1)
        print ""
        print enemy.name, "prepares to", enemy_move.style
        time.sleep(1)

        Who = who(enemy_move, player_move)
        if Who == 1:
            battle(player, enemy, temp_player, temp_enemy)
            if fight_timer:
                battle(enemy, player, temp_enemy, temp_player)
        elif Who == 0:
            battle(enemy, player, temp_enemy, temp_player)
            if fight_timer:
                battle(player, enemy, temp_player, temp_enemy)
        elif Who == "run":
            battle(enemy, player, temp_enemy, temp_player)
            fight_timer = False
            if player.life:
                return 1
            else:
                return 0

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
            GAME = fight(enemy)
            if player.life == True and GAME != 0 and not enemy.life:
                player.xp += int((enemy.attack+enemy.defence)*.2)
                playerboard[oldposision[0]][oldposision[1]], object_board[oldposision[0]][oldposision[1]] = body_icon, body_icon
                clear()
                print_board(playerboard)
                Still_alive = True
            elif GAME == 1:
                clear()
                print_board(playerboard)
                Still_alive = True
            else:
                Still_alive = False
                break

        if object_board[oldposision[0]][oldposision[1]] == health_icon:
            if player.health_check():
                if memory_board[oldposision[0]][oldposision[1]] <= 3:
                    player.health += player.level *25
            else:
                memory_board[oldposision[0]][oldposision[1]] -= 1
            if memory_board[oldposision[0]][oldposision[1]] == 3:
                playerboard[oldposision[0]][oldposision[1]], object_board[oldposision[0]][oldposision[1]] = land_icon, land_icon # Make chest_icon into bandit_icon

            
                


        print "HP:", player.health
        print "Level: ", player.level
        print "Xp: ", player.xp




        player.stat_check()
        print ""
        if Still_alive == True:
            W = raw_input("Where to move?")
        else:
            Still_alive = False
            break

        '''else:
            W = d3bug_bot(bot_speed)'''
        board_transport(W, error_message, player_xy)
    break
else:
    print "You have died!"
    time.sleep(22)