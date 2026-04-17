#Funciones del gestor de tareas
import os
import json

def leer_tareas():
    try:
        with open ("tareas.json") as archivo:
            tareas = json.load(archivo)
    except FileNotFoundError:
        with open ("tareas.json", "w") as archivo:
            tareas = json.dump(tareas,archivo)
    return tareas

def agregar_tarea(tareas):
        print("------------------")
        print("Ponga salir para volver al menu.")
        print("")
        while True:
            tarea_nueva = input("Escriba su tarea: ")
            if tarea_nueva.lower() == "salir":
                break
            else:
                tareas.append(tarea_nueva)
                with open ("txt\\lista_tareas.txt","a") as archivo:
                    archivo.write(f"{tarea_nueva}\n")
                    print("TAREA AGREGADA CORRECTAMENTE.")
                    print("")


def eliminar_tarea(tareas):
    for indice,tarea in enumerate(tareas):
        print(f"{indice + 1}: {tarea}")
    while True:
        try:
            print("")
            tarea_eliminada = int(input("Indique el numero de tarea que quiere eliminar: "))
            if 1 <= tarea_eliminada <= len(tareas):
                eliminacion = tareas.pop(tarea_eliminada - 1)
                with open ("txt\\lista_tareas.txt", "w") as archivo:
                    for linea in tareas:
                        archivo.write(f"{linea}\n")
                print(f"Tarea eliminada: {eliminacion}")
                break
            else:
                print("")
                print("Tarea inexistente, intente de nuevo.")
        except ValueError:
            print("")
            print("ingrese el numero de la tarea que desea eliminar.")

def vaciar_lista(tareas):
    if len(tareas) > 0:
        tareas.clear()
        print("SE ELIMINARON TODAS LAS TAREAS CORRECTAMENTE")
    else:
        print("No hay tareas que eliminar")
    with open ("txt\\lista_tareas.txt", "w") as archivo:
        archivo.writelines(tareas)

def abrir_archivo():
    try:
        os.startfile("txt\\lista_tareas.txt")    
    except Exception:
        print("Archivo inexistente")

def ver_tareas(tareas):
    print("----TAREAS----")
    for indice,tarea in enumerate(tareas):
        print(f"{indice + 1}: {tarea}")
    return tareas