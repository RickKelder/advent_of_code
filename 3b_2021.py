reader = open('3_input.txt')
lines = []
try:
    for line in reader.readlines():
    	lines.append(line.replace('\n', ''))
finally:
    reader.close()

def next_most_common(list_breakdown, binary, is_oyxgen):
	column_total = [sum(column) for column in zip(*list_breakdown)]
	most_common_list = list(map(lambda total: total >= len(list_breakdown)/2, column_total)) if is_oyxgen else list(map(lambda total: total < len(list_breakdown)/2, column_total))
	filtered_list = filter(lambda integerlist: int(bool(integerlist[0]) == most_common_list[0]), list_breakdown)
	binary = binary + str(int(most_common_list[0]))
	new_filtered_list = list(map(lambda sublist: sublist[1:], filtered_list))
	if len(new_filtered_list) > 1:
		return next_most_common(new_filtered_list, binary, is_oyxgen)
	if len(most_common_list) > 1:
		binary = binary + ''.join([str(x) for x in new_filtered_list[0]])
	return binary

#real stuff
list_breakdown = [list(map(int, list(line))) for line in lines]
oxygen_generator = int(next_most_common(list_breakdown, '', True),2);
co2_scrubber = int(next_most_common(list_breakdown, '', False),2);

print(f"done", oxygen_generator, co2_scrubber, oxygen_generator * co2_scrubber)