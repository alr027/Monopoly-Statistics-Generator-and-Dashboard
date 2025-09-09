import random;

#START: DATA COLLECTION PARAMETERS
players = input("Number of Players (2-8): ")
try:
    players = int(players)
    if players > 8 or players < 2:
        print("Invalid: out of range; Reverting to default of 4.")
        players = 4
except:
    print("Invalid: non-integer; Reverting to default of 4.")
    players = 4
turns = input("Turns per Player (1-200): ")
try:
    turns = int(turns)
    if turns < 1 or turns > 200:
        print("Invalid: out of range; Reverting to default of 90.")
        turns = 90
except:
    print("Invalid: non-integer; Reverting to default of 90.")
    turns = 90
games = input("Number of Games (1-1000): ")
try: 
    games = int(games)
    if games < 1 or games > 1000:
        print("Invalid: out of range; Reverting to default of 100.")
        games = 100
except:
    print("Invalid: non-integer; Reverting to default of 100.")
    games = 100
#END: DATA COLLECTION PARAMETERS
data_sheet = open("Monopoly_Generated_Data.txt", "w")
data_sheet.write("game_num,player_num,turn_num,die1,die2,roll_total,space1,adv_to_space,board_laps\n")

#START: VARIABLE, CARD, AND SPACE DEFINITIONS
die1 = 0
die2 = 0
doubles_count = 0
jail_count = 0
player_location = 0
grid_space = 2
chance_spaces = [7,22,36]
comm_chest_spaces = [2,17,33]
jail_free = []
chance_cards = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]  
    #1 = adv to space 39(Boardwalk)
    #2 = adv to space 0(Go)
    #3 = adv to space 24(Illionis Ave)
    #4 = adv to space 11(St.Charles Pl)
    #5 = adv to space 5,15,25,or 35[nearest railroad]
    #6 = adv to space 5,15,25,or 35[nearest railroad]
    #7 = adv to space 12 or 28[nearest utility]
    #8 = jail_free("chance")
    #9 = adv -3 spaces
    #10 = adv to jail
    #11 = adv to space 5(reading railroad)
    #12-16 = no movement
comm_chest_cards = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    #1 = adv to space 0(Go)
    #2 = jail_free("comm_chest")
    #3 = adv to jail
    #4-16 = no movement
#END: VARIABLE, CARD, AND SPACE DEFINITIONS

#START: DATA COLLECTION
g=1
while g<=games:      #num of games (100 defualt)
    #Shuffle chance and comm chest cards
    random.shuffle(chance_cards)
    random.shuffle(comm_chest_cards)

    p=1
    while p<=players:   #player count (4 default)
        board_laps = 0
        
        i=1
        while i<=turns:      #rolls per player per game (90 default)
            #write turn, player, & game iteration count
            data_sheet.write(str(g)+",")
            data_sheet.write(str(p)+",")
            data_sheet.write(str(i)+",")

            #roll dice and write rolls
            die1 = random.randint(1,6)
            data_sheet.write(str(die1)+",")
            die2 = random.randint(1,6)
            data_sheet.write(str(die2)+",")
            data_sheet.write(str(die1+die2)+",")

            #if in jail
            if player_location == -1:
                if jail_count == 2:
                    player_location = 10 + die1 + die2
                    jail_count = 0
                elif die1 == die2:
                    player_location = 10 + die1 + die2
                    jail_count = 0
                elif "chance" in jail_free:
                    jail_free.remove("chance")
                    chance_cards.append(8)
                    player_location = 10 + die1 + die2
                    jail_count = 0
                elif "comm_chest" in jail_free:
                    jail_free.remove("comm_chest")
                    comm_chest_cards.append(2)    
                    player_location = 10 + die1 + die2   
                    jail_count = 0
                else:
                    jail_count += 1      
            else:
                player_location += die1 + die2

            #if doubles, 3 in row = jail
            if die1 == die2:
                doubles_count += 1
            else:
                doubles_count = 0
            if doubles_count >= 3:
                player_location = -1
                doubles_count = 0

            #circled the board
            if player_location >= 40:
                player_location -= 40
                board_laps += 1
            
            #write location
            data_sheet.write(str(player_location)+",")

            #Chance card landing conditions
            if player_location in chance_spaces:
                #1=adv to space 39(Boardwalk)
                if chance_cards[0] == 1:
                    player_location = 39
                    data_sheet.write(str(player_location)+",")
                    chance_cards.append(chance_cards.pop(0))
                #2=adv to space 0(Go)
                elif chance_cards[0] == 2:
                    player_location = 0
                    data_sheet.write(str(player_location)+",")
                    chance_cards.append(chance_cards.pop(0))
                #3=adv to space 24(Illionis Ave)
                elif chance_cards[0] == 3:
                    player_location = 24
                    data_sheet.write(str(player_location)+",")
                    chance_cards.append(chance_cards.pop(0))
                #4=adv to space 11(St.Charles Pl)
                elif chance_cards[0] == 4:
                    player_location = 11
                    data_sheet.write(str(player_location)+",")
                    chance_cards.append(chance_cards.pop(0))
                #5=adv to space 5,15,25,or 35[nearest railroad]
                elif chance_cards[0] == 5:
                    if 5 > player_location > 35:
                        player_location = 5
                    elif player_location < 15:
                        player_location = 15
                    elif player_location < 25:
                        player_location = 25
                    elif player_location < 35:
                        player_location = 35
                    data_sheet.write(str(player_location)+",")
                    chance_cards.append(chance_cards.pop(0))
                #6=adv to space 5,15,25,or 35[nearest railroad]
                elif chance_cards[0] == 6:
                    if player_location < 5 or player_location >= 35:
                        player_location = 5
                    elif player_location < 15:
                        player_location = 15
                    elif player_location < 25:
                        player_location = 25
                    else:
                        player_location = 35                    
                    data_sheet.write(str(player_location)+",")
                    chance_cards.append(chance_cards.pop(0))
                #7=adv to space 12 or 28[nearest utility]
                elif chance_cards[0] == 7:
                    if player_location < 12 or player_location >= 28:
                        player_location = 12
                    else:
                        player_location = 28
                    data_sheet.write(str(player_location)+",")
                    chance_cards.append(chance_cards.pop(0))
                #8=jail_free + chance
                elif chance_cards[0] == 8:
                    jail_free.append("chance")
                    data_sheet.write(",")
                    chance_cards.remove(8)
                #9=adv -3 spaces
                elif chance_cards[0] == 9:
                    player_location -= 3
                    data_sheet.write(str(player_location)+",")
                    chance_cards.append(chance_cards.pop(0))
                #10=adv to jail
                elif chance_cards[0] == 10:
                    player_location = -1
                    data_sheet.write(str(player_location)+",")
                    chance_cards.append(chance_cards.pop(0))
                #11=adv to space 5(reading railroad)
                elif chance_cards[0] == 11:
                    player_location = 5
                    data_sheet.write(str(player_location)+",")
                    chance_cards.append(chance_cards.pop(0))
                else:
                    data_sheet.write(",")
                    chance_cards.append(chance_cards.pop(0)) 

            #Comm_chest card landing conditions
            elif player_location in comm_chest_spaces:
                #1=adv to space 0(Go)
                if comm_chest_cards[0] == 1:
                    player_location = 0
                    data_sheet.write(str(player_location)+",")
                    comm_chest_cards.append(comm_chest_cards.pop(0))
                #2=jail_free +3
                elif comm_chest_cards[0] == 2:
                    jail_free.append("comm_chest")
                    data_sheet.write(",")
                    comm_chest_cards.remove(2)
                #3=adv to jail
                elif comm_chest_cards[0] == 3:
                    player_location = -1
                    data_sheet.write(str(player_location)+",")
                    comm_chest_cards.append(comm_chest_cards.pop(0))
                else:
                    data_sheet.write(",")                    
                    comm_chest_cards.append(comm_chest_cards.pop(0))

            #go to jail space
            elif player_location == 30:
                player_location = -1
                data_sheet.write(str(player_location)+",")
            
            #start new row for new turn
            else:
                data_sheet.write(",")

            data_sheet.write(str(board_laps)+"\n")

            #adv turn iterations
            grid_space += 1
            i += 1
        
        #adv player iterations
        p+=1

    #adv game iterations
    if 8 not in chance_cards:
        chance_cards.append(8)
    if 2 not in comm_chest_cards:
        comm_chest_cards.append(2)

    #to track progress of data generation
    print("Finished game", g)
    g+=1
#END: DATA COLLECTION
print("DATA COLLECTION COMPLETE. ENDING PROGRAM.")

data_sheet.close()
