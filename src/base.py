class Todo:
  def __init__(self, text, is_completed = False) -> None:
    self.text = text
    self.is_completed = is_completed
  
  def show_todo(self):
    print(self.text)
