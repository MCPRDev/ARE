from colorama import Fore, Style
from os import system

def sign_up(x):
    while True:
        print("\n--- Registro de Usuario ---")
        nombre = input("Nombre: ").strip().title()
        apellido = input("Apellido: ").strip().title()
        usuario = input("Usuario: ").strip()
        contrasena = input("Contraseña: ").strip()  
        if usuario in x:
            print("⚠️ El nombre de usuario ya existe. Por favor, elija otro.")
            continue
        elif len(usuario) < 5:
            print(Fore.RED + Style.BRIGHT + "❌ Error: El nombre de usuario debe tener más de 5 caracteres.")
            continue
        elif len(contrasena) < 7:
            print(Fore.RED + Style.BRIGHT + "❌ Error: La contraseña debe tener al menos 7 caracteres.")
            continue
        else:
            if nombre.isalpha() and apellido.isalpha():
                x[usuario] = {"contrasena": contrasena, "nombre": nombre, "apellido": apellido}
                print("✅ Registro exitoso.")
                break
            else: 
                print(Fore.RED + Style.BRIGHT + "❌ Error: Nombre y apellido deben ser letras.")
                print(Fore.RED + "Por favor, ingresa solo caracteres alfabéticos.")
                continue

def login(x):
    while True:
        print("\n--- Inicio de Sesión ---")
        usuario = input("Usuario: ").strip()
        contrasena = input("Contraseña: ").strip()

        if usuario in x:
            if x[usuario]["contrasena"] == contrasena:
                print(f"✅ Bienvenido {x[usuario]['nombre']} {x[usuario]['apellido']}! Inicio de sesión exitoso.")
                return True
            else:
                system('cls')
                print("❌ Contraseña incorrecta.")
                continue
        else:
            system('cls')
            print("❌ El usuario no existe. Por favor, regístrese primero.")
            break
        break