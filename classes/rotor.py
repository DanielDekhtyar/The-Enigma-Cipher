"""
This is the class that defines the rotor for the Enigma machine.
It is based on the Enigma I machine, which where the most common configuration during WW2.

It contains:
1. Rotor number 1-5. Only 3 rotors are allowed at once. 5 rotors are available to choose from.
2. Rotor wiring as an array
3. Rotor notch (the letter that the rotor will turn)
4. Rotor setting (offset on the letter using the caesar cipher)
5. Rotor position (the letter that the rotor is currently at 0-25)
"""


import sys


class Rotor:
    """
    This class defines a rotor used in the Enigma machine.

    Attributes:
    - number (int): Rotor number 1-5. Only 3 rotors are allowed at once. 5 rotors are available to choose from.
    - wiring (list): Rotor wiring as an array.
    - notch (int): Rotor notch (the letter that the rotor will turn).
    - setting (int): Rotor setting (offset on the letter using the Caesar cipher).
    - position (int): Rotor position (the letter that the rotor is currently at 0-25).

    Methods:
    - __init__(self, number, setting, position): Initializes a Rotor instance with the specified parameters.
    - get_wiring(number): Returns the wiring setting for the specified rotor number.

    Note: The wiring settings are based on the Enigma I machine
    """
    def __init__(self, number, setting, position):
        # Rotor number 1-5. Only 3 rotors are allowed at once. 5 rotors are available to choose from.
        self.number = number
        # Rotor wiring as an array
        self.wiring = self.get_wiring(number)
        # Rotor notch (the letter that the rotor will turn)
        self.notch = self.get_notch(number)
        # Rotor setting (offset on the letter using the caesar cipher)
        self.setting = setting
        # Rotor position (the letter that the rotor is currently at 0-25)
        self.position = position
    
    
    # Wiring setting taken from https://www.cryptomuseum.com/crypto/enigma/wiring.htm for Enigma I machine
    def get_wiring(self, rotor_number):
        """
        The function `get_wiring` returns the wiring configuration for a given rotor number or
        reflector.
        
        Args:
        rotor_number: The parameter `rotor_number` is an integer that represents the number of the
        rotor. It is used to determine the wiring configuration for the specified rotor. The function
        `get_wiring` returns a list of integers that represents the wiring configuration for the
        specified rotor number.
        
        Returns:
        a list of integers representing the wiring configuration for a specific rotor or reflector.
        """
        # Rotor wiring for rotor I
        if rotor_number == 1:
            return [4, 10, 12, 5, 11, 6, 3, 16, 21, 25, 13, 19, 14, 22, 24, 7, 23, 20, 18, 15, 0, 8, 1, 17, 2, 9]
        
        # Rotor wiring for rotor II
        elif rotor_number == 2:
            return [0, 9, 3, 10, 18, 8, 17, 20, 23, 1, 11, 7, 22, 19, 12, 2, 16, 6, 25, 13, 15, 24, 5, 21, 14, 4]
        
        # Rotor wiring for rotor III
        elif rotor_number == 3:
            return [1, 3, 5, 7, 9, 2, 15, 17, 19, 23, 21, 25, 13, 24, 4, 8, 22, 6, 0, 10, 12, 20, 18, 16, 14]
        
        # Rotor wiring for rotor IV
        elif rotor_number == 4:
            return [4, 18, 14, 21, 15, 25, 9, 0, 24, 16, 20, 8, 17, 7, 23, 11, 13, 5, 19, 6, 10, 3, 2, 12, 22, 1]
        
        # Rotor wiring for rotor V
        elif rotor_number == 5:
            return [21, 25, 1, 17, 6, 8, 19, 24, 20, 15, 18, 3, 13, 7, 11, 23, 0, 22, 12, 9, 16, 14, 5, 4, 2, 10]
        
        # Error handling
        else:
            print(f"RotorSelectionError. Invalid rotor number received when creating a Rotor instance for rotor number {rotor_number}!")
            sys.exit(1)
        
        
    def get_notch(self, rotor_number):
        """
        The function `get_notch` returns the notch for a given rotor number.
        
        Args:
        rotor_number: The parameter `rotor_number` is an integer that represents the number of the
        rotor. It is used to determine the notch for the specified rotor. The function
        `get_notch` returns an integer that represents the notch for the specified rotor.
        
        Returns:
        an integer representing the notch for a specific rotor.
        """
        # Rotor notch for rotor I
        if rotor_number == 1:
            return 24
        
        # Rotor notch for rotor II
        elif rotor_number == 2:
            return 12
        
        # Rotor notch for rotor III
        elif rotor_number == 3:
            return 3
        
        # Rotor notch for rotor IV
        elif rotor_number == 4:
            return 17
        
        # Rotor notch for rotor V
        elif rotor_number == 5:
            return 7
    
    
    @property
    def number(self):
        return self._number
    
    @number.setter
    def number(self, value):
        if value < 1 or value > 5:
            print(f"RotorSelectionError. Invalid rotor number received when creating a Rotor instance for rotor number {value}!")
            print("Valid rotor numbers are 1-5.")
            sys.exit(1)
        else:
            self._number = value
    
    @property
    def notch(self):
        return self._notch
    
    @notch.setter
    def notch(self, value):
        if value < 0 or value > 25:
            print(f"RotorNotchError. Invalid rotor notch received when creating a Rotor instance for rotor number {self.number}!")
            print("Valid rotor notches are 0-25.")
            sys.exit(1)
        else:
            self._notch = value
    
    @property
    def setting(self):
        return self._setting
    
    @setting.setter
    def setting(self, value):
        # Ring setting is zero-indexed. 0 = No change, 1 = +1, 2 = +2, etc.
        value = value - 1
        
        if value < 0 or value > 25:
            print(f"RotorSettingError. Invalid rotor setting received when creating a Rotor instance for rotor number {self.number}!")
            print("Valid rotor settings are 0-25.")
            sys.exit(1)
        else:
            self._setting = value
    
    @property
    def position(self):
        return self._position
    
    @position.setter
    def position(self, value):
        if value < 0 or value > 25:
            print(f"RotorPositionError. Invalid rotor position received when creating a Rotor instance for rotor number {self.number}!")
            print("Valid rotor positions are 0-25.")
            sys.exit(1)
        else:
            self._position = value
