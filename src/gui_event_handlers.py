"""
Here are event handling functions that are called when an event happens in the GUI
"""

import tkinter
from tkinter import Text, ttk
from classes.rotor import Rotor
from src import ciphering_algorithm
import webbrowser


def encipher_text(
    input_text: str,
    plugboard_settings: [int, int],
    rotor_settings: [int, int],
    output_text: Text,
) -> None:
    """
    Enciphers the input text using the Enigma machine.

    Args:
    - input_text (str): The text to be enciphered.
    - plugboard_settings (list[int, int]): The plugboard settings as a list of pairs of integers representing the connected letters.
    - rotor_settings (list[list[int, int, int]]): The rotor settings as a list of lists. Each inner list contains the rotor number, rotor shift, and rotor position.
    - output_text (Text): The output text widget where the enciphered text will be displayed.

    Returns:
    - None
    """
    
    # If the Enigma settings are not valid then no encryption will be done and an error message will be displayed in the output box. See : is_valid_settings()
    if not is_valid_settings(plugboard_settings, rotor_settings, output_text):
        # If false is returned then there is an error. Otherwise the code will continue to run as usual.
        return
    
    # Make the input text uppercase and strip any whitespaces from the start and end of the string
    input_text = input_text.upper().strip()

    # Initialize the rotors (Rotor class) for the Enigma machine based on the provided rotor settings.
    # Returns the tuple of the 3 rotors (Rotor class) for the Enigma machine.
    rotors = initialize_rotors(rotor_settings)
    
    # Convert letters to numbers. Zero-indexed. A is 0, B is 1, C is 2 etc.
    plugboard_settings = [
        [ord(letter) - ord("A") for letter in sublist] for sublist in plugboard_settings
    ]

    # Unpack the rotors tuple
    rotor_1, rotor_2, rotor_3 = rotors[0], rotors[1], rotors[2]
    
    # Send the string in to the enciphering algorithm
    enciphered_text = ciphering_algorithm.encipher(
        input_text, rotor_1, rotor_2, rotor_3, plugboard_settings
    )

    display_enciphered_text(enciphered_text, output_text)


def display_enciphered_text(enciphered_text: str, output_text: Text) -> None:
    """
    Display the output text in the output box

    Args:
    - enciphered_text (str): The enciphered text to be displayed.
    - output_text (Text): The output text widget where the enciphered text will be displayed.
    """
    # Clear existing text in the text box
    output_text.delete("1.0", "end-1c")
    # Set the foreground color to black
    output_text.config(foreground="black")
    # Insert the new text into the text box
    output_text.insert("1.0", enciphered_text)
    

def initialize_rotors(rotor_settings: [int, int]) -> tuple[Rotor]:
    """
    Initialize the rotors for the Enigma machine based on the provided rotor settings.

    Args:
    - rotor_settings (list[list[int, int, int]]): The rotor settings as a list of lists. Each inner list contains the rotor number, rotor shift, and rotor position.

    Returns:
    - tuple[Rotor]: A tuple containing the initialized rotor objects.
    
    --------------------------------------------------------------------------------
    
    rotor_settings[0] is the right most rotor, rotor_settings[1] is the middle rotor, rotor_settings[2] is the left rotor

    rotor_settings[X][0] is the number of the rotor. I, II, III, IV, V
    rotor_settings[X][1] is the rotor shift.
    rotor_settings[X][2] is the rotor position.
    """
    
    rotor_1 = Rotor(
        int(rotor_settings[0][0]), int(rotor_settings[0][1]), int(rotor_settings[0][2])
    )
    rotor_2 = Rotor(
        int(rotor_settings[1][0]), int(rotor_settings[1][1]), int(rotor_settings[1][2])
    )
    rotor_3 = Rotor(
        int(rotor_settings[2][0]), int(rotor_settings[2][1]), int(rotor_settings[2][2])
    )

    return rotor_1, rotor_2, rotor_3


def copy_text(text_box: Text) -> None:
    """
    Copy the text from the given text box to the clipboard.

    Parameters:
    - text_box (Text): The text box from which to copy the text.

    Returns:
    - None
    """

    # Get the text from the text box
    text = text_box.get("1.0", "end-1c")

    # Clear the clipboard
    text_box.clipboard_clear()

    # Append the text to the clipboard
    text_box.clipboard_append(text)

    # Update the clipboard
    text_box.update()


def paste_text(text_box: Text) -> None:
    """
    Paste the text from the clipboard into the given Text widget.

    Parameters:
    - text_box (Text): The Text widget to paste the text into.

    Returns:
    - None

    Description:
    This function checks if the clipboard contains text.
    If it does, it clears the existing text in the Text widget and pastes the text from the clipboard.
    Then, it inserts the text into the Text widget.
    """

    # Check if the clipboard contains text
    try:
        # Clear the existing text in the Text widget
        text_box.delete("1.0", "end")

        # Get the text from the clipboard
        text = text_box.clipboard_get()

        # Insert the text into the text box
        text_box.insert("insert", text)
    except tkinter.TclError:
        # Error handling in case the clipboard is empty
        print("Error: Unable to retrieve text from clipboard")


def get_rotor_settings(
    rotor_left_number: ttk.Combobox,
    rotor_left_position: ttk.Combobox,
    rotor_left_shift: ttk.Combobox,
    rotor_ctr_number: ttk.Combobox,
    rotor_ctr_position: ttk.Combobox,
    rotor_ctr_shift: ttk.Combobox,
    rotor_right_number: ttk.Combobox,
    rotor_right_position: ttk.Combobox,
    rotor_right_shift: ttk.Combobox,
):
    """
    Get the rotor settings from the GUI and return them as a list.

    Parameters:
    - rotor_left_number (ttk.Combobox): Combobox widget for selecting the left rotor number.
    - rotor_left_position (ttk.Combobox): Combobox widget for selecting the left rotor position.
    - rotor_left_shift (ttk.Combobox): Combobox widget for selecting the left rotor shift.
    - rotor_ctr_number (ttk.Combobox): Combobox widget for selecting the center rotor number.
    - rotor_ctr_position (ttk.Combobox): Combobox widget for selecting the center rotor position.
    - rotor_ctr_shift (ttk.Combobox): Combobox widget for selecting the center rotor shift.
    - rotor_right_number (ttk.Combobox): Combobox widget for selecting the right rotor number.
    - rotor_right_position (ttk.Combobox): Combobox widget for selecting the right rotor position.
    - rotor_right_shift (ttk.Combobox): Combobox widget for selecting the right rotor shift.

    Returns:
    - list: A list containing the rotor settings in the following format:
        [
            [right_rotor_number, right_rotor_shift, right_rotor_position],
            [center_rotor_number, center_rotor_shift, center_rotor_position],
            [left_rotor_number, left_rotor_shift, left_rotor_position]
        ]
    """
    
    """
    rotor_settings = [0] is the left rotor
    rotor_settings = [1] is the center rotor
    rotor_settings = [2] is the right rotor
    """

    rotor_settings = [
        [
            rotor_number_roman_to_int(rotor_right_number.get()),
            rotor_right_shift.get(),
            rotor_right_position.get(),
        ],
        [
            rotor_number_roman_to_int(rotor_ctr_number.get()),
            rotor_ctr_shift.get(),
            rotor_ctr_position.get(),
        ],
        [
            rotor_number_roman_to_int(rotor_left_number.get()),
            rotor_left_shift.get(),
            rotor_left_position.get(),
        ],
    ]

    return rotor_settings


# Converts rotor numbers from the roman format to integers
def rotor_number_roman_to_int(rotor_roman: str) -> int:
    """
    Converts a Roman numeral representation of a rotor number to its corresponding integer value.

    Parameters:
    - rotor_roman (str): The Roman numeral representation of the rotor number.

    Returns:
    - int: The integer value of the rotor number.

    Example:
        rotor_number_roman_to_int("III")
        # Output: 3
    """
    if rotor_roman == "I":
        return 1
    if rotor_roman == "II":
        return 2
    if rotor_roman == "III":
        return 3
    if rotor_roman == "IV":
        return 4
    if rotor_roman == "V":
        return 5
    else:
        return None


# Take all the values of the comboboxes and put them into a 2D array
def get_plugboard_2D_array(plugboard_inputs: list) -> list:
    """
    Return a 2D array representing the plugboard connections.

    Parameters:
    - plugboard_inputs (list): A list of input values from the plugboard.

    Returns:
    - list: A 2D array where each inner array represents a pair of connected inputs.

    Example:
    >>> get_plugboard_2D_array(['A', 'B', 'C', 'D'])
    [['A', 'B'], ['C', 'D']]
    """
    
    return [
        [plugboard_inputs[i].get(), plugboard_inputs[i + 1].get()]
        for i in range(0, len(plugboard_inputs), 2)
    ]


def is_valid_settings(plugboard_settings: [int, int], rotor_settings: [int, int], output_text):
    """
    Check if the provided plugboard and rotor settings are valid.

    Args:
    - plugboard_settings (list[int, int]): The plugboard settings as a list of pairs of integers representing the connected letters.
    - rotor_settings (list[list[int, int, int]]): The rotor settings as a list of lists. Each inner list contains the rotor number, rotor shift, and rotor position.
    - output_text: The output text widget where error messages will be displayed.

    Returns:
    - bool: True if the settings are valid, False otherwise.
    """
    
    
    """Check if there is no two instances of the same rotor number"""
    if len(rotor_settings) != len({tuple(setting) for setting in rotor_settings}):
        """If invalid, display an error message in the output box"""
        # Delete the existing text in the output box
        output_text.delete("1.0", "end-1c")
        # Set the foreground color to red
        output_text.config(foreground="red")
        # Put new text in to the box
        output_text.insert("1.0", "Two or more rotors are the same number.")
        return False
    
    """Check if there are two or more letters that are the same if the plugboard. Each letter can be only once"""
    # Flatten the 2D array and filter out empty cells
    flattened = [cell for row in plugboard_settings for cell in row if cell != ' ']
    
    # Check for duplicates
    if len(flattened) != len(set(flattened)):
        """If invalid, display an error message in the output box"""
        # Delete the existing text in the output box
        output_text.delete("1.0", "end-1c")
        # Set the foreground color to red
        output_text.config(foreground="red")
        # Put new text in to the box
        output_text.insert("1.0", "Two or more letters in the plugboard are the same.")
        return False
    
    else:
        return True


def clear_textbox(text_box: Text) -> None:
    """
    Clear the content of the given text box.

    Parameters:
    - text_box (Text): The text box to clear.

    Returns:
    - None
    """

    text_box.delete("1.0", "end")


def open_enigma_link(event):
    webbrowser.open_new_tab("https://www.cryptomuseum.com/crypto/enigma/i/index.htm")


def open_linkedin_link(event):
    webbrowser.open_new_tab("https://www.linkedin.com/in/daniel-dekhtyar/")


def open_github_link(event):
    webbrowser.open_new_tab("https://github.com/DanielDekhtyar")
