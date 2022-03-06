from os.path import dirname
import sys

sys.path.append(dirname(dirname(__file__)))

from src.polyno import Poly

def main():
    p1 = Poly({0:-1, 1:1, 3:2})
    p2 = Poly({0:2, 1:3, 2:4})

    print(p1 * 3)
if __name__ == '__main__':
    main()