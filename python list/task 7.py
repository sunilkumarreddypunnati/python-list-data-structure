'''Task 7: List Comprehension – Squares
Create a new list of squares of numbers from 1 to 10 using list comprehension.
Print only the even squares.
👉 Example List:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]'''
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares=[i**2 for i in numbers]
print("all squares:",squares)
even_squares=[ i for i in squares if i%2==0]
print("even squares:",even_squares)
