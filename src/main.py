import os
from base import MenuOption, TodoManager
from base import ROJO, VERDE, AMARILLO, AZUL, BOLD, ITALIC, RESET

# Función para limpiar la pantalla
def clear_screen():
  if os.name == 'nt':
    os.system('cls')  # Windows
  else:
    os.system('clear')  # Linux / macOS

def show_welcome_message():
  print(f'{RESET}*' * 65)
  print(''.ljust(25)+f'{AZUL}{BOLD}Gestor de Tareas{RESET}'+''.rjust(25))
  print('*' * 65 + '\n')

def main():
  todo_manager = TodoManager()

  # Diccionario de opciones usando instancias de la clase MenuOption
  menu_option_switcher = {
    1: MenuOption('Agregar una nueva tarea', todo_manager.add_new_todo),
    2: MenuOption('Modificar una tarea', todo_manager.modify_todo),
    3: MenuOption('Borrar una tarea', todo_manager.delete_todo),
    4: MenuOption('Lista de tareas', lambda: todo_manager.show_all_todos(True))
  }

  while True:
    # Limpiar la pantalla y mostrar el menú principal
    clear_screen()

    show_welcome_message()

    print(f'{VERDE}-- {ITALIC}Menu de opciones --{RESET}')

    available_options = [1]  # La opción de agregar siempre está disponible
    if len(todo_manager.todo_list) > 0:
      available_options.extend([2,3,4])
      print(f'''
      \t{AMARILLO}[1]{RESET} - Agregar una nueva tarea
      \t{AMARILLO}[2]{RESET} - Modificar una tarea
      \t{AMARILLO}[3]{RESET} - Eliminar una tarea
      \t{AMARILLO}[4]{RESET} - Mostrar todas las tareas
      \t{AMARILLO}[salir]{RESET} - Escribe {AMARILLO}salir{RESET} para terminar el programa.
      ''')
    else:
      print(f'''
      \t{AMARILLO}[1]{RESET} - Agregar una nueva tarea
      \t{AMARILLO}[salir]{RESET} - Escribe {AMARILLO}salir{RESET} para terminar el programa.
      ''')

    try:
      option_selected = input(f'(Menu principal) Elige una opción: {AMARILLO}').strip().lower()

      # Verificar si el valor introducido es alfanumerico y distinto de la cadena de texto 'salir'
      if option_selected.isalpha() and option_selected != 'salir':
        # Si es asi, levantamos una excepcion de tipo ValueError con un mensaje customizado
        raise ValueError(f'Valor de índice "{option_selected}" no valido. Prueba otra vez.')
      # Verificar si el valor introducido es alfanumerico e igual a la cadena de texto 'salir'
      if option_selected.isalpha() and option_selected == 'salir':
        # Si es asi, mostramos un mensaje informativo y salimos del bucle con break.
        print(F'\n{RESET}{AZUL}-- Programa finalizado{RESET} ' + f'{AZUL}-{RESET}' * 43 + '\n')
        break
      else:
        option_selected = int(option_selected)
        
        if option_selected in available_options:
          selected_option = menu_option_switcher[option_selected]
          print(f'{selected_option.get_label()}\n')
          selected_option.execute_action()
        else:
          # si el índice no esta dentro del rango de índices de la lista de opciones entonces levantamos una excepcion IndexError
          raise IndexError(f'No hay opciones con índice {option_selected}. Prueba otra vez.')
    except ValueError as ve:
      print(f'{ROJO}ValueError: {ve}{RESET}')
      input(f'Presiona {AMARILLO}Enter{RESET} para continuar.')
    except IndexError as ie:
      print(f'{ROJO}IndexError: {ie}{RESET}')
      input(f'Presiona {AMARILLO}Enter{RESET} para continuar.')
    except Exception as e:
      print(f'{ROJO}Exception: {e}{RESET}')
      input(f'Presiona {AMARILLO}Enter{RESET} para continuar.')

if __name__ == '__main__':
  main()

