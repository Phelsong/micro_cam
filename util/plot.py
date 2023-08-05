import matplotlib.pyplot as plt
import numpy as np


def generate_raw_visual(in_mesh, raw_mesh):
    # Create a new plot
    plt.style.use("_mpl-gallery")
    fig, axes = plt.subplots(subplot_kw={"projection": "3d"})
    # Load a processed mesh and plot it
    axes.plot_wireframe(in_mesh[:, 0], in_mesh[:, 1], np.array([in_mesh[:, 2]]))  # type: ignore
    # Auto scale to the mesh size
    scale = [[100, 100]]
    axes.auto_scale_xyz(scale, scale, scale)  # type: ignore
    # axes.set(xticklabels=[], yticklabels=[], zticklabels=[])
    # Show the plot to the screen
    plt.show()


# ---------------------------------------------------------------------
def gen_visual(in_file):
    # parse GCODE
    # TODO

    # Create a new plot
    plt.style.use("_mpl-gallery")  # type: ignore
    fig, axes = plt.subplots(subplot_kw={"projection": "3d"})  # type: ignore
    # Load the STL files and add the vectors to the plot
    axes.plot_wireframe(in_file.x, in_file.y, in_file.z)  # type: ignore
    # Auto scale to the mesh size
    scale = in_file.points.flatten()  # type: ignore
    axes.auto_scale_xyz(scale, scale, scale)  # type: ignore
    # axes.set(xticklabels=[], yticklabels=[], zticklabels=[])
    # Show the plot to the screen
    plt.show()
