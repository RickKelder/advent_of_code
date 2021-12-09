reader = open('9_input.txt')
lines = []
try:
    for line in reader.readlines():
    	lines.append(line.replace('\n', ''))
finally:
    reader.close()

class Point(object):
	def __init__(self, y, x):
		self.X = x
		self.Y = y

	def toHash(self):
		return str(self.Y)+','+str(self.X)

def flood(heightmap, point, points_visited):
	if (point.toHash() in points_visited):
		return
	# print("visiting", point.toHash())
	points_visited.append(point.toHash())
	if point.Y > 0 and heightmap[point.Y-1][point.X] != 9:
		flood(heightmap, Point(point.Y-1, point.X), points_visited)
	if point.Y < len(heightmap)-1 and heightmap[point.Y+1][point.X] != 9:
		flood(heightmap, Point(point.Y+1, point.X), points_visited)
	if point.X > 0 and heightmap[point.Y][point.X-1] != 9:
		flood(heightmap, Point(point.Y, point.X-1), points_visited)
	if point.X < len(heightmap[0])-1 and heightmap[point.Y][point.X+1] != 9:
		flood(heightmap, Point(point.Y, point.X+1), points_visited)
	return points_visited

#main
def main():
	heightmap = [[int(character) for character in line] for line in lines]
	lowestmap = []
	bassins = []
	for y in range(len(heightmap)):
		lowestmap.append([])
		for x in range(len(heightmap[0])):
			current_value = heightmap[y][x]
			lowestmap[y].append(
				(y == 0 or current_value < heightmap[y-1][x]) and (x == 0 or current_value < heightmap[y][x-1]) and
				(y == len(heightmap)-1 or current_value < heightmap[y+1][x]) and (x == len(heightmap[0])-1 or current_value < heightmap[y][x+1])
			)
			if (lowestmap[y][x]):
				bassins.append(flood(heightmap, Point(y, x), []))

	bassin_lengths = [len(bassin) for bassin in bassins]
	answer = 1
	for i in range(3):
		answer = answer * max(bassin_lengths)
		bassin_lengths.remove(max(bassin_lengths))

	print(f"answer:", answer)

main()