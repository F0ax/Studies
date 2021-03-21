# Pass "wb" to write a new file, or "ab" to append
import logging


logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)

with open("bytes.txt", "wb") as binary_file:
    # Write text or bytes to the file
    binary_file.write("Write text by encoding\n".encode('utf8'))
    binary_file.write("Don't forget to use special symbols like äöüß\n".encode('utf8'))
    num_bytes_written = binary_file.write(b'\xDE\xAD\xBE\xEF\x00\x01\x02\x03')
    logging.debug("Wrote %d bytes." % num_bytes_written)