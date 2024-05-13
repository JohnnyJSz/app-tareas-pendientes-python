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

class TodoManager:
  """
    Gestiona una lista de tareas, permitiendo agregar, modificar, eliminar y mostrar tareas.

    Attributes:
      todo_list (list): Lista que almacena instancias de objetos Todo.
    """
  def __init__(self) -> None:
    """
      Inicializa un nuevo TodoManager con una lista de tareas vacía.
    """
    self.todo_list = list()
  
  def add_new_todo(self):
    """
      Añade nuevas tareas a la lista hasta que el usuario decida salir.
      El usuario introduce tareas por medio de la entrada estándar.
    """
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
    """
      Permite al usuario modificar el estado de completado de una tarea existente.
      Las tareas se listan y el usuario puede seleccionar una por su índice para modificarla.
    """
    # Mostrar la lista de tareas antes de modificarlas
    self.show_all_todos()

    while True:
      try:
        index_input = input(f'\n\tIntroduce el índice de la tarea a modificar (o presiona {AMARILLO}Enter{RESET} para salir): {AMARILLO}')

        # Cuando el usuario introduce cualquier otro texto
        if index_input.isalpha():
          # Levantamos una excepcion de tipo ValueError con un mensaje customizado
          raise ValueError(f'Valor de índice "{index_input}" no valido. Prueba otra vez.')
        
        # Cuando el usuario pulsa Enter
        if index_input.strip() == "":
          break

        list_index = int(index_input)
    
        # Verifica si el índice introducido no esta dentro del rango de índices de la lista
        if list_index < 0 or list_index >= len(self.todo_list):
          # Levantamos una excepcion de tipo IndexError con un mensaje customizado
          raise IndexError(f'No hay tareas con índice {list_index}. Prueba otra vez.')
      
        # Procedemos a modificar el valor, invirtiendo si es False to True y viceversa.
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
    """
      Permite al usuario eliminar una tarea existente.
      Las tareas se listan y el usuario puede seleccionar una por su índice para eliminarla.
    """
    self.show_all_todos()
    while True:
      try:
        index_input = input(f'\n\tIntroduce el índice de la tarea a eliminar (o presiona {AMARILLO}Enter{RESET} para salir): {AMARILLO}')

        if index_input.isalpha() and index_input != 'salir':
          raise ValueError(f'Valor de índice "{index_input}" no valido. Prueba otra vez.')
        
        if index_input.strip() == "":
          break

        list_index = int(index_input)
    
        if list_index < 0 or list_index >= len(self.todo_list):
          raise IndexError(f'No hay tareas con índice {list_index}. Prueba otra vez.')
        
        todo_text = self.todo_list[list_index].get_todo()

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
    """
      Muestra todas las tareas en la lista.
    
      Args:
        is_menu_option (bool): Si es True, significa que es parte de las opciones de menu principal 
        y se añade una opcion que permite al usuario salir presionando Enter. Si es False simplemente
        muestra la lista de tareas
    """
    if len(self.todo_list) != 0:
      for index, todo in enumerate(self.todo_list):
        print(f'\t{AMARILLO}[{index}]{RESET} - {VERDE + 'completado'.ljust(10) + RESET if todo.get_is_completed() == True else ROJO + 'pendiente'.ljust(10) + RESET} - {AZUL}{todo.get_todo()}{RESET}')
    else:
      print(f'\t{AMARILLO}No hay tareas{RESET}')
    if is_menu_option:
      while True:
        try:
          exit_input = input(f'\n\t(presiona {AMARILLO}Enter{RESET} para salir)')

          if exit_input.strip() == "":
            break
          else:
            raise ValueError(f'Valor de índice "{exit_input}" no valido. Prueba otra vez.')
        except ValueError as ve:
          print(f'\t{ROJO}ValueError: {ve}{RESET}')


