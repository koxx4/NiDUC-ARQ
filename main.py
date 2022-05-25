from bitarray import bitarray
from crc import encode_crc, has_valid_crc
from channels import binary_symmetric, send_through_channel
from channels import gilbert_elliot
from generator import random_ascii_words
from parity import encode_parity_bit, validate_parity_encoded_data


data = random_ascii_words(10)

polynomial = '1011'

parityEncodedData = encode_parity_bit(data)
crcEncodedData = encode_crc(data, polynomial)

bsChannel = binary_symmetric(0.1)
geChannel = gilbert_elliot(0.75, 0.2, 0.15)

dataAfterSendBSCrc = send_through_channel(crcEncodedData, bsChannel)
dataAfterSendGECrc = send_through_channel(crcEncodedData, geChannel)
dataAfterSendBSParity = send_through_channel(parityEncodedData, bsChannel)
dataAfterSendGEParity = send_through_channel(parityEncodedData, geChannel)

print('Data before send: {}'.format(data))

print('CRC encoded data before send: {}'.format(crcEncodedData))

print('Parity encoded data before send: {}'.format(parityEncodedData))

print('CRC encoded data after BS: {}'.format(dataAfterSendBSCrc))

print('CRC encoded data after GE: {}'.format(dataAfterSendGECrc))

print('Parity encoded data after BS: {}'.format(dataAfterSendBSParity))

print('Parity encoded data after GE: {}'.format(dataAfterSendGEParity))

print('Sanity check - data before crc check: {}'.format(
    has_valid_crc(crcEncodedData, polynomial)))

print('CRC data check after BS: {}'.format(
    has_valid_crc(dataAfterSendBSCrc, polynomial)))

print('CRC data check after GE: {}'.format(
    has_valid_crc(dataAfterSendGECrc, polynomial)))

print('Parity data check after BS: {}'.format(
    validate_parity_encoded_data(dataAfterSendBSParity)))

print('Parity data check after GE: {}'.format(
    validate_parity_encoded_data(dataAfterSendGEParity)))
