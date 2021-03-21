import logging
import os


logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

with open("test_file.dat", "rb") as binary_file:
    logging.debug(binary_file)
    # Read the whole file at once
    data = binary_file.read()
    logging.debug(data)

with open("test_file.dat", "rb") as text_file:
    # One option is to call readline() explicitly
    # single_line = text_file.readline()

    # It is easier to use a for loop to iterate each line
    for line in text_file:
        logging.debug(line)
