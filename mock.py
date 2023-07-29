import random

class Mock:
  @staticmethod
  def generate_integer_list(size, max_value):
    return [random.randint(0, max_value) for i in range(size)]