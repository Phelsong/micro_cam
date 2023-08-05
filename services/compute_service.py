""" ~exe function chain """
# lib
import tomllib
from typing import Any

# import
from functions.import_stl import new_mesh
from functions.import_grid import new_grid
from functions.gcode import Gcode
from functions.mesh_config import Mesh_Config
from functions.mesh_parser import Mesh_Parser
from functions.file_writer import Writer
from functions.object_merger import Object_Merger
from .app_logger import _Logger


# -------------------


def map_to_gcode(filepath: str) -> None:
    """main app function"""
    # ----

    config_path = "profiles\\example.toml"
    f_name = "test.tap"
    logger = _Logger()
    logger.info(f"Compiling G-Code for {f_name}...")

    # ----

    print("building config")
    with open(config_path, "rb") as f:
        config_data: dict[str, Any] = tomllib.load(f)
    gcode: object = Gcode()

    # raw_mesh, mesh_map = new_mesh(file_path, config)
    raw_mesh, mesh_map = new_grid(filepath, config_data["scale"])

    config: Mesh_Config = Mesh_Config(f_name, config_data=config_data, mesh=raw_mesh)

    # ----------------

    print("parsing mesh")
    parser: Mesh_Parser = Mesh_Parser(mesh_map, config)
    parser.parse_mesh()

    # ----------------

    print("attempting object merge")
    merger = Object_Merger(config)
    merger.merge_objects()

    # ----------------
    print("writing gcode to file")
    writer = Writer(config.filename, gcode)
    writer.write_lines()
    # writer.write_each()
    # ----------------


# ========================================================
