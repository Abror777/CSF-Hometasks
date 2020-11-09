"""
Teaching Week 2
Geneslant Program
"""

"""
The first example
Example 1: Define a function that takes an argument.
Identify what code is the argument and what code is the parameter.dlsejnfsefnksjzefnkzsejnf
"""


def example1(string, isAdmin=False):
    # Parameters usage example
    print("The passed data is", string)

    # Argument usage
    print("The passed argument is", isAdmin)
    pass


"""
The second example
Example 2: Call your function from Example
1 three times with different kinds of arguments:
a value, a variable, and an expression.
Identify which kind of argument is which.
"""


def example2():
    # Parameter with String type
    example1("just string")

    # Parameter with Number type
    example1(10101001101)

    # Parameter & Argument
    example1(True, True)
    pass


"""
The third example
Example 3: Create a function with a local variable.
Show what happens when you try to use that variable outside the function.
Explain the results.
"""

variable_for_example3 = "passing string"


def example3():
    print("Printing variable from outside:", variable_for_example3)
    pass


"""
The fourth example
Example 4: Create a function that takes an argument. 
Give the function parameter a unique name. 
Show what happens when you try to use that parameter name outside the function. 
Explain the results.
"""

variable_for_example4, example = "hello", "world"


# Taking existing variable name as argument
def example4(example):

    # If you took existing argument as variable
    # Function's argument will shadow existing variable
    # But still you can specify the type in order to differentiate

    """
    :type example: str
    """

    # Now, let's print the argument here with
    # variable_for_example4
    print("The passed argument is:", example)

    # Expecting value is hello because whatever I'll
    # put to example variable, it will be shadowed with
    # new variable argument here

    pass


"""
The fifth example
Example 5: Show what happens when a variable defined outside a function 
has the same name as a local variable inside a function. 
Explain what happens to the value of each variable as the program runs.
"""


def example5():

    # As we remember, it accepts example
    # Now let's try with example either
    example4(example=example)
    pass


# The main program where I'll be executing all inits
def main():
    # Executing the first example
    example1("Hello", True)

    # Executing the first example
    example2()

    # Executing the first example
    example3()

    # Executing the first example
    example4(variable_for_example4)

    # Executing the first example
    example5()

    pass


# Initiating main program
if __name__ == '__main__':

    try:
        main()
    except Exception as error:
        print("Error occurred:", error)
    pass
© 2020 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
