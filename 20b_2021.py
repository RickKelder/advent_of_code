import copy

reader = open('20_input.txt')
lines = []
try:
    for line in reader.readlines():
    	lines.append(line.replace('\n', ''))
finally:
    reader.close()

def replace_image_line(line):
	return [1 if char == '#' else 0 for char in line]

def create_larger_image(image, first_enhance_sign):
	for row in image:
		row.insert(0, first_enhance_sign)
		row.append(first_enhance_sign)
	image.insert(0, [first_enhance_sign for i in range(len(image[0]))])
	image.append([first_enhance_sign for i in range(len(image[0]))])

def get_pixel(image, new_image, row, col, image_enhancement, first_enhance_sign):
	binary_string = ""
	for i in range(3):
		row_index = row-1+i
		for j in range(3):
			col_index = col-1+j
			if row_index < 0 or row_index >= len(image) or col_index < 0 or col_index >= len(image[0]):
				binary_string += str(first_enhance_sign)
			else:
				binary_string += str(int(image[row_index][col_index]))
	new_value = image_enhancement[int(binary_string, 2)]
	new_image[row][col] = new_value

def enhance(image, image_enhancement, first_enhance_sign):
	new_image = copy.deepcopy(image)
	for row_index in range(len(image)):
		for col_index in range(len(image[0])):
			get_pixel(image, new_image, row_index, col_index, image_enhancement, first_enhance_sign)
	return new_image

def print_image(image):
	for row in image:
		print("".join(["#" if num else "." for num in row]))

#main
def main():
	image_enhancement = None
	image = []
	for line in lines:
		if image_enhancement == None:
			image_enhancement = replace_image_line(line)
		elif line != "":
			image.append(replace_image_line(line))

	for i in range(50):
		first_enhance_sign = 0 if i % 2 == 0 else image_enhancement[0]
		create_larger_image(image, first_enhance_sign)
		image = enhance(image, image_enhancement, first_enhance_sign)

	images_lit = sum([int(col) for row in image for col in row])

	print(f"answer:", images_lit)

main()