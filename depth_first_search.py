def depth_first_search(graph, root):
	visited = list()
	graph_stack = list()

	graph_stack.append(root)
	node = root

	while len(graph_stack) > 0:
		if node not in visited:
			visited.append(node)
			adjacent = graph[node]

			if set(adjacent).issubset(set(visited)):
				graph_stack.pop()
			if len(graph_stack) > 0:
				node = graph_stack[-1]
				continue
			else:
				remaining_elements = set(adjacent).difference(set(visited))

			first_adjacent = sorted(remaining_elements)[0]
			graph_stack.append(first_adjacent)
			node = first_adjacent
			return visited