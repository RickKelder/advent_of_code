reader = open('6_input.txt')
lines = []
try:
    for line in reader.readlines():
    	lines.append(line.replace('\n', ''))
finally:
    reader.close()

#main
simulate_days = 80

def age_one_day(age_array):
	update_fish = age_array.pop(0)
	age_array.append(0)
	age_array[6] += update_fish
	age_array[8] += update_fish

def main():
	start_time = time.time()
	initial_fish = list(map(int, lines[0].split(",")))
	age_array = [0 for i in range(9)]
	for fish_age in initial_fish:
		age_array[fish_age] += 1
	for i in range(simulate_days):
		age_one_day(age_array)

	print(sum(age_array))

main()