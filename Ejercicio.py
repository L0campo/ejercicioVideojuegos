import os
os.system('cls' if os.name == 'nt' else 'clear')

# Lista global para juegos
juegos = []

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    print("===MENU===")
    print("1.Agregar juego")
    print("2.Ver colección")
    print("3.Marcar completado")
    print("4.Estadísticas")
    print("0.salir")



def add_game():  
    print("---Agregar juego---")
    nom=input("ingrese nombre del juego: ") # Usar input() para datos
    gen=input("ingrese genero del juego: ")
    New=(nom,gen,False)# Crear tupla (nombre, genero, False)
    juegos.append(New)# Usar append() en lista
    print("el juego se ingesado con exito")


def view_games():
        print("---Tu Colección---")
        if juegos:# Usar if not para verificar lista vacía
             for i, (nombre,genero,jugado) in enumerate(juegos):# Usar for con enumerate()
              estado = "✓" if jugado else "✗"
              print(f"{i+1}: {nombre} ({genero}) [{estado}]")# Desempaquetar tupla
        else :
            print("no hay juegos")


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
                clear_screen()
                add_game()
                input("precione Enter para continuar...")
                clear_screen()

            case 2:
                clear_screen()
                view_games()
                input("precione Enter para continuar...")
                clear_screen()

            case 3:
                pass

            case 4:
                pass













    except ValueError: 
         print("erro")