from base import Todo

def add_new_todo(list):
    new_todo = Todo(input('\tIntroduce tu tarea: '))
    list.append(new_todo)
    print(f'\tLa tarea [{new_todo.get_todo()}] se ha añadido correctamente.')

def modify_todo(list):
  #Lo primero mostrar la lista de tareas a modificar para una mejor seleccion
  show_all_todos(list)

  # Uso un bucle con True para ejecutar el bloque las veces necesarias hasta llegar
  # a una potencial salida usando break, que se dara cuando se consiga modificar una tarea.
  while True:
    try:
      # Aqui el usuario tendra que introducir un indice de todo para modificarlo
      index = index = input('\tIntroduce el índice de la tarea a modificar o escribre "salir" para volver al menu principal: ')

      # Verificar si el valor introducido es alfanumerico y distinto de la cadena de texto 'salir'
      if index.isalpha() and index != 'salir':
        # Si es asi, levantamos una excepcion de tipo ValueError con un mensaje customizado
        raise ValueError(f'Valor de índice "{index}" no valido. Prueba otra vez.')
      
      # Verificar si el valor introducido es alfanumerico e igual a la cadena de texto 'salir'
      if index.isalpha() and index == 'salir':
        # Si es asi, mostramos un mensaje informativo y salimos del bucle con break.
        print('\tVolviendo al menu principal\n')
        break
      else:
        # Convertimos el índice a un tipo integer
        index = int(index)
    
        # Verifica si el índice no esta dentro del rango de índices de la lista
        if index < 0 or index >= len(list):
          # Si es asi, levantamos una excepcion de tipo IndexError con un mensaje customizado
          raise IndexError(f'No hay tareas con índice {index}. Prueba otra vez.')
        
        todo = list[index]
        todo.set_is_completed(not(todo.get_is_completed()))

        print(f'\tLa tarea [{todo.get_todo()}] se ha actualizado a [{todo.get_is_completed_text()}] correctamente.')
        show_all_todos(list)
    except ValueError as ve:
      print('\tValueError: ',ve)
    except IndexError as ie:
      print('\tIndexError: ',ie)
    except Exception as e:
      print('\tException: ',e)

def delete_todo(list):
    show_all_todos(list)
    # Uso un bucle con True para ejecutar el bloque las veces necesarias hasta llegar
    # a una potencial salida usando break, que se dara cuando se consiga borrar una tarea.
    while True:
      try:
        index = input('\tIntroduce el índice de la tarea a eliminar o escribre "salir" para volver al menu principal: ')

        # Verificar si el valor introducido es alfanumerico y distinto de la cadena de texto 'salir'
        if index.isalpha() and index != 'salir':
          # Si es asi, levantamos una excepcion de tipo ValueError con un mensaje customizado
          raise ValueError(f'Valor de índice "{index}" no valido. Prueba otra vez.')
        
        # Verificar si el valor introducido es alfanumerico e igual a la cadena de texto 'salir'
        if index.isalpha() and index == 'salir':
          # Si es asi, mostramos un mensaje informativo y salimos del bucle con break.
          print('\tVolviendo al menu principal\n')
          break
        else:
          # Convertimos el índice a un tipo integer
          index = int(index)
      
          # Verifica si el índice no esta dentro del rango de índices de la lista
          if index < 0 or index >= len(list):
            # Si es asi, levantamos una excepcion de tipo IndexError con un mensaje customizado
            raise IndexError(f'No hay tareas con índice {index}. Prueba otra vez.')
          
          todo_text = list[index].get_todo()
          # Si el índice es correcto (existe un elemento en la lista con dicho índice), eliminarlo y salir.
          list.remove(list[index])
          print(f'\tLa tarea [{todo_text}] se ha eliminado correctamente.')
          show_all_todos(list)
      except ValueError as ve:
        print('\tValueError: ',ve)
      except IndexError as ie:
        print('\tIndexError: ',ie)
      except Exception as e:
        print('\tException: ',e)

def show_all_todos(list):
  if len(list) == 0:
    print('\tNo hay tareas')
  else:
    for index, todo in enumerate(list):
      print(f'\t[{index}] {todo.get_todo()} - id({todo.get_id()}) - ({'completado' if todo.get_is_completed() == True else 'pendiente'})')
      
def show_main_menu(list):
  if len(list) == 0:
    print('''\t[1] - Agregar una nueva tarea
    \t[5] - Mostrar el menu principal
    \t[salir] - Escribe "salir" para terminar el programa.''')
  else:
    print('''\t[1] - Agregar una nueva tarea
    \t[2] - Modificar una tarea
    \t[3] - Mostrar todas las tareas
    \t[4] - Eliminar una tarea
    \t[5] - Mostrar el menu principal
    \t[salir] - Escribe "salir" para terminar el programa.''')