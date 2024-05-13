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
  """
    Representa una opción individual en un menú interactivo.
    
    Attributes:
      label (str): Descripción de la opción, que se muestra en el menú.
      action (callable): Función sin parámetros que se ejecuta cuando se selecciona esta opción.
  """
  def __init__(self, label, action) -> None:
    """
      Inicializa una nueva instancia de MenuOption con una etiqueta y una acción.
      
      Args:
        label (str): El texto de la etiqueta para la opción del menú. Se espera que sea una cadena sin formato.
        action (callable): La función que se llamará cuando esta opción del menú sea seleccionada.
    """
    self.formatted_label = f'{RESET}{VERDE}\n-- {ITALIC}{label} --{RESET}'
    self.label = label
    self.action = action
  
  def get_label(self):
    """
      Devuelve la etiqueta sin formato, de la opción del menú.
      
      Returns:
          str: La etiqueta de esta opción de menú.
    """
    return self.label
  
  def get_formatted_label(self):
    """
      Devuelve la etiqueta formateada de la opción del menú.
      
      Returns:
          str: La etiqueta formateada de esta opción de menú.
    """
    return self.formatted_label
  
  def execute_action(self):
    """
      Ejecuta la acción asociada con esta opción del menú.
    """
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
  """
    Representa una tarea con un texto descriptivo y un estado de completado.

    Attributes:
      text (str): El texto de la tarea.
      is_completed (bool): Verdadero si la tarea está completada, falso si está pendiente.
  """
  def __init__(self, text, is_completed = False) -> None:
    """
      Inicializa una nueva tarea con texto y estado opcionalmente completado.

      Args:
        text (str): El texto que describe la tarea.
        is_completed (bool, optional): Estado inicial de la tarea, verdadero si está completada. 
        Por defecto es False.
    """
    self.text = text
    self.is_completed = is_completed
  
  def get_todo(self):
    """
      Devuelve el texto de la tarea.

      Returns:
        str: El texto de la tarea.
    """
    return self.text
  
  def get_is_completed_text(self):
    """
      Devuelve el estado de la tarea en formato textual.

      Returns:
        str: 'completado' si la tarea está completada, 'pendiente' si no lo está.
    """
    return 'completado' if self.is_completed else 'pendiente'
  
  def get_is_completed(self):
    """
      Devuelve el estado de completado de la tarea.

      Returns:
          bool: Verdadero si la tarea está completada, falso si está pendiente.
    """
    return self.is_completed
  
  def set_is_completed(self, is_completed):
    """
      Establece el estado de completado de la tarea.

      Args:
        is_completed (bool): Verdadero para marcar la tarea como completada, falso para marcarla como pendiente.
    """
    self.is_completed = is_completed
