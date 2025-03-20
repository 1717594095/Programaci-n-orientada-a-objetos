import tkinter as tk
from tkinter import ttk, messagebox, Menu, scrolledtext

def agregar_tarea():
    tarea = campo_texto.get()
    if tarea:
        lista_tareas.insert(tk.END, tarea)
        campo_texto.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingresa una tarea.")

def eliminar_tarea():
    seleccion = lista_tareas.curselection()
    if seleccion:
        lista_tareas.delete(seleccion)
    else:
        messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea para eliminar.")

def mostrar_seleccion():
    seleccion = lista_tareas.get(lista_tareas.curselection())
    messagebox.showinfo("Tarea Seleccionada", f"Has seleccionado: {seleccion}")

def menu_accion():
    messagebox.showinfo("Menú", "Opción del menú seleccionada.")

root = tk.Tk()
root.title("Gestor de Tareas")
root.geometry("700x500")

# Panel para Controles de Entrada
panel_entrada = tk.Frame(root, borderwidth=2, relief="groove", bg="light grey")
panel_entrada.pack(padx=10, pady=5, fill=tk.X)

titulo_entrada = tk.Label(panel_entrada, text="Agregar Tarea", bg="light grey")
titulo_entrada.pack(side=tk.TOP, fill=tk.X)

# Campo de texto para ingresar tareas
campo_texto = tk.Entry(panel_entrada)
campo_texto.pack(side=tk.TOP, fill=tk.X, padx=5)

# Botón para agregar tarea
boton_agregar = tk.Button(panel_entrada, text="Agregar Tarea", command=agregar_tarea)
boton_agregar.pack(side=tk.TOP, padx=5, pady=5)

# Lista de tareas
lista_tareas = tk.Listbox(root, selectmode=tk.SINGLE)
lista_tareas.pack(padx=10, pady=5, fill=tk.BOTH, expand=True)

# Botón para eliminar tarea
boton_eliminar = tk.Button(root, text="Eliminar Tarea Seleccionada", command=eliminar_tarea)
boton_eliminar.pack(pady=5)

# Configuración de menú
barra_menu = Menu(root)
menu_archivo = Menu(barra_menu, tearoff=0)
menu_archivo.add_command(label="Abrir", command=menu_accion)
menu_archivo.add_command(label="Guardar", command=menu_accion)
menu_archivo.add_separator()
menu_archivo.add_command(label="Salir", command=root.quit)
barra_menu.add_cascade(label="Archivo", menu=menu_archivo)

root.config(menu=barra_menu)
root.mainloop()