# Extracted from python-book.pdf, page 58.

# initialize the amount variable
marks = 10000
# perform division with 0
try:
    a = marks / 0
    print(a)
except Exception as e:
    print("Exception Caught", e)
