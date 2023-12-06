import re

def game_possible(game:list, game_powers:list):
    '''
    Across game in a game, find the maximum value for each color cube and determine
        1) if the game is possible, return bool
        2) the power of the minimum cubes to make game possible
    '''
    color_max = {'red': 12, 'green': 13, 'blue': 14}
    game_max = {'red': 0, 'green': 0, 'blue': 0}
    power = 1
    possible = True
    for draw in game:
        color_counts = draw.split(',')
        for cc in color_counts:
            n = int(re.findall(r'\d+', cc)[0])
            color = re.findall("[a-zA-Z]+", cc)[0]
            if n > game_max[color]: # Colors will always be red/green/blue
                game_max[color] = n
            if (n > color_max[color]) & (possible): # Colors will always be red/green/blue
                possible = False
    
    for val in game_max.values():
        power = power * val
    game_powers.append(power)
    return possible
            

def parse_line(line:str, possible_games:list, game_powers:list):
    '''
    Process text for a single game and calculate possibility scenarios
    '''
    colon_split = line.split(":")
    game_number = int(re.findall(r'\d+', colon_split[0])[0])
    game = colon_split[1].split(";")
    possible = game_possible(game, game_powers)

    if possible:
        possible_games.append(game_number)


if __name__ == "__main__":
    FILEPATH = 'day2.txt'
    with open(FILEPATH) as f:
        raw = f.readlines()
        lines = [i.strip('\n') for i in raw]
        possible_games = []
        game_powers = []
        for line in lines:
            parse_line(line, possible_games, game_powers)
        
        print(f'Sum of possible games {sum(possible_games)}')
        print(f'Sum of game powers {sum(game_powers)}')