#.PY principal para juntar el rompecabezas y almacenar los datos
import time
from os import system
from colorama import Fore, Style
from fuctions import *
import fuctions
from Sign_up_and_login import sign_up, login
import random

#Variables globales utilizadas
registros = {}
id_estudiante = 0
id_eliminados = []

#Diccionario de almacenamiento de datos de los estudiantes, separados por grados
grados = {
    "primero" : {},
    "segundo" : {},
    "tercero" : {},
    "cuarto" : {},
    "quinto" : {},
    "sexto" : {},
}


while True:
    menus.mostrar_menu_sesion()
    seleccion = menus.seleccionar_opcion_sesion()
    match seleccion:
        case 1:
            if not registros:
                    system('cls')
                    print(Fore.RED + Style.BRIGHT + "⚠️ ERROR: No hay usuarios registrados.")
                    print(Fore.RED + "Por favor, registre al menos un usuario antes de continuar.")
                    continue
            else:
                 system('cls')
                 if login(registros):
                      time.sleep(1)
                      system('cls')
                      break
                 else:
                      time.sleep(1)
                      system('cls')
                      continue
        case 2:
              system('cls')
              sign_up(registros)
              time.sleep(0.5)
              system('cls')
              print(Fore.GREEN + Style.BRIGHT + "✅ Por favor, ahora iniciar sesión.")
              print(Fore.GREEN + "Accede a tu cuenta para continuar.")
              continue
        case 3:
              system('cls')
              salida.animacion_salida()
              exit()
        case _:
            system('cls')
            print(Fore.RED + Style.BRIGHT + "⚠️ Opción inválida.")
            print(Fore.RED + "Por favor, selecciona una opción válida del menú.")

while True:
     menus.mostrar_menu()
     seleccion = menus.seleccionar_opcion_principal()
     match seleccion:
          case 1:
               system('cls')
               entradas = input(Fore.BLUE + Style.BRIGHT + f"📚 ¿Cuántos estudiantes deseas agregar? {Fore.LIGHTBLUE_EX}[Ingresar {Fore.RED}0{Fore.LIGHTBLUE_EX} si no desea agregar ningun estudiante]{Fore.BLUE}:  ").strip()
               if entradas.isdigit():
                        entradas = int(entradas)
                        for nuevo in range(entradas):
                             if id_eliminados:
                                   pass
                             else:
                                   id_estudiante += 1 #Problema: Se aumenta el ID_estudiante a pesar de haber ID elimianadas, solucionar la proxima vez
                             accion_temporal = acciones()
                             accion_temporal.selector_grado()
                             accion_temporal.nuevo_estudiante(grados, id_estudiante, id_eliminados)
                             time.sleep(2)
                             system('cls')
               else:
                    system('cls')
                    print(Fore.RED + Style.BRIGHT + "❌ Error: El valor ingresado debe ser la cantidad de estudiantes que desea agregar.")
                    print(Fore.RED + "Por favor, ingréselo de forma numérica. Ejemplo: 5")
          case 2:
                 system('cls')
                 e_registros = False #Bandera para determinar si hay o no registros
                 for grado, estudiantes_registrados in grados.items(): #Verificar si hay registros de estudiantes
                    if estudiantes_registrados:
                       accion_temporal = acciones(init=False)
                       accion_temporal.buscador_de_estudiante(grados)
                       accion_temporal.eliminar_estudiante(grados, id_eliminados)
                       e_registros = True
               
                 if not e_registros:#En caso de no haber no dejara usar la funcion, al ser e_registro falso pasa a ser verdadero y se ejecuta el print, si pasa a ser verdadero sera falso (por el 'not')
                      print(Fore.RED + Style.BRIGHT + "📋 No hay registro de estudiantes.")
          case 3:
                 system('cls')
                 e_registros = False 
                 for grado, estudiantes_registrados in grados.items():
                    if estudiantes_registrados:
                       accion_temporal = acciones(init=False)
                       accion_temporal.buscador_de_estudiante(grados)
                       accion_temporal.modificar_estudiante(grados)
                       e_registros = True
               
                 if not e_registros:
                      print(Fore.RED + Style.BRIGHT + "📋 No hay registro de estudiantes.")
                 system('cls')
                 accion_temporal = acciones(init=False)
                 accion_temporal.buscador_de_estudiante(grados)
                 accion_temporal.modificar_estudiante(grados)
          case 4:
                 system('cls')
                 e_registros = False 
                 for grado, estudiantes_registrados in grados.items():
                    if estudiantes_registrados:
                       muestra_de_estudiantes.muestra_por_grupo(grados)
                       e_registros = True
                       break
               
                 if not e_registros:
                      print(Fore.RED + Style.BRIGHT + "📋 No hay registro de estudiantes.")
          case 5:
                 system('cls')
                 e_registros = False 
                 for grado, estudiantes_registrados in grados.items():
                    if estudiantes_registrados:
                       muestra_de_estudiantes.muestra_general(grados)
                       e_registros = True
                       break
               
                 if not e_registros:
                      print(Fore.RED + Style.BRIGHT + "📋 No hay registro de estudiantes.")
          case 6:
               salida.animacion_salida()
               exit()