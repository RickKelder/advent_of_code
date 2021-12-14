reader = open('14_input.txt')
lines = []
try:
    for line in reader.readlines():
    	lines.append(line.replace('\n', ''))
finally:
    reader.close()

def swap_polymers(current_polymer, polymer_templates):
	new_string = ""
	for i in range(len(current_polymer)):
		if (i != 0):
			key = current_polymer[i-1]+current_polymer[i]
			if key in polymer_templates:
				new_string = new_string + current_polymer[i-1] + polymer_templates[key]
	return new_string + current_polymer[-1]

#main
def main():
	unique_characters = set()
	polymer_templates = {}
	current_polymer = ""
	for line in lines:
		if "->" in line:
			splitted_line = line.split(" -> ");
			polymer_templates[splitted_line[0]] = splitted_line[1]
			unique_characters.add(splitted_line[1])
		elif not(line == ""):
			current_polymer	= line
			for char in current_polymer:
				unique_characters.add(char)

	rounds = 10
	for current_round in range(rounds):
		current_polymer = swap_polymers(current_polymer, polymer_templates)

	min_chars = max_chars = -1
	for char in unique_characters:
		count_char = current_polymer.count(char)
		if min_chars == -1 or count_char < min_chars:
			min_chars = count_char
		if max_chars == -1 or count_char > max_chars:
			max_chars = count_char

	print(f"answer:", max_chars-min_chars)

main()