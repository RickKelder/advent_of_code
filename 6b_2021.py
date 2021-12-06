reader = open('4_input.txt')
lines = []
try:
    for line in reader.readlines():
    	lines.append(line.replace('\n', ''))
finally:
    reader.close()

def getBoards():
	boards = []
	newBoardMatrix = []
	for line in lines[2:]:
		if line == "":
			boards.append(Board(newBoardMatrix))
			newBoardMatrix = []
		else:
			newBoardMatrix.extend([number for number in map(int, line.replace("  ", " ").split())])
	boards.append(Board(newBoardMatrix))
	return boards

class Board:
	def __init__(self, matrix):
		self.matrix = matrix
		self.marked = [0 for i in range(len(self.matrix))] 
		self.winIndex = -1

	def mark(self, number):
		if number in self.matrix:
			self.marked[self.matrix.index(number)] = 1

	def isWinning(self):
		rows = [sum(self.marked[i:i+5]) for i in range(0, len(self.marked), 5)]
		columns = [sum(self.marked[i::5]) for i in range(5)]
		return (5 in rows or 5 in columns)

	def getUnmarkedSum(self):
		returnSum = 0
		for i in range(len(self.matrix)):
			if self.marked[i] == 0:
				returnSum += self.matrix[i]
		return returnSum

	def setWinIndex(self, winIndex, lastNumber):
		self.winIndex = winIndex
		self.lastNumber	= lastNumber

def getWinningBoard(boards):
	for i in range(len(numbersToDraw)):
		for board in boards:
			board.mark(numbersToDraw[i])
			if board.isWinning():
				return (numbersToDraw[i], board)

def getLosingBoard(boards):
	for i in range(len(numbersToDraw)):
		for board in boards:
			if board.winIndex == -1:
				board.mark(numbersToDraw[i])
				if board.isWinning():
					board.setWinIndex(i, numbersToDraw[i])
	maxBoard = boards[0]
	for board in boards:
		if board.winIndex > maxBoard.winIndex:
			maxBoard = board
	return (maxBoard.lastNumber, maxBoard)

#real stuff

numbersToDraw = list(map(int, lines[0].split(',')))
boards = getBoards()
(lastNumber, winningBoard) = getWinningBoard(boards)
(lastLosingNumber, losingBoard) = getLosingBoard(boards)

print(f"answer", lastLosingNumber, losingBoard.getUnmarkedSum(), lastLosingNumber*losingBoard.getUnmarkedSum())