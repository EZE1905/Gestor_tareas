#Codigo del gestor de tareas
from mgestor_tareas import mostrar_menu

tareas = []

while True:
    #MENU
    mostrar_menu()
    eleccion = int(input("Elija una opcion: "))
    print("")

    if eleccion > 6:
        print("")
        print("Opcion incorreta, intente de nuevo")
        print("")
    elif eleccion == 1:
        tarea_nueva = input("Escriba su tarea: ")
        tareas.append(tarea_nueva)
    elif eleccion == 2: 
        for indice,tarea in enumerate(tareas):
            print(f"{indice + 1}: {tarea}")
        tarea_eliminada = int(input("Indique el numero de tarea que quiere eliminar: "))
        tareas.pop(tarea_eliminada - 1)
    elif eleccion == 3: 
        print("----TAREAS----")
        for indice,tarea in enumerate(tareas):
            print(f"{indice + 1}: {tarea}")
    elif eleccion == 4: 
        print("tareas guardadas")
        print("")
    elif eleccion == 5:
        tareas.clear()
    elif eleccion == 6:
        break