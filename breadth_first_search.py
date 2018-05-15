from collections import deque

def breadth_first_search(graph, root):
	visited = list()
	queue = dequeue([root])
	visited.append(root)
	node = root

	while len(queue) > 0:
		node = queue.popleft()
		adjacent = graph[node]
		remaining_elements = set(adjacent).difference(set(visited))
		if len(remaining_elements) > 0:
			for element in sorted(remaining_elements):
				visited.append(element)
				queue.append(element)
	return visited