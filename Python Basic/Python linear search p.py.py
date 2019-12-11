''' Linear serach algorithm 
1. worst case
2.average case
3.Best case

'''
def search(arr, x, n):
	i = 0
	for i in range(i, n):
		if(arr[i]==x):
			return i
	return -1

arr= [1, 3, 5, 4]
n = len(arr)
x = 5
index = search(arr, x ,n)
print("index position of {} in {} is {}".format(x,arr,index))

def search(arr):
	for i in range(0, n):
		if (arr[i] == x):
			return i
	return -1
x = 3
arr = [1, 4, 5, 6, 3]
n = len(arr)
index = search(arr)
print("Index position Of {} in {} is {}".format(x, arr, index))