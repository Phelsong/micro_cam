""" in mesh object pointer"""

# libs
import numpy as np

# imports
from functions.mesh_config import Mesh_Config
from .mesh_line import Mesh_Line

# =====================================


class Mesh_Queue(object):
    """stack sorter"""

    def __init__(self, config: Mesh_Config):
        # TODO: update to use M_Stack
        self.stack: list = []
        self.sub_stack: list = []
        self.q_line: list = []
        self.height_max: float = config.height_max
        self.x_width: float = config.x_width
        self.y_width: float = config.y_width
        self.last_qx: float = 0
        self.last_qy: float = 0
        self.last_qz: float = 0
        self.is_first_sort: bool = True
        self.jump = False

    # =====================================
    def append(self, item) -> None:
        """append item to queue stack"""
        self.stack.append(item)

    # =====================================
    def set_last_coord(self, coord: np.ndarray) -> None:
        """set last coord var"""
        # ----
        self.last_qx: float = coord[0]
        self.last_qy: float = coord[1]
        self.last_qz: float = coord[2]

    # =====================================
    def clear(self) -> None:
        """clear queue stack"""
        # ----

        self.sort()
        self.is_first_sort = False

        # ----

        while len(self.sub_stack) > 0:
            self.stack: list = []
            self.stack.extend(self.sub_stack)
            self.sub_stack = []
            # print(len(self.stack))
            self.sort()
        # -------------

    # =====================================
    def sort(self) -> None:
        """sort queue stack"""
        # ----
        x_width = self.x_width
        # ----
        for line in self.stack:
            new = False
            # -----------------
            try:
                re_que = False
                id = np.round(float(line[0][1]) * 1.5, 3)  # 1.5 to prevent merge
                m_line = Mesh_Line(id=id)
                self.last_qx = line[0][0]
                check_y = np.diff((line[0][1], self.last_qy))

                # ----

                if check_y > self.y_width:
                    new = True

                # ----

                # -----------------
                for coord in line:
                    # ----

                    if re_que is True:
                        self.q_line.append(coord)
                        continue

                    # ----
                    if self.last_qx == coord[0] and self.last_qy == coord[1]:
                        # dont add duplicates
                        continue

                    # ----

                    check_qx = np.diff((self.last_qx, coord[0]))
                    if check_qx > x_width:
                        self.q_line.append(coord)
                        new = True
                        re_que = True

                    # ----
                    else:
                        m_line.append(coord)
                        self.set_last_coord(coord)

                    # ----
                # ---------
                m_line.append([self.last_qx, self.last_qy, self.height_max])
                m_line.close(new)
                # ---------

            # -------------
            except IndexError as e:
                print(e)
                continue
            finally:
                if len(self.q_line) > 0:
                    self.sub_stack.append(self.q_line)
                    self.q_line = []
            # -----------
        # =======================================
