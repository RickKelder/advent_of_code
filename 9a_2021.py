reader = open('9_input.txt')
lines = []
try:
    for line in reader.readlines():
    	lines.append(line.replace('\n', ''))
finally:
    reader.close()

#main
def main():
	heightmap = [[int(character) for character in line] for line in lines]
	lowestmap = []
	heightmap_sum = 0
	for y in range(len(heightmap)):
		lowestmap.append([])
		for x in range(len(heightmap[0])):
			current_value = heightmap[y][x]
			lowestmap[y].append(
				(y == 0 or current_value < heightmap[y-1][x]) and (x == 0 or current_value < heightmap[y][x-1]) and
				(y == len(heightmap)-1 or current_value < heightmap[y+1][x]) and (x == len(heightmap[0])-1 or current_value < heightmap[y][x+1])
			)
			if lowestmap[y][x]:
				heightmap_sum += int(current_value)+1
	# print(heightmap)
	# print(lowestmap)

	print(f"answer:", heightmap_sum)

main()