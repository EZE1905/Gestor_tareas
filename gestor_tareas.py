#Codigo del gestor de tareas
from mgestor_tareas import mostrar_menu,agregar_tarea,eliminar_tarea,ver_tareas,vaciar_lista,abrir_archivo

tareas = []

with open ("txt\\lista_tareas.txt") as archivo:
    for linea in archivo:
        linea_limpia = linea.strip()
        tareas.append(linea_limpia)


while True:
    #MENU
    mostrar_menu()
    try:

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
            if len(tareas) > 0:
                ver_tareas(tareas)
            else:
                print("No hay tareas anotadas")
        elif eleccion == 4: 
            abrir_archivo()
        elif eleccion == 5:
            vaciar_lista(tareas)
        elif eleccion == 6:
            break
    except ValueError:
        print("")
        print("Ingrese una de la opciones")