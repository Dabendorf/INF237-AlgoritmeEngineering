from random import randint

num_test_cases = 300
print(num_test_cases)

for _ in range(num_test_cases):
	num_nodes = randint(1, 16)
	if num_nodes!=1:
		num_edges = randint(0, (num_nodes * (num_nodes-1))/2-1)
	else:
		num_edges = 0

	print(f"{num_nodes} {num_edges}")

	for i in range(num_edges):
		node_a = randint(0, num_nodes-1)
		node_b = randint(0, num_nodes-1)

		print(f"{node_a} {node_b}")