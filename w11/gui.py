import tkinter as tk

def submit():
    print("Submitted")

def reset():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)

# Create window
root = tk.Tk()
root.title("Window Wizard")

# Add widgets
tk.Label(root, text="Label 1").grid(row=0)
tk.Label(root, text="Label 2").grid(row=1)
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
tk.Button(root, text="Submit", command=submit).grid(row=2, column=0)
tk.Button(root, text="Reset", command=reset).grid(row=2, column=1)

root.mainloop()
