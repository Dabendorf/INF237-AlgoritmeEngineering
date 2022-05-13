from sys import stdin
from math import ceil, floor, log10

# https://open.kattis.com/problems/howmanydigits

elements = list()
for el in stdin.readlines():
	elements.append(int(el))

max_element = max(elements)

length_factorials = dict()
len_new = 1
for i in range(1, max_element+1):
	len_new += log10(i)
	length_factorials[i] = len_new

length_factorials.update({0:1, 1:1, 2:1, 3:1, 4:2, 5:3, 6:3})

for el in elements:
	if el < 7:
		print(length_factorials[el])
	else:
		print(floor(length_factorials[el]))