from base import Todo

def main():
  todo_list = list()

  def add_new_todo():
    print('Añadir una nueva tarea seleccionado')
    new_todo_text = input('Tarea: ')
    new_todo = {
      'text': new_todo_text,
      'is_completed': False
    }
    todo_list.append(new_todo)

  def show_all_todos():
    print('* Lista de tareas')
    if len(todo_list) == 0:
      print('\tNo hay tareas')
    else:
      for index, todo in enumerate(todo_list):
        print(f'\t{index} - {todo['text']} ({'completed' if todo['is_completed'] == True else 'not completed'})')

  def delete_todo():
    print('Borrar una tarea seleccionado')
    try:
      delete_todo_index = int(input('Introduce el indice de la tarea a eliminar: '))
      todo_list.remove(todo_list[delete_todo_index])
      print('La tarea se ha eliminado correctamente.')
    except ValueError:
      print('Ese indice no es correcto (No esta presente en la lista de tareas). Por favor introduce otro indice.')

  def exit():
    print('Salir de la aplicacion seleccionado')
    

  def show_options_menu():
    print('* Menu de opciones')
    print('''\t1 - Agregar una nueva tarea
\t2 - Mostrar todas las tareas
\t3 - Eliminar una tarea
\t4 - Mostrar menu de opciones
\t5 - Salir.''')

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

