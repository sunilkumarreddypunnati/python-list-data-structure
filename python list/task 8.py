'''Task 8: Filter Odd Numbers

From the given list, create a new list containing only odd numbers 
using list comprehension.
Print the new list.
👉 Example List:
numbers = [12, 3, 7, 18, 21, 44, 55, 62, 71]'''
numbers = [12, 3, 7, 18, 21, 44, 55, 62, 71]
odd_numbers=[i for i in numbers if i%2!=0]
print(odd_numbers)