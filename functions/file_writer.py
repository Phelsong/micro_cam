""" File Writer"""

# lib
from typing import TextIO
import numpy as np

# imports


# ============================


class Writer(object):
    """File Writer"""

    def __init__(self, path, gcode) -> None:
        self.file = path
        self.g_lib = gcode

        # ==============================

        """NOT FULLY IMPLEMENTED"""

    def write_header(self, f) -> None:
        for line in self.g_lib.header:
            f.write(f"{line}\n")

    # ==============================

    def write_footer(self, f) -> None:
        """NOT FULLY IMPLEMENTED"""
        for line in self.g_lib.footer:
            f.write(f"{line}")

    # ==============================

    def write_lines(
        self,
    ):
        """Write Lines to File"""
        from functions.mesh_object import MESH_OBJECTS

        print("number of mesh objects:", len(MESH_OBJECTS))
        gcode = self.g_lib
        direction: bool = True
        # first_coord = [0, 0]
        last_coord: list[int] = [0, 0]

        # -----------
        with open(f"./temp/{self.file}", "a") as f:
            # ---
            self.write_header(f)

            # ---

            for obj in MESH_OBJECTS:
                # ------

                for line in MESH_OBJECTS[obj].lines:
                    # --------
                    d_line = (
                        MESH_OBJECTS[obj].lines[line][
                            MESH_OBJECTS[obj].lines[line][:, 0].argsort(axis=0)[::-1]
                        ]
                        if direction is True
                        else MESH_OBJECTS[obj].lines[line][
                            MESH_OBJECTS[obj].lines[line][:, 0].argsort(axis=0)
                        ]
                    )

                    # -----

                    # first_coord = [d_line[0][0], d_line[0][1] * -1]
                    last_coord = [d_line[-1][0], d_line[-1][1] * -1]

                    # ------

                    f.write(f"{gcode.change_line_speed}")
                    f.write(f"G1 X{d_line[0, 0]} Y{d_line[0, 1]* -1} Z2.0\n")
                    f.write(f"G1 X{d_line[0, 0]} Y{d_line[0, 1]* -1} Z{d_line[0, 2]}\n")
                    f.write(f"{gcode.line_speed}")

                    # ------

                    for coord in d_line:
                        x = round(float(coord[0]), 3)  #
                        y = round(float(coord[1]), 3) * -1  # invert for reasons
                        z = round(float(coord[2]), 4) if coord[2] > 0.02 else 0.02
                        f.write(f"G1 X{x} Y{y} Z{z}\n")
                        # ---------

                    # -----------
                    # shuffle
                    if direction is True:
                        f.write(f"G1 X{last_coord[0]} Y{last_coord[1]} Z2\n")
                        direction = False
                    else:
                        f.write(f"G1 X{last_coord[0]} Y{last_coord[1]} Z2\n")
                        direction = True

    # =========================================================================================

    def write_each(
        self,
    ):
        """Writes each object to a seperate File"""
        # TODO: UPDATE to make Write_lines!!!!

        from functions.mesh_object import MESH_OBJECTS

        print(len(MESH_OBJECTS))
        gcode = self.g_lib
        direction: bool = True

        for obj in MESH_OBJECTS:
            with open(f"./temp/{MESH_OBJECTS[obj].id}.tap", "a") as f:
                # ------
                for line in MESH_OBJECTS[obj].lines:
                    d_line = (
                        MESH_OBJECTS[obj].lines[line][
                            MESH_OBJECTS[obj].lines[line][:, 0].argsort(axis=0)[::-1]
                        ]
                        if direction is True
                        else MESH_OBJECTS[obj].lines[line][
                            MESH_OBJECTS[obj].lines[line][:, 0].argsort(axis=0)
                        ]
                    )
                    f.write(f"{gcode.change_line_speed}")
                    f.write(f"G1 X{d_line[0, 0]} Y{d_line[0, 1]} Z{d_line[0, 2]} \n")
                    f.write(f"{gcode.line_speed}")
                    for coord in d_line:
                        x = np.round(float(coord[0]), 2)
                        y = np.round(float(coord[1]), 2)
                        z = np.round(float(coord[2]), 2)
                        f.write(f"G1 X{x} Y{y} Z{z}\n")
                    # shuffle
                    if direction is True:
                        direction = False
                    else:
                        direction = True


# =========================================================================================
