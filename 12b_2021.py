reader = open('12_input.txt')
lines = []
try:
    for line in reader.readlines():
    	lines.append(line.replace('\n', ''))
finally:
    reader.close()

class Node(object):
	def __init__(self, name):
		self.name = name
		self.connections = {}

def parse_line(network, line):
	splitted_line = line.split("-")
	node0 = get_or_create_node(network, splitted_line[0])
	node1 = get_or_create_node(network, splitted_line[1])
	add_connection(network, node0, node1)

def add_connection(network, node0, node1):
	node0.connections[node1.name] = node1
	node1.connections[node0.name] = node0

def get_or_create_node(network, name):
	if name not in network:
		network[name] = Node(name)
	return network[name]

def walk_path(network, routes, current_route, small_nodes_walked, small_cave_twice):
	for connection_index in current_route[-1].connections:
		connection = current_route[-1].connections[connection_index]
		new_route = current_route.copy()
		new_route.append(connection)
		if connection.name != "end" and connection.name != "start" and (connection.name not in small_nodes_walked or not(small_cave_twice)):
			new_small_cave_twice = small_cave_twice
			if connection.name != "end" and connection.name != "start" and connection.name in small_nodes_walked and connection.name.islower():
				new_small_cave_twice = True
			new_small_nodes_walked = small_nodes_walked.copy()
			if connection.name.islower() and connection.name not in new_small_nodes_walked:
				new_small_nodes_walked.append(connection.name)
			walk_path(network, routes, new_route, new_small_nodes_walked, new_small_cave_twice)
		if connection.name == "end":
			end_route = current_route.copy()
			end_route.append(connection)
			routes.append(end_route)

#main
def main():
	network = {}
	for line in lines:
		parse_line(network, line)

	routes = []
	walk_path(network, routes, [network['start']], [], False)
	print(len(routes))
	# for route in routes:
	# 	route_tekst = ""
	# 	for node in route:
	# 		route_tekst += ","+node.name
	# 	print(route_tekst)

	print(f"answer:")

main()