""" Coordinate correlation check function"""
# libs
from numpy import tan, arctan, sqrt, square

# -------------
# imports
# --------------
# global variables
debug = True
# ================================


def check_coord(ref_point: list, n_point: list) -> bool:
    """
    This function takes two points on a plane as input and returns True if they are close enough to each other. It does this by:
    Calculating the arc tangent of ref_cord and adding 1 (to elongate the curve) to it, storing it in ref_arc variable
    Calculating the square root of the product of the tangents of ref_cord and n_cord squared
    Dividing out by ref_arc and subtracting 1 from it (to elongate the curve), storing it in coord variable
    Checking if coord is between 0 and 1 using an if statement
    Returning True as the output of the function, if the points are close enough to each other.

    This uses a variation of the haversine formula
    """
    global debug
    print("ran")
    try:
        ref_cord = square(sum(ref_point))
        n_cord = square(sum(n_point))
        ref_arc = arctan(ref_cord) + 1
        out = sqrt((square(tan(ref_cord) * tan(n_cord))))
        coord = out / ref_arc - 1
        # -------------
        if coord < 1 and coord > 0:
            if debug is True:
                print(
                    ref_point, n_point, coord, file=open(".\\temp\\coor_log.txt", "a")
                )
            return True
        else:
            return False
    except Exception:
        return False
