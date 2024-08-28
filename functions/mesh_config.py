""" Functions for mapping G-Code .np/ files"""

# libs
import numpy as np


# TODO Set up caching for config files
#  =======
class Mesh_Config(object):
    def __init__(self, filename: str, *, config_data: dict, mesh: np.ndarray):
        self.filename: str = filename  # file_name
        self.mesh: np.ndarray = mesh
        self.scale: float = config_data["scale"]
        # --------------------
        # padding
        self.padding_x: float = config_data["padding"]["x"]
        self.padding_y: float = config_data["padding"]["y"]
        # ----------------------
        # offsets
        self.median_offset: float = config_data["median_offset"]
        self.x_offset: float = config_data["x_offset"]
        self.y_offset: float = config_data["y_offset"]
        self.z_offset: float = config_data["z_offset"]

        # ----------------------
        # min/max
        self.min_x: float = np.min(self.mesh[:, 0])
        self.max_x: float = np.max(self.mesh[:, 0])
        # --
        self.min_y: float = np.min(self.mesh[:, 1])
        self.max_y: float = np.max(self.mesh[:, 1])
        # --
        self.min_z: float = np.min(self.mesh[:, 2])
        self.max_z: float = np.max(self.mesh[:, 2])

        # --
        # ----------------------
        # point-to-point widths
        # arbitrary values that works for pads
        self.x_width: float = np.multiply(self.scale, 0.01)  # 0.25
        self.y_width: float = np.multiply(self.scale, 0.01)  # 0.25
        print(self.x_width, self.y_width)
        # ----------------------
        # bounds for cutting
        self.x_bound: float = np.multiply(self.max_x, self.padding_x).round(2)
        self.y_bound: float = np.multiply(self.max_y, self.padding_y).round(2)
        self.z_bound: float = np.multiply(self.max_z, self.z_offset)
        self.x_median: float = (
            np.median(self.mesh[:, 0]) + self.median_offset
        )  # type:ignore
        # ----------------------
        # height max for the machine, used for adding safety margins
        # TODO, retrace where this is referenced to fix the redundancy
        self.height_max: float = np.round(self.z_bound, 0)
        # -----------------------
        # dimensions in units | unused
        # self.dimension_x = 100
        # self.dimension_y = 100

        self.calc_sub_id = lambda p: np.round(float(p) * 1.5, 2)

    def get_checkpoints(self):
        point = self.max_y + 0.5
        points = []
        point -= self.max_y / 4
        while point > self.min_y:
            points.append(np.around(point, decimals=1))
            point -= self.max_y / 4
        points.append(np.around(self.min_y, decimals=1))
        return points
