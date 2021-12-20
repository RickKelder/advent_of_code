import math

reader = open('19_input.txt')
lines = []
try:
    for line in reader.readlines():
    	lines.append(line.replace('\n', ''))
finally:
    reader.close()

def get_distance_between_vectors(vector1, vector2):
	return math.sqrt((vector2[0]-vector1[0])**2+(vector2[1]-vector1[1])**2+(vector2[2]-vector1[2])**2)

def get_vector_length(vector):
	return math.sqrt(vector[0]*vector[0]+vector[1]*vector[1]+vector[2]*vector[2])

def get_vector_minus_vector(vector1, vector2):
	return [vector1[0]-vector2[0], vector1[1]-vector2[1], vector1[2]-vector2[2]]

class Beacon(object):
	def __init__(self, vector, vector_to_scanner):
		self.other_beacons = {}
		self.vector = vector
		self.vector_to_scanner = vector_to_scanner

	def add_beacons(self, other_beacon_list):
		for beacon in other_beacon_list:
			if beacon != self:
				self.other_beacons[get_distance_between_vectors(self.vector, beacon.vector)] = beacon

	def update_beacon(self, other_beacon_list):
		for distance in other_beacon_list:
			if distance not in self.other_beacons:
				self.other_beacons[distance] = other_beacon_list[distance]

class World(object):
	def __init__(self, zero_scanner):
		self.beacons = []
		self.zero_scanner = zero_scanner
		self._add_zero_scanner()

	def _add_zero_scanner(self):
		for beacon_report in self.zero_scanner.beacon_reports:
			beacon_to_add = Beacon(beacon_report, self.zero_scanner)
			beacon_to_add.vector_to_zero = beacon_to_add.vector
			self.beacons.append(beacon_to_add)
		for beacon in self.beacons:
			beacon.add_beacons(self.beacons.copy())
			self.zero_scanner.new_beacons.append(beacon)

	def add_scanner(self, scanner):
		beacons = []
		for beacon_report in scanner.beacon_reports:
			beacons.append(Beacon(beacon_report, scanner))
		for beacon in beacons:
			beacon.add_beacons(beacons.copy())
			beacon_check = self.check_beacon(beacon)
			if beacon_check != None:
				scanner.overlapping_beacons.append((beacon.vector, beacon_check))
			else:
				scanner.new_beacons.append((beacon.vector, beacon))

	def check_beacon(self, beacon_to_check):
		beacon_found = None
		for beacon in self.beacons:
			intersect = set(beacon.other_beacons.keys()).intersection(set(beacon_to_check.other_beacons.keys()))
			if len(intersect) > 1: #if we found more then 10 match, we know that we are the same beacon
				beacon_found = beacon
				break
		if beacon_found != None:
			beacon_found.update_beacon(beacon_to_check.other_beacons)
		else:
			self.beacons.append(beacon_to_check)
		return beacon_found

class Scanner(object):
	def __init__(self, index):
		self.index = index
		self.beacon_reports = []
		self.overlapping_beacons = []
		self.new_beacons = []

	def add_beacon_report(self, beacon_report):
		self.beacon_reports.append([int(pos) for pos in beacon_report.split(",")])

	def print(self):
		print("---")
		for i in range(len(self.beacon_reports)-1):
			print(self.beacon_reports[i])

	def calc_position(self):
		for (beacon_report, beacon) in self.overlapping_beacons:
			print(beacon_report, beacon.vector, beacon.vector_to_scanner.index, get_vector_minus_vector(beacon_report, beacon.vector))

#main
def main():
	scanners = []
	current_scanner = None
	for line in lines:
		if line.startswith("---"):
			current_scanner = Scanner(len(scanners))
		elif line == "":
			scanners.append(current_scanner)
		else:
			current_scanner.add_beacon_report(line)
	scanners.append(current_scanner)

	world = World(scanners[0])
	for i in range(len(scanners)-1):
		print("adding ", i+1)
		world.add_scanner(scanners[i+1])

	print(f"answer:", len(world.beacons))

main()



# scanner distance from beacons to beacons
# S1 .  .   .  B3
# .  .  B2  .  .
# .  .  .   .  .
# B1 .  S2  .  B4  .  B5
#
# S1: B1 -> B2 = 1.7
# S1: B1 -> B3 = 3.3
# S1: B1 -> B4 = 3
# S1: B2 -> B1 = 1.7
# S1: B2 -> B3 = 1.6
# S1: B2 -> B4 = 1.8
# S1: B3 -> B1 = 3.3
# S1: B3 -> B2 = 1.6
# S1: B3 -> B4 = 2
# S1: B4 -> B1 = 3
# S1: B4 -> B2 = 1.8
# S1: B4 -> B3 = 2

# S2: B1 -> B2 = 1.7
# S2: B1 -> B4 = 3
# S2: B2 -> B1 = 1.7
# S2: B2 -> B4 = 1.8
# S2: B4 -> B1 = 3
# S2: B4 -> B2 = 1.8
# S2: B1 -> B5 = 4.5
# ...