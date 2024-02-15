#
# Select a file using a kind of regular expression and print it on the console.
# Written by Matias Bendel.
#

import glob
import re
import os

for file in os.listdir('C:\\temp\\postgresql'):
    # python_output-2023-07-12.21.14.39.897
    if re.match("python_output-\d+\-\d+\-\d+\.\d+\.\d+\.\d+\.\d+\.csv", file):
        print("Enviando datos del archivo: ", file)
        path = 'C:\\temp\\postgresql\\'+file

print(path)       

with open(path, 'r') as f:
    for row in f:
        for j in row:
            print(j, end=" ")
        print("")
