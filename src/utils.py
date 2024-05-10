from base import Todo

def add_new_todo(list):
    while True:
      new_todo_input = input('\tIntroduce tu tarea (o presiona Enter para salir): ')

      # Verificar si el usuario ha presionado Enter sin texto para salir
      if new_todo_input.strip() == "":
        break

      # Crear una nueva tarea si el texto no está vacío
      new_todo = Todo(new_todo_input)
      list.append(new_todo)
      print(f'\tLa tarea [{new_todo.get_todo()}] se ha añadido correctamente.')
      show_all_todos(list)

def modify_todo(list):
  #Lo primero mostrar la lista de tareas a modificar para una mejor seleccion
  show_all_todos(list)

  # Uso un bucle con True para ejecutar el bloque las veces necesarias hasta llegar
  # a una potencial salida usando break, que se dara cuando se consiga modificar una tarea.
  while True:
    try:
      # Aqui el usuario tendra que introducir un indice de todo para modificarlo
      index_input = input('\tIntroduce el índice de la tarea a modificar (o presiona Enter para salir): ')

      # Verificar si el valor introducido es alfanumerico y distinto de la cadena de texto 'salir'
      if index_input.isalpha() and index_input != 'salir':
        # Si es asi, levantamos una excepcion de tipo ValueError con un mensaje customizado
        raise ValueError(f'Valor de índice "{index_input}" no valido. Prueba otra vez.')
      
      # Verificar si el usuario ha presionado Enter sin texto para salir
      if index_input.strip() == "":
        break
      else:
        # Convertimos el índice a un tipo integer
        list_index = int(index_input)
    
        # Verifica si el índice no esta dentro del rango de índices de la lista
        if list_index < 0 or list_index >= len(list):
          # Si es asi, levantamos una excepcion de tipo IndexError con un mensaje customizado
          raise IndexError(f'No hay tareas con índice {list_index}. Prueba otra vez.')
        
        todo = list[list_index]
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
        index_input = input('\tIntroduce el índice de la tarea a eliminar (o presiona Enter para salir): ')

        # Verificar si el valor introducido es alfanumerico y distinto de la cadena de texto 'salir'
        if index_input.isalpha() and index_input != 'salir':
          # Si es asi, levantamos una excepcion de tipo ValueError con un mensaje customizado
          raise ValueError(f'Valor de índice "{index_input}" no valido. Prueba otra vez.')
        
        # Verificar si el usuario ha presionado Enter sin texto para salir
        if index_input.strip() == "":
          break
        else:
          # Convertimos el índice a un tipo integer
          list_index = int(index_input)
      
          # Verifica si el índice no esta dentro del rango de índices de la lista
          if list_index < 0 or list_index >= len(list):
            # Si es asi, levantamos una excepcion de tipo IndexError con un mensaje customizado
            raise IndexError(f'No hay tareas con índice {list_index}. Prueba otra vez.')
          
          todo_text = list[list_index].get_todo()
          # Si el índice es correcto (existe un elemento en la lista con dicho índice), eliminarlo y salir.
          list.remove(list[list_index])
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
  print(' ** Menu de opciones **')
  if len(list) == 0:
    print('''\t[1] - Agregar una nueva tarea
    \t[salir] - Escribe "salir" para terminar el programa.''')
  else:
    print('''\t[1] - Agregar una nueva tarea
    \t[2] - Modificar una tarea
    \t[3] - Eliminar una tarea
    \t[4] - Mostrar todas las tareas
    \t[salir] - Escribe "salir" para terminar el programa.''')