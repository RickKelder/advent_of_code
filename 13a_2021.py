reader = open('13_input.txt')
lines = []
try:
    for line in reader.readlines():
    	lines.append(line.replace('\n', ''))
finally:
    reader.close()

def mark_spot(field, splitted_spot):
	field[int(splitted_spot[1])][int(splitted_spot[0])] = True

def fold_up(field, y):
	y_val = int(y.replace("fold along y=", ""))
	top_field = field[:y_val]
	bot_field = field[y_val+1:]
	for row in range(len(top_field)):
		for col in range(len(top_field[row])):
			top_field[row][col] = top_field[row][col] or bot_field[len(bot_field)-1-row][col]
	return top_field

def fold_left(field, x):
	x_val = int(x.replace("fold along x=", ""))
	left_field = []
	right_field = []
	for row in field:
		left_field.append(row[:x_val])
		right_field.append(row[x_val+1:])
	for row in range(len(left_field)):
		for col in range(len(left_field[row])):
			left_field[row][col] = left_field[row][col] or right_field[row][len(left_field[row])-1-col]
	return left_field

def print_field(field):
	for row in range(len(field)):
		line = ""
		for col in range(len(field[row])):
			line += ""+("#" if field[row][col] else ".")
		print(line)
	print("\n")

#main
def main():
	max_rows = max_cols = 0
	mark_spots = []
	folds = []
	for line in lines:
		if line.startswith("fold"):
			folds.append(line)
		elif not(line == ""):
			splitted_spot = line.split(",")
			max_rows = max(int(splitted_spot[1]), max_rows)
			max_cols = max(int(splitted_spot[0]), max_cols)
			mark_spots.append(splitted_spot)

	field = [[False for col in range(max_cols+1)] for row in range(max_rows+1)]
	for mark_spot_line in mark_spots:
		mark_spot(field, mark_spot_line)
	for fold_line in folds:
		if "y=" in fold_line:
			field = fold_up(field, fold_line)	
			break
		else:
			field = fold_left(field, fold_line)
			break

	print_field(field)
	count_dots = sum([col for row in field for col in row])

	print(f"answer:", count_dots)

main()