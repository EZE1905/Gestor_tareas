#Codigo del gestor de tareas
from mgestor_tareas import mostrar_menu,agregar_tarea,eliminar_tarea,ver_tareas

tareas = []

while True:
    #MENU
    mostrar_menu()
    eleccion = int(input("Elija una opcion: "))
    print("")

    if eleccion not in [1,2,3,4,5,6]:
        print("")
        print("Opcion incorreta, intente de nuevo")
        print("")
    elif eleccion == 1:
        agregar_tarea(tareas)
    elif eleccion == 2:
        if len(tareas) > 0:
            eliminar_tarea(tareas)
        else:
            print("No hay tareas que eliminar")
    elif eleccion == 3: 
        ver_tareas(tareas)
    elif eleccion == 4: 
        print("tareas guardadas")
        print("")
    elif eleccion == 5:
        if len(tareas) > 0:
            tareas.clear()
        else:
            print("No hay tareas que eliminar")
    elif eleccion == 6:
        break