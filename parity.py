from bitarray import bitarray

from util import bits_from_bytes


# 0 - is even, 1 - odd
def calculate_parity_bit(data: bitarray) -> int:
    parity: int = 0

    for bit in data:
        parity ^= bit

    return parity


def encode_parity_bit(data: bytes|bytearray) -> bytes:
    bits = bits_from_bytes(data)
    parityBit = calculate_parity_bit(bits)

    bits.append(parityBit)

    return bits.tobytes()


def validate_parity_encoded_data(data: bytes|bytearray) -> bool:

    bits = bits_from_bytes(data)

    shouldBe: int = calculate_parity_bit(bits[:len(bits) - 1])
    whatIs: int = bits[len(bits) - 1]

    return shouldBe == whatIs


def decode_parity_bit(data: bytes|bytearray) -> bytes:

    bits = bits_from_bytes(data)

    bits.pop()

    return bits.tobytes()
