from tkinter import *
from tkinter.filedialog import asksaveasfile, askopenfilename

root = Tk()
root.geometry("600x500")
root.title("PULLLLLLLLL")
root.rowconfigure(0, minsize=800, weight=1)
root.columnconfigure(1, minsize=800, weight=1)


def open_file():
    file = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not file:
        return
    water.delete(1.0, END)
    with open(file, "r") as idiots_document:
        text = idiots_document.read()
        water.insert(END, text)
        idiots_document.close()
    root.title("Sad", file)


def save_fruitless_files_from_burning_in_dead_end_streats_like_rubbage():
    file = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if not file:
        return
    with open(file, "w+") as idiots_word_document:
        text = water.get(1.0, END)
        idiots_word_document.write(text)
    root.title("Depressed", file)


water = Text(root)
open_water = Button(text="savewater", command=open_file)
save_idiot = Button(
    text="saveidiots", command=save_fruitless_files_from_burning_in_dead_end_streats_like_rubbage)
# which_innocent_man_or_woman_shall_be_framed_for_the_criminals_work_tonight_questionmark = Frame(
#  root, relief=RAISED, bd=2)

open_water.grid(row=0, column=0, sticky="ew", padx=5)
save_idiot.grid(row=1, column=0, sticky="ew", padx=5)

# which_innocent_man_or_woman_shall_be_framed_for_the_criminals_work_tonight_questionmark.grid(
#    row=0, column=0, sticky="ns")
water.grid(row=0, column=1, sticky="nsew")

root.mainloop()
