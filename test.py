# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int,input().split()))

# arr = [] 
# left, right = 0, len(arr)
# target = 0
# while left <= right:
#     mid = left + (right - left) // 2
    
#     if left < target:
#         left = mid + 1
#     else:
#         right = mid - 1
# print(left)


nums = [6,5,4,3,2,1,0]

def swap(l,r):
    start, end = l,r+1
    pvot = l
    l += 1
    
    while l <= r:
        while l < end and nums[l] <= nums[pvot]:
            l += 1
        while r >= start and nums[r] > nums[pvot]:
            r -= 1
        if l <= r:
            nums[l], nums[r] = nums[r], nums[l]
        else:      
            nums[pvot], nums[r] = nums[r], nums[pvot]
    
swap(0,len(nums)-1)
print(nums)