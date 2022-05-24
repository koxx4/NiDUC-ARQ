from bitarray import bitarray
from bitarray.util import int2ba
from crc import crc
from crc import crc_interactive
from crc import is_valid_crc
from crc import is_valid_crc_interactive


data = bitarray()
data.frombytes(b'Hello')

polynomial = bitarray('1011')

crc_value: int = crc_interactive(data, polynomial)

info = "Value of crc is: {}, in bits: {}, original data {}".format(
    crc_value, int2ba(crc_value, len(polynomial) - 1).to01(), data.to01())
print(info)
print("Is {} valid crc for {} ? {}"
      .format(int2ba(crc_value, len(polynomial) - 1).to01(), data.to01(), is_valid_crc_interactive(data, polynomial, crc_value)))
