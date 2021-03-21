import io
import logging


logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

binary_stream = io.BytesIO()
# Binary data and strings are different types, so a str
# must be encoded to binary using ascii, utf-8, or other.
text = "Hello, world!::"
binary_stream.write(text.encode('ascii'))
binary_stream.write(text.encode('utf-8'))

# Move cursor back to the beginning of the buffer
binary_stream.seek(0)

# Read all data from the buffer
stream_data = binary_stream.read()

# The stream_data is type 'bytes', immutable
logging.debug(type(stream_data))
logging.debug(stream_data)

# To modify the actual contents of the existing buffer
# use getbuffer() to get an object you can modify.
# Modifying this object updates the underlying BytesIO buffer
mutable_buffer = binary_stream.getbuffer()
logging.debug(type(mutable_buffer))  # class 'memoryview'
mutable_buffer[0] = 0xFF

# Re-read the original stream. Contents will be modified
# because we modified the mutable buffer
binary_stream.seek(0)
logging.debug(binary_stream.read())