def findSmallest(arr):
	smallest = arr[0]   #to store the smallest value
	smallest_index = 0 #to store the smallest index
	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index


def selectionSort(arr): #the function sorts the array
	newArr = []
	for i in range(len(arr)):
		smallest = findSmallest(arr)     #finds the smallest element in the array and
		newArr.append(arr.pop(smallest)) # adds it to the new array
	return newArr

print(selectionSort([5,3,6,2,10, 101, 77, 98, 53, 0]))
