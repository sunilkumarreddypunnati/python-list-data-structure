'''Task 4: Remove Elements
nums = [5, 10, 15, 20, 25, 30, 35]
Remove the 3rd element using del.
Remove the value 25 using remove().
Pop the last element.
Print the list after each operation.'''
nums = [5, 10, 15, 20, 25, 30, 35]
del nums[2]
print(nums)
nums.remove(25)
print(nums)
nums.pop()
print(nums)