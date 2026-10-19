# Extracted from python-book.pdf, page 23.
# NEEDS REVIEW: automatic OCR output did not pass a syntax check (SyntaxError: invalid syntax).
# Compare with the screenshot in the PDF before using.

# List of items
items = |[1,  3,  2,  7,  9,  4,  'Blue',  'Red',  'Green'|]
# Prints all items
print(items)
# We count items/elements from 0 -  Position/Index
# Prints the item in second position/index in the List
print(items[1])

# Prints from second item to third item.  (minus 1)
print(items[1:4])

# Prints from Third item in the  list and above.
print(items[3:])

# Prints from first to the fifth item
print(items[:6])

# Since we do not have item at Index 14.
# Python shows an out of bounds exeption.
print(items[14])
