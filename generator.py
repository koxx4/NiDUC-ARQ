import random
from bitarray import bitarray
from lorem_text import lorem


def randomAsciiWords(count: int) -> bytes:
    return bytes(lorem.words(count))


def randomAsciiSentences(count: int) -> bytes:
    return bytes(lorem.sentence(count))


# Paragraph consist of 2 to 4 sentences
def randomAsciiParagraph(count: int) -> bytes:
    return bytes(lorem.paragraph(count))


def randomBytes(count: int) -> bytes:
    return random.randbytes()


def randomBits(count: int) -> bitarray:
    bits: bitarray = bitarray()

    for i in range(0, count):
        bits.append(random.randint(0, 1))

    return bits
