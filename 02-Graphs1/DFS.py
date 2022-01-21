def dfs(adj_list, u, visited):
	visited.append(u)

	print(u)
	for v in adj_list[u]:
		if v not in visited:
			dfs(adj_list, v, visited)



# Driver code
if __name__=='__main__':
	visited = []

	adj_list = dict()
	adj_list[1] = [4,2]
	adj_list[2] = [1,4,3]
	adj_list[3] = [2,4]
	adj_list[4] = [1,2,3]

	dfs(adj_list, 1, visited)