import heapq

reader = open('15_input.txt')
lines = []
try:
    for line in reader.readlines():
    	lines.append(line.replace('\n', ''))
finally:
    reader.close()

class Point(object):
	def __init__(self, row, col, val):
		self.row = row
		self.col = col
		self.val = val
		self.prevTotalCost = 0
		self.previousNode = None

	def getTotalCost(self):
		return self.prevTotalCost + self.val

	def toHash(self):
		return str(self.row)+','+str(self.col)

	def __lt__(self, other):
		return self.val < other.val

	def __le__(self, other):
		return self.val <= other.val

class PathAlgorithm(object):
	def pointToVisit(self, current_point, rowIncrease, colIncrease, pointMap, agenda):
		pointToVisit = pointMap[current_point.row+rowIncrease][current_point.col+colIncrease]
		if (pointToVisit.previousNode == None or pointToVisit.prevTotalCost > current_point.getTotalCost()):
			pointToVisit.previousNode = current_point
			pointToVisit.prevTotalCost = current_point.getTotalCost()
			heapq.heappush(agenda, (current_point.getTotalCost(), pointToVisit))

	def get_path(self, start, goal, riskmap):
		maxCol = len(riskmap[0])-1
		maxRow = len(riskmap)-1
		print(maxRow, maxCol, goal.toHash())
		pointMap = []
		for rowIndex in range(maxRow+1):
			pointRow = []
			for colIndex in range(maxCol+1):
				pointRow.append(Point(rowIndex, colIndex, riskmap[rowIndex][colIndex]))
			pointMap.append(pointRow)
		agenda = []
		heapq.heappush(agenda, (0, start))
		while len(agenda) > 0 and start.toHash() != goal.toHash():
			(cost, current_point) = heapq.heappop(agenda)
			if (cost > current_point.getTotalCost()):
				continue
			if (current_point.col > 0):
				self.pointToVisit(current_point, 0, -1, pointMap, agenda)
			if (current_point.col < maxCol):
				self.pointToVisit(current_point, 0, 1, pointMap, agenda)
			if (current_point.row > 0):
				self.pointToVisit(current_point, -1, 0, pointMap, agenda)
			if (current_point.row < maxRow):
				self.pointToVisit(current_point, 1, 0, pointMap, agenda)
		print(pointMap[goal.row][goal.col].getTotalCost())

def rowPlusOne(row):
	return [val+1 if val < 9 else 1 for val in row]

def makeRiskMapLarger(riskmap):
	new_risk_map = []
	cur_horizontal_riskmap = []
	for row in riskmap:
		new_row = row
		last_row = row
		for i in range(4):
			last_row = rowPlusOne(last_row)
			new_row.extend(last_row)
		cur_horizontal_riskmap.append(new_row)
	new_risk_map.extend(cur_horizontal_riskmap)
	for i in range(4):
		new_horizontal_riskmap = []
		for row in cur_horizontal_riskmap:
			new_horizontal_riskmap.append(rowPlusOne(row))
		new_risk_map.extend(new_horizontal_riskmap)
		cur_horizontal_riskmap = new_horizontal_riskmap
	return new_risk_map

#main
def main():
	riskmap = [[int(character) for character in line] for line in lines]
	riskmap = makeRiskMapLarger(riskmap)
	pathAlgo = PathAlgorithm()
	path = pathAlgo.get_path(Point(0,0,0), Point(len(riskmap)-1, len(riskmap[0])-1, riskmap[len(riskmap)-1][len(riskmap[0])-1]), riskmap)
	

	print(f"answer:")

main()