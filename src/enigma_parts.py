"""
Here goes all the parts of the Enigma machine enciphering algorithm
"""

from classes.rotor import Rotor


def plugboard(letter: int, plugboard, reversed_plugboard):
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


def rotor(letter: int, rotor: Rotor):
    """
    The function `rotor` performs the encryption process using a rotor in the Enigma machine.

    Args:
    letter (int): The letter parameter is an integer representing the position of the letter in the alphabet.
    For example, 'A' would be represented by 0, 'B' by 1, and so on.
    rotor (Rotor): The `rotor` parameter is an instance of the `Rotor` class.

    Returns:
    The encrypted letter, which is the original letter adjusted based on the rotor's absolute position,
    changed according to the rotor wiring, and shifted by the rotor setting.

    Note:
    If the letter is not found in the rotor wiring, the function will print an error message and
    return the original letter as a placeholder.
    """
    # Adjust the letter based on the rotor's absolute position (The rotors turn)
    letter = (letter + rotor.position) % 26
    
    # Change the letter according to the rotor wiring
    letter = rotor.wiring[letter]
    
    # Shift the letter by the rotor setting
    letter = rotor_setting_shift(letter, rotor)
    
    return letter


def rotor_reversed(letter: int, rotor: Rotor):
    """
    The function `rotor_reversed` reverses the encryption process performed by a rotor in the Enigma machine.

    Args:
    letter (int): The letter parameter is an integer representing the position of the letter in the alphabet.
    For example, 'A' would be represented by 0, 'B' by 1, and so on.
    rotor (Rotor): The `rotor` parameter is an instance of the `Rotor` class.

    Returns:
    The decrypted letter, which is the original letter reversed through the rotor wiring and shifted back by the rotor setting.

    Note:
    If the letter is not found in the rotor wiring, the function will print an error message and return the original letter as a placeholder.
    """
    # Check if the letter is in the rotor wiring
    if letter in rotor.wiring:
        # Reverse the letter through the rotor wiring
        letter = rotor.wiring.index(letter)

        # Reverse the letter by shifting it back by the rotor setting
        letter = (letter - rotor.setting) % 26

        return letter
    else:
        # Handle the case where the letter is not in the rotor wiring
        print(f"Letter {letter} not found in rotor wiring.")
        # You might want to decide on the appropriate action, e.g., return an error code or raise an exception.
        # For now, returning the original letter as a placeholder.
        return letter


def rotor_setting_shift(letter: int, rotor: Rotor):
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