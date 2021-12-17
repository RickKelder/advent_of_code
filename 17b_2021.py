import math
reader = open('17_input.txt')
lines = []
try:
    for line in reader.readlines():
    	lines.append(line.replace('\n', ''))
finally:
    reader.close()

def findAllY(minY, maxY, minX, maxX):
	print(minY, maxY)
	combinations = 0
	for x in range(100):
		direction = (1, -1)[x<0]
		for y in range(-200, 200):
			currentX = currentY = 0
			xVelocity = x
			yVelocity = y
			while currentX <= maxX and currentY >= minY:
				if currentX >= minX and currentX <= maxX and currentY >= minY and currentY <= maxY:
					combinations += 1
					break
				currentX += xVelocity
				currentY += yVelocity
				if (xVelocity != 0):
					xVelocity -= direction
				yVelocity -= 1
	return combinations

#main
def main():
	splitted_line = lines[0].split(", y=")
	xTarget = [int(x) for x in splitted_line[0].replace("target area: x=", "").split("..")]
	yTarget = [int(y) for y in splitted_line[1].split("..")]

	allCombinations = findAllY(yTarget[0], yTarget[1], xTarget[0], xTarget[1])

	print(xTarget, yTarget, allCombinations)

main()