# The Enigma Cipher

## 📝 Changelog:

> ### Last Version : 0.1.0
>
> ### Last Update : 27-01-2024
>
> _Date format DD-MM-YYYY_


### 🗓️ _Version 0.1.0 - 27-01-2024 (latest commit)_

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
- The enciphering process should be check for correctness.
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