from base import Todo

def main():
  todo_list: Todo = list()

  def add_new_todo(): #?DONE
    print('* Agregar una nueva tarea')
    new_todo = Todo(input('Tarea: '))
    todo_list.append(new_todo)

  def mark_as_pending(): #TODO
    print('TODO Tarea marcada como pendiente')

  def mark_as_complete(): #TODO
    print('TODO Tarea marcada como completada')

  def show_all_todos(): #?DONE
    print('* Lista de tareas')
    if len(todo_list) == 0:
      print('\tNo hay tareas')
    else:
      for index, todo in enumerate(todo_list):
        print(f'\t{index} - {todo.get_todo()} ({'completado' if todo.get_is_completed() == True else 'pendiente'})')

  def delete_todo(): #?DONE
    print('* Borrar una tarea')
    try:
      delete_todo_index = int(input('Introduce el indice de la tarea a eliminar: '))
      todo_list.remove(todo_list[delete_todo_index])
      print('La tarea se ha eliminado correctamente.')
    except ValueError:
      print('Ese indice no es correcto (No esta presente en la lista de tareas). Por favor introduce otro indice.')

  def exit(): #?DONE
    print('Salir de la aplicacion seleccionado')
    

  def show_options_menu():
    print('* Menu de opciones')
    print('''\t1 - Agregar una nueva tarea
\t2 - Marcar tarea como pendiente
\t3 - Marcar tarea como completada
\t4 - Mostrar todas las tareas
\t5 - Eliminar una tarea
\t6 - Mostrar menu de opciones
\t7 - Salir.''')

  # Cuando la app se ejecuta debo mostrar
  print('\t** Bienvenido/a **')
  option_selected = 0
  switcher = {
    1: add_new_todo,
    2: mark_as_pending,
    3: mark_as_complete,
    4: show_all_todos,
    5: delete_todo,
    6: show_options_menu,
    7: exit
  }
  show_options_menu()
  while option_selected != 7:
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

if __name__ == '__main__':
  main()

