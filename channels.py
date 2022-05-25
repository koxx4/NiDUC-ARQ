from bitarray import bitarray
import komm
import random

from util import bits_from_bytes


def binary_symmetric(probability: int):
    return komm.BinarySymmetricChannel(probability)


def gilbert_elliot(reverseGood: float, reverseBad: float, errorChance: float):
    def channel(input) -> list:
        output = []
        isBad = False

        for i in input:
            if isBad:
                if random.random() < errorChance:
                    output.append((i + 1) % 2)
                else:
                    output.append(i)
                isBad = random.random() < reverseGood
                continue

            output.append(i)
            isBad = random.random() < reverseBad

        return output

    return channel

def send_through_channel(data: bytes | bytearray, channel) -> bytes:

    sent = channel(bits_from_bytes(data))

    if not isinstance(sent, list):
        sent = sent.tolist()

    return bitarray(sent).tobytes()
