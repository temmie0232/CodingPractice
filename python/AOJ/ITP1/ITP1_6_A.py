
import math


n = int(input())
n_itr = math.floor(n/2)

nums = list(map(int,input().split()))

#print(f"sqrt={n_itr}")

for i in range(n_itr):
    #print(f"{i}回目 : ")
    nums[0+i],nums[n-1-i] = nums[n-1-i],nums[0+i]
    #print(nums)

itr = 1
    
for i in nums:

    if itr == len(nums):
        print(i)
    else:
        print(i,end=" ")
    
    itr += 1