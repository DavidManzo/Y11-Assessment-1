from testhelper import test
# IDEA: compare each possible sum (123,456,789,147,258,369,159,357) to each other,
# if they ALL are equal to each other, print "true". if even one sum is different
# from the rest, print "false"
def is_square_magic(square):
    pass # Replace this with your code






### TESTS - Run the code that calls the function to check it works.
valid_square = [[4, 9, 2], 
          [3, 5, 7], 
          [8, 1, 6]]

invalid_square = [[4, 9, 2], 
          [8, 1, 6],
          [3, 5, 7]]

test("Magic Square 1", True, is_square_magic(valid_square))
test("Magic Square 2", False, is_square_magic(invalid_square))