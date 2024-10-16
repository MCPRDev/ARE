import time
import sys
from os import system
from colorama import Fore, Style, init, Back
init(autoreset=True)

#Diversos menu que se utilizaran a lo largo del programa, retornando un valor numero como seleccion
class menus():
    def mostrar_menu_sesion():
        print(Fore.CYAN + Style.BRIGHT + "═════════════════════════════════════════════════════")
        print(Fore.CYAN + Style.BRIGHT + "               📋 Bienvenido al A.R.E                ") #Administrador de registros escolares
        print(Fore.CYAN + Style.BRIGHT + "═════════════════════════════════════════════════════")
        print(Fore.GREEN + "1. 🟢 Iniciar sesión")
        print(Fore.YELLOW + "2. 📝 Registrarse")
        print(Fore.RED + "3. ❌ Salir")
        print(Fore.CYAN + Style.BRIGHT + "═════════════════════════════════════════════════════")
    def seleccionar_opcion_sesion():
        try:
            opcion = int(input(Fore.CYAN + "👉 Por favor, selecciona una opción (1-3): "))
            return opcion
        except ValueError:
            print(Fore.RED + "⚠️ Entrada no válida. Por favor, ingresa un número.")
            return None
    def mostrar_menu():
        print(Fore.BLUE + Style.BRIGHT + "═════════════════════════════════════════════════════")
        print(Fore.BLUE + Style.BRIGHT + "            🎓 Menú de Gestión de Estudiantes         ")
        print(Fore.BLUE + Style.BRIGHT + "═════════════════════════════════════════════════════")
        print(Fore.GREEN + "1. ➕ Agregar Estudiante")
        print(Fore.RED + "2. ➖ Eliminar Estudiante")
        print(Fore.YELLOW + "3. 📝 Modificar Estudiante")
        print(Fore.YELLOW + "4. 📚 Lista de estudiantes por grado")
        print(Fore.CYAN + "5. 🏫 Lista general de estudiantes")
        print(Fore.MAGENTA + "6. ❌ Salir")
        print(Fore.BLUE + Style.BRIGHT + "═════════════════════════════════════════════════════")
    def seleccionar_opcion_principal():
        try:
            opcion = int(input(Fore.BLUE + "👉 Por favor, selecciona una opción (1-6): "))
            return opcion
        except ValueError:
            print(Fore.RED + "⚠️ Entrada no válida. Por favor, ingresa un número.")
            return None

#Acciones que se realizaran para agregar, eliminar o modificar datos de los estudiantes
class acciones():
    def __init__(self, init=True):
        if init:
            print(Fore.YELLOW + Style.BRIGHT + "📋 Por favor, ingresa los datos del estudiante.")
            print(Fore.YELLOW + "Si no tiene alguno de los datos, escribe N/A.")
            while True:
                self.primer_nombre = input(str(Fore.BLUE + "Primer Nombre: ")).strip().capitalize()
                if self.primer_nombre.isalpha():
                    system('cls')
                    print(Fore.CYAN + Style.BRIGHT + f"Primer Nombre: {Fore.LIGHTGREEN_EX}{self.primer_nombre}") 
                    break
                else:
                    print(Fore.RED + "⚠️ Error: El primer nombre debe contener solo letras.")
                    continue
            while True:
                self.segundo_nombre = input(str(Fore.BLUE + "Segundo Nombre (si aplica, de lo contrario escribe N/A): ")).strip().capitalize()
                if self.segundo_nombre.isalpha() or self.segundo_nombre.upper() == 'N/A':
                    system('cls')
                    print(Fore.CYAN + Style.BRIGHT + f"Primer Nombre: {Fore.LIGHTGREEN_EX}{self.primer_nombre}")
                    print(Fore.CYAN + Style.BRIGHT + f"Segundo Nombre: {Fore.LIGHTGREEN_EX}{self.segundo_nombre}")
                    break
                else:
                    print(Fore.RED + "⚠️ Error: El segundo nombre debe contener solo letras o ser 'N/A'.")
                    continue
            while True:
                self.primer_apellido = input(str(Fore.BLUE + "Primer Apellido: ")).strip().capitalize()
                if self.primer_apellido.isalpha():
                    system('cls')
                    print(Fore.CYAN + Style.BRIGHT + f"Primer Nombre: {Fore.LIGHTGREEN_EX}{self.primer_nombre}")
                    print(Fore.CYAN + Style.BRIGHT + f"Segundo Nombre: {Fore.LIGHTGREEN_EX}{self.segundo_nombre}")
                    print(Fore.CYAN + Style.BRIGHT + f"Primer Apellido: {Fore.LIGHTGREEN_EX}{self.primer_apellido}")
                    break
                else:
                    print(Fore.RED + "⚠️ Error: El primer apellido debe contener solo letras.")
                    continue
            while True:
                self.segundo_apellido = input(str(Fore.BLUE + "Segundo Apellido (si aplica, de lo contrario escribe N/A): ")).strip().capitalize()
                if self.segundo_apellido.isalpha() or self.segundo_apellido.upper() == 'N/A':
                    system('cls')
                    print(Fore.CYAN + Style.BRIGHT + f"Primer Nombre: {Fore.LIGHTGREEN_EX}{self.primer_nombre}")
                    print(Fore.CYAN + Style.BRIGHT + f"Segundo Nombre: {Fore.LIGHTGREEN_EX}{self.segundo_nombre}")
                    print(Fore.CYAN + Style.BRIGHT + f"Primer Apellido: {Fore.LIGHTGREEN_EX}{self.primer_apellido}")
                    print(Fore.CYAN + Style.BRIGHT + f"Segundo Apellido: {Fore.LIGHTGREEN_EX}{self.segundo_apellido}")
                    break
                else:
                    print(Fore.RED + "⚠️ Error: El segundo apellido debe contener solo letras o ser 'N/A'.")
                    continue
            while True:
                self.edad = input(Fore.BLUE + "Edad: ").strip()
                if self.edad.isdigit():
                    self.edad = int(self.edad)
                    if self.edad < 5 or self.edad > 13:
                        print(Fore.RED + Style.BRIGHT + "⚠️ Solo se aceptan niños de mínimo 5 años y máximo 13 años en el registro de primaria.")
                        print(Fore.RED + Style.BRIGHT + "⚠️ Asegúrese de ingresar una edad válida dentro del rango permitido (El rango aceptado es de 5 a 13 años).")
                        continue
                    else:
                        break
                else:
                 print(Fore.RED + Style.BRIGHT + "⚠️ Error: La edad debe ser un número entero positivo. Por favor, intenta de nuevo.")  
                continue
            self.grado_seleccionado = None
        else:
            self.grado_seleccionado = None

    def selector_grado(self):
        while True:
            system('cls')
            print(Fore.BLUE + Style.BRIGHT + "📘 ¿Qué grado desea seleccionar para este estudiante?")
            print(Fore.GREEN + "[1] ➜ Primer Grado")
            print(Fore.GREEN + "[2] ➜ Segundo Grado")
            print(Fore.YELLOW + "[3] ➜ Tercer Grado")
            print(Fore.YELLOW + "[4] ➜ Cuarto Grado")
            print(Fore.CYAN + "[5] ➜ Quinto Grado")
            print(Fore.CYAN + "[6] ➜ Sexto Grado")
            grado = input(Fore.BLUE + "👉 Selecciona una opción (1-6): ").strip()
            if grado.isdigit():
                grado = int(grado)
                if 1 <= grado <= 6:
                    self.grado_seleccionado = int(grado)
                    self.grado_seleccionado  = ["primero", "segundo", "tercero", "cuarto", "quinto", "sexto"][self.grado_seleccionado - 1] #Se almacena en una lista para no asignar los valores por if, y solo acceder a los grados por medio de posicion
                    break
                elif grado == 0:
                    print(Fore.YELLOW + Style.BRIGHT + "🔄 Ha seleccionado 0, volviendo al menú principal...")
                    time.sleep(1)
                    system('cls')
                    break
                else:   
                    print(Fore.RED + Style.BRIGHT + "❌ Error: Debe seleccionar uno de los 6 grados disponibles.")
                    continue
            else:
                    print(Fore.RED + Style.BRIGHT + "❌ Error: Debe seleccionar uno de los 6 grados disponibles.")
                    print(Fore.RED + "Por favor, elige un número del 1 al 6 correspondiente al grado que deseas agregar al estudiante.")
                    continue   
            
    def buscador_de_estudiante(self, diccionario):
        print(Fore.BLUE + Style.BRIGHT + "🆔Si ingresa el ID: 0, no se realizara ningun cambio ")
        self.temporal_id = input(Fore.BLUE + Style.BRIGHT + "🆔 Ingresa el ID del estudiante: ").strip() #ID que se le asigna para buscar al estudiante en los diferentes diccionarios (grados)
        if self.temporal_id.isdigit():
            self.temporal_id = int(self.temporal_id)
            self.id_temporal_estudiante = f'estudiante {self.temporal_id}'
            self.estudiante_encontrado = None
            self.grado_encontrado = None
            for grado, estudiante in diccionario.items(): #Con las iteraciones de grado y estudiante buscamos en el diccionario asignado en la funcion
                if self.id_temporal_estudiante in estudiante: #Si se encuentra algun estudiante con la ID ingresada se asignara un valor a las variables anteriores que estan con NONE(sin valor)
                    self.estudiante_encontrado = estudiante[self.id_temporal_estudiante] #Se asigna la variable
                    self.grado_encontrado = grado #Se asigna el grado en el que fue encontrado
                    break
            else:
                print(Fore.RED + Style.BRIGHT + f"❌ No se ha encontrado ningún estudiante con el ID {Fore.LIGHTRED_EX}{self.temporal_id}.")
                print(Fore.RED + Style.BRIGHT + "⚠️ Regresando al menu principal.")
                time.sleep(1)
                system('cls')
        elif self.temporal_id == 0: #Por si desea salir
            print(Fore.RED + Style.BRIGHT + "⚠️ No se ha seleccionado ningún estudiante.")
            print(Fore.RED + Style.BRIGHT + "⚠️ Regresando al menu principal.")
            time.sleep(1)
            system('cls')

    def nuevo_estudiante(self, diccionario, id, eliminados): #solo se solicita el diccionario en el que se va a almacenar y una lista de las id que fueron eliminadas para asignarla
        if eliminados:
            id = eliminados.pop()
        else:
            id = id
        diccionario[self.grado_seleccionado].update({f'estudiante {id}' : {'primer_nombre' : self.primer_nombre, 
                                                                          'segundo_nombre' : self.segundo_nombre, 
                                                                          'primer_apellido' : self.primer_apellido, 
                                                                          'segundo_apellido' : self.segundo_apellido, 
                                                                          'edad' : self.edad,
                                                                          'grado' : self.grado_seleccionado,
                                                                          'id' : id}})
        print(Fore.GREEN + Style.BRIGHT + f"✅ {Fore.GREEN}Estudiante {Fore.RED}{self.primer_nombre} {self.primer_apellido} {Fore.GREEN}con edad {Fore.RED}{self.edad} {Fore.GREEN}ha sido agregado al grado {Fore.RED}{self.grado_seleccionado}{Fore.GREEN}.")
        print(Fore.CYAN + Style.BRIGHT + f"🆔 ID asignada: {Fore.RED}{id}")

    def eliminar_estudiante(self, diccionario, eliminados): 
            estudiante_encontrado = self.estudiante_encontrado
            grado_encontrado = self.grado_encontrado
            if estudiante_encontrado: #Si hay algun dato en la variable se realizara el procedimiento
                try:
                    nombre = diccionario[self.grado_encontrado][self.id_temporal_estudiante].get("primer_nombre")
                    apellido = diccionario[self.grado_encontrado][self.id_temporal_estudiante].get("primer_apellido")
                    edad = diccionario[self.grado_encontrado][self.id_temporal_estudiante].get("edad")
                    print(Fore.YELLOW + Style.BRIGHT + f"🔍 ¿Está seguro que desea eliminar del registro al estudiante {nombre} {apellido} con edad {edad} y ID de registro {self.temporal_id} ubicado en el grado {grado_encontrado}?")
                    print(Fore.YELLOW + "Una vez realizado el cambio no se podrá recuperar.")
                    print(Fore.YELLOW + "[1] - Sí")
                    print(Fore.YELLOW + "[2] - No")
                    eleccion = input(Fore.CYAN + "Por favor, elija una opción (1 o 2): ").strip()
                    if eleccion == '1':
                        eliminados.append(self.temporal_id)
                        diccionario[self.grado_encontrado].pop(self.id_temporal_estudiante)
                        #animacion de eliminado hecha por ChatGPT
                        mensaje = "Eliminando"
                        print(mensaje, end='', flush=True)
                        for _ in range(3): 
                            sys.stdout.write('.') #Escribe en la consola sin hacer salto de linea como el print()
                            sys.stdout.flush() #Lo que realiza esta parte de codigo es mostrar inmediatamente el texto en la salida de la consola
                            time.sleep(0.5) #Tiempo que tarda entre cada punto
                        system('cls') #Lo tipico de borrado al finalizar esta animacion by ChatGPT
                    elif eleccion == '2':
                        print(Fore.YELLOW + Style.BRIGHT + "🔄 No se realizará ningún cambio.")
                        print(Fore.YELLOW + "Regresando al menú principal...")
                    else:
                        print(Fore.RED + Style.BRIGHT + "❌ Valor no reconocido.")
                        print(Fore.YELLOW + "🔄 Volviendo al menú principal...")
                except KeyError: #por cualquier error que pueda haber al ingresar el id y al buscarla en el diccionario de un error de key
                    print(Fore.RED + Style.BRIGHT + f"❌ El ID {self.temporal_id} ingresado no se ha encontrado en el registro.")
                    print(Fore.YELLOW + "🔄 Regresando al menú principal...")
                    time.sleep(1)
                    system('cls')

    def modificar_estudiante(self, diccionario):
            estudiante_encontrado = self.estudiante_encontrado
            grado_encontrado = self.grado_encontrado
            if estudiante_encontrado: #Si hay algun dato en la variable se realizara el procedimiento
                try:
                    while True:
                        primer_nombre = diccionario[self.grado_encontrado][self.id_temporal_estudiante].get("primer_nombre")
                        segundo_nombre = diccionario[self.grado_encontrado][self.id_temporal_estudiante].get("segundo_nombre")
                        primer_apellido = diccionario[self.grado_encontrado][self.id_temporal_estudiante].get("primer_apellido")
                        segundo_apellido = diccionario[self.grado_encontrado][self.id_temporal_estudiante].get("segundo_apellido")
                        edad = diccionario[self.grado_encontrado][self.id_temporal_estudiante].get("edad")
                        id_asignada = self.temporal_id
                        grado_asignado = self.grado_encontrado.capitalize()
                        grado_guardado = diccionario[self.grado_encontrado][self.id_temporal_estudiante].get("grado")
                        print(Fore.CYAN + Style.BRIGHT + "Información del Estudiante")
                        print(Fore.CYAN + Style.BRIGHT + "-" * 50)
                        print(Fore.GREEN + f"Primer Nombre:    {primer_nombre}")
                        print(Fore.GREEN + f"Segundo Nombre:   {segundo_nombre}")
                        print(Fore.GREEN + f"Primer Apellido:  {primer_apellido}")
                        print(Fore.GREEN + f"Segundo Apellido: {segundo_apellido}")
                        print(Fore.GREEN + f"Edad:             {edad}")
                        print(Fore.GREEN + f"ID:               {id_asignada}")
                        print(Fore.GREEN + f"Grado:            {grado_asignado}")
                        print(Fore.CYAN + Style.BRIGHT + "-" * 50)
                        print(Fore.YELLOW + "¿Qué dato deseas modificar?")
                        print(Fore.YELLOW + "[1] Primer Nombre")
                        print(Fore.YELLOW + "[2] Segundo Nombre")
                        print(Fore.YELLOW + "[3] Primer Apellido")
                        print(Fore.YELLOW + "[4] Segundo Apellido")
                        print(Fore.YELLOW + "[5] Edad")
                        print(Fore.YELLOW + "[6] Grado")
                        print(Fore.YELLOW + "[7] Salir")
                        while True:
                            try:
                                sub_eleccion = int(input(Fore.YELLOW + Style.BRIGHT + "Ingresa una de las 7 opciones disponibles: "))
                                break
                            except ValueError:
                                print(Fore.RED + Style.BRIGHT + "❌ Valor no reconocido. Favor ingresar 1 de las 7 opciones.")
                                continue
                        match sub_eleccion: #Match-case para las diferentes opciones que nos ofreceran para modificar los datos del estudiante, a excepcion de la ID que es estatica
                            case 1:
                                while True: #while True para verificar las opciones sean correctas, hasta no obtener el resultado quierido se continuara repitiendo
                                    print(Fore.YELLOW + Style.BRIGHT + f"🔄 Usted va a modificar el primer nombre: {Fore.RED}{primer_nombre}.")
                                    actualizar_dato = str(input(Fore.CYAN + Style.BRIGHT + "Ingrese el nuevo primer nombre: ")).strip().capitalize()
                                    if actualizar_dato.isalpha():
                                        diccionario[self.grado_encontrado][self.id_temporal_estudiante]['primer_nombre'] = actualizar_dato
                                        print(Fore.GREEN + Style.BRIGHT + f"✅ El nuevo primer nombre se ha actualizado a: {Fore.RED}{actualizar_dato}.")
                                        time.sleep(0.8)
                                        system('cls')
                                        break
                                    else:
                                        print(Fore.RED + Style.BRIGHT + "❌ Error: El valor a actualizar debe estar escrito en letras. Vuelva a intentarlo.")
                                        continue
                            case 2:
                                while True:
                                    print(Fore.YELLOW + Style.BRIGHT + f"🔄 Usted va a modificar el segundo nombre {Fore.LIGHTGREEN_EX}(Escribir si no se tiene el dato N/A): {Fore.RED}{segundo_nombre}.")
                                    actualizar_dato = str(input(Fore.CYAN + Style.BRIGHT + "Ingrese el nuevo segundo nombre: ")).strip().capitalize()
                                    if actualizar_dato.isalpha() or actualizar_dato.upper() == "N/A":
                                        diccionario[self.grado_encontrado][self.id_temporal_estudiante]['segundo_nombre'] = actualizar_dato
                                        print(Fore.GREEN + Style.BRIGHT + f"✅ El nuevo segundo nombre se ha actualizado a: {Fore.RED}{actualizar_dato}.")
                                        time.sleep(0.8)
                                        system('cls')
                                        break
                                    else:
                                        print(Fore.RED + Style.BRIGHT + "❌ Error: El valor a actualizar debe estar escrito en letras. Vuelva a intentarlo.")
                                        continue
                            case 3:
                                while True:
                                    print(Fore.YELLOW + Style.BRIGHT + f"🔄 Usted va a modificar el primer apellido: {Fore.RED}{primer_apellido}.")
                                    actualizar_dato = str(input(Fore.CYAN + Style.BRIGHT + "Ingrese el nuevo primer apellido: ")).strip().capitalize()
                                    if actualizar_dato.isalpha():
                                        diccionario[self.grado_encontrado][self.id_temporal_estudiante]['primer_apellido'] = actualizar_dato
                                        print(Fore.GREEN + Style.BRIGHT + f"✅ El nuevo primer apellido se ha actualizado a: {Fore.RED}{actualizar_dato}.")
                                        time.sleep(0.8)
                                        system('cls')
                                        break
                                    else:
                                        print(Fore.RED + Style.BRIGHT + "❌ Error: El valor a actualizar debe estar escrito en letras. Vuelva a intentarlo.")
                                        continue
                            case 4:
                                while True:
                                    print(Fore.YELLOW + Style.BRIGHT + f"🔄 Usted va a modificar el segundo nombre {Fore.LIGHTGREEN_EX}(Escribir si no se tiene el dato N/A): {Fore.RED}{segundo_apellido}.")
                                    actualizar_dato = str(input(Fore.CYAN + Style.BRIGHT + "Ingrese el nuevo segundo apellido: ")).strip().capitalize()
                                    if actualizar_dato.isalpha() or actualizar_dato.upper() == "N/A":
                                        diccionario[self.grado_encontrado][self.id_temporal_estudiante]['segundo_apellido'] = actualizar_dato
                                        print(Fore.GREEN + Style.BRIGHT + f"✅ El nuevo segundo apellido se ha actualizado a: {Fore.RED}{actualizar_dato}.")
                                        time.sleep(0.8)
                                        system('cls')
                                        break
                                    else:
                                        print(Fore.RED + Style.BRIGHT + "❌ Error: El valor a actualizar debe estar escrito en letras. Vuelva a intentarlo.")
                                        continue
                            case 5:
                                while True:
                                    print(Fore.YELLOW + Style.BRIGHT + f"🔄 Usted va a modificar la edad: {Fore.RED}{edad}.")
                                    actualizar_dato = str(input(Fore.CYAN + Style.BRIGHT + "Ingrese la nueva edad: ")).strip()
                                    if actualizar_dato.isdigit():
                                        actualizar_dato = int(actualizar_dato)
                                        if actualizar_dato < 5 or actualizar_dato > 13:
                                            print(Fore.RED + Style.BRIGHT + "⚠️ Solo se aceptan niños de mínimo 5 años y máximo 13 años en el registro de primaria.")
                                            print(Fore.RED + Style.BRIGHT + "⚠️ Asegúrese de ingresar una edad válida dentro del rango permitido (El rango aceptado es de 5 a 13 años).")
                                        else:
                                            diccionario[self.grado_encontrado][self.id_temporal_estudiante]['edad'] = actualizar_dato
                                            print(Fore.GREEN + Style.BRIGHT + f"✅ La nueva edad se ha actualizado a: {Fore.RED}{actualizar_dato}.")
                                            time.sleep(0.8)
                                            system('cls')
                                            break
                                    else:
                                        print(Fore.RED + Style.BRIGHT + "❌ Error: El valor ingresado debe ser un número. Vuelva a intentarlo.")
                                        continue
                            case 6:
                                system('cls')
                                while True:
                                    print(Fore.YELLOW + Style.BRIGHT + f"🔄 Usted va a realizar un cambio de grado al estudiante: {primer_nombre} {primer_apellido} con edad {edad} y ID de registro {id_asignada}.")
                                    print(Fore.CYAN + Style.BRIGHT + "📚 ¿A qué grado le gustaría cambiar? Por favor, elija una opción:")
                                    print(Fore.GREEN + "1. Primero")
                                    print(Fore.GREEN + "2. Segundo")
                                    print(Fore.GREEN + "3. Tercero")
                                    print(Fore.GREEN + "4. Cuarto")
                                    print(Fore.GREEN + "5. Quinto")
                                    print(Fore.GREEN + "6. Sexto")
                                    print(Fore.RED + "7. Salir")
                                    nuevo_grado = input(Fore.YELLOW + Style.BRIGHT + "🔢 Ingrese una de las 7 opciones disponibles: ")
                                    if nuevo_grado.isdigit():
                                        nuevo_grado = int(nuevo_grado)
                                        if nuevo_grado == 7:
                                            print(Fore.CYAN + Style.BRIGHT + "🔙 Saliendo del cambio de grado...")
                                            time.sleep(0.5)
                                            system('cls')
                                            break
                                        nuevo_grado = ["primero", "segundo", "tercero", "cuarto", "quinto", "sexto"][nuevo_grado - 1]
                                        if nuevo_grado == grado_asignado or nuevo_grado == grado_guardado: #Si el grado es igual al grado que esta actualmente, no se puede modificar
                                            system('cls')
                                            print(Fore.RED + Style.BRIGHT + f"❌ Este estudiante ya está inscrito en {Fore.RED}{grado_asignado}.")
                                            continue
                                        else:
                                            diccionario[self.grado_encontrado][self.id_temporal_estudiante]['grado'] = nuevo_grado
                                            diccionario[nuevo_grado][self.id_temporal_estudiante] = diccionario[self.grado_encontrado].pop(self.id_temporal_estudiante)
                                            print(Fore.GREEN + Style.BRIGHT + f"✅ Se han trasladado todos los datos del estudiante al nuevo grado: {nuevo_grado} exitosamente.")
                                            time.sleep(0.5)
                                            print(Fore.CYAN + Style.BRIGHT + "🔙 Saliendo al menú principal...")
                                            time.sleep(0.5)
                                            system('cls')
                                            break
                                        break
                                    else:
                                        system('cls')
                                        print(Fore.RED + Style.BRIGHT + "❌ Valor no reconocido, selecciona 1 de las 7 opciones.")
                                        continue
                            case 7:
                                print(Fore.CYAN + Style.BRIGHT + "🔙 Saliendo al menú principal...")
                                time.sleep(0.5)
                                system('cls')
                                break
                            case _:
                                print(Fore.RED + Style.BRIGHT + "❌ Valor no reconocido, selecciona 1 de las 7 opciones.")
                                continue
                except KeyError: #Este error se ejecuta cada vez que se cambia de grado, por lo que la funcion for para buscar al estudiante por ID ya no lo reconoce el diccionario y como ya Itero 1 vez y se ejecuto una vez no lo volvera a hacer hasta ser llamada
                    print(Fore.RED + Style.BRIGHT + f"❌ El ID {self.temporal_id} se ha cambiado de grado.")
                    print(Fore.YELLOW + "🔄 Regresando al menú principal...")
                    time.sleep(1.5)
                    system('cls')

#Una animacion de salida
class salida(): 
    def animacion_salida():
        mensaje = "👋 Gracias por usar A.R.E. ¡Hasta pronto!"
        decoracion = ["🌸", "✨", "💫", "🌟", "💖", "⭐", "🌺"]

        print("\n" + Fore.CYAN + Style.BRIGHT + "Cerrando el programa...")
        for i in range(3):
            for deco in decoracion:
                sys.stdout.write(Fore.MAGENTA + Style.BRIGHT + f"\r{deco} {mensaje} {deco}")
                sys.stdout.flush()
                time.sleep(0.3) 
        print("\n" + Fore.GREEN + Style.BRIGHT + "A.R.E cerrado exitosamente. 👋")

#Muestra en pantalla los estudiantes agregados
class muestra_de_estudiantes():
    def muestra_por_grupo(diccionario):
        while True:
            try:
                print(Fore.GREEN + Style.BRIGHT + "1. Primero")
                print(Fore.GREEN + "2. Segundo")
                print(Fore.GREEN + "3. Tercero")
                print(Fore.GREEN + "4. Cuarto")
                print(Fore.GREEN + "5. Quinto")
                print(Fore.GREEN + "6. Sexto")
                print(Fore.RED + "7. Salir")
                seleccion_de_grupo = int(input(Fore.CYAN + Style.BRIGHT + "👥 Selecciona qué grupo deseas ver: "))
                system('cls')
                break
            except ValueError:
                system('cls')
                print(Fore.RED + Style.BRIGHT + "❌ Valor no reconocido. Por favor, ingresa 1 de las 7 opciones.")
                continue
        if seleccion_de_grupo == 7:
           print(Fore.YELLOW + Style.BRIGHT + "Saliendo...")
           time.sleep(0.7)
           system('cls')
           return None
        elif 1 <= seleccion_de_grupo <= 6: #Se hace una verificacion dentro del rango
            seleccion_grado = ["primero", "segundo", "tercero", "cuarto", "quinto", "sexto"][seleccion_de_grupo - 1]
            print(Back.BLUE + Fore.WHITE + Style.BRIGHT + f"{' '*5}📘 Grado: {seleccion_grado} {' '*5}")
            print(Fore.YELLOW + Style.BRIGHT + "\nDetalles del Estudiante:")
            print(Fore.GREEN + "-" * 100)
            print(Fore.CYAN + Style.BRIGHT + "{:<20} {:<20} {:<20} {:<20} {:<10} {:<10}".format("Primer Nombre", "Segundo Nombre", "Primer Apellido", "Segundo Apellido", "Edad", "ID"))
            print(Fore.GREEN + "-" * 100)
            for grado, estudiante in diccionario.items(): #Realizamos una iteracion en el diccionario global donde grado itera sobre los valores del diccionario principal y estudiante sobre los valores que estan dentro de los grados
                if grado == seleccion_grado: #Realiza la verificacion por cada iteracion para que solo se ejecute por ese grado con el que se comparo con la condicional
                    for id_estudiante, detalles in estudiante.items(): #Luego tenemos que estudiante almacena mas diccionario con datos que son los 'estudiantes {id}' donde se almacenan los datos de cada estudiantes, y detalles itera sobre esos datos que estan dentro de el ID
                        primer_nombre = detalles.get('primer_nombre') #Como detalles esta pasando sobre estos valores podemos solicitarles los diversos valores que necesitamos para mostrar
                        segundo_nombre = detalles.get('segundo_nombre')
                        primer_apellido = detalles.get('primer_apellido')
                        segundo_apellido = detalles.get('segundo_apellido')
                        edad = detalles.get('edad')
                        id_establecida = detalles.get('id')
                        print(Fore.WHITE + Style.BRIGHT + "{:<20} {:<20} {:<20} {:<20} {:<10} {:<10}".format(primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, edad, id_establecida))
            while True:
                try:
                    salida = int(input(Fore.MAGENTA + Style.BRIGHT + "🔢 Marque cualquier número para salir: "))
                    system('cls')
                    break
                except ValueError:
                    print(Fore.RED + Style.BRIGHT + "❌ Valor no reconocido. Asegúrese de que sea un número.")
                    continue
        else:
            print(Fore.RED + Style.BRIGHT + "❌ Valor no reconocido. Asegúrese de que sea un número dentro del rango (1 - 7).")
    def muestra_general(diccionario):
        print(Fore.YELLOW + Style.BRIGHT + "\nDetalles del Estudiante:")
        print(Fore.GREEN + "-" * 110)
        print(Fore.CYAN + Style.BRIGHT + "{:<20} {:<20} {:<20} {:<20} {:<10} {:<10} {:<10}".format("Primer Nombre", "Segundo Nombre", "Primer Apellido", "Segundo Apellido", "Grado", "Edad", "ID"))
        print(Fore.GREEN + "-" * 110)
        for grado, estudiante in diccionario.items():
            for id_estudiante, detalles in estudiante.items():
                primer_nombre = detalles.get('primer_nombre') #Como detalles esta pasando sobre estos valores podemos solicitarles los diversos valores que necesitamos para mostrar
                segundo_nombre = detalles.get('segundo_nombre')
                primer_apellido = detalles.get('primer_apellido')
                segundo_apellido = detalles.get('segundo_apellido')
                g_rado = detalles.get('grado')
                edad = detalles.get('edad')
                id_establecida = detalles.get('id')
                print(Fore.WHITE + Style.BRIGHT + "{:<20} {:<20} {:<20} {:<20} {:<10} {:<10} {:<10}".format(primer_nombre, segundo_nombre, primer_apellido, segundo_apellido, g_rado, edad, id_establecida))
        while True:
            try:
                salida = int(input(Fore.MAGENTA + Style.BRIGHT + "🔢 Marque cualquier número para salir: "))
                system('cls')
                break
            except ValueError:
                print(Fore.RED + Style.BRIGHT + "❌ Valor no reconocido. Asegúrese de que sea un número.")
                continue