import math

reader = open('14_input.txt')
lines = []
try:
    for line in reader.readlines():
    	lines.append(line.replace('\n', ''))
finally:
    reader.close()

def add_amount(obj, key, amount):
	if key in obj:
		obj[key] += amount
	else:
		obj[key] = amount

def add_one(obj, key):
	add_amount(obj, key, 1)

def swap_polymers(current_polymer, polymer_templates):
	new_polymer = {}
	for key in current_polymer:
		new_polymer[key] = current_polymer[key]
	for key in current_polymer:
		if (current_polymer[key] > 0):
			new_char = polymer_templates[key]
			new_polymer[key] -= current_polymer[key]
			add_amount(new_polymer, key[0]+new_char, current_polymer[key])
			add_amount(new_polymer, new_char+key[1], current_polymer[key])
	return new_polymer

#main
def main():
	polymer_templates = {}
	current_polymer = {}
	for line in lines:
		if "->" in line:
			splitted_line = line.split(" -> ");
			polymer_templates[splitted_line[0]] = splitted_line[1]
		elif not(line == ""):
			for i in range(len(line)):
				if (i != 0):
					add_one(current_polymer, line[i-1]+line[i])

	rounds = 40
	for current_round in range(rounds):
		current_polymer = swap_polymers(current_polymer, polymer_templates)

	character_count = {}
	for key in current_polymer:
		add_amount(character_count, key[0], current_polymer[key])
		add_amount(character_count, key[1], current_polymer[key])
	min_chars = max_chars = -1
	for char in character_count:
		character_count[char] = math.ceil(character_count[char]/2)
		count_char = character_count[char]
		if min_chars == -1 or count_char < min_chars:
			min_chars = count_char
		if max_chars == -1 or count_char > max_chars:
			max_chars = count_char
	

	print(f"answer:", max_chars - min_chars)

main()