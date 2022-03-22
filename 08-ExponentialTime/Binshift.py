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

print(f"To swap: {ind0}, {ind1}, {ind2}, {ind3}")

print("Index masks")
mask0 = 3 << (16-ind0-1)*2
mask1 = 3 << (16-ind1-1)*2
mask2 = 3 << (16-ind2-1)*2
mask3 = 3 << (16-ind3-1)*2
printBinBlocks(mask0)
printBinBlocks(mask1)
printBinBlocks(mask2)
printBinBlocks(mask3)

print("Values")
val0 = pattern & mask0
val1 = pattern & mask1
val2 = pattern & mask2
val3 = pattern & mask3
printBinBlocks(val0)
printBinBlocks(val1)
printBinBlocks(val2)
printBinBlocks(val3)

pattern = pattern & ~mask0
pattern = pattern & ~mask1
pattern = pattern & ~mask2
pattern = pattern & ~mask3

val0 >>= (16-ind0-1)*2
val1 >>= (16-ind1-1)*2
val2 >>= (16-ind2-1)*2
val3 >>= (16-ind3-1)*2

pattern |= val0 << (16-ind1-1)*2
pattern |= val1 << (16-ind2-1)*2
pattern |= val2 << (16-ind3-1)*2
pattern |= val3 << (16-ind0-1)*2

print("Famoser output")
printBinBlocks(pattern)