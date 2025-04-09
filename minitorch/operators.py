"""Collection of the core mathematical operators used throughout the code base."""

import math
from functools import reduce
# ## Task 0.1
from typing import Callable, Iterable

def mul(x: float, y: float) -> float:
    """Multiply two numbers."""
    return x * y
def id(x: float) -> float:
    """Identity function."""
    return x
def add(x: float, y: float) -> float:
    """Add two numbers."""
    return x + y
def neg(x: float) -> float:
    """Negate a number."""
    return -x
def lt(x: float, y: float) -> bool: 
    """Less than."""
    return x < y
def eq(x: float, y: float) -> bool:
    """Equal."""
    return x == y
def max(x: float, y: float) -> float:
    """Maximum of two numbers."""
    return x if x > y else y
def is_close(x: float, y: float) -> bool:
    """Check if two numbers are close."""
    return abs(x - y) < 1e-2
def sigmoid(x: float) -> float:
    """Sigmoid function."""
    if x >= 0:
        return 1.0 / (1.0 + math.exp(-x))
    else:
        return math.exp(x) / (1.0 + math.exp(x))
def relu(x: float) -> float:
    """ReLU function."""
    return max(0, x)
def log(x: float) -> float:
    """Natural logarithm."""
    return math.log(x)
def exp(x: float) -> float:
    """Exponential function."""
    return math.exp(x)
def log_back(x: float) -> float:
    """Derivative of log function."""
    return 1 / x
def inv(x: float) -> float:
    """Inverse function."""
    return 1 / x
def inv_back(x: float) -> float:
    """Derivative of inverse function."""
    return -1 / (x ** 2)
def relu_back(x: float) -> float:
    """Derivative of ReLU function."""
    return 1 if x > 0 else 0

#
# Implementation of a prelude of elementary functions.

# Mathematical functions:
# - mul
# - id
# - add
# - neg
# - lt
# - eq
# - max
# - is_close
# - sigmoid
# - relu
# - log
# - exp
# - log_back
# - inv
# - inv_back
# - relu_back
#
# For sigmoid calculate as:
# $f(x) =  \frac{1.0}{(1.0 + e^{-x})}$ if x >=0 else $\frac{e^x}{(1.0 + e^{x})}$
# For is_close:
# $f(x) = |x - y| < 1e-2$


# TODO: Implement for Task 0.1.


# ## Task 0.3

# Small practice library of elementary higher-order functions.

# Implement the following core functions
# - map
# - zipWith
# - reduce
#
# Use these to implement
# - negList : negate a list
# - addLists : add two lists together
# - sum: sum lists
# - prod: take the product of lists


# TODO: Implement for Task 0.3.
def addLists(x: Iterable[float], y: Iterable[float]) -> Iterable[float]:
    """Add two lists together."""
    return map(add, x, y)
def negList(x: Iterable[float]) -> Iterable[float]:
    """Negate a list."""
    return map(neg, x)
def sum(x: Iterable[float]) -> float:
    """Sum a list."""
    return reduce(add, x)
def prod(x: Iterable[float]) -> float:
    """Take the product of a list."""
    return reduce(mul, x)