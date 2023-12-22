import tkinter as tk
import win32api
import win32con

# Configuración de Alto Rendimiento
def alto_rendimiento():
    win32api.SetSystemPowerState(None, win32con.POWER_STATE_MAXIMUM_PERFORMANCE)
    win32api.SetProcessPriorityBoost(win32api.GetCurrentProcess(), 1)

# Configuración de Alta Calidad
def alta_calidad():
    win32api.SetSystemPowerState(None, win32con.POWER_STATE_MAXIMIZE_EFFICIENCY)
    win32api.SetProcessPriorityBoost(win32api.GetCurrentProcess(), 0)

# Configuración Equilibrada
def equilibrado():
    win32api.SetSystemPowerState(None, win32con.POWER_STATE_BALANCED)
    win32api.SetProcessPriorityBoost(win32api.GetCurrentProcess(), 0)

# Crear ventana de la aplicación
app = tk.Tk()
app.title("Configuración de Rendimiento")
app.geometry("300x200")

# Crear botones de configuración de rendimiento
btn_alto_rendimiento = tk.Button(app, text="Alto Rendimiento", command=alto_rendimiento)
btn_alto_rendimiento.pack(pady=10)

btn_alta_calidad = tk.Button(app, text="Alta Calidad", command=alta_calidad)
btn_alta_calidad.pack(pady=10)

btn_equilibrado = tk.Button(app, text="Equilibrado", command=equilibrado)
btn_equilibrado.pack(pady=10)

# Crear footer
footer = tk.Frame(app, height=31)
footer.pack(side=tk.BOTTOM, fill=tk.X)

# Crear etiqueta en el footer
etiqueta = tk.Label(footer, text="© 2023, Todos los derechos reservados [TatoCoffeeCoDeX]", font=("Arial", 8))
etiqueta.pack(side=tk.RIGHT, padx=5, pady=5)

# Ejecutar ventana de la aplicación
app.mainloop()
