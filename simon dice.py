import tkinter as tk
import socket

def send_command(command):
    client.send(command.encode())  # Envía el comando al servidor

def red_led():
    send_command("ROJO")

def blue_led():
    send_command("AZUL")

def yellow_led():
    send_command("AMARILLO")

def green_led():
    send_command("VERDE")

# Configuración del cliente para conectarse al servidor
HOST = '192.168.68.92'  # Dirección IP del servidor
PORT = 65432  # Puerto de comunicación

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

# Creación de la interfaz gráfica
root = tk.Tk()
root.title("Control de LEDs")

red_button = tk.Button(root, text="Rojo", command=red_led)
red_button.pack()

blue_button = tk.Button(root, text="Azul", command=blue_led)
blue_button.pack()
yellow_button = tk.Button(root, text="Amarillo", command=yellow_led)
yellow_button.pack()

green_button = tk.Button(root, text="Verde", command=green_led)
green_button.pack()

root.mainloop()