data_input = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

#configurazione iniziale
red_cubes = 12
green_cubes = 13
blue_cubes = 14

possible_games_sum = 0
#ogni game
for game in data_input.split('\n'):
  
    game_info = game.split(':')
    game_number = int(game_info[0].split()[1])
    sets_data = game_info[1].split(';')
    possible_game = True

    #ogni set
    for set_data in sets_data:
        elements = set_data.strip().split(', ')
        #controlla elementi
        for element in elements:
            parts = element.split()
            color = parts[1]
            count = int(parts[0])
            if (color == 'red' and count > red_cubes) or \
               (color == 'green' and count > green_cubes) or \
               (color == 'blue' and count > blue_cubes):
                possible_game = False
                break
    
    #game fattibile
    if possible_game:
        possible_games_sum += game_number

print(possible_games_sum)


#---------------------------------------------------------------------------------------
#PART TWO

sumpower = 0
#ogni game
for game in data_input.split('\n'):
  
    game_info = game.split(':')
    game_number = int(game_info[0].split()[1])
    sets_data = game_info[1].split(';')
    possible_game = True
    
    temp_red = 0
    temp_blue = 0 
    temp_grern = 0
    #ogni set
    for set_data in sets_data:
        elements = set_data.strip().split(', ')
        #controlla elementi
        for element in elements:
            parts = element.split()
            color = parts[1]
            count = int(parts[0])
            #in ogni set 
            if (color == 'red' and count > temp_red):
                temp_red = count
            if (color == 'green' and count > temp_grern):
                temp_grern = count
            if (color == 'blue' and count > temp_blue):
                temp_blue = count
        
    power =  temp_blue * temp_grern * temp_red   
    sumpower += power


print(sumpower)
