# Codigos de colores ANSI
ROJO = '\033[91m'
VERDE = '\033[92m'
AMARILLO = '\033[93m'
AZUL = '\033[94m'

# Codigos de formateo de texto ANSI
BOLD = '\033[1m'
ITALIC = '\033[3m'

# Codigo de reset ANSI
RESET = "\033[0m"

class MenuOption:
  def __init__(self, label, action) -> None:
    self.label = f'{RESET}{VERDE}\n-- {ITALIC}{label} --{RESET}'
    self.action = action
  
  def get_label(self):
    return self.label
  
  def execute_action(self):
    self.action()

class TodoManager:
  def __init__(self) -> None:
    self.todo_list = list()
  
  def add_new_todo(self):
    while True:
      new_todo_input = input(f'\tIntroduce tu tarea (o presiona {AMARILLO}Enter{RESET} para salir): {AZUL}')

      # Verificar si el usuario ha presionado Enter sin texto para salir
      if new_todo_input.strip() == "":
        break

      # Crear una nueva tarea si el texto no está vacío
      new_todo = Todo(new_todo_input)
      self.todo_list.append(new_todo)
      print(f'\t{VERDE}La tarea [{new_todo.get_todo()}] se ha añadido correctamente.{RESET}\n')

  def modify_todo(self):
    #Lo primero mostrar la lista de tareas a modificar para una mejor seleccion
    self.show_all_todos()

    # Uso un bucle con True para ejecutar el bloque las veces necesarias hasta llegar
    # a una potencial salida usando break, que se dara cuando se consiga modificar una tarea.
    while True:
      try:
        # Aqui el usuario tendra que introducir un indice de todo para modificarlo
        index_input = input(f'\n\tIntroduce el índice de la tarea a modificar (o presiona {AMARILLO}Enter{RESET} para salir): {AMARILLO}')

        # Verificar si el valor introducido es alfanumerico y distinto de la cadena de texto 'salir'
        if index_input.isalpha():
          # Si es asi, levantamos una excepcion de tipo ValueError con un mensaje customizado
          raise ValueError(f'Valor de índice "{index_input}" no valido. Prueba otra vez.')
        
        # Verificar si el usuario ha presionado Enter sin texto para salir
        if index_input.strip() == "":
          break
        else:
          # Convertimos el índice a un tipo integer
          list_index = int(index_input)
      
          # Verifica si el índice no esta dentro del rango de índices de la lista
          if list_index < 0 or list_index >= len(self.todo_list):
            # Si es asi, levantamos una excepcion de tipo IndexError con un mensaje customizado
            raise IndexError(f'No hay tareas con índice {list_index}. Prueba otra vez.')
          
          todo = self.todo_list[list_index]
          todo.set_is_completed(not(todo.get_is_completed()))

          print(f'\t{VERDE}La tarea [{todo.get_todo()}] se ha actualizado a [{todo.get_is_completed_text()}] correctamente.{RESET}\n')
          self.show_all_todos()
      except ValueError as ve:
        print(f'\t{ROJO}ValueError: {ve}{RESET}')
      except IndexError as ie:
        print(f'\t{ROJO}IndexError: {ie}{RESET}')
      except Exception as e:
        print(f'\t{ROJO}Exception: {e}{RESET}')

  def delete_todo(self):
    self.show_all_todos()
    # Uso un bucle con True para ejecutar el bloque las veces necesarias hasta llegar
    # a una potencial salida usando break, que se dara cuando se consiga borrar una tarea.
    while True:
      try:
        index_input = input(f'\n\tIntroduce el índice de la tarea a eliminar (o presiona {AMARILLO}Enter{RESET} para salir): {AMARILLO}')

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
          if list_index < 0 or list_index >= len(self.todo_list):
            # Si es asi, levantamos una excepcion de tipo IndexError con un mensaje customizado
            raise IndexError(f'No hay tareas con índice {list_index}. Prueba otra vez.')
          
          todo_text = self.todo_list[list_index].get_todo()
          # Si el índice es correcto (existe un elemento en la lista con dicho índice), eliminarlo y salir.
          self.todo_list.remove(self.todo_list[list_index])
          print(f'\t{VERDE}La tarea [{todo_text}] se ha eliminado correctamente.{RESET}\n')
          self.show_all_todos()
      except ValueError as ve:
        print(f'\t{ROJO}ValueError: {ve}{RESET}')
      except IndexError as ie:
        print(f'\t{ROJO}IndexError: {ie}{RESET}')
      except Exception as e:
        print(f'\t{ROJO}Exception: {e}{RESET}')

  def show_all_todos(self, is_menu_option = False):
    if len(self.todo_list) != 0:
      for index, todo in enumerate(self.todo_list):
        print(f'\t{AMARILLO}[{index}]{RESET} - {VERDE + 'completado'.ljust(10) + RESET if todo.get_is_completed() == True else ROJO + 'pendiente'.ljust(10) + RESET} - {AZUL}{todo.get_todo()}{RESET}')
    else:
      print(f'\t{AMARILLO}No hay tareas{RESET}')
    if is_menu_option:
      while True:
        try:
          exit_input = input(f'\n\t(presiona {AMARILLO}Enter{RESET} para salir)')

          # Verificar si el usuario ha presionado Enter sin texto para salir
          if exit_input.strip() == "":
            break
          else:
            raise ValueError(f'Valor de índice "{exit_input}" no valido. Prueba otra vez.')
        except ValueError as ve:
          print(f'\t{ROJO}ValueError: {ve}{RESET}')

class Todo:
  def __init__(self, text, is_completed = False) -> None:
    self.text = text
    self.is_completed = is_completed
  
  def get_todo(self):
    return self.text
  
  def get_is_completed_text(self):
    return 'completado' if self.is_completed else 'pendiente'
  
  def get_is_completed(self):
    return self.is_completed
  
  def set_is_completed(self, is_completed):
    self.is_completed = is_completed
