"""
This files contains all the code that ciphers the text according to the Enigma cipher
"""


from classes.rotor import Rotor
from src import enigma_parts


def encipher(text: str, rotor_1: Rotor, rotor_2: Rotor, rotor_3: Rotor, plugboard_settings: list[int, int]):
    """
    Encrypts the given text using the Enigma machine.

    Args:
        text (str): The text to be encrypted.
        rotor_1 (Rotor): The first rotor in the Enigma machine.
        rotor_2 (Rotor): The second rotor in the Enigma machine.
        rotor_3 (Rotor): The third rotor in the Enigma machine.
        plugboard_settings (list[int, int]): The plugboard settings.

    Returns:
        str: The encrypted text.
    """
    # Create the plugboard 2D array
    plugboard, reversed_plugboard = create_the_plugboard(plugboard_settings)
    
    # Stores the text after it went through the Enigma machine
    result_text = ""
    
    # Loop through each character in the string
    for char in text:
        if char.isalpha():
            # Convert the character to its number value. A = 0, B = 1, etc.
            letter_int = ord(char) - ord('A')
            print(f"Letter {char} is converted to {letter_int}")
            # Call the Enigma machine to encrypt the character
            enciphered_letter = enigma_machine(letter_int, rotor_1, rotor_2, rotor_3, plugboard, reversed_plugboard)
            print(f"Rotor positions are: Rotor 1: {rotor_1.position}, Rotor 2: {rotor_2.position}, Rotor 3: {rotor_3.position}")

            # Convert the number value back to a character and append to the result string
            char_back = chr(enciphered_letter + ord('A'))
            result_text += char_back
        else:
            # If not a letter then just append the char as it is
            result_text += char
    
    return result_text


def enigma_machine(
    letter: int,
    rotor_1: Rotor,
    rotor_2: Rotor,
    rotor_3: Rotor,
    plugboard: list[int, int],
    reversed_plugboard: list[int, int]):
    
    
    """
    Encrypts or decrypts a letter using the Enigma machine.

    Parameters:
    - letter (int): The letter to be encrypted or decrypted, represented as an integer from 0 to 25.
    - rotor_1 (Rotor): The first rotor to be used in the encryption or decryption process.
    - rotor_2 (Rotor): The second rotor to be used in the encryption or decryption process.
    - rotor_3 (Rotor): The third rotor to be used in the encryption or decryption process.
    - plugboard (list[int, int]): A list representing the plugboard configuration, where each element is a
    pair of integers representing the input and output letters.
    - reversed_plugboard (list[int, int]): A list representing the reverse plugboard configuration,
    where each element is a pair of integers representing the output and input letters.

    Returns:
    - int: The encrypted or decrypted letter, represented as an integer from 0 to 25.

    The function performs the encryption or decryption process using the Enigma machine. It takes a letter and passes
    it through the plugboard, the rotors, the reflector, and then back through the rotors and the plugboard again.
    The resulting letter is returned.

    Note:
    - The Enigma machine is a cipher machine used during World War II for encryption and decryption of secret messages.
    - The rotors in the Enigma machine are responsible for the substitution of letters.
    - The plugboard in the Enigma machine is responsible for additional letter substitution.
    - The reflector in the Enigma machine is responsible for reflecting the signal back through the rotors.
    - The rotor positions are updated after each letter is encrypted or decrypted.
    - The plugboard configuration and rotor settings determine the encryption or decryption process.
    """
    
    
    rotors = [rotor_1, rotor_2, rotor_3]
    
    # Create the reflector.
    # Based on the standard wiring UKW-B reflector in the Enigma I machine
    # Look : https://www.cryptomuseum.com/crypto/enigma/i
    reflector = [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 14, 10, 12, 8, 4, 1, 5, 25, 2, 22, 21, 9, 0, 19]
    
    # Pass the letter through the plugboard
    letter = enigma_parts.plugboard(letter, plugboard, reversed_plugboard)
    
    # Turn the rotors as needed
    rotor_turn(rotors)
    
    # Pass the letter through the first rotor
    letter = enigma_parts.rotor(letter, rotor_1)
    
    # Pass the letter through the second rotor
    letter = enigma_parts.rotor(letter, rotor_2)
    
    # Pass the letter through the third rotor
    letter = enigma_parts.rotor(letter, rotor_3)
    
    # Pass the letter through the reflector
    letter = reflector[letter]
    
    # Pass the letter through the third rotor in reverse
    letter = enigma_parts.rotor_reversed(letter, rotor_3)
    
    # Pass the letter through the second rotor in reverse
    letter = enigma_parts.rotor_reversed(letter, rotor_2)
    
    # Pass the letter through the first rotor in reverse
    letter = enigma_parts.rotor_reversed(letter, rotor_1)
    
    # Pass the letter through the plugboard again
    letter = enigma_parts.plugboard(letter, plugboard, reversed_plugboard)
    
    
    return letter


def create_the_plugboard(plugboard_settings: list[int, int]):
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


def rotor_turn(rotors: list[Rotor]):
    """
    Turns the rotors in the Enigma machine.

    Parameters:
    - rotors (list[Rotor]): A list of Rotor objects representing the rotors in the Enigma machine.

    The function rotates the rotors in the Enigma machine according to the specified rules.
    The first rotor is always rotated by one position.
    If the notch of the first rotor is reached, the second rotor is also rotated by one position.
    If the notch of the second rotor is reached, the third rotor is rotated by one position.

    Note:
    - The Enigma machine is a cipher machine used during World War II for encryption and decryption of secret messages.
    - The rotors in the Enigma machine are responsible for the substitution of letters.
    - The rotor positions are updated after each letter is encrypted or decrypted.
    """
    
    # Turn the rotor as needed
    # rotors[0] is the first rotor. rotors[1] is the second rotor, and rotors[2] is the third rotor.
    
    # Move the first rotor forward by one position.
    rotors[0].position += 1
    rotors[0].position %= 26
    
    # Check if the second rotor has reached the notch. If so, move the second rotor forward by one position.
    if rotors[0].notch == rotors[0].position:
        rotors[1].position += 1
        rotors[1].position %= 26
    
    # Check if the third rotor has reached the notch. If so, move the third rotor forward by one position.
    if rotors[1].notch == rotors[1].position:
        rotors[2].position += 1
        rotors[2].position %= 26