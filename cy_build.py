from distutils.command.build_ext import build_ext
from Cython.Build import cythonize
from setuptools import setup

# TODO: loop and add each file in .functions


def run_setup() -> None:
    setup(
        ext_modules=cythonize(
            [
                ".\\functions\\import_grid.py",
                ".\\functions\\import_stl.py",
                ".\\functions\\line_generator.py",
                ".\\functions\\m_config.py",
                ".\\functions\\m_parser.py",
                ".\\functions\\m_queue.py",
                ".\\functions\\m_object.py",
                ".\\functions\\m_line.py",
                ".\\functions\\m_stack.py",
                ".\\functions\\obj_merger.py",
                ".\\functions\\writer.py",
            ],
            compiler_directives={"language_level": "3"},  # must be 3,
        )
    )


if __name__ == "__main__":
    run_setup()
