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
				return (command, char)
	return None

#main
def main():
	commands = [[char for char in line] for line in lines]
	corrupt = []
	for command in commands:
		corrupt_value = check_command(command)
		if corrupt_value != None:
			corrupt.append(corrupt_value)

	answer = 0
	for (corrupt_command, corrupt_symbol) in corrupt:
		match corrupt_symbol:
			case ')': answer += 3
			case ']': answer += 57
			case '}': answer += 1197
			case '>': answer += 25137


	print(f"answer:", answer)

main()