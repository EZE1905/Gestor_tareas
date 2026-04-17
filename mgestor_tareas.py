#Funciones del gestor de tareas
import json

def leer_tareas():
    try:
        with open ("tareas.json") as archivo:
            tareas = json.load(archivo)
    except FileNotFoundError:
        with open ("tareas.json", "w") as archivo:
            tareas = json.dump(tareas,archivo)
    return tareas

def agregar_tarea(tareas,tarea):
            tareas.append(tarea)
            with open ("tareas.json", "w") as archivo:
                json.dump(tareas,archivo,indent=4) 


def eliminar_tarea(tareas,indice):
    tareas.pop(indice)
    with open ("tareas.json", "w") as archivo:
        json.dump(tareas,archivo,indent=4) 
    return tareas