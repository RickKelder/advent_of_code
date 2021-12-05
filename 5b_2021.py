import numpy as np
import time

reader = open('5_input.txt')
lines = []
try:
    for line in reader.readlines():
    	lines.append(line.replace('\n', ''))
finally:
    reader.close()

class Oceanfloor:
	def __init__(self, size):
		self.matrix = [[0 for i in range(size)] for j in range(size)]

	def process_line(self, position):
		from_vector = np.array(list(map(int, position[0].split(","))))
		to_vector = np.array(list(map(int, position[1].split(","))))
		self._process_vectors(from_vector, to_vector)

	def _process_vectors(self, from_vector, to_vector):
		diff_vector = to_vector - from_vector
		if not(self._is_valid_move(diff_vector, abs(diff_vector[0]), abs(diff_vector[1]))):
			return
		diff_vector_sign = np.sign(diff_vector)
		for i in range(max(abs(diff_vector))+1):
			self._mark(from_vector+diff_vector_sign*i)

	def _is_valid_move(self, diff_vector, change_horizontal, change_vertical):
		return (diff_vector[0] == 0 or diff_vector[1] == 0 or change_horizontal == change_vertical)

	def _mark(self, position):
		self.matrix[position[0]][position[1]] += 1

	def getValueHigherThan(self, amountToCheck):
		return sum(col > amountToCheck for row in self.matrix for col in row)

#main
def main():
	start_time = time.time()
	locations = list(map(lambda line: line.split(" -> "), lines))
	oceanfloor = Oceanfloor(1000)
	for location in locations:
		oceanfloor.process_line(location)
	amountOfOverlaps = oceanfloor.getValueHigherThan(1)
	print(f"answer:", amountOfOverlaps)
	print("runtime: %s seconds" % (time.time() - start_time))

main()