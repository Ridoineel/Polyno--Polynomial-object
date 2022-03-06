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
	parameter is dictionary object with key=degree and value=coef
	**degree:coef**

```python
>>> P1 = Poly({1:1, 2:3})
>>> P2 = Poly({0:5, 3:2})
```

	By default, Poly.coefs is list of polynomial degrees according to reversed sorted Poly.degs.
	Exemple: P2.coefs is [2, 5], not [2, 0, 0, 5]

	Below, get absolute list in ascending order of coefficients

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
>>> P2 = Poly({0:5, 3:2})
>>> print(P2.derivative())
6x^2
>>> print(P2.derivative(2))
12x
>>> print(P2.derivative(3))
12
>>>
```

## Other method
> eval: value of P(x) <br/>
> integral: polynomial integral from a to b <br/>
> zero: solution of P(x) = 0 for x in [a, b] interval <br/>

# Futures
>
>
>