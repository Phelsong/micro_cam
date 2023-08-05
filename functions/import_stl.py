"""STL import stuff"""
# libs
import numpy as np
from stl import Mesh

# imports
from functions.line_generator import generate_lines

# ====================================
# TODO: UPDATE TO MATCH


def new_mesh(file_path: str, scale):  # -> tuple[np.ndarray, dict]
    """Generates new Mesh object"""
    sm = Mesh.from_file(file_path)
    # reshape from 3,3 to 1,3
    re_points = np.reshape(sm.points, (-1, 3))
    # rotate mesh
    re_points[:, [1, 2]] = re_points[:, [2, 1]]
    # scale
    re_points = np.divide(re_points, scale)
    # sort by input Y
    raw_points = re_points[re_points[:, 1].argsort()]  # [::-1]
    # break mesh into Y lines
    mesh_map = generate_lines(re_points)

    return raw_points, mesh_map


# ===============================================================
