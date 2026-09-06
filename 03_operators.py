"""
========================================================
           LECTURE 1 - FILE 3: OPERATORS
========================================================
Topics: Arithmetic, Comparison, Assignment, Logical,
        Membership, Identity, Bitwise Operators
========================================================
"""

# ========================================================
# PART A: ARITHMETIC OPERATORS
# ========================================================

# Q1. A cinema ticket costs 750 PKR.
#     A customer buys 4 tickets.
#
#     Calculate and print the total cost.

ticket_price = 750
number_of_tickets = 4

total_cost = ticket_price * number_of_tickets

print("Total Cost:", total_cost, "PKR")

# --------------------------------------------------------

# Q2. A rectangle has a length of 24 cm and a width
#     of 9 cm.
#
#     Calculate and print:
#     - Area
#     - Perimeter

length = 24
width = 9

area = length * width
perimeter = 2 * (length + width)

print("Area:", area, "cm²")
print("Perimeter:", perimeter, "cm")

# --------------------------------------------------------

# ========================================================
# PART B: COMPARISON OPERATORS
# ========================================================

# Q3. A game requires a player to have at least
#     500 points to unlock the next level.
#
#     Store the player's score in a variable.
#     Check whether the player can unlock the level.

player_score = 650

can_unlock_level = player_score >= 500

print("Can Unlock Level:", can_unlock_level)

# --------------------------------------------------------

# ========================================================
# PART C: ASSIGNMENT OPERATORS
# ========================================================

# Q4. A wallet initially contains 2,000 PKR.
#
#     Using assignment operators:
#     - Add 500
#     - Subtract 250
#     - Add 1,000
#
#     Print the balance after each operation.

balance = 2000

balance += 500
print("After Adding 500:", balance)

balance -= 250
print("After Subtracting 250:", balance)

balance += 1000
print("After Adding 1000:", balance)

# --------------------------------------------------------

# ========================================================
# PART D: LOGICAL OPERATORS
# ========================================================

# Q5. A student can enter a competition if:
#
#     - Their age is at least 18
#     - AND they have a valid registration
#
#     Create suitable variables and use the 'and'
#     operator to determine whether they can participate.

age = 18
valid_registration = True

can_participate = age >= 18 and valid_registration

print("Can Participate:", can_participate)

# --------------------------------------------------------





