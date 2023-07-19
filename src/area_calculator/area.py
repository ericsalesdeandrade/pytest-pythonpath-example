"""
Python code to calculate area of various shapes
"""

def square(side: float) -> float:
    """
    Calculate area of a square
    """
    return round(side * side, 2)

def rectangle(length: float, breadth: float) -> float:
    """
    Calculate area of a rectangle
    """
    return round(length * breadth, 2)

def circle(radius: float) -> float:
    """
    Calculate area of a circle
    """
    return round(3.14 * radius * radius, 2)

def triangle(base: float, height: float) -> float:
    """
    Calculate area of a triangle
    """
    return round(0.5 * base * height, 2)