'''
@author : CodePerfectPlus
@Topic  : Buuble Sort 
'''

def sort(nums):
	for i in range(len(nums)-1,0,-1):
		for j in range(i):
			if nums[j] > nums[j+1]:
				temp = nums[j]
				nums[j] = nums[j +1]
				nums[j + 1] =temp



list_01 = [2, 5, 5, 7, 3, 7, 2, 23, 5, 7, 45, 54, 754]

sort(list_01)
print(list_01)
