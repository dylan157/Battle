#!/usr/bin/env python
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
    def __init__(self, name):
        self.kills = 0
        self.level = 1
        self.xp = 0
        self.name = name
        self.health = 100
        self.max_health = 100
        self.attack = 100
        self.defence = 100
        self.weapon = 0
        self.weaponName = "Fists"
        self.side = 0
        self.sideName = "Arms"
        self.life = True
        self.gold = 0
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
        names = ["Bandit", "Random angry guy", "Scavenger", "Death dunden", "Wild Bone Biter", "Skeleton", "Kill Caller", "KILLTOLN"  ]
        weapons = ["Fists", "Stick", "Brick", "Pole", "Hammer", "knife", "Sharp knife", "Razor Teeth" "Bone Bat", "Katana", "KIll SCREAM", "ION LAZOR", "KILL BAT 2.0"]
        sides = ["Arms", "Leathers", "Arms", "Wooden board", "Thick Leathers", "Kevlar Amour", "Thick Skin", "Leather Robe", "Hard Bones", "Bone Shield", "Hard Bones", "Bone Shield", "Skin Silk Battle Robe", "Kill shield", "METAL AMOUR", "BALLISTIC AMOUR 2.0"]
        self.level = randint(0, int(player.kills%9/2))
        self.name = names[self.level]
        if self.level == 0:
            self.level += 1 
        self.health = randint(int(static_player[1] * self.level*.4), int(static_player[1] * self.level*.9))
        self.attack = randint(int(static_player[1] * self.level*.4), int(static_player[1] * self.level*.9))
        self.defence = randint(int(static_player[1] * self.level*.4), int(static_player[1] * self.level*.9))
        self.life = True
        self.weapon = randint(0, 1)
        self.side = randint(0, 1)
        if self.weapon == 1:
            self.weaponName = weapons[self.level+1]
        else:
            self.weaponName = weapons[self.level]
        if self.side == 1:
            self.sideName = sides[self.level+1]
        else:
            self.sideName = sides[self.level]
    def calls(self):
        calls = ["Your going to die!", "Say hello to my little friend!", "Take this!", "Prepare to turn to paste!", "blub blub", "Squarch!", "Its peanut butter jelly time!", "Bleed, BLEED!", "Bossani will end you mortal!", "Your time is limited!", "Are we inside a game?", "The grass was greener!", "Say hello to skeaks for me!", "You will never leave alive!", "Argh!!!!", "*Tries to fly*.. Damn, i cant fly", "Why cant we just be friends?", "Say goodbye to your spine", "Always remember to bring a towel!", "I will kill you, then the demons will kill you :D", "Please just die", "Die", "Can you stop breathing?", "Banana blast!", "LUBBA BUB BUB", "DDIIEE!", "all your castles are belong to us!"]
        calls2 = ["ARHGGGGGG!", "SCREEEECH!", "DIIIIIEEEE!", "RAWWWW!!", "EHHHHHHHCHHH!", "KSSSSKSSK!!", "ICCHCHH!!", "KILL ALL HUMANS", "BEEP BOP", "01001011 01001001 01001100 01001100", "DIE DIE DIE", "'WARNING, FRIENDBOT SET TO KILL MODE. TO CHANGE YOUR FRIENDBOTS PLAYMODE, PLEASE REFER TO THE USERS MANUAL'", "Hello friend!", "HUMAN.LIFE MUST = 0"]
        if self.level <= 2:
            print "" 
            print self.name + " says: " + "'" + calls[randint(0, len(calls)-1)] + "'"
         
        else:
            if self.level < 7:
                print "" 
                print self.name + " says: " + calls2[randint(0, 6)]
                
            else:   
                print "" 
                print self.name + " says: " + calls2[randint(6, len(calls2)-1)]
                
class Boss(object):
    def __init__(self):
        self.name = "Bossani!"
        self.health = randint(int(static_player[1] * 2), int(static_player[1] * 2.2))
        self.attack = randint(int(static_player[0] * 1.6), int(static_player[0] * 2.2))
        self.defence = randint(int(static_player[2] * 1.6), int(static_player[2] * 2.2))
        self.life = True
        self.weapon = 5
        self.side = 5
        if self.weapon == 5:
            self.weaponName = "Temple Bat"

        if self.side == 5:
            self.sideName = "Bossanis "
        else:
            self.sideName = "Tail"
    def calls(self):
        calls2 = ["ARHGGGGGG!", "SCREEEECH!", "DIIIIIEEEE!", "RAWWWW!!", "EHHHHHHHCHHH!"]
        print "" 
        print self.name + " says: " + "'" + calls2[randint(0, len(calls2)-1)] + "'"
         



#------------------------------------------------------------------------------------------------------- Varibles
def intro():
    print "Welcome to Battle-with-map!"
    time.sleep(2)
    print "The current objective is to buy everything in the store ($$)"
    time.sleep(2)
    print "To get gold you must kill monsters! (XX)"
    time.sleep(2)
    print "Monsters will spawn in the top half of the screen after you step on spawn (~~)"
    time.sleep(2)
    print "Once all monsters are dead. step on spawn to generate new enemys!"
    time.sleep(2)
#intro()

player = Player(raw_input("Name your character: "))

#boring varibles
player_score = 0
error_message = ""
ran = randint 
Still_alive = True


#other varibles
win = 300
gold_count = 2
enemy_count = 4
Map_Size_X_Y = 10



#bot varibles
d3bug = False
bot_speed = 0.05
bot_memory = 2
max_step = 2

#Icons
land_icon = ' '
bandit_icon = 'X'
health_icon = '+'
player_icon = "##"
wall_icon = "-"
body_icon = "*"
shop_icon = "$"
spawn_icon = "~"
boss_icon0 = "@"
boss_icon1 = "("
boss_icon2 = ")"
boss_icon3 = "V"



#------------------------------------------------------------------------------------------------------- Map gen/icon length/Object placer/player start location
icon_length = len(player_icon)
bandit_icon = bandit_icon*icon_length
health_icon = health_icon*icon_length
land_icon = land_icon*icon_length
wall_icon = wall_icon*icon_length
body_icon = body_icon*icon_length
shop_icon = shop_icon*icon_length
spawn_icon = spawn_icon*icon_length
boss_icon0 = boss_icon0*icon_length
boss_icon1 = boss_icon1*icon_length
boss_icon2 = boss_icon2*icon_length
boss_icon3 = boss_icon3*icon_length



object_board = []
memory_board = []
playerboard = []

for click in range(Map_Size_X_Y):
    object_board.append([land_icon] * Map_Size_X_Y)
    playerboard.append([land_icon] * Map_Size_X_Y)
    memory_board.append([0] * Map_Size_X_Y)

Used_coordinates = []# this varible prevents object placement conflict by recording xy's already in use(e.g bandit_icon in 4,7 so a gold_icon cant also be placed there )
player_xy = [(len(object_board)-2), 0, 0]
Used_coordinates.append(str(player_xy[0]) + str(player_xy[1]))


tick = 0
for block in range(len(playerboard)):
    playerboard[len(playerboard)/2][tick] = wall_icon
    Used_coordinates.append(str(len(playerboard)/2) + str(tick))#Wall
    playerboard[(len(object_board)-1)][(len(object_board)-1)] = spawn_icon
    object_board[(len(object_board)-1)][(len(object_board)-1)] = spawn_icon
    Used_coordinates.append(str((len(object_board)-1)) + str(len(object_board)-1))#spawn

    if tick == (len(playerboard)/2):
        Used_coordinates.append(str(len(playerboard)/2) + str(tick))
        shop_wall_location = str(len(playerboard)/2) + str(tick)
        playerboard[(len(playerboard)/2)+1][tick] = shop_icon
        object_board[(len(playerboard)/2)+1][tick] = shop_icon
        Used_coordinates.append(str((len(playerboard)/2)+1) + str(tick))
    tick += 1#wall placer


def Object_Placement(object_count, object_to_be_placed, specific_x, specific_y):
    spot = []
    calculated_board_x, calculated_board_y = specific_x, specific_y
    if specific_x == "n":
        calculated_board_x = (len(object_board)-1)
    if specific_y == "n":
        calculated_board_y = (len(object_board)-1)
    for x in range(object_count): # How many random numbers?
        x, z = 0, 0        
        def baker():
            global x
            global z
            x, z = randint(0, calculated_board_y), randint(0, calculated_board_x)            
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
Object_Placement(gold_count, health_icon, "n", "n")
#Object_Placement(weapon_count, weapon_icon, "n", "n") ########## add me in!!!


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
        player.level, player.gold, player.attack, player.health = 15766, 15766, 15766, 15766
    em = move_choice
    if move_choice == "XP!":
        player.xp += 10
        player.gold
    if move_choice == "RESET":
        who[0] = 0
        who[1] = 0
    if move_choice == "STP":
        print static_player[0]
        print static_player[1]
        print static_player[2]
        time.sleep(3)

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
        em = "Controls: w,a,s,d + enter"
    error_message = em
    return who

#------------------------------------------------------------------------------------------------------- Battle loop
def fight(enemy):
    player_weapon = ""
    enemy_weapon  = ""
    global fight_timer
    global battle_timer
    clear()
    print "A", enemy.name ,"appears!"
    time.sleep(1)
    weapon_check = ""
    if enemy.weapon > 0:
        weapon_check = "and has a weapon! >" + enemy.weaponName
    if (enemy.health + enemy.attack + enemy.defence) > (player.health + player.attack + player.defence):
        print "He looks tough" + weapon_check + "!"
    else:
        print "He looks weak" + weapon_check + "!"
    enemy.calls()
    time.sleep(2)
    fight_timer = True

    while fight_timer:
        battle_timer += 1
        class attack_style(object):
            def __init__(self, ch_attack_style, who):
                self.ch_attack_style = ch_attack_style
                if self.ch_attack_style == "o":
                    self.style = "Attack"
                    self.defence = 1 + who.side
                    self.attack = 1 + who.weapon
                    self.speed = 1
                elif self.ch_attack_style in ("d", "b"):
                    self.style = "Block!"
                    self.defence = 2 + who.side
                    self.attack = 0.5 + who.weapon
                    self.speed = 0
                elif self.ch_attack_style == "p":
                    self.style = "Throws a power attack!"
                    self.defence = 0.5 + who.side
                    self.attack = 3 + who.weapon
                    self.speed = 2
                elif self.ch_attack_style == "r":
                    self.style = "Retreat!"
                    self.defence = 2 + who.side
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
            def attack(attack, defence):
                damage = int(attack / ran(2, int(defence*0.1)))
                if damage < (defence*0.1):
                    damage = 0

                return damage
            global fight_timer
            
            time.sleep(1)
            hit = attack(fighter_stat.attack, (opponent_stat.defence))
            if hit > 0:
                opponent.health -= hit
                print ""
                print fighter.name, "hit", opponent.name, "using", fighter.weaponName
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
                print opponent.name, "Blocked", fighter.name, "using", opponent.sideName
                time.sleep(1)
            if opponent.health <= 0:
                opponent.health = 0
                opponent.life = False
                print ""
                print opponent.name, "is dead!"
                fight_timer = False

        print ""
        print "Enter battle tactic:"
        print "'d'-Defencive"
        print "'o'-Basic attack"
        print "'p'-Power attack"
        print "'r'-Run"
        print "'s'-Battle stats"
        chosen_move = ""
        while chosen_move not in ("d", "o", "p", "r"):
            chosen_move = raw_input("Enter now: ")
            if chosen_move == "s":
                clear()
                print "Enemy health:", enemy.health
                print "Enemy weapon:", enemy.weaponName
                print "Your health:", player.health
                print "Your weapon:", player.weaponName
                print "Your side:", player.sideName
        player_move = attack_style(chosen_move, player)
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
            if player_move.style == "Retreat!" :
                player_speed = 0
                return "run"
            elif player_speed > enemy_speed:
                return 1
            elif player_speed < enemy_speed:
                return 0
            else:
                return randint(0,1)

        clear()
        print player.name, "prepares to", player_move.style,
        time.sleep(1)
        print ""
        print enemy.name, "prepares to", enemy_move.style
        time.sleep(1)

        Who = who(enemy_move, player_move)
        if Who == 1:
            battle(player, enemy, temp_player, temp_enemy)
            if fight_timer:
                enemy.calls()
                time.sleep(2)
                battle(enemy, player, temp_enemy, temp_player)
        elif Who == 0:
            enemy.calls()
            time.sleep(2)
            battle(enemy, player, temp_enemy, temp_player)
            if fight_timer:
                battle(player, enemy, temp_player, temp_enemy)
        elif Who == "run" or player_move.style == "Retreat!":
            enemy.calls()
            time.sleep(2)
            battle(enemy, player, temp_enemy, temp_player)
            fight_timer = False
            if player.life:
                return 1
            else:
                return 0

        time.sleep(1)

def boss_animation():
    global playerboard
    work_xy = [0,0]
    tick = 0
    trail_text = "[ "
    boss_name = "BOSSANI WILL KILL YOU"
    for block in range(len(playerboard)):
        playerboard[len(playerboard)/2][tick] = wall_icon

    
    while True:
        playerboard[work_xy[0]][work_xy[1]] = trail_text[tick%len(trail_text)-1]
        tick += 1
        if work_xy[1] + int(1) <= (len(object_board)-1): #Boss animation 
            work_xy[1] += int(1)
        else:
            if (playerboard[work_xy[0] + 1][work_xy[1]]) not in (wall_icon):
                work_xy[0] += int(1)
                work_xy[1] = 0
            else: break
        time.sleep(bot_speed/4)
        clear()
        print_board(playerboard)
    work_xy = [0,0]
    time.sleep(bot_speed)
    for plays in range(8):
        tick = 0
        while True:
            playerboard[work_xy[0]][work_xy[1]] = boss_name[tick%len(trail_text)-1]
            tick += 1
            if work_xy[1] + int(1) <= (len(object_board)-1): 
                work_xy[1] += int(1)
            else:
                if (playerboard[work_xy[0] + 1][work_xy[1]]) not in (wall_icon):
                    work_xy[0] += int(1)
                    work_xy[1] = 0
                else: break
        work_xy = [0,0]
        clear()
        print_board(playerboard)
        time.sleep(bot_speed/4)

        while True:
            playerboard[work_xy[0]][work_xy[1]] = player_icon
            if work_xy[1] + int(1) <= (len(object_board)-1): 
                work_xy[1] += int(1)
            else:
                if (playerboard[work_xy[0] + 1][work_xy[1]]) not in (wall_icon):
                    work_xy[0] += int(1)
                    work_xy[1] = 0
                else: break
        work_xy = [0,0]
        clear()
        print_board(playerboard)
        time.sleep(bot_speed)

        while True:
            playerboard[work_xy[0]][work_xy[1]] = land_icon
            if work_xy[1] + int(1) <= (len(object_board)-1): 
                work_xy[1] += int(1)
            else:
                if (playerboard[work_xy[0] + 1][work_xy[1]]) not in (wall_icon):
                    work_xy[0] += int(1)
                    work_xy[1] = 0
                else: break
        work_xy = [0,0]
        work_xy = [0,0]
        clear()
        print_board(playerboard)
        time.sleep(bot_speed)

        while True:
            playerboard[work_xy[0]][work_xy[1]] = shop_icon
            if work_xy[1] + int(1) <= (len(object_board)-1): 
                work_xy[1] += int(1)
            else:
                if (playerboard[work_xy[0] + 1][work_xy[1]]) not in (wall_icon):
                    work_xy[0] += int(1)
                    work_xy[1] = 0
                else: break
        work_xy = [0,0]
        clear()
        print_board(playerboard)
        time.sleep(bot_speed)

        while True:
            playerboard[work_xy[0]][work_xy[1]] = land_icon
            if work_xy[1] + int(1) <= (len(object_board)-1): 
                work_xy[1] += int(1)
            else:
                if (playerboard[work_xy[0] + 1][work_xy[1]]) not in (wall_icon):
                    work_xy[0] += int(1)
                    work_xy[1] = 0
                else: break
        work_xy = [0,0]
        clear()
        print_board(playerboard)
    #playerboard[(len(playerboard)/3)-2][(len(playerboard)/2)] = boss_icon0
    playerboard[(len(playerboard)/3)-1][(len(playerboard)/2)-1] = boss_icon1
    playerboard[(len(playerboard)/3)-1][(len(playerboard)/2)] = boss_icon2
    object_board[(len(playerboard)/3)-1][(len(playerboard)/2)-1] = boss_icon1
    object_board[(len(playerboard)/3)-1][(len(playerboard)/2)] = boss_icon2
    #playerboard[(len(playerboard)/3)-1][(len(playerboard)/2)] = boss_icon3
    print_board(playerboard)


    
        




        


class Shop(): # move me to top
    def __init__(self):
        self.items = ["Basic knife       30  Gold", "Basic shield      60  Gold", "Steel sword       100  Gold", "Steel shield      145  Gold", "Ritchie's sword   400 Gold", "Ritchie's shield  650 Gold", "Access to zone 0  50  Gold"]
    def shop(self):
        clear()
        if playerboard[int(shop_wall_location[0])][0] != land_icon:
            self.items[6] = "Access to zone 0  50  Gold"
        if player.gold >= 0:
            print "Welcome to Ritchie's shop!"
            print ""
            counter = 0
            for stock in self.items:
                print str(counter) + ".", self.items[counter]
                counter += 1
            print str(counter) + ".", "Health            10  Gold"
            print ""
            print "Enter 'e' to exit"
            print "You have", player.gold, "gold"
            print ""
            buy = raw_input("Enter item number to buy item  -")
            if buy == "0" and self.items[0] != "SOLD" and player.gold >= 30:
                player.gold -= 30
                player.weapon = 1
                player.weaponName = "Knife"
                print "You have purchased a Basic knife!"
                self.items[0] = "SOLD"
                time.sleep(1)
                self.shop()

            elif buy == "1" and self.items[1] != "SOLD" and player.gold >= 60:
                player.gold -= 60
                player.side = 1
                player.sideName = "Shield"
                print "You have purchased a Basic shield!"
                self.items[1] = "SOLD"
                time.sleep(1)
                self.shop()

            elif buy == "2" and self.items[2] != "SOLD" and player.gold >= 100:
                player.gold -= 100
                player.weapon = 2
                player.weaponName = "Steel sword"
                print "You have purchased a Steel sword!"
                self.items[2] = "SOLD"
                time.sleep(1)
                self.shop()

            elif buy == "3" and self.items[3] != "SOLD" and player.gold >= 145:
                    player.gold -= 145
                    player.side = 2
                    player.sideName = "Steel shield"
                    print "You have purchased a Steel shield!"
                    self.items[3] = "SOLD"
                    time.sleep(1)
                    self.shop()

            elif buy == "4" and self.items[4] != "SOLD" and player.gold >= 400:
                    player.gold -= 400
                    player.weapon = 3
                    player.weaponName = "Ritchie's sword"
                    print "You have purchased Ritchie's sword!"
                    self.items[4] = "SOLD"
                    time.sleep(1)
                    self.shop()

            elif buy == "5" and self.items[5] != "SOLD" and player.gold >= 650:
                    player.gold -= 650
                    player.side = 3
                    player.sideName = "Ritchie's shield!"
                    print "You have purchased a Ritchie's shield!"
                    self.items[5] = "SOLD"
                    time.sleep(1)
                    self.shop()

            elif buy == "6" and player.gold >= 10 and playerboard[int(shop_wall_location[0])][0] != land_icon:
                    player.gold -= 10
                    print "You have purchased access to zone 0!"
                    playerboard[int(shop_wall_location[0])][0] = land_icon
                    self.items[6] = "ZONE 0 IS ACCESSABLE"
                    time.sleep(1)
                    self.shop()
            elif buy == "7":
                if player.health_check():
                    player.health += player.level *25
                    player.gold -= 10
                    self.shop()
                else:
                    clear()
                    print "You already have full heath!"
                    time.sleep(1)
                    self.shop()
            elif buy == "e":
                print "bye!"
                time.sleep(1)
            else:
                clear()
                print "You can't buy that!"
                time.sleep(1)
                self.shop()

        else:
            print "sorry! Looks like you're too poor to shop here :P"
            time.sleep(1)
            print "SLAM!"
            time.sleep(1)
shop_use = Shop()
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
        playerboard[player_xy[0]][player_xy[1]] = player_icon # The players location on the board is only temporary. 
        print_board(playerboard) # After print_board, the players location is replaced with the xy value from object board
        print ""

        playerboard[oldposision[0]][oldposision[1]] = object_board[oldposision[0]][oldposision[1]] # Make players current xy  == object (bandit icon etc)
        memory_board[oldposision[0]][oldposision[1]] += 1 #Block usage counter (You have stepped on this square x times)


        # Reactions to board icons
        if object_board[oldposision[0]][oldposision[1]] == bandit_icon:
            enemy = Enemy()
            battle_timer = 0
            GAME = fight(enemy)
            if player.life == True and GAME != 0 and not enemy.life:
                player.kills += 1
                player.xp += int((enemy.attack+enemy.defence)*randint(1, 4)/10*(battle_timer*0.5))
                player.gold += int((enemy.attack+enemy.defence)*.6)/battle_timer
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


        if playerboard[oldposision[0]][oldposision[1]] in (boss_icon0, boss_icon1, boss_icon2, boss_icon3):
            enemy = Boss()
            battle_timer = 0
            GAME = fight(enemy)
            if player.life == True and GAME != 0 and not enemy.life:
                player.kills += 1
                player.xp += int((enemy.attack+enemy.defence)*.3)
                player.gold += int((enemy.attack+enemy.defence)*.6)/battle_timer
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

        if object_board[oldposision[0]][oldposision[1]] == shop_icon:
            shop_use.shop()
            clear()
            print_board(playerboard)


        if object_board[oldposision[0]][oldposision[1]] == spawn_icon:
            ban_count = 0
            body_count = 0
            for test in playerboard:
                for test2 in test:
                    if test2 == bandit_icon:
                        ban_count += 1
                    if test2 == body_icon:
                        body_count += 1


            if ban_count == 0:
                player.gold += 25
                static_player = [player.attack, player.max_health, player.defence]
                Object_Placement(enemy_count, bandit_icon, "n", ((len(playerboard)/2)-1))
            if body_count >= 8:
                boss_animation()


        print "HP:", player.health, "  Level: ", player.level, "  Xp: ", player.xp, "  Gold: ", player.gold



        player.stat_check()
        if Still_alive == True:
            W = raw_input("w - a - s - d: ")
            if W == "bossani":
                boss_animation()
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