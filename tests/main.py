from os.path import dirname
import sys

sys.path.append(dirname(dirname(__file__)))

from src.polyno import Poly

def main():
    # TEST
    [2, 0, -2, 1]
    p = Poly([2, 0, -2, 1])
    print(p)
    print(p.derivative())
    print(p.derivative(2))
    print(p.derivative(3))
    print(p.derivative(10000))
    print(p.eval(4))

    # P2 = Poly([2, 0, 0, 5])
    # print(P2.derivative(2))
    # print(P2.derivative(3))

if __name__ == "__main__":
    main()