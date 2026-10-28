"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""
# 1. In:The eight dress prices from exercise 4.0
# 2. Process:Display the Mountain, reversed, ascending, and descending orders
# 3. Out:Four list orders, followed by the unchanged original list
# 4. My four orders, and which ones modify the original:Mountain, reversed, ascending, and descending orders
#None modifies the original

# Your code below

prices = [200, 220, 300, 180, 185, 190, 280, 255]

# reversed copy of the original list
reversed_prices = prices[::-1]
print("Reversed:", reversed_prices)

# from lowest to highest
ascending_prices = sorted(prices)
print("Ascending:", ascending_prices)

# from highest to lowest
descending_prices = sorted(prices, reverse=True)
print("Descending:", descending_prices)

# mountain shape
left_side = ascending_prices[::2]
right_side = ascending_prices[1::2]
mountain_prices = left_side + right_side[::-1]
print("Mountain:", mountain_prices)

# Display the original list last to confirm it is unchanged.
print("Original:", prices)


# Test: the final original list matched 4.0 