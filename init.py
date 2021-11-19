#!bin/python3
nums = [2, 33, 45, 4, 12, 56, 22, 30, 5, 48]
target = 78
def sum (nums):
    for i in range(len(nums)):
        temp = nums[i]
        for j in range(len(nums)):
            if i<j:
                t = temp + nums[j]
                if t == target :
                    print (nums[i], "+" , nums[j], "=", target, " for index1 = ", i, "index2 = ", j, "\n")
sum(nums)