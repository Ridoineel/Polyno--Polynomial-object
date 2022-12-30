# Polyno
Polynomial object (class) 

## Installation
```bash
pip install polyno
```

## Import Poly object
```python
from polyno import Poly
```

### Set P1 and P2 for the examples below
	The parameter of Poly object is 
	a vector of coefficients in descending 
	according to the degrees order 
	or a dictionnary {degree:coef}



```python
>>> P1 = Poly([3, 1, 0])
>>> P2 = Poly({0:5, 3:2})
```

```python
>>> P2.coefficients()
[5.0, 0, 0, 2.0]
>>> 
```

## Print polynomial
```python
>>> P1.toString()
'3x^2 + x'
>>> print(P1)
3x^2 + x
>>> print(P2)
2x^3 + 5
>>> 
```

## Addition (with Poly and scalar)
```python
>>> P1 + P2
2x^3 + 3x^2 + x + 5
>>>
>>> P1 + 2
3x^2 + x + 2
>>>
```

## Substraction (with Poly and scalar)
```python
>>> P1 - P2
-2x^3 + 3x^2 + x - 5
>>> P2 - P1
2x^3 - 3x^2 - x + 5
>>> P1 - 2
3x^2 + x - 2
>>>
```

## Multiplication with scalar
```python
>>> P1 * -2
-6x^2 - 2x
>>> P2 * 3
6x^3 + 15
>>> 
```

## Multiplication with Poly
```python
>>> P1 * P2
6x^5 + 2x^4 + 15x^2 + 5x
>>> 
```

## Division with scalar
```python
>>> P2/2
x^3 + 2.5
>>> 
```

## Derivative
```python
>>> P1.derivative()
6x + 1
>>> 
```

## k_th order Derivative 
```python
>>> print(P2.derivative()) 	# first order
6x^2
>>> print(P2.derivative(2)) # second order
12x
>>> print(P2.derivative(3)) # third order
12
>>>
```

## Other methods
> eval: value of P(x) <br/>
> integral: polynomial integral from a to b <br/>
> zero: solution of P(x) = 0 for x in [a, b] interval <br/>

## Eval
```python
>>> P1.eval(2)
14
```

## Integral

```python
>>> # integeral of P2 from 1 to 3
>>> P2.integral(1, 3)
50
```

## Zero

> f(x) = 0 ==> x ?

```python
>>> # solution of P(x) = 0 ?
>>> P = Poly({2:-1, 1:-1, 0:1})
>>> P.zero(0, 10)
0.6180338561534882
>>> P.zero(-3, 0)
-1.6180343627929688
>>> 
>>> P.zero(3, 6) # no solution
>>> P.zero(-3, 3) # two solution, 
>>> # but nothing is returned 
>>> # because of dichotomy (binary search) algorithm
```

# Futures
>
>
>