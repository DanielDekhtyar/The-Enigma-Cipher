"""
Here is a test to see if the enciphering algorithm is working properly.
To do so we need to do the following steps:

1. Encipher a word
2. Take the encrypted word and decipher it

The deciphered word should be the same as the original word.
"""

from src.ciphering_algorithm import encipher
from classes.rotor import Rotor


def test_encipher():
    word = "Enigma".upper() # The word don't have to be all uppercase
    
    # Create an instance of the Enigma machine that I want to test on
    encrypting_enigma = Enigma_machine()
    
    # Save all the part of the Enigma as variables
    # Reflector excluded because it is set and can not be changed by the user
    rotor_1 = encrypting_enigma.rotor_1
    rotor_2 = encrypting_enigma.rotor_2
    rotor_3 = encrypting_enigma.rotor_3
    rotor_4 = encrypting_enigma.rotor_4
    rotor_5 = encrypting_enigma.rotor_5
    plugboard = encrypting_enigma.plugboard
    
    encrypted_word = encipher(word, rotor_3, rotor_2, rotor_1, plugboard)
    
    # A second enigma machine is created with the same exact settings as the first
    decrypting_enigma = Enigma_machine()
    
    # Save all the part of the Enigma as variables
    # Reflector excluded because it is set and can not be changed by the user
    decrypted_rotor_1 = decrypting_enigma.rotor_1
    decrypted_rotor_2 = decrypting_enigma.rotor_2
    decrypted_rotor_3 = decrypting_enigma.rotor_3
    decrypted_rotor_4 = decrypting_enigma.rotor_4
    decrypted_rotor_5 = decrypting_enigma.rotor_5
    decrypted_plugboard = decrypting_enigma.plugboard
    
    decrypted_word = encipher(encrypted_word, decrypted_rotor_3, decrypted_rotor_2, decrypted_rotor_1, decrypted_plugboard)
    
    assert word == decrypted_word


class Enigma_machine():
    def __init__(self):
        self._plugboard = self.set_plugboard()
        self._rotor_1 = Rotor(3, 12, 1)
        self._rotor_2 = Rotor(2, 4, 7)
        self._rotor_3 = Rotor(1, 1, 5)
        self._rotor_4 = Rotor(4, 12, 8)
        self._rotor_5 = Rotor(5, 6, 16)

    @property
    def plugboard(self):
        return self._plugboard

    def set_plugboard(self):
        plugboard: [int, int] = [
            [6, 10],
            [3, 11],
            [8, 24],
            [0, 16],
            [5, 7],
            [22, 1],
            [19, 23],
            [15, 18],
            [14, 12],
            [25, 20],
        ]
        return plugboard

    @property
    def rotor_1(self):
        return self._rotor_1

    @property
    def rotor_2(self):
        return self._rotor_2

    @property
    def rotor_3(self):
        return self._rotor_3

    @property
    def rotor_4(self):
        return self._rotor_4

    @property
    def rotor_5(self):
        return self._rotor_5

