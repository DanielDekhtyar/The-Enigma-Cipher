"""
This is a file describing the GUI for the Enigma cipher app created using Tkinter
"""

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Text, Button, PhotoImage, ttk
from utils.resource_path import resource_path
from src import gui_event_handlers


OUTPUT_PATH = Path(__file__).parent
path_to_assets_folder = OUTPUT_PATH / Path(resource_path(r"The-Enigma-Cipher\assets"))
ASSETS_PATH = f"{path_to_assets_folder}/frame0"


"""Return the absolute path to a file or directory relative to the assets folder."""
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1255x790")
window.configure(bg="#FFFFFF")
window.title("The Enigma Cipher")

# Set the icon of the window
window.iconbitmap(f"{path_to_assets_folder}/icon.ico")


# Create the main window of the application
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=790,
    width=1255,
    bd=0,
    highlightthickness=0,
    relief="ridge",
)

canvas.place(x=0, y=0)


"""Add texts on the screen"""
canvas.create_text(
    34.0,
    40.0,
    anchor="nw",
    text="The Enigma Cipher",
    fill="#000000",
    font=("Courier New", 48 * -1),
)

canvas.create_text(
    34.0,
    104.0,
    anchor="nw",
    text="Input Text",
    fill="#000000",
    font=("Comic Sans MS", 24 * -1),
)

canvas.create_text(
    1020.0,
    20.0,
    anchor="nw",
    text="Enigma settings",
    fill="#000000",
    font=("InriaSans Regular", 32 * -1),
)

canvas.create_text(
    34.0,
    452.0,
    anchor="nw",
    text="Output Text",
    fill="#000000",
    font=("Comic Sans MS", 24 * -1),
)

canvas.create_text(
    1082.0,
    250.0,
    anchor="nw",
    text="Plugboard",
    fill="#000000",
    font=("InriaSans LightItalic", 20 * -1),
)

canvas.create_text(
    1063.0,
    65.0,
    anchor="nw",
    text="Rotors from left to right",
    fill="#000000",
    font=("Comic Sans MS", 12 * -1, "italic"),
)

canvas.create_text(
    1050.0,
    85.0,
    anchor="nw",
    text="Number | Position | Shift",
    fill="#000000",
    font=("Comic Sans MS", 14 * -1, "italic"),
)

canvas.create_text(
    950.0,
    112.0,
    anchor="nw",
    text="First rotor",
    fill="#000000",
    font=("InriaSans Regular", 15 * -1),
)

canvas.create_text(
    950.0,
    159.0,
    anchor="nw",
    text="Second rotor",
    fill="#000000",
    font=("InriaSans Regular", 15 * -1),
)

canvas.create_text(
    950.0,
    206.0,
    anchor="nw",
    text="Third rotor",
    fill="#000000",
    font=("InriaSans Regular", 15 * -1),
)


"""Add Enigma logo"""
enigma_logo_img = PhotoImage(file=relative_to_assets("Enigma logo.png"))
enigma_logo = canvas.create_image(720.0, 64.0, image=enigma_logo_img)


"""Add the input and output boxes"""
# Input
input_text_img = PhotoImage(file=relative_to_assets("I-O text box.png"))
input_text_bg = canvas.create_image(484.5, 278.5, image=input_text_img)
input_text = Text(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
input_text.place(x=49.0, y=160.0, width=871.0, height=245.0)

# Output
output_text_img = PhotoImage(file=relative_to_assets("I-O text box.png"))
output_text_bg = canvas.create_image(484.5, 629.5, image=output_text_img)
output_text = Text(bd=0, bg="#FFFFFF", fg="#000716", highlightthickness=0)
output_text.place(x=49.0, y=510.0, width=871.0, height=245.0)


"""Add buttons"""
# Encipher text
encipher_text_img = PhotoImage(file=relative_to_assets("encipher_text_button.png"))
encipher_text_button = Button(
    image=encipher_text_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: gui_event_handlers.encipher_text(
        input_text.get("1.0", "end-1c"),
        gui_event_handlers.get_plugboard_2D_array(plugboard_inputs),
        gui_event_handlers.get_rotor_settings(
            rotor_left_number,
            rotor_left_position,
            rotor_left_shift,
            rotor_center_number,
            rotor_center_position,
            rotor_center_shift,
            rotor_right_number,
            rotor_right_position,
            rotor_right_shift,
        ),
        output_text,
    ),
    relief="flat",
)
encipher_text_button.place(
    x=800.0, y=417.0, width=135.372802734375, height=42.25373077392578
)

# Copy
copy_img = PhotoImage(file=relative_to_assets("Copy button.png"))
copy_button = Button(
    image=copy_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: gui_event_handlers.copy_text(output_text),
    relief="flat",
)
copy_button.place(x=214.0, y=449.0, width=104.13290405273438, height=39.86198043823242)

# Paste
paste_img = PhotoImage(file=relative_to_assets("Paste button.png"))
paste_button = Button(
    image=paste_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: gui_event_handlers.paste_text(input_text),
    relief="flat",
)
paste_button.place(x=214.0, y=101.0, width=104.13290405273438, height=39.86198043823242)

# Encryption waring text
canvas.create_text(
    35.0,
    415.0,
    anchor="nw",
    text="Warning : Only English characters will be enciphered. Any other characters will stay the same.",
    fill="#000000",
    font=("InriaSans Regular", 15 * -1),
)


"""Add arrows in plugboard"""
arrows_img = PhotoImage(file=relative_to_assets("arrows.png"))
arrows = canvas.create_image(1125.833740234375, 524.8312683105469, image=arrows_img)


"""Add rotors"""
# Rotor number selection
rotor_choices = ["I", "II", "III", "IV", "V"]

rotor_left_number = ttk.Combobox(window, values=rotor_choices)
rotor_left_number.place(x=1060, y=112, width=35, height=20)
rotor_left_number.set("I")  # Set the default value to 'I'

rotor_center_number = ttk.Combobox(window, values=rotor_choices)
rotor_center_number.place(x=1060, y=159, width=35, height=20)
rotor_center_number.set("II")

rotor_right_number = ttk.Combobox(window, values=rotor_choices)
rotor_right_number.place(x=1060, y=206, width=35, height=20)
rotor_right_number.set("III")

# Rotor position and shift selection
rotor_positions_and_shifts = [i + 1 for i in range(26)]

# Rotor left
rotor_left_position = ttk.Combobox(window, values=rotor_positions_and_shifts)
rotor_left_position.place(x=1120, y=112, width=35, height=20)
rotor_left_position.set(1)  # Set the default value to 1

rotor_left_shift = ttk.Combobox(window, values=rotor_positions_and_shifts)
rotor_left_shift.place(x=1182, y=112, width=35, height=20)
rotor_left_shift.set(1)

# Rotor center
rotor_center_position = ttk.Combobox(window, values=rotor_positions_and_shifts)
rotor_center_position.place(x=1120, y=159, width=35, height=20)
rotor_center_position.set(1)

rotor_center_shift = ttk.Combobox(window, values=rotor_positions_and_shifts)
rotor_center_shift.place(x=1182, y=159, width=35, height=20)
rotor_center_shift.set(1)

# Rotor right
rotor_right_position = ttk.Combobox(window, values=rotor_positions_and_shifts)
rotor_right_position.place(x=1120, y=206, width=35, height=20)
rotor_right_position.set(1)

rotor_right_shift = ttk.Combobox(window, values=rotor_positions_and_shifts)
rotor_right_shift.place(x=1182, y=206, width=35, height=20)
rotor_right_shift.set(1)


"""Add the plugboard"""
plugboard_letters = [
    " ",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]

# Pair 1
pb_1 = ttk.Combobox(window, values=plugboard_letters)
pb_1.place(x=1063, y=283, width=35, height=20)
pb_1.set(" ")  # Set the default value to 'A'

pb_2 = ttk.Combobox(window, values=plugboard_letters)
pb_2.place(x=1155, y=283, width=35, height=20)
pb_2.set(" ")

# Pair 2
pb_3 = ttk.Combobox(window, values=plugboard_letters)
pb_3.place(x=1063, y=324, width=35, height=20)
pb_3.set(" ")

pb_4 = ttk.Combobox(window, values=plugboard_letters)
pb_4.place(x=1155, y=324, width=35, height=20)
pb_4.set(" ")

# Pair 3
pb_5 = ttk.Combobox(window, values=plugboard_letters)
pb_5.place(x=1063, y=363, width=35, height=20)
pb_5.set(" ")

pb_6 = ttk.Combobox(window, values=plugboard_letters)
pb_6.place(x=1155, y=363, width=35, height=20)
pb_6.set(" ")

# Pair 4
pb_7 = ttk.Combobox(window, values=plugboard_letters)
pb_7.place(x=1063, y=400, width=35, height=20)
pb_7.set(" ")

pb_8 = ttk.Combobox(window, values=plugboard_letters)
pb_8.place(x=1155, y=400, width=35, height=20)
pb_8.set(" ")

# Pair 5
pb_9 = ttk.Combobox(window, values=plugboard_letters)
pb_9.place(x=1063, y=438, width=35, height=20)
pb_9.set(" ")

pb_10 = ttk.Combobox(window, values=plugboard_letters)
pb_10.place(x=1155, y=438, width=35, height=20)
pb_10.set(" ")

# Pair 6
pb_11 = ttk.Combobox(window, values=plugboard_letters)
pb_11.place(x=1063, y=476, width=35, height=20)
pb_11.set(" ")

pb_12 = ttk.Combobox(window, values=plugboard_letters)
pb_12.place(x=1155, y=476, width=35, height=20)
pb_12.set(" ")

# Pair 7
pb_13 = ttk.Combobox(window, values=plugboard_letters)
pb_13.place(x=1063, y=513, width=35, height=20)
pb_13.set(" ")

pb_14 = ttk.Combobox(window, values=plugboard_letters)
pb_14.place(x=1155, y=513, width=35, height=20)
pb_14.set(" ")

# Pair 8
pb_15 = ttk.Combobox(window, values=plugboard_letters)
pb_15.place(x=1063, y=551, width=35, height=20)
pb_15.set(" ")

pb_16 = ttk.Combobox(window, values=plugboard_letters)
pb_16.place(x=1155, y=551, width=35, height=20)
pb_16.set(" ")

# Pair 9
pb_17 = ttk.Combobox(window, values=plugboard_letters)
pb_17.place(x=1063, y=589, width=35, height=20)
pb_17.set(" ")

pb_18 = ttk.Combobox(window, values=plugboard_letters)
pb_18.place(x=1155, y=589, width=35, height=20)
pb_18.set(" ")

# Pair 10
pb_19 = ttk.Combobox(window, values=plugboard_letters)
pb_19.place(x=1063, y=629, width=35, height=20)
pb_19.set(" ")

pb_20 = ttk.Combobox(window, values=plugboard_letters)
pb_20.place(x=1155, y=629, width=35, height=20)
pb_20.set(" ")

# Pair 11
pb_21 = ttk.Combobox(window, values=plugboard_letters)
pb_21.place(x=1063, y=666, width=35, height=20)
pb_21.set(" ")

pb_22 = ttk.Combobox(window, values=plugboard_letters)
pb_22.place(x=1155, y=666, width=35, height=20)
pb_22.set(" ")

# Pair 12
pb_23 = ttk.Combobox(window, values=plugboard_letters)
pb_23.place(x=1063, y=705, width=35, height=20)
pb_23.set(" ")

pb_24 = ttk.Combobox(window, values=plugboard_letters)
pb_24.place(x=1155, y=705, width=35, height=20)
pb_24.set(" ")

# Pair 13
pb_25 = ttk.Combobox(window, values=plugboard_letters)
pb_25.place(x=1063, y=745, width=35, height=20)
pb_25.set(" ")

pb_26 = ttk.Combobox(window, values=plugboard_letters)
pb_26.place(x=1155, y=745, width=35, height=20)
pb_26.set(" ")


# An array of all the plugboard comboboxes
plugboard_inputs: list[ttk.Combobox] = [
    pb_1,
    pb_2,
    pb_3,
    pb_4,
    pb_5,
    pb_6,
    pb_7,
    pb_8,
    pb_9,
    pb_10,
    pb_11,
    pb_12,
    pb_13,
    pb_14,
    pb_15,
    pb_16,
    pb_17,
    pb_18,
    pb_19,
    pb_20,
    pb_21,
    pb_22,
    pb_23,
    pb_24,
    pb_25,
    pb_26,
]

window.resizable(False, False)
window.mainloop()
