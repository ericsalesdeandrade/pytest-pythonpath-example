# import sys
# sys.path.append('src')


from src.area_calculator.area import (
    square, 
    rectangle, 
    circle, 
    triangle
)

def test_square():
    """
    Test square function
    """
    assert square(2) == 4
    assert square(3) == 9
    assert square(4) == 16

def test_rectangle():
    """
    Test rectangle function
    """
    assert rectangle(2, 3) == 6
    assert rectangle(3, 4) == 12
    assert rectangle(4, 5) == 20

def test_circle():
    """
    Test circle function
    """
    assert circle(2) == 12.56
    assert circle(3) == 28.26
    assert circle(4) == 50.24

def test_triangle():
    """
    Test triangle function
    """
    assert triangle(2, 3) == 3
    assert triangle(3, 4) == 6
    assert triangle(4, 5) == 10