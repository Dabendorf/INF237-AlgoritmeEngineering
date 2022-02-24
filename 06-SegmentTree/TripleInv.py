import sys


# Python3 program to count inversions of  
# size three using Binary Indexed Tree  
  
# Returns sum of arr[0..index]. This function 
# assumes that the array is preprocessed and  
# partial sums of array elements are stored 
# in BITree[].  
def getSum(BITree, index): 
    sum = 0 # Initialize result  
      
    # Traverse ancestors of BITree[index]  
    while (index > 0):  
  
        # Add current element of  
        # BITree to sum  
        sum += BITree[index]  
  
        # Move index to parent node  
        # in getSum View  
        index -= index & (-index)  
  
    return sum
  
# Updates a node in Binary Index Tree  
# (BITree) at given index in BITree. 
# The given value 'val' is added to BITree[i]  
# and all of its ancestors in tree.  
def updateBIT( BITree, n, index, val): 
  
    # Traverse all ancestors and add 'val'  
    while (index <= n):  
  
        # Add 'val' to current node of BI Tree  
        BITree[index] += val  
  
        # Update index to that of parent  
        # in update View  
        index += index & (-index)  
  
# Converts an array to an array with values  
# from 1 to n and relative order of smaller  
# and greater elements remains same. For example,  
# 7, -90, 100, 1 is converted to 3, 1, 4 ,2  
def convert(arr, n) : 
  
    # Create a copy of arrp[] in temp and  
    # sort the temp array in increasing order  
    temp = [0] * n  
    for i in range(n): 
        temp[i] = arr[i]  
    temp = sorted(temp) 
    j = 1
      
    # Traverse all array elements  
    for i in temp:  
  
        # lower_bound() Returns poer to  
        # the first element greater than 
        # or equal to arr[i]  
        arr[arr.index(i)] = j 
        j += 1
  
# Returns count of inversions of size three  
def getInvCount( arr, n): 
  
    # Convert arr[] to an array with values  
    # from 1 to n and relative order of smaller  
    # and greater elements remains same. For example, 
    # 7, -90, 100, 1 is converted to 3, 1, 4 ,2  
    convert(arr, n)  
  
    # Create and initialize smaller and  
    # greater arrays  
    greater1 = [0] * n 
    smaller1 = [0] * n  
    for i in range(n): 
        greater1[i], smaller1[i] = 0, 0
  
    # Create and initialize an array to  
    # store Binary Indexed Tree  
    BIT = [0] * (n + 1)  
    for i in range(1, n + 1):  
        BIT[i] = 0
    for i in range(n - 1, -1, -1): 
  
        smaller1[i] = getSum(BIT, arr[i] - 1)  
        updateBIT(BIT, n, arr[i], 1)  
  
    # Reset BIT  
    for i in range(1, n + 1):  
        BIT[i] = 0
  
    # Count greater elements  
    for i in range(n):  
  
        greater1[i] = i - getSum(BIT, arr[i])  
        updateBIT(BIT, n, arr[i], 1)  
  
    # Compute Inversion count using smaller[]  
    # and greater[].  
    invcount = 0
    for i in range(n):  
        invcount += smaller1[i] * greater1[i]  
  
    return invcount  
      
def main():
	sys.stdin.readline()
	numbers = list(map(int, sys.stdin.readline().strip().split()))
	print(getInvCount(numbers, len(numbers)))


# Driver code  
if __name__ =="__main__": 
    main()
    

