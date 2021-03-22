import os
import logging
import pathlib
from pathlib import Path

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

# Defineing important paths
script_path_abs = Path(__file__).absolute().parent
data_path_abs = Path(script_path_abs).joinpath('Data')
test_file_path = Path(data_path_abs).joinpath('test_file.dat')


file_length_in_bytes = os.path.getsize(test_file_path)
logging.info(file_length_in_bytes)