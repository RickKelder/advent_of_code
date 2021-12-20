import math
import itertools

reader = open('19_input.txt')
lines = []
try:
    for line in reader.readlines():
    	lines.append(line.replace('\n', ''))
finally:
    reader.close()

# get 24 orientations with roll and turn https://stackoverflow.com/questions/16452383/how-to-get-all-24-rotations-of-a-3-dimensional-array
def roll(v): return [v[0],v[2],-v[1]]
def turn(v): return [-v[1],v[0],v[2]]
def sequence (v):
    for cycle in range(2):
        for step in range(3):  
            v = roll(v)
            yield(v)           
            for i in range(3): 
                v = turn(v)
                yield(v)
        v = roll(turn(roll(v))) 

def get_distance_between_vectors(vector1, vector2):
	return math.sqrt((vector2[0]-vector1[0])**2+(vector2[1]-vector1[1])**2+(vector2[2]-vector1[2])**2)

def get_vector_length(vector):
	return math.sqrt(vector[0]*vector[0]+vector[1]*vector[1]+vector[2]*vector[2])

def get_vector_minus_vector(vector1, vector2):
	return [vector1[0]-vector2[0], vector1[1]-vector2[1], vector1[2]-vector2[2]]

def get_vector_plus_vector(vector1, vector2):
	return [vector1[0]+vector2[0], vector1[1]+vector2[1], vector1[2]+vector2[2]]

def get_distance_manhattan(vector1, vector2):
	return abs(vector1[0]-vector2[0]) + abs(vector1[1]-vector2[1]) + abs(vector1[2]-vector2[2])

class Beacon(object):
	def __init__(self, vector):
		self.other_beacons = {}
		self.vector = vector

	def set_beacons(self, other_beacon_list):
		self.other_beacons = {}
		for beacon in other_beacon_list:
			if beacon != self:
				self.other_beacons[abs(get_distance_between_vectors(self.vector, beacon.vector))] = beacon

class Scanner(object):
	def __init__(self, index):
		self.index = index
		self.beacon_reports = []
		self.beacons = []
		self.overlapping_beacons = []
		self.location = []

	def set_beacons(self):
		self.beacons = []
		for beacon_report in self.beacon_reports:
			self.beacons.append(Beacon(beacon_report))
		for beacon in self.beacons:
			beacon.set_beacons(self.beacons.copy())

	def add_beacon_report(self, beacon_report):
		self.beacon_reports.append([int(pos) for pos in beacon_report.split(",")])

	def print(self):
		print("---")
		for i in range(len(self.beacon_reports)-1):
			print(self.beacon_reports[i])

	def check_intersect(self, other_scanner):
		# print("check", self.index, other_scanner.index)
		beacons_found = []
		for beacon in self.beacons:
			beacon_found = self.check_beacon(beacon, other_scanner)
			if beacon_found != None:
				beacons_found.append((beacon, beacon_found))
		if len(beacons_found)==12:
			self.calc_orientation(beacons_found, other_scanner)
			return True
		return False

	def check_beacon(self, beacon, other_scanner):
		other_scanner_beacon_found = None
		for other_scanner_beacon in other_scanner.beacons:
			intersect = set(beacon.other_beacons.keys()).intersection(set(other_scanner_beacon.other_beacons.keys()))
			if len(intersect) > 10: #if we found more then 10 match, we know that we are the same beacon
				other_scanner_beacon_found = other_scanner_beacon
				break
		return other_scanner_beacon_found

	def calc_orientation(self, beacon_map, other_scanner):
		print("orienting", self.index, other_scanner.index);
		orientation = {}
		for (beacon, other_scanner_beacon) in beacon_map:
			combinations = list(sequence(beacon.vector))
			for i in range(len(combinations)):
				combination = combinations[i]
				diff = get_vector_minus_vector(other_scanner_beacon.vector, combination)
				diff_string = ",".join(map(str, diff))
				if diff_string not in orientation:
					orientation[diff_string] = []
				orientation[diff_string].append(i)
		for orr in orientation:
			if len(orientation[orr]) >= 12:
		 		self.set_orientation(orr, orientation[orr][0], other_scanner)

	def set_orientation(self, position_string, orientation, other_scanner):
		position = list(map(int, position_string.split(",")))
		for beacon in self.beacons:
			combinations = list(sequence(beacon.vector))
			beacon.vector = get_vector_plus_vector(combinations[orientation], position)
		for beacon in self.beacons:
			beacon.set_beacons(self.beacons.copy())
		self.location = position

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

	scanners[0].set_beacons()
	scanners[0].location = [0,0,0]
	scanners_found = [scanners[0]]
	scanners_to_find = []
	for i in range(len(scanners)-1):
		scanners[i+1].set_beacons()
		scanners_to_find.append(scanners[i+1])

	while len(scanners_to_find) > 0:
		scanner_check = scanners_to_find.pop(0)
		scanner_overlaps = False
		for scanner_found in scanners_found:
			if scanner_check.check_intersect(scanner_found):
				scanner_overlaps = True
				break
		if scanner_overlaps:
			scanners_found.append(scanner_check)
			print(scanner_check.location)
		else:
			scanners_to_find.append(scanner_check)

	max_distance = 0
	for (scanner1, scanner2) in list(itertools.combinations(scanners, 2)):
		manhattan_distance = get_distance_manhattan(scanner1.location, scanner2.location)
		max_distance = max(max_distance, manhattan_distance)

	print(f"answer:", max_distance)
main()

# 1: 68,-1246,-43
# 2: 1105,-1205,1229
# 3: -92,-2380,-20
# 4: -20,-1133,1061

# -68,1246,43 => 68,-1246,-43

# -68,1246,43 and -160,1134,23 => -92,-2380,-20

# 68,-1246,-43
# -88,-113,1104    =>
# -20,-1133,1061

# -168,1125,-72

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