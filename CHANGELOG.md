# The Enigma Cipher

## 📝 Changelog:

> ### Last Version : 0.2.1
>
> ### Last Update : 30-01-2024
>
> _Date format DD-MM-YYYY_


### 🗓️ _Version 0.2.1 - 30-01-2024 (latest commit)_

---

#### 🛠️ Fixed
- The bug mentioned in the commit of v0.2.0, when the rotors don't turn the way they should, was fixed.  
It was fixed by adding a boolean that tracks if the first rotor is currently at it's notch position.  
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