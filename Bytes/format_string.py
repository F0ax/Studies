import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

a_byte = b'\xFF'  # 255
i = ord(a_byte)   # Get the integer value of the byte

bin = "{0:b}".format(i) # binary: 11111111
hex = "{0:x}".format(i) # hexadecimal: ff
oct = "{0:o}".format(i) # octal: 377

logging.info(bin)
logging.info(hex)
logging.info(oct)