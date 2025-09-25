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
    print("----Juegos Completados y Por Completar----")
    if juegos:
          
          for i, (nombre,genero,jugado) in enumerate(juegos):
              estado = "✓" if jugado else "✗"
              print(f"{i+1}: {nombre} ({genero}) [{estado}]")
          i=int(input("ingrese el numero del juego para marcarlo como completado: "))
          i=i-1

          if 0<= i <= len(juegos) :
              nombre,genero,jugado= juegos[i]
              juegos[i]= (nombre,genero,True)
              print(f"✅ {nombre} ha sido completado exitosamente")
            
          else :
              print("error intente de nuevo")
              complete_game()


    else :
        print("no hay juegos")

   
   
    # Usar if not para lista vacía
    # Usar >= y <= para validar índice
    # Modificar tupla en lista
    

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
                clear_screen()
                complete_game()
                input("precione Enter para continuar...")
                clear_screen()

            case 4:
                pass













    except ValueError: 
         print("erro")