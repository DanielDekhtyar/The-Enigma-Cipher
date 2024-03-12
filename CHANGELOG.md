# The Enigma Cipher

## 📝 Changelog:

> ### Last Version : 1.0.2
>
> ### Last Update : 12-03-2024
>
> _Date format DD-MM-YYYY_


### 🗓️ _Version 1.0.2 - 12-03-2024 ([commit 12634c1](https://github.com/DanielDekhtyar/The-Enigma-Cipher/commit/12634c1))_

--

#### 🚀 Added
- Added a link to the GitHub `README.md` file to explain how to configure the enigma.
- Added a text with the version of the app at the bottom right side and when clicked it opens `CHANGELOG.md` on GitHub.


### 🗓️ _Version 1.0.1 - 07-03-2024 ([commit ee718e0](https://github.com/DanielDekhtyar/The-Enigma-Cipher/commit/ee718e0))_

---

#### 🚀 Added
- In `is_valid_settings()` a section of code was added to check if every letter in the plugboard has a pair letter.  
This addresses a bug when a letter can have no pair.


### 🔥 Enhancements
- In `ciphering_algorithm.py`, `result_text: str` was renamed to `enciphered_text: str`.
- In `gui_event_handlers.py`, `display_enciphered_text()` was renamed to `display_text()` and changed to take a new parameter `color: str` (color of the text),  
so now it can be universally used to print text into any textbox, regardless if it is an error message (red), regular text (black) or any other text.
- `is_valid_settings()` was changed to take advantage of the enhanced `display_text()` function.


### 🗓️ _Version 1.0.0 - 05-02-2024 ([commit 578ce1d](https://github.com/DanielDekhtyar/The-Enigma-Cipher/commit/578ce1d))_

---

#### 🚀 Added
- `is_valid_settings()` in `gui_event_handlers.py` checks if the rotor settings given by the user are valid or not.  
If the input is invalid, a red error message will be displayed in the output box.  
- `Clear` buttons added to the GUI. When clicked they clear all the text inside the respective text box.
- Info text was added to the bottom of the GUI with relevant links.


### 🗓️ _Version 0.9.1 - 04-02-2024 ([commit 2116c10](https://github.com/DanielDekhtyar/The-Enigma-Cipher/commit/2116c10))_

---

### 🔥 Enhancements
- The enciphering algorithm is now fully working as the real Enigma 1 machine with the correct enciphering algorithm.
- In the previous version, the notch wasn't in the right place. Now it is in the so-called turnover position. Here is a [link](https://www.cryptomuseum.com/crypto/enigma/i/index.htm) to the Crypto Museum website explaining it.


### 🗓️ _Version 0.9.0 - 03-02-2024 ([commit 4aba150](https://github.com/DanielDekhtyar/The-Enigma-Cipher/commit/4aba150))_

---

#### 🚀 Added
- GUI functionality implemented.
- All the event handlers implemented inside `gui_event_handlers.py`
- Here is how the enciphering algorithm works in `encipher_text()`:
    - `encipher_text()` in `gui_event_handlers.py` takes the input text and the enigma settings.
    - Then it passes it to the enciphering algorithm (See: `encipher()` in `ciphering_algorithm.py`).
    - Gets back the enciphered text and displays it in the output box.
- A description of every function in `gui_event_handlers.py`
    - `display_enciphered_text` displays the enciphered text to the output box.
    - `initialize_rotors()` takes the rotors settings given by the user and initializes 3 rotors (`Rotor` class) with the given parameters.
    - `copy_text()` copies the text from the output box to the Windows clipboard.
    - `paste_text()` pastes whatever is currently in the clipboard, to the input box.
    - `get_rotor_settings()` is one of the functions called from `GUI.py` whenever the `Encipher Text` button is clicked.  
    It takes the Comboboxes values and creates a 2D array where all the settings for all the rotors are together under one variable `rotor_settings`.
    - `rotor_number_roman_to_int()` is called by `get_rotor_settings()` to convert roman numbers to integers. I => 1, II => 2 etc.
    - `get_plugboard_2D_array()` takes an array with all the combo boxes representing the plugboard connections and returns a 2D array of the plugboard pairs.  
    The inner array is the pairs themselves. This is a pair of letters that will be swapped: `[X][0] <=> [X][1]`


### 🔥 Enhancements
- `plugboard()` in `enigma_parts.py` was renamed to `pass_through_plugboard()` to better reflect its purpose.


### 🗓️ _Version 0.2.1 - 30-01-2024 ([commit fc2fc3e](https://github.com/DanielDekhtyar/The-Enigma-Cipher/commit/fc2fc3e))_

---

#### 🛠️ Fixed
- The bug mentioned in the commit of v0.2.0, when the rotors don't turn the way they should, was fixed.  
It was fixed by adding a boolean that tracks if the first rotor is currently at its notch position.  
If it is not at the notch position then no move will accrue.


### 🗓️ _Version 0.2.0 - 30-01-2024 ([commit 7c43db5](https://github.com/DanielDekhtyar/The-Enigma-Cipher/commit/7c43db5))_

---

### 🔥 Enhancements
- `rotor()` in `enigma_parts.py` was renamed to `pass_through_rotor()`
- `pass_through_rotor()` was completely rewritten to make it work better and fix bugs raised in v0.1.0
- `get_wiring()` in `Rotor` class was renamed to `set_wiring()` to better represent it's propose.
- `get_notch()` in `Rotor` class was renamed to `set_notch()` to better represent it's propose.
- `rotor_turn()` was implemented inside the `Rotor` class as `@classmethod`.  
It turns the rotors by one position whenever needed.
- `create_the_plugboard()` moved from `ciphering_algorithm.py` to `enigma_parts.py` for better code structure.
- All the to-dos from version 0.1.0 were fixed and now work as expected.

#### 🐞 To-Do 
- When a rotor is set to its notch position, it will turn the other rotors more than one time.  
It should turn a rotor just once every full turn.
The problem may be in `get_new_rotor_position()` inside the `Rotor` class.


### 🗓️ _Version 0.1.0 - 27-01-2024 ([commit 461645d](https://github.com/DanielDekhtyar/The-Enigma-Cipher/commit/461645d))_

---

#### 🚀 Added
- The first version of the Enigma cipher algorithm.
- `enigma.py` is a temporary code that feeds data into `encipher()`.  
It will later be done via a GUI.
- `ciphering_algorithm.py` contains the main logic of the enciphering algorithm of the Enigma.
- `encipher()` is mainly a `for loop` that iterates over all the chars in the string and feeds it into the `enigma_machine()`.  
The enciphered letter returned from the `enigma_machine()` is added to `result_text: str`
- `enigma_machine()` simulates all the steps in the Enigma enciphering algorithm and can encipher just one letter at a time.


#### 🐞 To-Do 
- When giving input `HELLO`, I get this error "Letter 11 not found in rotor wiring."  
Probably, it is caused by the reversed rotor function.
- The enciphering process should be checked for correctness.
- The code crashes when given a long input :  
```
Traceback (most recent call last):
    File "d:\Programming\The-Enigma-Cipher\Enigma.py", line 60, in <module>
        main()
    File "d:\Programming\The-Enigma-Cipher\Enigma.py", line 53, in main
        result_text = ciphering_algorithm.encipher(input_text, rotor_1, rotor_2, rotor_3, plugboard)
                    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "d:\Programming\The-Enigma-Cipher\src\ciphering_algorithm.py", line 37, in encipher
        enciphered_letter = enigma_machine(letter_int, rotor_1, rotor_2, rotor_3, plugboard, reversed_plugboard)
                            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "d:\Programming\The-Enigma-Cipher\src\ciphering_algorithm.py", line 103, in enigma_machine
        letter = enigma_parts.rotor(letter, rotor_1)
                ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "d:\Programming\The-Enigma-Cipher\src\enigma_parts.py", line 58, in rotor
        letter = rotor.wiring[letter]
                ~~~~~~~~~~~~^^^^^^^^
IndexError: list index out of range
```