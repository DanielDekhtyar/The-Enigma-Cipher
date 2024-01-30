"""
This is the class that defines the rotor for the Enigma machine.
It is based on the Enigma I machine, which where the most common configuration during WW2.
"""

import sys


class Rotor:
    """
    This class defines a rotor for the Enigma machine based on the Enigma I machine.

    Attributes:
    - number (int): Rotor number 1-5. Only 3 rotors are allowed at once. 5 rotors are available to choose from.
    - wiring (list): Rotor wiring as an array.
    - notch (int): Rotor notch (the letter that triggers rotor turnover).
    - setting (int): Rotor setting (offset on the letter using the Caesar cipher).
    - position (int): Rotor position (the letter that the rotor is currently at 0-25).

    Methods:
    - rotor_turn(rotors: list) -> None:
        Rotates the rotors based on certain conditions. Internal method.

    - set_wiring(rotor_number: int) -> list:
        Returns the wiring configuration for the specified rotor number.

    - set_notch(rotor_number: int) -> int:
        Returns the notch position for the specified rotor number.

    Properties:
    - wiring (list): Get the rotor wiring configuration.
    - number (int): Get or set the rotor number.
    - notch (int): Get or set the rotor notch.
    - setting (int): Get or set the rotor setting.
    - position (int): Get or set the rotor position.
    """

    def __init__(self, number: int, setting: int, position: int):
        # Rotor number 1-5. Only 3 rotors are allowed at once. 5 rotors are available to choose from.
        self._number = number
        # Rotor wiring as an array
        self._wiring = self.set_wiring(number)
        # Rotor notch (the letter that the rotor will turn)
        self._notch = self.set_notch(number)
        # Rotor setting (offset on the letter using the caesar cipher)
        self._setting = setting
        # Rotor position (the letter that the rotor is currently at 0-25)
        self._position = position

    @classmethod
    def rotor_turn(self, rotors: list) -> None:
        """
        Rotates the rotors in the provided list based on certain conditions.

        Args:
        - rotors (list): A list of rotor objects to be rotated.
        """

        def get_new_rotor_position(rotors: list, rotor_number: int) -> None:
            """
            Increments the position of the specified rotor by one and ensures it does not exceed 25.

            Args:
            - rotors (list): A list of rotor objects.
            - rotor_number (int): The index of the rotor in the rotors list.
            """

            # Get the rotor current position.
            rotor_position = rotors[rotor_number].position

            # Increment the rotor position by one.
            rotor_position += 1

            # Make sure that the rotor position does not exceed 26. If it does, subtract 26 from it.
            if rotor_position > 25:
                rotor_position %= 26

            # Set the new rotor position to the rotor
            rotors[rotor_number].position = rotor_position

        # rotors[0] is the first rotor. rotors[1] is the second rotor, and rotors[2] is the third rotor.

        # Move the first rotor forward by one position.
        rotor_number = 0
        get_new_rotor_position(rotors, rotor_number)

        """
        Tracks if the first rotor has reached it's notch position (rotor_1.notch). This is used to determine if the second and third rotors can move or not.
        It addresses a bug when while the second rotor stays at the notch position, the third rotor will move every time the function is called.
        The third rotor should only move when the second rotor has moved a full circle.
        """
        if rotors[0].position == rotors[0].notch:
            first_rotor_reached_notch = True
        else:
            first_rotor_reached_notch = False

        # Check if the second rotor has reached the notch. If so, move the second rotor forward by one position.
        if first_rotor_reached_notch:
            rotor_number = 1
            get_new_rotor_position(rotors, rotor_number)

        # Tracks if the second rotor has reached the notch. This is used to determine if the third rotor can move or not.
        # For more info look at the docstring right above
        if rotors[1].position == rotors[1].notch:
            second_rotor_reached_notch = True
        else:
            second_rotor_reached_notch = False

        # Check if the third rotor has reached the notch. If so, move the third rotor forward by one position.
        if first_rotor_reached_notch and second_rotor_reached_notch:
            rotor_number = 2
            get_new_rotor_position(rotors, rotor_number)

    # Wiring setting taken from https://www.cryptomuseum.com/crypto/enigma/wiring.htm for Enigma I machine
    def set_wiring(self, rotor_number):
        """
        Returns the wiring configuration for the specified rotor number.

        Args:
        - rotor_number (int): The number of the rotor.

        Returns:
        - list: The wiring configuration for the specified rotor.
        """

        # Set wiring for rotor I
        if rotor_number == 1:
            return [
                4,
                10,
                12,
                5,
                11,
                6,
                3,
                16,
                21,
                25,
                13,
                19,
                14,
                22,
                24,
                7,
                23,
                20,
                18,
                15,
                0,
                8,
                1,
                17,
                2,
                9,
            ]

        # Set wiring for rotor II
        elif rotor_number == 2:
            return [
                0,
                9,
                3,
                10,
                18,
                8,
                17,
                20,
                23,
                1,
                11,
                7,
                22,
                19,
                12,
                2,
                16,
                6,
                25,
                13,
                15,
                24,
                5,
                21,
                14,
                4,
            ]

        # Set wiring for rotor III
        elif rotor_number == 3:
            return [
                1,
                3,
                5,
                7,
                9,
                11,
                2,
                15,
                17,
                19,
                23,
                21,
                25,
                13,
                24,
                4,
                8,
                22,
                6,
                0,
                10,
                12,
                20,
                18,
                16,
                14,
            ]

        # Set wiring for rotor IV
        elif rotor_number == 4:
            return [
                4,
                18,
                14,
                21,
                15,
                25,
                9,
                0,
                24,
                16,
                20,
                8,
                17,
                7,
                23,
                11,
                13,
                5,
                19,
                6,
                10,
                3,
                2,
                12,
                22,
                1,
            ]

        # Set wiring for rotor V
        elif rotor_number == 5:
            return [
                21,
                25,
                1,
                17,
                6,
                8,
                19,
                24,
                20,
                15,
                18,
                3,
                13,
                7,
                11,
                23,
                0,
                22,
                12,
                9,
                16,
                14,
                5,
                4,
                2,
                10,
            ]

        # Error handling
        else:
            print(
                f"RotorSelectionError. Invalid rotor number received when creating a Rotor instance for rotor number {rotor_number}!"
            )
            sys.exit(1)

    def set_notch(self, rotor_number):
        """
        Returns the notch position for the specified rotor number.

        Args:
        - rotor_number (int): The number of the rotor.

        Returns:
        - int: The notch position for the specified rotor.
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
    def wiring(self):
        return self._wiring

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, value):
        if value < 1 or value > 5:
            print(
                f"RotorSelectionError. Invalid rotor number received when creating a Rotor instance for rotor number {value}!"
            )
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
            print(
                f"RotorNotchError. Invalid rotor notch received when creating a Rotor instance for rotor number {self.number}!"
            )
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
            print(
                f"RotorSettingError. Invalid rotor setting received when creating a Rotor instance for rotor number {self.number}!"
            )
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
            print(
                f"RotorPositionError. Invalid rotor position received when creating a Rotor instance for rotor number {self.number}!"
            )
            print("Valid rotor positions are 0-25.")
            sys.exit(1)
        else:
            self._position = value
