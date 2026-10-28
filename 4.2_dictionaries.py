"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:A dictionary describing a dress with five fields
# 2. Process:Read the name, update stock, remove size, and display the fields
# 3. Out:The dress information before and after the changes
# 4. My object, my five fields, and why those:My object is a jersey dress.
# name & color & size identifies the product.
# price records its selling price in euros.
# stock shows how many units are available.


# Your code below

# Create a dictionary describing the dress.
dress = {
    "name": "jersey dress",
    "price": 300,
    "color": "black",
    "size": "L",
    "stock": 20
}

# printing the dictionary
print("The dictionary is:", dress)
print("Product name:", dress["name"])

# Change the stock after selling one dress
dress["stock"] = 19
print("After updating stock:", dress)

# Remove the size and display the removed value.
removed_size = dress.pop("size")
print("After removing size:", dress)
print("The removed size is:", removed_size)

# Display each remaining field with its value.
for field, value in dress.items():
    print(field, ":", value)


print("Material:", dress.get("material", "Not available"))

#test:dress["material"] caused a KeyError because the field was missing.
#Using get() displayed "Not available" and the program continued