from base import Todo

def main():
  todo_list = list()

  def add_new_todo():
    print('Añadir una nueva tarea seleccionado')

  def show_all_todos():
    print('* Lista de tareas')
    if len(todo_list) == 0:
      print('\tNo hay tareas')
    else:
      print('Alguna tarea hay - todo')

  def delete_todo():
    print('Borrar una tarea seleccionado')

  def exit():
    print('Salir de la aplicacion seleccionado')
    

  def show_options_menu():
    print('* Menu de opciones')
    print('''
\t1 - Agregar una nueva tarea
\t2 - Mostrar todas las tareas
\t3 - Eliminar una tarea
\t4 - Mostrar menu de opciones
\t5 - Salir.
''')

  # Cuando la app se ejecuta debo mostrar
  print('\t** Bienvenido/a **')
  option_selected = 0
  switcher = {
    1: add_new_todo,
    2: show_all_todos,
    3: delete_todo,
    4: show_options_menu,
    5: exit
  }
  show_options_menu()
  while option_selected != 5:
    try:
      option_selected = int(input('Elige una opcion: '))
      if option_selected in switcher:
        switcher[option_selected]()
      else:
        print('Elige una opcion disponible del menu de opciones')
    except ValueError:
      print('Entrada no valida, por favor introduce un numero.')
  else:
    print('Hasta pronto!')

  """ 
  Esto funciona correctamente, lo comento para usar luego

  todo1 = Todo('Pasear al perro')
  todo1.show_todo()
  print(todo1.is_completed)

  todo2 = Todo('Revisar el correo', True)
  todo2.show_todo()
  print(todo2.is_completed) 
  """

if __name__ == '__main__':
  main()

