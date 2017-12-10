
import math

def get_lines(initial_line_length: float) -> tuple:
     y = initial_line_length
     x = (3 * y - math.sqrt((3*y)**2 - 4 * y**2)) / 2
     my_tuple = (round(x), round(y-x))
     return my_tuple






if __name__ == '__main__':
    print(get_lines(12))