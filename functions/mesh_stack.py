""" in mesh object pointer"""

import numpy as np

# imports
from functions.mesh_config import Mesh_Config

# =====================================


class Mesh_Stack(object):
    """sub stack sorter"""

    def __init__(self, config: Mesh_Config):
        self.id = 0
        # self.dict: dict = {}
        self.stack: list = []
        self.q_line: list = []
        # self.dict.setdefault(id, self.stack)

    def append_coord(self, coord: np.ndarray):
        self.q_line.append(coord)

    def append_line(self):
        self.stack.append(self.q_line)
        self.q_line = []


# =====================================
