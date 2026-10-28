"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: answer to a yes/no question.
# 2. Process:Repeat the question until yes, no, or ten attempts
# 3. Out:The number of attempts and the final result
# 4. My stop condition, my attempt limit, my summary:
#Stop when the user enters yes or no.
# Allow at most ten attempts, then stop with a limit message.
# Accept capitals and extra spaces as equivalent answers.
# The summary shows attempts used and the final choice or limit reached.


# Your code below


attempts = 0
max_attempts = 10
answer = None

while answer not in ("yes", "no") and attempts < max_attempts:
    answer = input("Do you want to continue? (yes/no): ").strip().lower()
    attempts += 1

# Show the number of attempts and the final result.
print("Attempts used:", attempts)

if answer == "yes":
    print("You chose to continue.")
elif answer == "no":
    print("You chose to stop.")
else:
    print("Maximum attempts reached. No valid answer received.")


#test:ten useless answers stopped the loop after ten attempts.
#yes and no were each accepted on the first attempt
#YES with spaces was accepted as yes