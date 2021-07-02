# POLYNOMIALS
Polynomial object (class) 

  The main object that manages the polynomials is in the polynomal module (polynomial.py)
  
  EXEMPLE:
  
    # TEST
    print("\tTEST")
    p = Poly({3:2, 2:0, 1:-2, 0:1})

    print(f"P(x) = {p}")
    print(f"P(0) = {p.eval(0)}; P(1) = {p.eval(1)}; P(-4) = {p.eval(-4)}")
    print(f"P'(x) = {p.derive()}")
    print(f"Primitive of P(x) is {p.primitive()}")
    print(f"value of integraf's P(x) from -1 to 1 is {p.integral(-1, 1)}")
    print(f'In [-5, 5], P(x) = 0 => x in {p.zeros(-5, 5, 0.0001)}')
    
    
    # Output
          TEST
    P(x) = 2x^3 - 2x + 1
    P(0) = 1; P(1) = 1; P(-4) = -119
    P'(x) = 6x^2 - 2
    Primitive of P(x) is 0.5x^4 - x^2 + x
    value of integraf's P(x) from -1 to 1 is 2
    In [-5, 5], P(x) = 0 => x in [-1.191558837890625, -1.1914825439453125]

  
  Read main.py file and execute it for a good understanding of the object 
