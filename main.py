from channels import binary_symmetric, send_through_channel
from channels import gilbert_elliot
from generator import random_ascii_words, random_polynomials
from tests import *


data = random_ascii_words(100)
crcPolynomials = random_polynomials(
    totalAmount=10 * 3, stepLen=3, startingLen=3)

bsChannel = binary_symmetric(0.1)
geChannel = gilbert_elliot(0.75, 0.2, 0.15)
retries = 1000

testsCRC(bsChannel, data, crcPolynomials, retries,
         'Binary symmetric {}'.format(0.1))
testsCRC(geChannel, data, crcPolynomials, retries,
         'Gilbert-Elliot {} {} {}'.format(0.75, 0.2, 0.15))

testsParityBit(bsChannel, data, retries, 'Binary symmetric {}'.format(0.1))
testsParityBit(geChannel, data, retries,
               'Gilbert-Elliot {} {} {}'.format(0.75, 0.2, 0.15))
