"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:enter an integer N (from 1 to N)
# 2. Process:Check whether each integer from 1 to N is odd or even
# 3. Out:Each number from 1 to N with its odd or even label
# 4. What happens on 0, on a negative number, on a very large number:
# For zero: display a message and do not run the loop.
# For negative numbers: display a message and do not run the loop.
# For positive numbers: allow all values, including 5000, with no upper limit.

# Your code below

# enter an integer
N = int(input("Enter a positive integer: "))

# Reject zero and negative numbers
if N <= 0:
    print("Please enter a positive integer.")
else:
    for number in range(1, N + 1):
        if number % 2 == 0:
            print(f"{number} is even")
        else:
            print(f"{number} is odd")


# Test: 6 produced three odd and three even numbers.
# Test: 0 displayed a message without running the loop.
# Test: -4 displayed a message without running the loop.
# Test: 5000 printed the results from 1 to 5000.