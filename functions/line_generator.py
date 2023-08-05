"""Line Generator"""
# libs
import numpy as np

from numpy import ndarray

# imports
from functions.mesh_config import Mesh_Config

LINES = {}


class Source_Line(object):
    """Y Slice of the Mesh Object"""

    def __init__(self, in_row: np.ndarray) -> None:
        """Takes an Array [0,2] of a Y slice"""
        # set id to a python compatible float for indexing later
        self.id = np.round(float(in_row[1]), 2)
        # f16 for speed (in theory)
        self.points: ndarray = np.array(in_row[0:3].round(2), dtype=np.float16)
        self.build_lines()

    def build_lines(self) -> None:
        """Generate or Append to Line"""
        if LINES.get(self.id) is None:
            LINES.setdefault(self.id, np.array(self.points, ndmin=2, dtype=np.float16))
        # --------------
        else:
            LINES[self.id] = np.vstack((LINES[self.id], self.points))
        # ---


# -------------------------------------------------------------------


def generate_lines(in_array) -> dict[float, ndarray]:
    # --------

    for li in in_array:
        # for i in range(1, 10000, 500):
        Source_Line(li)
    # --------

    return LINES


# -------------------------------------------------------------------
