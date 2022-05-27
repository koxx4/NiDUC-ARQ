from channels import send_through_channel
from crc import encode_crc, has_valid_crc
from parity import encode_parity_bit, validate_parity_encoded_data


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


def testsCRC(channel, data, polynomials, retries, channelDescription):

    for polynomial in polynomials:

        result = crcErrorDetectionAccuracy(
            channel, data, polynomial, retries) * 100

        print('CRC - error detection, channel: {}\nPolynomial: {}, Retries: {}\nRate: {}%'.format(
            channelDescription, polynomial, retries, result
        ))


def testsParityBit(channel, data, retries, channelDescription):

    result = parityErrorDetectionAccuracy(channel, data, retries) * 100

    print('Parity bit - error detection, channel: {}\nRetries: {}\nRate: {}%'.format(
        channelDescription, retries, result
    ))
