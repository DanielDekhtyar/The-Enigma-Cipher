"""
The main code that runs when trying to encipher using the enigma machine.
"""

from src import ciphering_algorithm
from classes.rotor import Rotor


def main():
    """
    The `main` function is the entry point of the program.
    It prompts the user to enter a text to be encrypted, initializes the rotor settings and positions,
    and calls the `encipher` function from the `ciphering_algorithm` module to encrypt the input text using the Enigma machine.

    Returns:
        None
    """

    input_text = input("Enter the text to be encrypted: ")
    input_text = input_text.replace("\n", "")
    input_text = input_text.upper().strip()

    rotor_1_number = 3
    rotor_1_shift = 12
    rotor_1_position = 1

    rotor_2_number = 2
    rotor_2_shift = 4
    rotor_2_position = 7

    rotor_3_number = 1
    rotor_3_shift = 1
    rotor_3_position = 5

    # Initialize the plugboard
    plugboard_settings: [int, int] = []

    # Populate the plugboard with pairs of letters to be swapped
    # plugboard_settings = [
    #     [6, 10],
    #     [3, 11],
    #     [8, 24],
    #     [0, 16],
    #     [5, 7],
    #     [22, 1],
    #     [19, 23],
    #     [15, 18],
    #     [14, 12],
    #     [25, 20],
    # ]

    rotor_1 = Rotor(rotor_1_number, rotor_1_shift, rotor_1_position)
    rotor_2 = Rotor(rotor_2_number, rotor_2_shift, rotor_2_position)
    rotor_3 = Rotor(rotor_3_number, rotor_3_shift, rotor_3_position)

    result_text = ciphering_algorithm.encipher(
        input_text, rotor_1, rotor_2, rotor_3, plugboard_settings
    )

    print("===============================================")
    print(result_text)
    print("===============================================")


if __name__ == "__main__":
    main()
