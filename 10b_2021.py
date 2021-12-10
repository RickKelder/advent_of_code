reader = open('10_input.txt')
lines = []
try:
    for line in reader.readlines():
    	lines.append(line.replace('\n', ''))
finally:
    reader.close()

def check_command(command):
	open_symbols = []
	for char in command:
		if char in "[({<":
			open_symbols.append(char)
		if char in "])}>":
			symbol_to_check = open_symbols.pop()
			# print("checking", symbol_to_check, ord(symbol_to_check), char, ord(char))
			if not(ord(symbol_to_check) == ord(char)-1 or ord(symbol_to_check) == ord(char)-2):
				return None
	return open_symbols

def get_completion(open_symbols):
	completion = []
	for char in list(reversed(open_symbols)):
		match char:
			case '(': completion.append(')')
			case '[': completion.append(']')
			case '{': completion.append('}')
			case '<': completion.append('>')
	return completion

def calc_completion_value(symbols):
	value = 0
	for char in symbols:
		value *= 5
		match char:
			case ')': value += 1
			case ']': value += 2
			case '}': value += 3
			case '>': value += 4
	return value

#main
def main():
	commands = [[char for char in line] for line in lines]
	incomplete_commands = []
	for command in commands:
		command_value = check_command(command)
		if command_value != None:
			incomplete_commands.append(command_value)

	values = []
	for incomplete_command in incomplete_commands:
		values.append(calc_completion_value(get_completion(incomplete_command)))
	sorted_values = sorted(values)
	answer = sorted_values[int(len(sorted_values)/2)]

	print(f"answer:", answer)

main()