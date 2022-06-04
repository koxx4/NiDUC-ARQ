from bitarray import bitarray
from util import bits_from_bytes


def encode_repetition(data: bytes, repCount: int = 2) -> bytes:
    bits = bits_from_bytes(data)
    encodedSize = len(bits) * repCount

    bitsEncoded = bitarray()

    for bit in bits:
        for j in range(0, repCount):
            bitsEncoded.append(bit)
    
    return bitsEncoded.tobytes()
    

def validate_encoded_repetition(encodedData: bytes, repCount: int = 2) -> bool:
    bits = bits_from_bytes(encodedData)

    for i in range(0, len(bits), repCount):
        for j in range(i, i + repCount):
            if(bits[i] != bits[j]):
                return False
    
    return True