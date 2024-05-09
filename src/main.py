from base import Todo
from utils import add_new_todo, delete_todo, show_all_todos, show_main_menu

def main():
  todo_list: Todo = list()

  switcher = {
    1: lambda: add_new_todo(todo_list), # DONE - recibe la lista como parametro
    # 2: mark_as_pending,
    # 3: mark_as_complete,
    4: lambda: show_all_todos(todo_list), # DONE - recibe la lista como parametro
    5: lambda: delete_todo(todo_list), # DONE - recibe la lista como parametro
    6: show_main_menu, # DONE
  }

  print('\t** Bienvenido/a **')
  show_main_menu()
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
        if option_selected in switcher:
          switcher[option_selected]()
        else:
          print('Elige un índice disponible en el menu principal')
    except ValueError as ve:
        print('ValueError: ',ve)

if __name__ == '__main__':
  main()

