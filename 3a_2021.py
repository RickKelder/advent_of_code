reader = open('3_input.txt')
lines = []
try:
    for line in reader.readlines():
    	lines.append(line.replace('\n', ''))
finally:
    reader.close()

#real stuff
list_breakdown = [list(map(int, list(line))) for line in lines]
column_total = [sum(column) for column in zip(*list_breakdown)]
gamma_list = (list(map(lambda total: total > len(lines)/2, column_total)))
epsilon_list = (list(map(lambda total: total < len(lines)/2, column_total)))
gamma = int(''.join([str(int(x)) for x in gamma_list]),2)
epsilon = int(''.join([str(int(x)) for x in epsilon_list]),2)

print(f"done", gamma, epsilon, gamma*epsilon)