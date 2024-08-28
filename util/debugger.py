""" debugging tools """

# lib
import pandas as pd
import numpy as np
import tomllib

# import
from functions.gcode import Gcode
from functions.mesh_config import Mesh_Config
from functions.file_writer import Writer
from services.compute_service import map_to_gcode

# -------------------------------------------------------------


def dump_to_file(in_path):
    """source txt/csv file to.tap file with no processing"""
    df = pd.read_csv(in_path)
    with open(".\\temp\\text.tap", "a") as f:
        for coord in df.values:
            x = coord[0] / 25
            y = coord[1] / 25 * -1  # invert for reasons
            z = coord[2] / 25 if coord[2] > 0.02 else 0.02
            f.write(f"G1 X{x} Y{y} Z{z}\n")


def run_compute_test(test_file: str = "data/Stl_testfiles/140_-_120_mm.STL"):
    map_to_gcode(test_file)


if __name__ == "__main__":
    # test_file = ".\\140_-_120_mm.STL"
    run_compute_test(test_file="data/Stl_testfiles/140_-_120_mm.STL")
    # dump_to_file("data/test.txt")
