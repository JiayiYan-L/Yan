"""Exercise 3.0 — Computing with what the user typed

WHAT THE PROGRAM MUST DO
    Ask for two numbers and display the result of the four operations.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should your program do when the second number is zero? Decide, write your
       decision down, and only then implement it.

WHAT THE AI CANNOT KNOW
    Your answer to question 4. There are at least three defensible ones: refuse the
    value and ask again, display a message instead of a result, or stop the program.
    Pick one and be able to defend it.

CHECK IT YOURSELF
    Compute 7 divided by 2 in your head. Run your program with 7 and 2. If your program
    shows 3, it is not wrong by accident: find out why, and write the reason in a comment.
    Then run it with 0 as the second number.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:Two numbers entered 
# 2. Process:Calculate their sum, difference, product, and quotient
# 3. Out:The results of the four arithmetic operations
# 4. What happens when the second number is zero, and why:If the second number is zero, show a message instead of the division result,
# because division by zero is undefined

# Your code below
number_1 = float(input("Enter the first number:"))
number_2 = float(input("Enter the second number:"))

print(number_1, number_2)

# sum of two numbers
sum = number_1 + number_2
print("The sum of two numbers is:", sum )

#difference of two numbers
diff = number_1 - number_2
print("the difference between two numbers is:", diff)

#multiplication of two numbers
product = number_1 * number_2
print("The product of two numbers is:", product)

# division of two numbers
if number_2 == 0:
    print("Warning: Cannot divide by zero.")
else:
    division = number_1/number_2
    print("The division of two numbers is:", division)


#test:Enter the first number:7.0
#Enter the second number:2.0
#The sum of two numbers is: 9.0
#the difference between two numbers is: 5.0
#The product of two numbers is: 14.0
#The division of two numbers is: 3.5

#test:Enter the first number:7.0 Enter the second number:0.0
#The sum of two numbers is: 7.0
#the difference between two numbers is: 7.0
#The product of two numbers is: 0.0
#Warning: Cannot divide by zero.