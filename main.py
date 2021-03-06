import sys

from channels import binary_symmetric
from channels import gilbert_elliot
from generator import random_ascii_words, random_polynomials
from tests import *

data = random_ascii_words(10)
crcPolynomials = random_polynomials(
    totalAmount=10 * 3, stepLen=3, startingLen=3)

bsChannel = binary_symmetric(0.1)
geChannel = gilbert_elliot(0.75, 0.2, 0.15)
retries = 1000

#-----------CRC-----------------
testsCRC(bsChannel, data, crcPolynomials, retries,
         'Binary symmetric {}'.format(0.1))
testsCRC(geChannel, data, crcPolynomials, retries,
         'Gilbert-Elliot {} {} {}'.format(0.75, 0.2, 0.15))

#-----------PARITY----------------- 010110 -> 0101101 -> 1001101 ->  
testsParityBit(bsChannel, data, retries, 'Binary symmetric {}'.format(0.1))
testsParityBit(geChannel, data, retries,
               'Gilbert-Elliot {} {} {}'.format(0.75, 0.2, 0.15))

#-----------REPETITION------------- 
testsRepetition(bsChannel, data, 2, retries, 'Binary symmetric {}'.format(0.1))
testsRepetition(geChannel, data, 2, retries,
               'Gilbert-Elliot {} {} {}'.format(0.75, 0.2, 0.15))

testsRepetition(bsChannel, data, 3, retries, 'Binary symmetric {}'.format(0.1))
testsRepetition(geChannel, data, 3, retries,
               'Gilbert-Elliot {} {} {}'.format(0.75, 0.2, 0.15))

testsRepetition(bsChannel, data, 4, retries, 'Binary symmetric {}'.format(0.1))
testsRepetition(geChannel, data, 4, retries,
               'Gilbert-Elliot {} {} {}'.format(0.75, 0.2, 0.15))

