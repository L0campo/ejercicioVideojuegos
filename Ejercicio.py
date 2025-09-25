import os
os.system("clear")

# Lista global para juegos
juegos = []

def clear_screen():
    os.system("clear")


def menu():
    print("===MENU===")
    print("1.Agregar juego")
    print("2.Ver colección")
    print("3.Marcar completado")
    print("4.Estadísticas")
    print("0.salir")


# Usar input() y return
def add_game():
    global juegos  
    nom=input("ingrese nombre del juego: ") # Usar input() para datos
    gen=input("ingrese genero del juego: ")
    New=(nom,gen,False)# Crear tupla (nombre, genero, False)
    juegos.append(New)# Usar append() en lista



    pass

def view_games():
    if juegos > 0:
        print("\nLista numerada:")
        contador = 1
        for juegos in juegos:
            print(f"{contador}. {juegos}")
            contador += 1
    # Usar if not para verificar lista vacía
    # Usar for con enumerate()
    # Desempaquetar tupla
    pass

def complete_game():
    # Usar if not para lista vacía
    # Usar >= y <= para validar índice
    # Modificar tupla en lista
    pass

def show_stats():
    # Usar for para contar
    # Operadores aritméticos
    pass

def main():
    # Usar while con booleano
    # Usar if/elif/else para opciones
    pass



isActive= True
while isActive:
    menu()
    try: 
        opcion=int(input("digite una opcion del 0-4: "))
        match opcion:

            case 0:

                isActive=False

            case 1:
                pass

            case 2:
                pass

            case 3:
                pass

            case 4:
                pass













    except ValueError: 
         print("erro")