import logging

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

# Binary to Text
binary_data = b'I am text.'
text = binary_data.decode('utf-8')
logging.info(text)

binary_data = bytes([65, 66, 67])  # ASCII values for A, B, C
text = binary_data.decode('utf-8')
logging.info(text)