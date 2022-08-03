#taking input for the integer array
A = list(map(int,input().split()))

loop_pass = 1
#iterating loop from second index of array to length of array
for j in range(1,len(A)):
	#store the value present in array at index j in key
	key = A[j]
	
	#checking the elements present from left of j to 0
	#store j-1 in i
	i = j - 1
	#iterating loop until the it reach the first index of A and A[i] value is greater than key
	while i>=0 and A[i]>key:
		#store the A[i] in A[i+1]
		A[i+1] = A[i]
		#decrementing i
		i -= 1
	#store the key value in A[i+1]
	A[i+1] = key

	#printing each pass of the sorting logic
	print(f"Pass {loop_pass}: {A}")
	loop_pass += 1

#printing the sorted array
print("Sorted array: ",A)