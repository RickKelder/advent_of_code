import math

reader = open('16_input.txt')
lines = []
try:
    for line in reader.readlines():
    	lines.append(line.replace('\n', ''))
finally:
    reader.close()

def hex_to_binary(hex_val):
  return bin(int(hex_val, 16))[2:].zfill(len(hex_val) * 4)

class Packet(object):
	def __init__(self, binary_string):
		self.binary_string = binary_string
		self.subpackets = []
		# print(self.binary_string)
		self.parseVersion()
		self.parsePacketType()
		if self.packet_type == 4:
			self.parseLiteral()
		else:
			self.parseOperator()

	def parseVersion(self):
		self.version = int(self.binary_string[:3], 2)

	def parsePacketType(self):
		self.packet_type = int(self.binary_string[3:6], 2)

	def parseLiteral(self):
		current_index = 6
		literal_string = ""
		while (self.binary_string[current_index] == '1'):
			literal_string += self.binary_string[current_index+1:current_index+5]
			current_index+=5
		literal_string += self.binary_string[current_index+1:current_index+5]
		self.literal = int(literal_string, 2)
		self.total_length = current_index+5

	def parseNSubPackets(self):
		self.total_length = 18
		for i in range(self.length_packets):
			newpacket = Packet(self.binary_string[self.total_length:])
			self.subpackets.append(newpacket)
			self.total_length += newpacket.total_length

	def parseTotalLengthSubPackets(self):
		current_index = 22
		while(current_index < self.total_length-4):
			newpacket = Packet(self.binary_string[current_index:])
			self.subpackets.append(newpacket)
			current_index += newpacket.total_length

	def parseOperator(self):
		self.length_type = self.binary_string[6]
		if (self.length_type == '0'):
			self.length_packets = int(self.binary_string[7:22],2)
			self.total_length = 22+self.length_packets
			self.parseTotalLengthSubPackets()
		else:
			self.length_packets = int(self.binary_string[7:18],2)
			self.parseNSubPackets()

	def getValue(self):
		subpacket_value_list = sum([subpacket.getValue() for subpacket in self.subpackets])
		match self.packet_type:
			case 0: #sum
				return sum(subpacket_value_list)
			case 1: #product
				return math.prod(subpacket_value_list)
			case 2: #min
				return min(subpacket_value_list)
			case 3: #max
				return max(subpacket_value_list)
			case 4: #literal
				return self.literal
			case 5: #gt
				return int(subpacket_value_list[0] > subpacket_value_list[1])
			case 6: #lt
				return int(subpacket_value_list[0] < subpacket_value_list[1])
			case 7: #eq
				return int(subpacket_value_list[0] == subpacket_value_list[1])
		return 0


#main
def main():
	binaries = [Packet(hex_to_binary(line)) for line in lines]

	print(f"answer:", binaries[0].getValue())

main()