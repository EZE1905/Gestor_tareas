#Funciones del gestor de tareas
def mostrar_menu():
    #MENU
    print("")
    print("----MENU----")
    print("1. Agregar Tarea")
    print("2. Eliminar Tarea")
    print("3. Ver Tareas")
    print("4. Guardar Tareas")
    print("5. Eliminar todas las Tareas")
    print("6. Salir")
    print("")

def agregar_tarea(tareas):
    tarea_nueva = input("Escriba su tarea: ")
    tareas.append(tarea_nueva)
    return tareas

def eliminar_tarea(tareas):
    for indice,tarea in enumerate(tareas):
        print(f"{indice + 1}: {tarea}")
    tarea_eliminada = int(input("Indique el numero de tarea que quiere eliminar: "))
    if tarea_eliminada > len(tareas):
        print("Tarea inexistente, intente de nuevo")
    else:
        tareas.pop(tarea_eliminada - 1)
    return tareas

def ver_tareas(tareas):
    print("----TAREAS----")
    for indice,tarea in enumerate(tareas):
        print(f"{indice + 1}: {tarea}")
    return tareas