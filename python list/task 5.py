'''Task 5: Search & Count
nums = [2, 4, 6, 8, 4, 10, 4, 12, 14, 4]
Check if 4 exists in the list.
Print its first index.
Count how many times 4 appears.'''
nums = [2, 4, 6, 8, 4, 10, 4, 12, 14, 4]
if 4 in nums:
    print("4 exists in the list")
    print("the first index of 4 is:",nums.index(4))
    print("how many times 4 appears:",nums.count(4))
else:
    print("4 does not exists in the list")