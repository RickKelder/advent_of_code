reader = open('2_input.txt')
lines = []
try:
    for line in reader.readlines():
    	lines.append(line)
finally:
    reader.close()

#real stuff
instructions = [line.split() for line in lines]
instructions = map(lambda splittedLine: (splittedLine[0], int(splittedLine[1])), instructions)
horizontal = depth = 0
for (instruction,value) in instructions:
	horizontalMultiplier = (1 if instruction == "forward" else 0)
	verticalMultiplier = (1 if instruction == "down" else (-1 if instruction == "up" else 0))
	#print(instruction, horizontalIncrease, verticalIncrease)
	horizontal = horizontal + value * horizontalMultiplier
	depth = depth + value * verticalMultiplier

print(f"done", horizontal * depth)