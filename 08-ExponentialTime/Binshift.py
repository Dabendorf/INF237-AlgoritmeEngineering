from typing import overload


def printBinBlocks(num):
	overall_str = list(bin(num)[2:].rjust(32, "0"))
	for outer in range(4):
		for middle in range(4):
			for inner in range(2):
				ind = outer*8+middle*2+inner
				print(overall_str[ind], end="")
			print(" ", end="")
		print("| ", end="")
	print()
	

pattern = 2765355624
printBinBlocks(pattern)

ind0 = 1
ind1 = 5
ind2 = 7
ind3 = 11

print("Index masks")
#for i in range(16):
#	printBinBlocks(3 << (16-i-1)*2)
print(f"To swap: {ind0}, {ind1}, {ind2}, {ind3}")
printBinBlocks(3 << (16-ind0-1)*2)
printBinBlocks(3 << (16-ind1-1)*2)
printBinBlocks(3 << (16-ind2-1)*2)
printBinBlocks(3 << (16-ind3-1)*2)