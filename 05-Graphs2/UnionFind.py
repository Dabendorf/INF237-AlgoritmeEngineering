# This is an example of UnionFind from Pål

def main():
	vertices = [0, 1, 2, 3]
	comp = {i : i for i in vertices}
	# { 0: 0, 1: 1, 2: 2, ...} or array
	rank = {i : 0 for i in vertices}
	# { 0: 0, 1: 0, 2: 0, ...} or array

	print(find(0, comp))
	print(find(1, comp))
	print(find(2, comp))
	print(find(3, comp))
	union(0, 1, rank, comp)
	print(find(0, comp))
	print(find(1, comp))
	print(find(2, comp))
	print(find(3, comp))
	union(3, 0, rank, comp)
	print(find(0, comp))
	print(find(1, comp))
	print(find(2, comp))
	print(find(3, comp))

def find(u, comp):
	if comp[u] == u:
		return u
	else:
		parent = find(comp[u], comp)
		comp[u] = parent # update
		return parent

def union(u, v, rank, comp):
	r1 = find(u, comp)
	r2 = find(v, comp)
	if rank[r1] < rank[r2]:
		comp[r1] = r2
	elif rank[r2] < rank[r1]:
		comp[r2] = r1
	else:
		comp[r1] = r2
		rank[r2] += 1

if __name__ == "__main__":
	main()