#! /usr/bin/python3
# coding: utf-8;

from polynomial import Poly

def eval(p):
    print('Value of P(x)')

    x = float(input(">> Give x: "))
    if x.is_integer(): x = int(x)

    print(f"P({x}) = {p.eval(x)}")

def derive(p):
    print(f"P'(x) = {p.derive()}")

def primitive(p):
    print(f"P(x) primitive: {p.primitive()}")

def integral(p):
    print('Value of integral of P(x) from a to b')

    a = float(input('>> Give a: '))
    b = float(input('>> Give b: '))
    print()
    print(f"Value of integral of P(x) from {a} to {b} is equal to {p.integral(a, b)}")

def zeros(p):
    print("Shortest interval for P(x) = 0 solution \n by given interval [a, b] and precision value")

    a = float(input('>> Give a: '))
    b = float(input('>> Give b: '))
    prec = float(input('>> Give precision: '))
    print()

    print(f'In [{a}, {b}], P(x) = 0 => x in {p.zeros(a, b, prec)}')


actions = {
    1: eval,
    2: derive,
    3: primitive,
    4: integral,
    5: zeros
}

def main():
    
    datas = {3:2, 2:0, 1:-2, 0:1}
    p = Poly(datas)
    print("P(X) =", p)

    #MENU
    print('\tACTIONS\t >>')
    for i, func in actions.items():
        print(f"{i}: {func.__name__}")
    print()
    
    choice = -1
    while choice:

        try:
            choice = int(input('Choice action (0 for quit): '))
            assert choice

            if choice not in range(6):
                raise ValueError
        except ValueError:
            print('Invalid entry: type 0, 1, 2, 3, 4 or 5')
        except AssertionError:
            pass
        else:
            print()
            actions[int(choice)](p)
            print()

if __name__ == "__main__":
    main()
