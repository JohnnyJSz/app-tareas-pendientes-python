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
    # Uso un bucle con True para ejecutar el bloque las veces necesarias hasta llegar
    # a una potencial salida usando break, que se dara cuando se consiga borrar una tarea.
    while True:
      try:
        delete_todo_index = input('\tIntroduce el indice de la tarea a eliminar o escribre "salir" para volver al menu: ')
        # Verificar si el valor introducido es alfanumerico y distinto de la cadena de texto 'salir'
        if delete_todo_index.isalpha() and delete_todo_index != 'salir':
          # Si es asi, levantamos una excepcion de tipo ValueError con un mensaje customizado
          raise ValueError(f'Valor de indice "{delete_todo_index}" no valido. Prueba otra vez.')
        # Verificar si el valor introducido es alfanumerico e igual a la cadena de texto 'salir'
        if delete_todo_index.isalpha() and delete_todo_index == 'salir':
          # Si es asi, mostramos un mensaje informativo y salimos del bucle con break.
          print('\tVolviendo al menu principal')
          break
        else:
          # Si no, ejecutamos nuestra logica

          # Convertimos el indice a un tipo integer
          delete_todo_index = int(delete_todo_index)
      
          # Verifica si el indice no esta dentro del rango de indices de la lista
          if delete_todo_index < 0 or delete_todo_index >= len(todo_list):
            # Si es asi, levantamos una excepcion de tipo IndexError con un mensaje customizado
            raise IndexError(f'No hay tareas con indice {delete_todo_index}. Prueba otra vez.')
          
          # Si el indice es correcto (existe un elemento en la lista con dicho indice), eliminarlo y salir.
          todo_list.remove(todo_list[delete_todo_index])
          print('\tLa tarea se ha eliminado correctamente.')
          break
      except ValueError as ve:
        print('\tValueError: ',ve)
      except IndexError as ie:
        print('\tIndexError: ',ie)
      except Exception as e:
        print('\tException: ',e)

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
      option_selected = int(input('(Menu Principal) Elige una opcion: '))
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

