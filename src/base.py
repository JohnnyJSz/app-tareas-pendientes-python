class MenuOption:
  def __init__(self, label, action) -> None:
    self.label = label
    self.action = action
  
  def get_label(self):
    return self.label
  
  def execute_action(self):
    self.action()

class Todo:
  # Variable de clase para realizar un seguimiento del ID
  last_id = 0
  def __init__(self, text, is_completed = False) -> None:
    Todo.last_id += 1  # Incrementa el ID por cada nueva instancia
    self.id = Todo.last_id # Asigna el nuevo ID a la instancia
    self.text = text
    self.is_completed = is_completed
  
  def get_id(self):
    return self.id
  
  def get_todo(self):
    return self.text
  
  def get_is_completed(self):
    return self.is_completed
