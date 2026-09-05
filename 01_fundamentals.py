"""
========================================================
             LECTURE 1 - FILE 1: Fundamentals of python
========================================================
Topics: Character Set, Variables, Identifiers
Total Questions: 12
========================================================
"""
# ========================================================
# PART A: PYTHON CHARACTER SET
# ========================================================

# Q1. Print a short Python-themed banner using letters,
#     digits, spaces, and special characters.

print("PYTHON 3 >>> [START]")

# --------------------------------------------------------

# Q2. Print a product label containing:
#     - A product name
#     - A product code
#     - Special characters
#
#     Create the label yourself.

print("Product: Python Notebook")
print("Code: PY-2026")
print("Price: $80.00")

# --------------------------------------------------------

# Q3. Create and print a three-line message using
#     different characters and symbols.
#
#     Your output should look like a small terminal
#     welcome screen.

print("==============================")
print(">>> WELCOME TO PYTHON <<<")
print("==============================")


# ========================================================
# PART B: VARIABLES
# ========================================================

# Q4. A shop has 12 notebooks, each costing 80.
#
#     Create variables for the quantity and price.
#     Store the total cost in another variable.
#     Print the total.

quantity = 12
price = 80
total_cost = quantity * price

print(total_cost)

# --------------------------------------------------------

# Q5. Create variables to store the details of a movie:
#
#     - Movie title
#     - Release year
#     - Rating
#
#     Display the information using print().

movie_title = "Inception"
release_year = 2010
rating = 8.8

print("Movie Title:", movie_title)
print("Release Year:", release_year)
print("Rating:", rating)

# --------------------------------------------------------

# Q6. Create two variables containing different numbers.
#
#     Create separate variables to store:
#     - Their sum
#     - Their difference
#     - Their product
#
#     Print all three results.

number1 = 20
number2 = 5

sum_result = number1 + number2
difference = number1 - number2
product = number1 * number2

print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)


# --------------------------------------------------------

# Q7. A game player starts with 100 points.
#
#     Store the points in a variable.
#     Add 250 points to it.
#     Print the updated score.

points = 100
points = points + 250

print(points)

# --------------------------------------------------------

 Q8. Create three variables for the dimensions of a box:
#
#     length = 15
#     width = 8
#     height = 5
#
#     Store the volume in another variable and print it.

length = 15
width = 8
height = 5

volume = length * width * height

print(volume)

# --------------------------------------------------------

# Q9. Swap two variables WITHOUT using a third variable.
#     Start with: x = 5, y = 10
#     After swap: x should be 10, y should be 5
#     Print both after swapping.

x = 5
y = 10

x, y = y, x

print("x =", x)
print("y =", y)

# --------------------------------------------------------

# ========================================================
# PART C: RULES OF IDENTIFIERS
# ========================================================

# Q10. Create valid Python identifiers for these items:
#
#     - employee salary
#     - phone number
#     - department name
#     - joining year
#
#     Assign suitable values and print them.

employee_salary = 50000
phone_number = "03001234567"
department_name = "Computer Science"
joining_year = 2026

print("Employee Salary:", employee_salary)
print("Phone Number:", phone_number)
print("Department Name:", department_name)
print("Joining Year:", joining_year)

# --------------------------------------------------------