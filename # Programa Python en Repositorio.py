# Programa Python en Repositorio

import tkinter as tk

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Programa mejorado")
ventana.geometry("500x300")
ventana.configure(bg="#1e1e2f")

# Fuente moderna
fuente_titulo = ("Segoe UI", 20, "bold")
fuente_texto = ("Segoe UI", 12)

# Texto dinámico
textos = ["Bienvenido 👋", "Subiendo proyecto 🚀", "Listo para GitHub 😎"]
indice = 0

label = tk.Label(ventana, text=textos[indice], fg="white", bg="#1e1e2f", font=fuente_titulo)
label.pack(pady=40)

# Función para cambiar texto automáticamente
def cambiar_texto():
    global indice
    indice = (indice + 1) % len(textos)
    label.config(text=textos[indice])
    ventana.after(2000, cambiar_texto)

# Animación tipo fade (simulada cambiando color)
def animar_color(i=0):
    colores = ["#1e1e2f", "#2a2a40", "#35355a", "#404075"]
    ventana.configure(bg=colores[i])
    label.configure(bg=colores[i])
    ventana.after(500, lambda: animar_color((i+1) % len(colores)))

# Botón con efecto hover
def on_enter(e):
    boton.config(bg="#4CAF50")

def on_leave(e):
    boton.config(bg="#3a3a55")

boton = tk.Button(ventana, text="Iniciar", font=fuente_texto, bg="#3a3a55", fg="white", relief="flat")
boton.pack(pady=20)

boton.bind("<Enter>", on_enter)
boton.bind("<Leave>", on_leave)

# Iniciar animaciones
cambiar_texto()
animar_color()

ventana.mainloop()