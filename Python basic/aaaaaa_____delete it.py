# basic method of input output 
# input N 
n = int(input()) 
  
# input the array 
arr = [int(x) for x in input().split()] 
  
# initialize variable 
summation = 0
  
# calculate sum 
for x in arr: 
    summation += x 
      
# print answer 
print(summation) 