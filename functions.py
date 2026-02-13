#Write a Python function that accepts two numbers as input and returns their sum, difference, and product.
#-Add docstrings to the function to describe its purpose and parameters.
#-Have each member of the group modify the function to include additional operations (e.g., division, power).
#-Challenge: Use default arguments and keyword arguments in the function.


#Each semi-colon is used to tell python separate the docstrings with the line of code it's situated in.



def calculate_operations(num1, num2):
    sum_result = num1 + num2 ; """This variable stores the sum of num1 and num2.""" 
    print(f"Sum: {sum_result}")

    difference_result = num1 - num2; """This variable stores the difference of num1 and num2."""
    print(f"Difference: {difference_result}")

    product_result = num1 * num2 ; """This variable stores the product of num1 and num2."""
    print(f"Product: {product_result}")

    division_result = num1 / num2 ; """This variable stores the division of num1 by num2."""
    print(f"Division: {division_result}")

    exponentiation_result = num1 ** num2 ; """This variable stores the result of num1 raised to the power of num2."""
    print(f"Exponentiation: {exponentiation_result}")

    return sum_result, difference_result, product_result, division_result, exponentiation_result

calculate_operations(6,1)

#calculate_operations(num1=6,num2=1) #Example with a keyword argument; the order of the arguments can be changed when using keyword arguments. 

#A keyword argument is when you pass values using the parameter names instead of relying on position.