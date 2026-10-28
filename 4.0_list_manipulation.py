"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Eight dress prices in euros
# 2. Process:Select one price, sort the list, and calculate the average price
# 3. Out:The full list, highest price, sorted prices, and the average
# 4. What my list is about, and what I computed from it:My list contains dress prices, highest price,sorted prices,and I calculated their average.


# Your code below

def calculate_average(numbers):
    # Add all prices and count how many there are.
    total = sum(numbers)
    count = len(numbers)

    # Divide the total by the number of prices.
    average = total / count
    return average

prices = [200, 220, 300, 180, 185, 190, 280, 255]
print("Average price in euros:", calculate_average(prices))
print("All prices:", prices) 
print("Highest price:", max(prices))  
print("Sorted prices:", sorted(prices)) 


first_three = prices[:3]
test_average = sum(first_three) / len(first_three)
print("Average of the first 3 prices:", test_average)

# Test: (200 + 220 + 300) / 3 = 240 by hand.
# The program returned 240.0, matching my calculation.