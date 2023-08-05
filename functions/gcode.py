""" functions for G-Code generation"""
# libs


class Gcode(object):
    def __init__(self, start_point=None, end_point=None):
        self.header: list = []
        self.start_point = start_point
        self.end_point = end_point
        # self.feed_rate = None
        self.list: list = []
        #  -------------------
        # action list
        self.rapid = "G00"
        self.linear_move = "G01"
        self.dwell = "G04"
        self.stop = "M01"
        self.end = "M02"
        self.on_cw = "M03"
        self.on_ccw = "M04"
        self.spindle_off = "M05"
        self.end_program = "M30"
        self.home = "G28"
        self.move_to_start = "G53"
        self.abs_pos = "G90"
        self.incremental_pos = "G91"
        self.set_position = "G92"
        self.units_per_min = "G94"
        # --------------
        # macro list
        # self.corner_loop = "f150, G01 X Y Z"
        # self.new_block = ""
        # self.end_block = ""
        # self.end_macro = ""
        # self.start_macro = ""
        # self.end_loop = ""
        # self.start_loop = ""
        self.reset_point = "G1 X0.0000 Y0.0000 Z2\n"
        self.change_line_speed = "F70\n"
        self.line_speed = "F200\n"


# For point in Model, G01 X() y() Z()
# x>Y
# At end of each pass, reduce speed and continue
# return across next "line", G01 X() y() Z()
# ===
# after full pass run cross cut over the Model
# Y>X

# Compile the G-Code

# Convert STL data to GCODE
# gcode = stl_to_gcode(stl_data, ctx, queue)

# Create the G-Code
# print("Creating G-Code...")
# gcode = stl_to_gcode(stl_data, ctx, queue)

# example
# M3 Start Spindle
# G01 X? Y? Z?
# ...
# M5 Stop Spindle

# G20 (Units are Inches)
# G90 (Abs pos)
# G94 (units per min rate)


# G-code map over the negative
# if 0 cut
# M start
# G01 X() Y()
# else pass
# M stop
# G00

# Finally
# M2 End Program
