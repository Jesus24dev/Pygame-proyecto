import tkinter as tk
from tkinter import messagebox
import sys, os
from utils import carpetas

def submit():
    global player_name, selected_color
    player_name = entry_name.get()
    selected_color = color_var.get()
    if player_name.strip() == "":
        messagebox.showerror("Error", "Por favor, ingrese un nombre.")
    else:
        root.destroy()

def validate_name():
    if entry_name.get().strip() == "":
        messagebox.showerror("Error", "Por favor, ingrese un nombre.")

def on_closing():
    if messagebox.askokcancel("Salir", "¿Está seguro que desea salir?"):
        sys.exit()

root = tk.Tk()
root.title("FLAT WORLD - Datos")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 400
window_height = 300
x_position = (screen_width - window_width) // 2
y_position = (screen_height - window_height) // 2

root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

root.protocol("WM_DELETE_WINDOW", on_closing)

root.resizable(False, False)

player_name = ""
selected_color = ""

background_image = tk.PhotoImage(file=os.path.join(carpetas.FONDO, 'login.png'))
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

tk.Label(root, text="Nombre:").pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack(pady=5)

tk.Label(root, text="Seleccione un color").pack(pady=5)
colors = ["amarillo", "rojo", "verde", "azul"]
color_var = tk.StringVar(root)
color_var.set(colors[0])
color_menu = tk.OptionMenu(root, color_var, *colors)
color_menu.pack(pady=5)

submit_button = tk.Button(root, text="Aceptar", command=submit)
submit_button.pack(pady=5)

root.mainloop()



