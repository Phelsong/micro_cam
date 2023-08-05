import csv
import pandas as pd

with open(
    "O:\\0.code\\precisionfit\\data\\G-Code.csv",
    "rt",
) as csvfile:
    gcode_list = csv.reader(csvfile, delimiter='"', quoting=csv.QUOTE_ALL)
    new_list = []
    with open("O:\\0.code\\precisionfit\\data\\parsed.csv", "a") as file:
        for row in gcode_list:
            file.write(str(row[0] + "\n"))
