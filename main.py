from bitarray import bitarray
from bitarray.util import int2ba
from numpy import ndarray
from crc import crc
from crc import crc_interactive
from crc import is_valid_crc
from crc import is_valid_crc_interactive
from channels import binary_symmetric
from channels import gilbert_elliot


data = bitarray()
data.frombytes(b'Hello')
polynomial = bitarray('1011')

bsChannel = binary_symmetric(0.1)
geChannel = gilbert_elliot(0.75, 0.2, 0.15)
dataAfterSendBS: ndarray = bsChannel(data.tolist())
dataAfterSendGE = geChannel(data.tolist())

print('Before:')
print(data.tolist())

print('After (BS):')
print(dataAfterSendBS.tolist())

print('After (GE):')
print(dataAfterSendGE)
