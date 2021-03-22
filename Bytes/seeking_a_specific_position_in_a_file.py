import os
import pathlib
from pathlib import Path
import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

# Defineing important paths
script_path_abs = Path(__file__).absolute().parent
data_path_abs = Path(script_path_abs).joinpath('Data')
test_file_path = Path(data_path_abs).joinpath('test_file.dat')

# Seek can be called one of two ways:
#   x.seek(offset)
#   x.seek(offset, starting_point)

# starting_point can be 0, 1, or 2
# 0 - Default. Offset relative to beginning of file
# 1 - Start from the current position in the file
# 2 - Start from the end of a file (will require a negative offset)

with open(test_file_path, "rb") as binary_file:
    # Seek a specific position in the file and read N bytes
    binary_file.seek(0, 0)  # Go to beginning of the file
    couple_bytes = binary_file.read(15)
    logging.info("Output: %s" % couple_bytes)