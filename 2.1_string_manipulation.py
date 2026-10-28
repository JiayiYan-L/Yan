"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:A sentence“Python is very complicated“
# 2. Process:Apply four different text transformations
# 3. Out:Four different transformed versions of the sentence
# 4. My four transformations, and when each is useful
# upper(): Make text uppercase
# title(): Format a heading with capitalized words.
# lower(): Make text lowercase
# replace(): Replace spaces with underscores for a sentence.


# Your code below

text = input (" Enter a sentence: ")

print(text.upper())
print(text.title())
print(text.lower())
print(text.replace(" ", "_"))



#test:upper: All letters became uppercase; spaces remained
# Test title: Each word started with a capital; spaces remained
# Test lower: All letters became lowercase; spaces remained
# Test replace: Every space became an underscore,both the front and the back