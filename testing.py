#Write a Python function that accepts two numbers as input and returns their sum, difference, and product.
#-Add docstrings to the function to describe its purpose and parameters.
#-Have each member of the group modify the function to include additional operations (e.g., division, power).
#-Challenge: Use default arguments and keyword arguments in the function.


#Each semi-colon is used to tell python separate the docstrings with the line of code it's situated in.



def calculate_operations(a, b):
    sum_result = a + b ; """This variable stores the sum of a and b."""
    print(f"Sum: {sum_result}")

    difference_result = a - b; """This variable stores the difference of a and b."""
    print(f"Difference: {difference_result}")

    product_result = a * b ; """This variable stores the product of a and b."""
    print(f"Product: {product_result}")

    division_result = a / b ; """This variable stores the division of a by b."""
    print(f"Division: {division_result}")

    exponentiation_result = a ** b ; """This variable stores the result of a raised to the power of b."""
    print(f"Exponentiation: {exponentiation_result}")

    return sum_result, difference_result, product_result, division_result, exponentiation_result

calculate_operations(2, 7)
