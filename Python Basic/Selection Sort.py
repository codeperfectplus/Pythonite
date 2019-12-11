def sort(nums):
	for i in range(len(nums)-1):
		minpos = i
		for j in range(i,len(nums)):
			if nums[j] < nums [minpos]:
				minpos = j

		temp = nums[i]
		nums[i] = nums[minpos]
		nums[minpos] = temp
		print(nums)


nums = [5, 6, 3, 7, 8, 2]
sort(nums)
print(nums)