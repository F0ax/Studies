import logging
import pathlib
from pathlib import Path


logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

# Defineing important paths
script_path_abs = Path(__file__).absolute().parent
data_path_abs = Path(script_path_abs).joinpath('Data')
test_file_path = Path(data_path_abs).joinpath('test_file.dat')

with open(test_file_path, "rb") as binary_file:
    logging.debug(binary_file)
    # Read the whole file at once
    data = binary_file.read()
    logging.debug(data)

with open(test_file_path, "rb") as text_file:
    # One option is to call readline() explicitly
    # single_line = text_file.readline()

    # It is easier to use a for loop to iterate each line
    for line in text_file:
        logging.debug(line)
