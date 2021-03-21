import logging


logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

# Create empty bytes
empty_bytes = bytes(4)
logging.debug(type(empty_bytes))
logging.debug(empty_bytes)

# Cast bytes to bytearray
mutable_bytes = bytearray(empty_bytes)

# Bytearray allows modification
mutable_bytes[0] = 255
mutable_bytes.append(255)
logging.debug(mutable_bytes)
output_string = ":{}:"*len(mutable_bytes)
logging.debug(output_string.format(*mutable_bytes))

# Cast bytearray back to byte
immutable_bytes = bytes(mutable_bytes)
logging.debug(type(immutable_bytes))