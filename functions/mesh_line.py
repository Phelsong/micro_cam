""" **in** M_Object , post line sorting"""
# libs
import numpy as np

# imports
from .mesh_object import Mesh_Object, MESH_OBJECTS

# =========================


class Mesh_Line(object):
    def __init__(self, id: float):
        self.id: float = id
        self.coords: list = []
        self.min_x = lambda: self.coords[0][0]
        self.max_x = lambda: self.coords[-1][0]

    def append(self, coord):
        self.coords.append(coord)

    def close(self, new_obj: bool):
        """close line"""
        # ----
        if len(self.coords) < 1:
            return
            # ----
        if new_obj is False and len(MESH_OBJECTS) > 0:
            # add to last existing object
            last = next(reversed(MESH_OBJECTS.keys()))
            MESH_OBJECTS[last].append(self)
            # ----
        else:
            Mesh_Object(self)
        # --------------------

    def q_close(self):
        from .mesh_object import MESH_OBJECTS

        # ----
        min_x = self.min_x()
        max_x = self.max_x()
        # ----

        for obj in MESH_OBJECTS.values():
            # ----

            obj.calc_dimensions()

            # ----

            if min_x >= obj.min_x() and max_x <= obj.max_x():
                # -----

                if self.id in obj.lines.keys():
                    np.vstack((obj.lines[self.id], self.coords))
                    return

                # -----

                else:
                    obj.append(self)
                    return

                # -----
            # -----------
        Mesh_Object(self)


# ================================================================
