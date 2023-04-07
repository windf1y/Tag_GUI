import tkinter as tk

def clear_selection():
    lb.selection_clear(0, tk.END)

root = tk.Tk()

lb = tk.Listbox(root)
lb.pack()

for item in range(10):
    lb.insert(tk.END, f"Item {item}")

button = tk.Button(root, text="Clear selection", command=clear_selection)
button.pack()

root.mainloop()
