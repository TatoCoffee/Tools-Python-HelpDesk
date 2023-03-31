import os
import shutil
import tkinter as tk
from tkinter import messagebox

class App:
    def __init__(self, master):
        self.master = master
        master.title("Limpieza de Archivos Temporales")

        self.label = tk.Label(master, text="Presione el botón para eliminar los archivos temporales y el historial de navegación de Chrome y Edge")
        self.label.pack(pady=10)

        self.button = tk.Button(master, text="Eliminar", command=self.cleanup)
        self.button.pack(pady=5)

        #Footer
        self.footer = tk.Label(master, text="© 2023, Todos los derechos reservados Javier Prieto [TatoCoffeeCoDeX]")
        self.footer.pack(side=tk.BOTTOM, padx=10, pady=10)
        
    def cleanup(self):
        # Elimina la carpeta Temp y su contenido
        temp_folder = os.environ['TEMP']
        try:
            shutil.rmtree(temp_folder, ignore_errors=True)
        except PermissionError:
            confirm = tk.messagebox.askyesno("Error de Permisos", f"No se pudo eliminar la carpeta {temp_folder}. ¿Desea omitir este error?")
            if not confirm:
                return

        # Elimina la carpeta de usuario Temp y su contenido
        user_temp_folder = os.environ['TMP']
        try:
            shutil.rmtree(user_temp_folder, ignore_errors=True)
        except PermissionError:
            confirm = tk.messagebox.askyesno("Error de Permisos", f"No se pudo eliminar la carpeta {user_temp_folder}. ¿Desea omitir este error?")
            if not confirm:
                return

        # Elimina el historial de Chrome
        chrome_path = os.path.join(os.environ['LOCALAPPDATA'], 'Google', 'Chrome', 'User Data', 'Default')
        history_path = os.path.join(chrome_path, 'History')
        try:
            os.remove(history_path)
        except PermissionError:
            confirm = tk.messagebox.askyesno("Error de Permisos", f"No se pudo eliminar el historial de Chrome en {history_path}. ¿Desea omitir este error?")
            if not confirm:
                return

        # Elimina el historial de Edge
        edge_path = os.path.join(os.environ['LOCALAPPDATA'], 'Microsoft', 'Edge', 'User Data', 'Default')
        history_path = os.path.join(edge_path, 'History')
        try:
            os.remove(history_path)
        except PermissionError:
            confirm = tk.messagebox.askyesno("Error de Permisos", f"No se pudo eliminar el historial de Edge en {history_path}. ¿Desea omitir este error?")
            if not confirm:
                return

        tk.messagebox.showinfo("Limpieza Finalizada", "La limpieza de archivos temporales y el historial de navegación ha finalizado exitosamente.")

root = tk.Tk()
app = App(root)
root.mainloop()
