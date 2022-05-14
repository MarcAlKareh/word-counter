class Word_Counter:
  #constructor function
  def __init__(self):
    self.text = input('Add a piece of text: ') #string
    self.split_by = ' ';
    self.user_input = None

    self.return_words()

  def get_split_array(self):
    return self.text.split(self.split_by)
  
  def return_words(self):
    self.words = self.get_split_array()
    print(f'Number of words: {len(self.words)}')


app = Word_Counter()