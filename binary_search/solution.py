class Solution(object):
    def search(self, nums, target):
        return binary_search(nums, 0, len(nums)-1, target)
def binary_search(array, low, high, x):
    mid = low + (high - low) // 2
    print(mid)
    print(high)
    if high >= low and high < len(array):
        if array[mid] == x:
            return mid
        elif (x < array[mid]):
            return binary_search(array, low, mid - 1, x)
        elif x > array[mid]:
            return binary_search(array, mid + 1, high, x)
    else:
        return -1
nums = [-1,0,3,5,9,12]
a = binary_search(nums, 0, len(nums), 13)
print(a)