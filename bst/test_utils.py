import random
import os

class SyntheticData:
    @staticmethod
    def generate_integer_list(size, max_value):
        return [random.randint(0, max_value) for i in range(size)]

    @staticmethod
    def generate_random_integer(min, max):
        return random.randint(min, max)

class Export:
    @staticmethod
    def export_values_to_file(data):
        file = None
        try:
            file = open("data/export", "a")
        except:
            print("Couldn't export")
            file.close()
        finally:
            file.write(str(data))
            file.write("\n")
            file.close()