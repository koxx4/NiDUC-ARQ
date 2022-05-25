import colorama
from bitarray import bitarray
from bitarray.util import zeros
from bitarray.util import ba2int
from bitarray.util import int2ba
from colorama import Fore

from util import bits_from_bytes


def crc_interactive(data: bitarray, polynomial: bitarray) -> int:

    if len(data) == 0 or len(polynomial) <= 1:
        return 0

     # this is made on purpose -> we get copy
    polynomial = bitarray(polynomial)

    remainderWidth = len(polynomial) - 1

    dataWidthWithoutRemainder = len(data)

    dataCopy: bitarray = bitarray(data)
    dataCopy.extend(zeros(remainderWidth))

    polynomial.extend(zeros(len(dataCopy) - len(polynomial)))

    print('Pre start')
    print("{}|{}".format(dataCopy[:dataWidthWithoutRemainder].to01(
    ), dataCopy[dataWidthWithoutRemainder:].to01()))
    print('Polynomial is {}'.format(polynomial.to01()))

    currentDataBitIndex = 0
    while(dataCopy[:dataWidthWithoutRemainder].any()):

        while dataCopy[currentDataBitIndex] == 0:
            polynomial >>= 1
            currentDataBitIndex += 1

        print('Cycle:')
        print("DATA: {}|{}".format(dataCopy[:dataWidthWithoutRemainder].to01(
        ), Fore.GREEN + dataCopy[dataWidthWithoutRemainder:].to01() + Fore.RESET))
        print("POLY: {}|{}".format(polynomial[:dataWidthWithoutRemainder].to01(
        ), polynomial[dataWidthWithoutRemainder:].to01()))

        dataCopy ^= polynomial
        polynomial >>= 1
        currentDataBitIndex += 1

        input()

    crc = ba2int(dataCopy[dataWidthWithoutRemainder:])

    print(
        "CRC: {} -> {}".format(dataCopy[dataWidthWithoutRemainder:].to01(), crc))

    return crc


def validate_crc_interactive(data: bitarray, polynomial: bitarray, crc: bitarray) -> bool:

    if len(data) == 0 or len(polynomial) <= 1:
        return 0

    # this is made on purpose -> we get copy
    polynomial = bitarray(polynomial)
    crc = int2ba(crc, len(polynomial) - 1)

    dataWidthWithoutRemainder = len(data)

    dataCopy: bitarray = bitarray(data)
    dataCopy.extend(crc)

    polynomial.extend(zeros(len(dataCopy) - len(polynomial)))

    print('Pre start')
    print("{}|{}".format(dataCopy[:dataWidthWithoutRemainder].to01(
    ), dataCopy[dataWidthWithoutRemainder:].to01()))
    print('Polynomial is {}'.format(polynomial.to01()))

    currentDataBitIndex = 0
    while(dataCopy[:dataWidthWithoutRemainder].any()):

        while dataCopy[currentDataBitIndex] is 0:
            polynomial >>= 1
            currentDataBitIndex += 1

        print('Cycle:')
        print("DATA: {}|{}".format(dataCopy[:dataWidthWithoutRemainder].to01(
        ), Fore.GREEN + dataCopy[dataWidthWithoutRemainder:].to01() + Fore.RESET))
        print("POLY: {}|{}".format(polynomial[:dataWidthWithoutRemainder].to01(
        ), polynomial[dataWidthWithoutRemainder:].to01()))

        dataCopy ^= polynomial
        polynomial >>= 1
        currentDataBitIndex += 1

        input()

    remainder = ba2int(dataCopy[dataWidthWithoutRemainder:])

    print("Remainder: {}".format(dataCopy[dataWidthWithoutRemainder:].to01()))

    return remainder == 0


def crc(data: bitarray, polynomial: bitarray) -> int:

    if len(data) == 0 or len(polynomial) <= 1:
        return 0

    # this is made on purpose -> we get copy
    polynomial = bitarray(polynomial)

    remainderWidth = len(polynomial) - 1

    dataWidthWithoutRemainder = len(data)

    dataCopy: bitarray = bitarray(data)
    dataCopy.extend(zeros(remainderWidth))

    polynomial.extend(zeros(len(dataCopy) - len(polynomial)))

    currentDataBitIndex = 0
    while(dataCopy[:dataWidthWithoutRemainder].any()):

        while dataCopy[currentDataBitIndex] == 0:
            polynomial >>= 1
            currentDataBitIndex += 1

        dataCopy ^= polynomial
        polynomial >>= 1
        currentDataBitIndex += 1

    return ba2int(dataCopy[dataWidthWithoutRemainder:])


def validate_crc(data: bitarray, polynomial: bitarray, crc: int) -> bool:

    if len(data) == 0 or len(polynomial) <= 1:
        return 0

    # this is made on purpose -> we get copy
    polynomial = bitarray(polynomial)
    crc = int2ba(crc, len(polynomial) - 1)

    dataWidthWithoutRemainder = len(data)

    dataCopy: bitarray = bitarray(data)
    dataCopy.extend(crc)

    polynomial.extend(zeros(len(dataCopy) - len(polynomial)))

    currentDataBitIndex = 0
    while(dataCopy[:dataWidthWithoutRemainder].any()):

        while dataCopy[currentDataBitIndex] is 0:
            polynomial >>= 1
            currentDataBitIndex += 1

        dataCopy ^= polynomial
        polynomial >>= 1
        currentDataBitIndex += 1

    remainder = ba2int(dataCopy[dataWidthWithoutRemainder:])
    return remainder == 0


def encode_crc(data: bytes | bytearray, polynomial: str) -> bytes:
    bits = bits_from_bytes(data)
    polyBits = bitarray(polynomial)

    crcBytes = int2ba(crc(bits, polynomial), len(polynomial) - 1).tobytes()

    encoded = bytearray(bits.tobytes())
    encoded.extend(crcBytes)

    return encoded


def decode_crc(data: bytes | bytearray, polynomial: str) -> bytes:
    bits = bits_from_bytes(data)
    polyBits = bitarray(polynomial)

    for i in range(0, len(polyBits)):
        bits.pop()

    return bits.tobytes()


def has_valid_crc(data: bytes | bytearray, polynomial: str) -> bool:
    dataBits = bits_from_bytes(data)
    polyBits = bitarray(polynomial)

    crcBits = bits_from_bytes(data[len(data) - (int)(len(polynomial) / 8) - 1:])
    
    dataBits = dataBits[:len(dataBits) - len(crcBits)]

    crcBits = crcBits[:len(polynomial) - 1]


    return validate_crc(dataBits, polyBits, ba2int(crcBits))
