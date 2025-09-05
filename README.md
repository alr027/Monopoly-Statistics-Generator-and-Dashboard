README
File references are relative. Keep all files in the same location.

"Monopoly_Data_Generation.py"
Program prompts user to input desired number of players per game (2-8, 4 default), the number of turns per player (1-200, default 90), and desired number of games (1-1000, default 100) to run.
If no "Monopoly_Generated_Data.txt" file exists, one will be created; otherwise, the current file will be overwritten.
Data is writen into the "Monopoly_Generated_Data.txt" file by "game_num,player_num,turn_num,die1,die2,roll_total,space1,adv_to_space,board_laps".

"Monopoly_Generated_Data.txt" 
Holds comma seperated integers for "game_num,player_num,turn_num,die1,die2,roll_total,space1,adv_to_space,board_laps". Is created or overwritten with each run of "Monopoly_Data_Generation.py".

"Monopoly_Dashboard.xlsx"
Imports "Monopoly_Generated_Data.txt" data to the "Monopoly_Generated_Data" sheet.
"calc_sheet" assigns the names of spaces to their types and counts the number of times each appeared in the imported data. It also counts the min, max, total, and average board laps per player and the roll and die counts.
"pivots" groups the times landed on each space by their space type and totals them.
"dashboard" shows graphics for landing frequencies by space name and space type with a splicer to filter for desired space types. Additional graphics show the average roll total, the average die outcome, and the min, max, and avg board laps per player per game.
NOTE: Use "Refresh All" from the data ribbon each time the "Monopoly_Generated_Data.txt" file is changed or the dashboard with show the old data.
