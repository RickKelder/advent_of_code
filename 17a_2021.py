import math
reader = open('17_input.txt')
lines = []
try:
    for line in reader.readlines():
    	lines.append(line.replace('\n', ''))
finally:
    reader.close()

def findLowestX(minX, maxX):
	direction = (1, -1)[minX<0]
	currentX = 0
	foundTarget = False
	while not(foundTarget):
		currentX += direction
		foundTarget = (currentX*(currentX+1))/2 >= minX and (currentX*(currentX+1))/2 <= maxX
	return currentX

def checkY(startVelocityY, minSteps, minY, maxY):
	velocityY = startVelocityY
	currentY = 0
	while (currentY > maxY and not(currentY >= minY and currentY <= maxY)) or abs(velocityY) < minSteps:
		currentY += velocityY
		velocityY -= 1
	return currentY >= minY and currentY <= maxY

def findHighestY(lowestX, minY, maxY):
	bestY = 0
	for i in range(1000):
		if(checkY(i, lowestX, minY, maxY)):
			bestY = i
	return bestY

#main
def main():
	splitted_line = lines[0].split(", y=")
	xTarget = [int(x) for x in splitted_line[0].replace("target area: x=", "").split("..")]
	yTarget = [int(y) for y in splitted_line[1].split("..")]

	lowestX = findLowestX(xTarget[0], xTarget[1])
	highestY = findHighestY(lowestX, yTarget[0], yTarget[1])

	print(xTarget, yTarget, lowestX, highestY, (highestY*(highestY+1))/2)

main()