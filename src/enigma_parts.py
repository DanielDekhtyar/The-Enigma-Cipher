"""
Here is all the parts of the Enigma machine enciphering algorithm
"""

from classes.rotor import Rotor


def plugboard(letter: int, plugboard, reversed_plugboard) -> chr:
    """
    This function maps a given letter through the plugboard of an Enigma machine.

    Parameters:
    - letter (int): The letter to be mapped, represented as an integer from 0 to 25.
    - plugboard (dict): A dictionary representing the plugboard configuration,
    where the keys are the input letters and the values are the corresponding output letters.
    - reversed_plugboard (dict): A dictionary representing the reverse plugboard configuration,
    where the keys are the output letters and the values are the corresponding input letters.

    Returns:
    - int: The mapped letter, represented as an integer from 0 to 25.

    If the given letter is present in the plugboard configuration, the function returns the corresponding
    mapped letter from the plugboard dictionary.
    If the given letter is present in the reverse plugboard configuration, the function returns the corresponding
    mapped letter from the reversed_plugboard dictionary.
    If the given letter is not present in either configuration, the function returns the original letter unchanged.
    """

    if letter in plugboard:
        return plugboard[letter]
    elif letter in reversed_plugboard:
        return reversed_plugboard[letter]
    else:
        return letter


def pass_through_rotor(letter: int, rotor: Rotor, is_reversed: bool) -> chr:
    """
    Passes a letter through a rotor, considering the rotor's wiring, offset, and position.

    Args:
    - letter (int): The index of the input letter (0-25).
    - rotor (Rotor): The rotor through which the letter is passed.
    - is_reversed (bool): A boolean indicating whether the letter is passing through in reverse.

    Returns:
    - chr: The resulting letter after passing through the rotor.

    Note:
    - The function takes an input letter index (0-25), a rotor object, and a boolean flag to determine
    whether the letter is passing through the rotor in the forward direction or reversed.
    - The rotor's wiring, setting, and position are considered in the process.
    """
    rotor_wiring = rotor.wiring
    rotor_offset = rotor.setting
    rotor_position = rotor.position

    # Apply rotor position and setting
    letter_index = (letter + rotor_position - rotor_offset) % 26

    if is_reversed:
        # If passing in reverse, find the original letter in the wiring
        result_index = rotor_wiring.index(letter_index)
    else:
        # Pass through rotor wiring
        result_index = rotor_wiring[letter_index]

    # Reverse rotor position and setting adjustment
    result_index = (result_index - rotor_position + rotor_offset) % 26

    return result_index


def rotor_setting_shift(letter: int, rotor: Rotor) -> chr:
    """
    The function shifts a letter by the rotor setting, taking into account wrapping around.

    Args:
    letter (int): The letter parameter is an integer representing the position of the letter in the
    alphabet. For example, 'A' would be represented by 0, 'B' by 1, and so on.
    rotor (Rotor): The `rotor` parameter is an instance of the `Rotor` class.

    Returns:
    The encrypted letter, which is the original letter shifted by the rotor setting.
    """
    # Shift the letter by the rotor setting, and handle wrapping around
    # Rotor setting (also called Ring setting) is zero-indexed, 0 = No change, 1 = +1, 2 = +2, etc.
    encrypted_letter = (letter + rotor.setting) % 26

    return encrypted_letter


def create_the_plugboard(plugboard_settings: list[int, int]) -> tuple[dict, dict]:
    """
    Create the plugboard dictionary and its reverse dictionary.

    Args:
        plugboard_settings (list[int, int]): The list of plugboard settings.

    Returns:
        tuple: A tuple containing the plugboard dictionary and its reverse dictionary.
    """
    # Create the plugboard dictionary from the list of plugboard settings.
    plugboard = dict(plugboard_settings)

    # Reverse the dictionary using a dictionary comprehension
    reversed_plugboard = {value: key for key, value in plugboard.items()}

    return plugboard, reversed_plugboard
