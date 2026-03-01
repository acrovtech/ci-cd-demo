import tkinter as tk
import crud

def add_item():
    item = entry.get()
    if item:
        crud.create(item)
        entry.delete(0, tk.END)
        refresh_list()

def update_item():
    selection = listbox.curselection()
    item = entry.get()
    if selection and item:
        index = selection[0]
        crud.update(index, item)
        entry.delete(0, tk.END)
        refresh_list()

def delete_item():
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        crud.delete(index)
        refresh_list()

def refresh_list():
    listbox.delete(0, tk.END)
    for i, item in enumerate(crud.read()):
        listbox.insert(tk.END, f"{i}: {item}")

def on_select(event):
    selection = listbox.curselection()
    if selection:
        index = selection[0]
        item = crud.read()[index]
        entry.delete(0, tk.END)
        entry.insert(0, item)

root = tk.Tk()
root.title("CRUD Básico en Python CI/CD")
root.geometry("300x400")

tk.Label(root, text="Elemento:").pack(pady=5)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

add_button = tk.Button(frame_buttons, text="Agregar", command=add_item)
add_button.pack(side=tk.LEFT, padx=5)

update_button = tk.Button(frame_buttons, text="Actualizar", command=update_item)
update_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(frame_buttons, text="Eliminar", command=delete_item)
delete_button.pack(side=tk.LEFT, padx=5)

listbox = tk.Listbox(root, width=40, height=15)
listbox.pack(pady=10)
listbox.bind('<<ListboxSelect>>', on_select)

refresh_list()
root.mainloop()
