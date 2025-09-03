'''Task 6: Sorting & Reversing
nums = [34, 12, 56, 78, 23, 45, 67]
Sort ascending.
Sort descending.
Reverse using slicing.'''

nums = [34, 12, 56, 78, 23, 45, 67]
nums.sort()
print(nums)
nums.sort(reverse=True)
print(nums)
print(nums[::-1])