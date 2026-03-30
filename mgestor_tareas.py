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
        print("------------------")
        print("Ponga salir para volver al menu.")
        print("")
        while True:
            tarea_nueva = input("Escriba su tarea: ")
            if tarea_nueva.lower() == "salir":
                break
            else:
                tareas.append(tarea_nueva)
                print("TAREA AGREGADA CORRECTAMENTE")
        return tareas

def eliminar_tarea(tareas):
    for indice,tarea in enumerate(tareas):
        print(f"{indice + 1}: {tarea}")
    while True:
        try:
            print("")
            tarea_eliminada = int(input("Indique el numero de tarea que quiere eliminar: "))
            if 1 <= tarea_eliminada <= len(tareas):
                tareas.pop(tarea_eliminada - 1)
                break
            else:
                print("")
                print("Tarea inexistente, intente de nuevo")
        except:
            print("")
            print("ingrese el numero de la tarea que desea eliminar")
    return tareas

def ver_tareas(tareas):
    print("----TAREAS----")
    for indice,tarea in enumerate(tareas):
        print(f"{indice + 1}: {tarea}")
    return tareas