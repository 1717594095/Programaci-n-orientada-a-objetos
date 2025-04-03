import tkinter as tk
from tkinter import messagebox

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas Pendientes")

        self.tasks = []

        # Campo de entrada para nuevas tareas
        self.task_entry = tk.Entry(root, width=50)
        self.task_entry.pack(pady=10)
        self.task_entry.bind("<Return>", self.add_task)

        # Botón para añadir tareas
        self.add_button = tk.Button(root, text="Añadir Tarea", command=self.add_task)
        self.add_button.pack(pady=5)

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=50, height=10)
        self.task_listbox.pack(pady=10)

        # Botón para marcar como completada
        self.complete_button = tk.Button(root, text="Marcar como Completada", command=self.complete_task)
        self.complete_button.pack(pady=5)

        # Botón para eliminar tareas
        self.delete_button = tk.Button(root, text="Eliminar Tarea", command=self.delete_task)
        self.delete_button.pack(pady=5)

        # Atajos de teclado
        self.root.bind("<Return>", self.add_task)
        self.root.bind("c", self.complete_task)
        self.root.bind("d", self.delete_task)
        self.root.bind("<Escape>", self.close_app)

    def add_task(self, event=None):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.task_entry.delete(0, tk.END)

    def complete_task(self, event=None):
        try:
            selected_index = self.task_listbox.curselection()[0]
            completed_task = self.tasks[selected_index]
            self.tasks[selected_index] = f"{completed_task} (Completada)"
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea.")

    def delete_task(self, event=None):
        try:
            selected_index = self.task_listbox.curselection()[0]
            del self.tasks[selected_index]
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

    def close_app(self, event=None):
        self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManager(root)
    root.mainloop()