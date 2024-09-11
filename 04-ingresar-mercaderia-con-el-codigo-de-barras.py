import cv2
from pyzbar.pyzbar import decode
from tkinter import *
from tkinter import messagebox

# Definir la lista de mercadería
mercaderia = {}

# Función para escanear código de barras


def escanear_codigo():
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        for barcode in decode(frame):
            codigo = barcode.data.decode('utf-8')
            cap.release()
            cv2.destroyAllWindows()
            return codigo
        cv2.imshow('Escanear Código de Barras', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()

# Función para agregar productos


def agregar_producto():
    codigo = escanear_codigo()
    nombre = input("Ingresa el nombre del producto: ")
    cantidad = int(input("Ingresa la cantidad del producto: "))
    precio = float(input("Ingresa el precio del producto: "))
    if codigo in mercaderia:
        mercaderia[codigo]['cantidad'] += cantidad
    else:
        mercaderia[codigo] = {'nombre': nombre,
                              'cantidad': cantidad, 'precio': precio}
    print(f"Producto {nombre} agregado. Cantidad actual: {
          mercaderia[codigo]['cantidad']}")

# Función para vender productos


def vender_producto():
    codigo = escanear_codigo()
    cantidad = int(input("Ingresa la cantidad a vender: "))
    if codigo in mercaderia and mercaderia[codigo]['cantidad'] >= cantidad:
        mercaderia[codigo]['cantidad'] -= cantidad
        total_venta = cantidad * mercaderia[codigo]['precio']
        print(f"Producto {mercaderia[codigo]['nombre']} vendido. Cantidad restante: {
              mercaderia[codigo]['cantidad']}. Total de la venta: ${total_venta:.2f}")
        if mercaderia[codigo]['cantidad'] == 0:
            del mercaderia[codigo]
    else:
        print(f"No hay suficiente {mercaderia[codigo]['nombre']} para vender.")

# Función para mostrar la lista de mercadería


def mostrar_mercaderia():
    if mercaderia:
        print("Lista de mercadería:")
        for codigo, detalles in mercaderia.items():
            print(f"{detalles['nombre']}: Cantidad: {
                  detalles['cantidad']}, Precio: ${detalles['precio']:.2f}")
    else:
        print("No hay productos en la lista de mercadería.")

# Función principal


def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Agregar producto")
        print("2. Vender producto")
        print("3. Mostrar mercadería")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            agregar_producto()
        elif opcion == "2":
            vender_producto()
        elif opcion == "3":
            mostrar_mercaderia()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Inténtalo nuevamente.")


# Ejecutar el programa
menu()
