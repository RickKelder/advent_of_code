reader = open('8_input.txt')
lines = []
try:
    for line in reader.readlines():
    	lines.append(line.replace('\n', ''))
finally:
    reader.close()

#   0:      1:      2:      3:      4:
#  aaaa    ....    aaaa    aaaa    ....
# b    c  .    c  .    c  .    c  b    c
# b    c  .    c  .    c  .    c  b    c
#  ....    ....    dddd    dddd    dddd
# e    f  .    f  e    .  .    f  .    f
# e    f  .    f  e    .  .    f  .    f
#  gggg    ....    gggg    gggg    ....

#   5:      6:      7:      8:      9:
#  aaaa    aaaa    aaaa    aaaa    aaaa
# b    .  b    .  .    c  b    c  b    c
# b    .  b    .  .    c  b    c  b    c
#  dddd    dddd    ....    dddd    dddd
# .    f  e    f  .    f  e    f  .    f
# .    f  e    f  .    f  e    f  .    f
#  gggg    gggg    ....    gggg    gggg

# if one segment of 1 is not in string len 6 then 6
# if !6 and all segments of 4 are in string len 6 then 9
# ez 0 when string len 6 and 6 and 9 are deduced
# if all segments of 1 are in string len 5 then 3
# if !3 and all segments of 4 are in string len 6 then 5
# ez 2 when string len 5 and 3 and 5 are deduced

class Display():
	def __init__(self):
		self.input_digits = []
		self.output_digits = []

	def add_input_digit(self, digit):
		self.input_digits.append(digit)

	def add_output_digit(self, digit):
		self.output_digits.append(digit)

	def get_input_unique_digits(self):
		return filter(lambda digit: digit.output_number != None, self.input_digits)

	def get_output_unique_digits(self):
		return filter(lambda digit: digit.output_number != None, self.output_digits)

	def deduce_difficult(self, digit_array):
		for input_digit in self.input_digits:
			input_digit.deduce_difficult(digit_array[1], digit_array[4])
		for output_digit in self.output_digits:
			output_digit.deduce_difficult(digit_array[1], digit_array[4])

	def deduce(self):
		unique_digits = list(self.get_output_unique_digits())
		unique_digits.extend(list(self.get_input_unique_digits()));
		digit_array = [None]*10
		for unique_digit in unique_digits:
			digit_array[unique_digit.output_number] = unique_digit.sorted_wiring_string
		self.deduce_difficult(digit_array)
		self.output_value = int("".join([str(outputdigit.output_number) for outputdigit in self.output_digits]))
				

class Digit():
	def __init__(self, wiring):
		self.wiring_string = wiring
		self.sorted_wiring_string = sorted(self.wiring_string)
		self.output_number = None
		self._parse_easy_wiring()

	def _parse_easy_wiring(self):
		match len(self.wiring_string):
			case 2:
				self.output_number = 1
			case 3:
				self.output_number = 7
			case 4:
				self.output_number = 4
			case 7:
				self.output_number = 8

	def deduce_difficult(self, sorted_one_string, sorted_four_string):
		if self.output_number == None and len(self.sorted_wiring_string) == 6 and len([ element for element in sorted_one_string if element not in self.sorted_wiring_string]) > 0: # if one segment of 1 is not in string len 6 then 6
			self.output_number = 6
		if self.output_number == None and len(self.sorted_wiring_string) == 6 and len([ element for element in sorted_four_string if element not in self.sorted_wiring_string]) == 0: # if !6 and all segments of 4 are in string len 6 then 9
			self.output_number = 9
		if self.output_number == None and len(self.sorted_wiring_string) == 6: # ez 0 when string len 6 and 6 and 9 are deduced
			self.output_number = 0
		if self.output_number == None and len(self.sorted_wiring_string) == 5 and len([ element for element in sorted_one_string if element not in self.sorted_wiring_string]) == 0:  # if all segments of 1 are in string len 5 then 3
			self.output_number = 3
		if self.output_number == None and len(self.sorted_wiring_string) == 5 and len([ element for element in sorted_four_string if element not in self.sorted_wiring_string]) == 1: # if !3 and all segments of 4 are in string len 6 then 5
			self.output_number = 5
		if self.output_number == None and len(self.sorted_wiring_string) == 5: # ez 2 when string len 5 and 3 and 5 are deduced
			self.output_number = 2

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
		new_display.deduce()

	answer = sum([deduced_display.output_value for deduced_display in displays])

	print(f"answer:", answer)

main()