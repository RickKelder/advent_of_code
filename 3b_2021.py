reader = open('3_input.txt')
lines = []
try:
    for line in reader.readlines():
    	lines.append(line.replace('\n', ''))
finally:
    reader.close()

def next_most_common(list_breakdown, binary, is_oyxgen):
	most_common_list = get_most_common_list(list_breakdown, is_oyxgen)
	filtered_list = filter(lambda integerlist: int(bool(integerlist[0]) == most_common_list[0]), list_breakdown)
	new_filtered_list = list(map(lambda sublist: sublist[1:], filtered_list))
	binary = new_binary(binary, most_common_list, new_filtered_list);
	if len(new_filtered_list) > 1:
		return next_most_common(new_filtered_list, binary, is_oyxgen)
	return binary

def get_most_common_list(list_to_get, is_oyxgen):
	column_total = [sum(column) for column in zip(*list_to_get)]
	return list(map(lambda total: total >= len(list_to_get)/2, column_total)) if is_oyxgen else list(map(lambda total: total < len(list_to_get)/2, column_total))

def new_binary(binary, most_common_list, new_filtered_list):
	binary += str(int(most_common_list[0]))
	return binary if len(new_filtered_list) > 1 or len(most_common_list) <= 1 else binary+''.join([str(x) for x in new_filtered_list[0]])

#real stuff
list_breakdown = [list(map(int, list(line))) for line in lines]
oxygen_generator = int(next_most_common(list_breakdown, '', True),2);
co2_scrubber = int(next_most_common(list_breakdown, '', False),2);

print(f"answer:", oxygen_generator * co2_scrubber)