from channels import send_through_channel
from crc import encode_crc, has_valid_crc
from parity import encode_parity_bit, validate_parity_encoded_data
from repetition import encode_repetition, validate_encoded_repetition


def crcErrorDetectionAccuracy(channel, data: bytes, polynomial: str, retries: int) -> float:
    validMeasures = 0
    encodedData = encode_crc(data, polynomial)

    for i in range(0, retries):
        sentData = send_through_channel(encodedData, channel)
        validationResult = has_valid_crc(sentData, polynomial)

        if (encodedData != sentData and validationResult == False) or (encodedData == sentData and validationResult == True):
            validMeasures += 1

    return validMeasures / retries


def parityErrorDetectionAccuracy(channel, data: bytes, retries: int) -> float:
    validMeasures = 0
    encodedData = encode_parity_bit(data)

    for i in range(0, retries):
        sentData = send_through_channel(encodedData, channel)
        validationResult = validate_parity_encoded_data(sentData)

        if (encodedData != sentData and validationResult == False) or (encodedData == sentData and validationResult == True):
            validMeasures += 1

    return validMeasures / retries

def repetitionErrorDetectionAccuracy(channel, data: bytes, repCount: int, retries: int) -> float:
    validMeasures = 0
    encodedData = encode_repetition(data, repCount)

    for i in range(0, retries):
        sentData = send_through_channel(encodedData, channel)
        validationResult = validate_encoded_repetition(sentData, repCount)

        if (encodedData != sentData and validationResult == False) or (encodedData == sentData and validationResult == True):
            validMeasures += 1

    return validMeasures / retries


def testsCRC(channel, data, polynomials, retries: int, channelDescription: str):

    for polynomial in polynomials:

        result = crcErrorDetectionAccuracy(
            channel, data, polynomial, retries)

        print('CRC - error detection, channel: {}\nPolynomial: {}, Retries: {}\nRate: {:.3%}'.format(
            channelDescription, polynomial, retries, result
        ))


def testsParityBit(channel, data, retries: int, channelDescription: str):

    result = parityErrorDetectionAccuracy(channel, data, retries)

    print('Parity bit - error detection, channel: {}\nRetries: {}\nRate: {:.3%}'.format(
        channelDescription, retries, result
    ))

def testsRepetition(channel, data, repCount: int, retries: int, channelDescription: str):

    result = repetitionErrorDetectionAccuracy(channel, data, repCount, retries)

    print('Repetition code - error detection, repCount: {}, channel: {}\nRetries: {}\nRate: {:.3%}'.format(
        repCount, channelDescription, retries, result
    ))
