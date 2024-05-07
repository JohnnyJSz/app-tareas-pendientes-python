class Todo:
  def __init__(self, name) -> None:
    self.name = name
  
  def show_name(self):
    print(f'Nombre de la tarea: {self.name}')
