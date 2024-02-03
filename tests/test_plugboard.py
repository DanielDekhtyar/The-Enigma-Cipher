from src import enigma_parts


def test_pass_through_plugboard():
    # Initialize the plugboard
    plugboard_settings: [int, int] = []

    # Populate the plugboard with pairs of letters to be swapped
    plugboard_settings = [
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

    # Create the plugboard and reversed plugboard dictionaries
    # Reversed plugboard is the same is the regular plugboard, but with the keys and values swapped
    # This is done because letters can substitute each other no matter the order
    plugboard, reversed_plugboard = enigma_parts.create_the_plugboard(
        plugboard_settings
    )

    # Check that the letter that comes out of the plugboard is the letter that we want

    letter = 13
    letter = enigma_parts.pass_through_plugboard(letter, plugboard, reversed_plugboard)
    assert letter == 13

    letter = 23
    letter = enigma_parts.pass_through_plugboard(letter, plugboard, reversed_plugboard)
    assert letter == 19

    letter = 16
    letter = enigma_parts.pass_through_plugboard(letter, plugboard, reversed_plugboard)
    assert letter == 0

    letter = 10
    letter = enigma_parts.pass_through_plugboard(letter, plugboard, reversed_plugboard)
    assert letter == 6

    letter = 8
    letter = enigma_parts.pass_through_plugboard(letter, plugboard, reversed_plugboard)
    assert letter == 24

    letter = 25
    letter = enigma_parts.pass_through_plugboard(letter, plugboard, reversed_plugboard)
    assert letter == 20


def test_create_the_plugboard():
    # The letter pairs to be swapped in the plugboard
    plugboard_settings = [
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

    # Create the plugboard and reversed plugboard dictionaries
    plugboard, reversed_plugboard = enigma_parts.create_the_plugboard(
        plugboard_settings
    )

    # Check that the plugboard and reversed plugboard dictionaries are created correctly
    assert plugboard == {
        6: 10,
        3: 11,
        8: 24,
        0: 16,
        5: 7,
        22: 1,
        19: 23,
        15: 18,
        14: 12,
        25: 20,
    }
    assert reversed_plugboard == {
        10: 6,
        11: 3,
        24: 8,
        16: 0,
        7: 5,
        1: 22,
        23: 19,
        18: 15,
        12: 14,
        20: 25,
    }

    # Check that the plugboard has 10 pairs of letters and the reversed plugboard has 10 pairs of letters
    assert len(plugboard) == 10
    assert len(reversed_plugboard) == 10

    # Check that the letters are swapped correctly
    assert plugboard[5] == 7
    assert reversed_plugboard[7] == 5
