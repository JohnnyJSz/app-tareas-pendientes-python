import os
from base import MenuOption, Todo
from utils import add_new_todo, modify_todo, show_all_todos, delete_todo, show_main_menu

# Función para limpiar la pantalla
def clear_screen():
  if os.name == 'nt':
    os.system('cls')  # Windows
  else:
    os.system('clear')  # Linux / macOS

def main():
  todo_list: Todo = list()

  # Diccionario de opciones usando instancias de la clase MenuOption
  menu_option_switcher = {
    1: MenuOption('* Agregar una nueva tarea', lambda: add_new_todo(todo_list)),
    2: MenuOption('* Modificar una tarea', lambda: modify_todo(todo_list)),
    3: MenuOption('* Borrar una tarea', lambda: delete_todo(todo_list)),
    4: MenuOption('* Lista de tareas', lambda: show_all_todos(todo_list)),
  }

  while True:
    # Limpiar la pantalla y mostrar el menú principal
    clear_screen()
    print('\t**** Bienvenido/a ****')
    show_main_menu(todo_list)
    try:
      option_selected = input('(Menu principal) Elige una opción: ')

      # Verificar si el valor introducido es alfanumerico y distinto de la cadena de texto 'salir'
      if option_selected.isalpha() and option_selected != 'salir':
        # Si es asi, levantamos una excepcion de tipo ValueError con un mensaje customizado
        raise ValueError(f'Valor de índice "{option_selected}" no valido. Prueba otra vez.')
      # Verificar si el valor introducido es alfanumerico e igual a la cadena de texto 'salir'
      if option_selected.isalpha() and option_selected == 'salir':
        # Si es asi, mostramos un mensaje informativo y salimos del bucle con break.
        print('Adiós!')
        break
      else:
        option_selected = int(option_selected)
        
        if option_selected in menu_option_switcher:
          selected_option = menu_option_switcher[option_selected]
          print(selected_option.get_label())
          selected_option.execute_action()
        else:
          # si el índice no esta dentro del rango de índices de la lista de opciones entonces levantamos una excepcion IndexError
          raise IndexError(f'No hay opciones con índice {option_selected}. Prueba otra vez.')
    except ValueError as ve:
      print('ValueError: ',ve)
      input("Presiona Enter para continuar...")
    except IndexError as ie:
      print('IndexError: ',ie)
      input("Presiona Enter para continuar...")
    except Exception as e:
      print('Exception: ',e)
      input("Presiona Enter para continuar...")

    # # Pausar para que el usuario pueda ver el mensaje antes de limpiar la pantalla

if __name__ == '__main__':
  main()

