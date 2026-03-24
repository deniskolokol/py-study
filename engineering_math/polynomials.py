"""
This module contains functions to solve polynomial equations.

The `solve_itr` function uses an iterative approach to find solutions to the
given polynomial equation. Use it to find the smallest integer factor. Useful
for simple polynomials where symbolic solutions are not required. Simplifies
the mannual solution process for basic polynomials.

The `solve_sym` function uses the `sympy` library to find symbolic solutions to
the given polynomial equation. Use it to find symbolic solutions to polynomial
equations. Useful for more complex polynomials where symbolic solutions are
desired. Provides a more robust and accurate solution method for polynomials of
any degree.
"""

from sympy import symbols, solve, sympify


def solve_itr(func: str, num_solutions: int = 1 or None) -> list:
    """
    Solve the given polynomial equation using an iterative approach. Use only 
    for simple polynomials where symbolic solutions are not required. Simplifies
    the manual solution process for basic polynomials.

    Warning:
    - this only works if there is at least one integer solution
    - this will only solve for integer solutions, and will miss non-integer
      solutions
    - this will not work for polynomials with very large integer solutions, or
      with many solutions, as it will take a long time to find them all
    - this will not work for polynomials with no integer solutions, as it will
      run for 1000 iterations and then stop without finding any solutions
    """
    if num_solutions is not None:
        if num_solutions < 1:
            num_solutions = None # pyright: ignore[reportAssignmentType]

    res = list()
    x = 1
    for i in range(1000):
        if eval(func) == 0:
            res.append(x)

        if x > 0:
            x = 0 - x
        else:
            x = abs(x) + 1

        if num_solutions: 
            if len(res) == num_solutions:
                break

    return res


def solve_sym(func: str, num_solutions: int = 1 or None) -> list:
    """
    Solve the given polynomial equation using sympy.

    If num_solutions is None, return all solutions.
    Otherwise, return the specified number of integer solutions, sorted by
    absolute value and then by value (useful for finding the first integer
    factor).
    """
    func_ = sympify(func)
    x = symbols('x')
    result = solve(func_, x)
    if num_solutions is None:
        return result

    # Filter out non-integer solutions and sort by absolute value, then by value.
    result = sorted([x for x in result if int(x) == x], key=lambda x: (abs(x), x))
    return result[:num_solutions]


if __name__ == '__main__':
    func = input("Input function definition: ")
    num_solutions = input("Number of solutions to find ([Enter] for all): ")
    itr_or_sym = input("Use iterative method (Y/n)? ")

    # Iterative method is the default.
    if itr_or_sym is None:
        itr_or_sym = 'y'
    if itr_or_sym.lower() == 'y':
        fdef = solve_itr
    else:
        fdef = solve_sym

    if num_solutions.strip() == '':
        data = fdef(func)
    else:
        data = fdef(func, int(num_solutions))
    print(data)
