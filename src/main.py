from base import MenuOption, Todo
from utils import add_new_todo, delete_todo, show_all_todos, show_main_menu

def main():
  todo_list: Todo = list()

  # Diccionario de opciones usando instancias de la clase MenuOption
  menu_option_switcher = {
    1: MenuOption('* Agregar una nueva tarea', lambda: add_new_todo(todo_list)),
    # 2: mark_as_pending,
    # 3: mark_as_complete,
    4: MenuOption('* Lista de tareas', lambda: show_all_todos(todo_list)),
    5: MenuOption('* Borrar una tarea', lambda: delete_todo(todo_list)),
    6: MenuOption('* Menu principal', lambda: show_main_menu(todo_list)),
  }

  print('\t** Bienvenido/a **')
  show_main_menu(todo_list)
  while True:
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
          print('Elige un índice disponible en el menu principal')
    except ValueError as ve:
        print('ValueError: ',ve)

if __name__ == '__main__':
  main()

