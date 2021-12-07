reader = open('7_input.txt')
lines = []
try:
    for line in reader.readlines():
    	lines.append(line.replace('\n', ''))
finally:
    reader.close()

def calcFuelCost(crab_submarines, target):
	return sum(map(lambda num: ((abs(num-target)+1)/2)*abs(num-target), crab_submarines))

#main
def main():
	crab_submarines = list(map(int, lines[0].split(",")))
	end_target = start_target = round(sum(crab_submarines)/len(crab_submarines))
	fuel_cost_left = fuel_cost_right = fuel_cost = calcFuelCost(crab_submarines, end_target)
	increment_right = increment_left = 0
	while fuel_cost_left <= fuel_cost:
		fuel_cost = fuel_cost_left
		end_target = start_target + increment_left
		fuel_cost_left = calcFuelCost(crab_submarines, end_target + 1)
		print ("left", fuel_cost_left, fuel_cost)
		increment_left += 1;
	while fuel_cost_right <= fuel_cost:
		fuel_cost = fuel_cost_right
		end_target = start_target + increment_right
		fuel_cost_right = calcFuelCost(crab_submarines, end_target - 1)
		print ("right", fuel_cost_right, fuel_cost)
		increment_right += -1;

	print(f"answer:", start_target, end_target, fuel_cost_left, fuel_cost_right, fuel_cost)

main()