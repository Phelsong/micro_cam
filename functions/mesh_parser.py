"""m_parser"""
# libs
import numpy as np
from numpy import ndarray, dtype
from typing import Any


# imports
from .mesh_queue import Mesh_Queue
from .mesh_config import Mesh_Config
from .mesh_line import Mesh_Line
from .mesh_stack import Mesh_Stack

# ===========================
# TODO
# test moving the safety to writer
# update que to match parser logic


class Mesh_Parser(object):
    def __init__(self, mesh_map: dict, config: Mesh_Config):
        self.config: Mesh_Config = config
        self.mesh: dict = mesh_map
        self.que: Mesh_Queue = Mesh_Queue(config)
        self.dump: Mesh_Stack = Mesh_Stack(config)
        self.new_obj: bool = False

    def parse_mesh(self):
        """Parses the mesh block by `x` line, breaking elements across the queue"""

        x_width: float = self.config.x_width
        fl: np.ndarray = next(iter(self.mesh.values()))
        last_id: float | None = None
        last_x = fl[0][0]
        last_y = fl[0][1]

        # ------------------------
        for id, line in self.mesh.items():
            # --------------------------
            m_line: Mesh_Line = Mesh_Line(id)
            q_line: list = []
            to_que: bool = False
            new_obj: bool = False

            try:
                # sort line by x: right to left
                sorted_line: np.ndarray = line[line[:, 0].argsort(axis=0)]  # [::-1]

                # checks
                check_line: np.ndarray = np.diff((last_x, sorted_line[0][0]))
                check_y: np.ndarray | float = (
                    np.diff((last_id, id)) if last_id is not None else 0
                )
                last_x: float = sorted_line[0][0]

                # -------------
                if check_y > self.config.y_width:
                    new_obj = True

                # -------------------------------
                for coord in sorted_line:
                    # ---
                    x_point = coord[0]
                    y_point = coord[1]
                    z_point = coord[2]
                    check_x: ndarray[Any, dtype[Any]] = np.diff(
                        (last_x, x_point)
                    )  # check bounds
                    # ---

                    # ----------------------------------
                    # Pre-emptive filtering
                    # ----------------------------------

                    if (
                        abs(x_point) > self.config.x_bound
                        and abs(y_point) > self.config.y_bound
                    ):
                        # any coord outside of the padded area are seperated - pad specfic method
                        self.dump.append_coord(coord)
                        continue
                    # -----

                    if to_que is True:
                        q_line.append([x_point, y_point, z_point])
                        last_x = x_point
                        last_y = y_point
                        continue

                    # -----------------------------------
                    # Cases for sorting lines into chunks
                    # -----------------------------------

                    if check_line > x_width:
                        new_obj = True

                    # -----

                    elif check_x > x_width or x_point > self.config.x_median:
                        q_line.append(coord)
                        new_obj = True
                        to_que = True
                        continue

                    # -------

                    elif x_point == last_x and y_point == last_y:
                        continue

                    # -------

                    else:
                        # Case: good point, just add to the stack
                        m_line.append([x_point, y_point, z_point])
                        last_x = x_point
                        last_y = y_point

                    # -------

            except IndexError:
                print(f"IndexError: {line}")
                pass

            finally:
                # end of line ops
                last_id = id
                m_line.close(new_obj)
                if len(q_line) > 0:
                    self.que.append(q_line)

            # -------
        # ---------------------------------------
        self.last_point_safety()
        self.que.clear()

    # ==================================================

    def last_point_safety(self):
        """sets a final safety point to the last point in the first parser pass"""
        from .mesh_object import MESH_OBJECTS

        # ------

        last_key = next(reversed(MESH_OBJECTS.keys()))
        last_line = next(reversed(MESH_OBJECTS[last_key].lines.keys()))
        last_coord = MESH_OBJECTS[last_key].lines[last_line][-1]

        # ---

        safety_coord = [last_coord[0], last_coord[1], self.config.height_max]
        # reset_coord = [0, 0, self.config.height_max]

        # ------
        MESH_OBJECTS[last_key].lines[last_line] = np.vstack(
            (MESH_OBJECTS[last_key].lines[last_line], safety_coord)
        )
        # M_OBJECTS[last_key].lines[last_line] = np.vstack(
        #     (M_OBJECTS[last_key].lines[last_line], reset_coord)
        # )


# ==============================================================================
