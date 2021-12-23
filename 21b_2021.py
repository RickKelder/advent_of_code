import copy
import itertools
from collections import defaultdict

reader = open('21_input.txt')
lines = []
try:
    for line in reader.readlines():
    	lines.append(line.replace('\n', ''))
finally:
    reader.close()
#    0     12    3     45      6
# pos1 score1 pos2 score2 player

def default_value_combination_dict():
	return 0

def create_combinations():
	combinations = defaultdict(default_value_combination_dict)
	for combination in list(map(lambda tup: int(tup[0])+int(tup[1])+int(tup[2]), list(itertools.product('123', repeat=3)))):
		combinations[combination] += 1
	return combinations

def add_to_open_games(gamehash, num, open_games):
	if gamehash not in open_games:
		open_games[gamehash] = 0
	open_games[gamehash] += num

def string_replace(gamehash, index_from, index_to, new_string):
	return gamehash[:index_from] + new_string + gamehash[index_to:]

def do_round(open_games, winners, combinations):
	gamehash = next(iter(open_games))
	num = open_games.pop(gamehash)
	player = (int(gamehash[6])+1)%2
	player_increment = 3*player
	for combination in combinations:
		new_pos = (int(gamehash[0+player_increment])+combination)%10
		new_game_hash = string_replace(gamehash, 0+player_increment, 1+player_increment, str(new_pos))
		new_score = int(new_game_hash[1+player_increment:3+player_increment]) + (10 if new_pos == 0 else new_pos)
		if new_score >= 21:
			winners[player] += num*combinations[combination]
		else:
			new_game_hash = string_replace(new_game_hash, 1+player_increment, 3+player_increment, str(new_score).zfill(2))
			new_game_hash = new_game_hash[:-1]+str(player)
			add_to_open_games(new_game_hash, num*combinations[combination], open_games)

#main
def main():
	die = 1
	player = 1 #start reversed so we can flip it back to first in the do_round
	open_games = {}
	add_to_open_games(lines[0][-1]+'00'+lines[1][-1]+'001', 1, open_games)
	winners = [0, 0]
	combinations = create_combinations()
	while len(open_games) > 0:
		do_round(open_games, winners, combinations)

	print(f"answer:", winners)

main()

# 444356092776315, 341960390180808
# 444356092776315, 341960390180808