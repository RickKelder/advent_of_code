reader = open('8_input.txt')
lines = []
try:
    for line in reader.readlines():
    	lines.append(line.replace('\n', ''))
finally:
    reader.close()

class Display():
	def __init__(self):
		self.input_digits = []
		self.output_digits = []

	def add_input_digit(self, digit):
		self.input_digits.append(digit)

	def add_output_digit(self, digit):
		self.output_digits.append(digit)

	def get_output_unique_digits(self):
		return filter(lambda digit: digit.output_number != None, self.output_digits)

class Digit():
	def __init__(self, wiring):
		self.wiring_string = wiring
		self.output_number = None
		self._parse_wiring()
		#print(self.wiring_string, self.output_number);

	def _parse_wiring(self):
		match len(self.wiring_string):
			case 2:
				self.output_number = 1
			case 3:
				self.output_number = 7
			case 4:
				self.output_number = 4
			case 7:
				self.output_number = 8

#main
def main():
	displays = []
	for line in lines:
		new_display = Display()
		displays.append(new_display)
		wirings = line.split(" | ")
		for wiring in wirings[0].split():
			new_display.add_input_digit(Digit(wiring))
		for wiring in wirings[1].split():
			new_display.add_output_digit(Digit(wiring))

	amount_of_uniques = sum([len(list(disp.get_output_unique_digits())) for disp in displays])

	print(f"answer:", amount_of_uniques)

main()