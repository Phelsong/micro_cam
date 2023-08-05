""" import .txt vertex grid files"""
# libs
import pandas as pd
from pandas import DataFrame
import numpy as np
from numpy import ndarray, dtype, generic
from typing import Any

# imports
from functions.line_generator import generate_lines


def new_grid(filepath, scale) -> tuple[ndarray, dict[float, ndarray]]:
    """Read a vertex grid file"""
    df: DataFrame = pd.read_csv(filepath, header=None)
    raw_points: ndarray = df.values
    print("grid coordinates :", np.shape(raw_points))
    # reshape
    re_points: ndarray = np.reshape(raw_points, (-1, 3))
    # rotate mesh
    re_points[:, [1, 2]] = raw_points[:, [2, 1]]
    # scale
    re_points: ndarray = np.divide(re_points, scale)
    # sort by input Y
    raw_points: ndarray = re_points[re_points[:, 1].argsort()]  # [::-1]

    mesh_map: dict = generate_lines(raw_points)

    return raw_points, mesh_map
