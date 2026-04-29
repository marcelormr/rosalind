# Problem Summary

Given two positive integers representing the legs of a right triangle,
calculate the square of the hypotenuse.

This applies the Pythagorean theorem:

a² + b² = c²

where the required output is the value of c², not the square root.

# Approach

I assigned the two values to variables `a` and `b` and calculated:

`a * a + b * b`

The result was stored in `h` and printed as the final answer.

Since the problem asks for the square of the hypotenuse, there is no need
to calculate the square root.

# What This Exercise Reinforced

- variable assignment
- integer arithmetic in Python
- multiplication and operator precedence
- translating a mathematical formula into code

# Common Pitfalls

A common mistake is calculating the square root of the result, but the problem
only asks for the squared hypotenuse.

Another possible issue is confusing exponentiation with multiplication.
In Python, `a * a` and `a ** 2` both work, but `^` does not mean power.

# Takeaway

This exercise reinforced basic arithmetic operations and the importance of
reading problem statements carefully before implementing the solution.
