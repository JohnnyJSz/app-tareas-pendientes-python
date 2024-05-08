class Todo:
  def __init__(self, text, is_completed = False) -> None:
    self.text = text
    self.is_completed = is_completed
  
  def get_todo(self):
    return self.text
  
  def get_is_completed(self):
    return self.is_completed
