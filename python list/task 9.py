'''Task 9: Sum & Max/Min
Calculate the sum of all numbers in the list.
Find the largest and smallest number without using max() or min().
👉 Example List:
numbers = [23, 1, 45, 12, 67, 34, 89, 2, 5]'''
numbers = [23, 1, 45, 12, 67, 34, 89, 2, 5]
total=0
for i in  numbers:
    total+=i
print(total)
largest=numbers[0]
for i in numbers:
    if i>largest:
      largest=i
print(largest)
smallest=numbers[0]
for i in numbers:
    if i<smallest:
      smallest=i
print(smallest)

