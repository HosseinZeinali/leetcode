class Solution(object):
    def findPairs(self, nums, k):
        a = {}
        nums = sorted(nums)
        res = 0
        j = 0
        for num in nums:
            i = binary_search(nums, j+1, len(nums) - 1, num+k)
            if i != -1:
                if nums[i] > nums[j]:
                    try:
                        a[str(nums[j])+":"+str(nums[i])]
                    except:
                        a[str(nums[j])+":"+str(nums[i])] = True
                        res = res + 1
                else:
                    try:
                        a[str(nums[i])+":"+str(nums[j])]
                    except:
                        a[str(nums[i])+":"+str(nums[j])] = True
                        res = res + 1
            j = j+1
        return res


def binary_search(array, low, high, x):
    mid = low + (high - low) // 2
    if high >= low:
        if array[mid] == x:
            return mid
        elif (x < array[mid]):
            return binary_search(array, low, mid - 1, x)
        elif x > array[mid]:
            return binary_search(array, mid + 1, high, x)
    else:
        return -1

solution = Solution()
a =  [3,1,4,1,5]
r = solution.findPairs(a, 2)
print(r)