from bitarray import bitarray


def bits_from_bytes(data: bytes | bytearray) -> bitarray:
    x = bitarray()
    x.frombytes(data)

    return x
