reader = open('21_input.txt')
lines = []
try:
    for line in reader.readlines():
    	lines.append(line.replace('\n', ''))
finally:
    reader.close()

#main
def main():
	players_position = [int(lines[0][-1]), int(lines[1][-1])]
	players_score = [0, 0]
	die = 1
	player = 0
	while max(players_score) < 1000:
		positions_to_add = die%100+(die+1)%100+(die+2)%100
		players_position[player] = (players_position[player]+positions_to_add)%10
		players_score[player] += 10 if players_position[player] == 0 else players_position[player]
		die += 3
		player = (player+1)%2
		
	print(f"answer:", (die-1)*min(players_score))

main()