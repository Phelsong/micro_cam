""" in mesh object pointer"""
# lib
import numpy as np

# ----
MESH_OBJECTS = {}


# ===========
class Mesh_Object(object):
    """sorted mesh object"""

    def __init__(self, line) -> None:  # type: ignore
        self.id: float = len(M_OBJECTS) + 1
        self.lines: dict[float, np.ndarray] = {
            line.id: np.array(line.coords, dtype=np.float16)
        }
        # TODO: set this to only run if the object has been updated since last run
        self.dimensions: list[float] = [0, 0, 0, 0]  # min_x, max_x, min_y, max_y
        # ---------------
        self.min_x = lambda: self.dimensions[0]
        self.max_x = lambda: self.dimensions[1]
        self.min_y = lambda: self.dimensions[2]
        self.max_y = lambda: self.dimensions[3]
        # ---------------
        MESH_OBJECTS.setdefault(self.id, self)

    # ==================
    def append(self, line) -> None:
        self.lines[line.id] = np.array(line.coords, dtype=np.float16)

    # ==================
    def line_min_x(self, id):
        return min([e[0:1] for e in self.lines[id]])

    # ==================
    def line_max_x(self, id):
        return max([e[0:1] for e in self.lines[id]])

    # ==================
    def calc_dimensions(self) -> None:
        """Calculate the dimensions of the object"""

        # ----

        min_x: float = 20
        max_x: float = -20
        min_y: float = min(self.lines.keys())
        max_y: float = max(self.lines.keys())

        # ----

        for line in self.lines.keys():
            # ----
            line_min_x = min(self.line_min_x(line))
            line_max_x = max(self.line_max_x(line))
            # ----
            if line_min_x < min_x:
                min_x = line_min_x
            if line_max_x > max_x:
                max_x = line_max_x
        # --------------

        self.dimensions = [min_x, max_x, min_y, max_y]

    # =============================

    def add(self, id, line) -> None:
        """Add a line to the object"""
        try:
            np.vstack((self.lines[id], line))
        except KeyError:
            self.lines[id] = np.array(line, dtype=np.float16)

    # =============================

    def merge(self, in_obj):
        """Merge two objects"""
        # ----
        stack = {}
        # ----

        for id, line in in_obj.lines.items():
            if id in self.lines:
                self.lines[id] = np.vstack((self.lines[id], line))
            else:
                stack[id] = line
        # ----------

        for id, li in stack.items():
            self.add(id, li)

        # ----------


# =============================
