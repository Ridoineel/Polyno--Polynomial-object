#! /usr/bin/env python3
# coding: utf-8;

""" 
	Author: RidoineEl
	Object: Polynomial obejct (class)
"""

class Poly():
	""" Polynomial: dn*X^n + d_n'*X^n' + ..... d_0

	@param: dictionary object in format degree:coefficient,

	@attribs
		-coef : coefficients list
		-deg : degrees list
	
	@method:
		__repr__: for print preview
		__add__: "+" operand between Poly and Poly or number (int or float)
		__sub__: "-" operand between Poly and Poly or number (int or float)
		__mul__: "*" operand between Poly and number (int or float)
		__truediv__: "/" operand between Poly and number (int or float), just Poly / number
		eval: Value returned polynomial with unknow value x
		derive: polynomial derive
		primitive: polynomial primitive
		integral: polynomial integrav from a to b
		zeros: interval of P(X) = 0 solution by precision value

	
	EXAMPLE:
			>> datas = {2:4, 1:2}
			>> p = Poly(datas)
			>> print(p)
			4*x^2 + 2*x
			>> p / 2
			2*x^2 + x
			>> p.eval(-1/2)
			0
			>> p.derive()
			8*x + 2
			>> p2 == Poly({3:2, 2:4, 0:4})
			>> print(p2)
			2*x^3 + 4*x^2 + 4
			>> p + p2
			2*x^3 + 8*x^2 + 2*x + 4
			>> ##############################
		
				
				AUTHOR: RidoineEl

	"""

	def __init__(self, datas: dict):
		datas = sorted(datas.items(), reverse=True)

		self.deg = list()
		self.coef = list()

		# deg:coef if coef not null
		for deg, coef in datas:
			if coef != 0:
				self.deg.append(int(deg) if float(deg).is_integer() else deg)
				self.coef.append(int(coef) if float(coef).is_integer() else coef)

	def __repr__(self):
		""" Return polynomial render with print() and type in terminal
			exemple: >> p = Poly({2:1, 1:4, 0:8})
					 >> p
					 x^2 + 4x + 8
					 >> print(p)
					 x^2 + 4x + 8

		"""

		answer = str()
		for i in range(len(self.coef)): 
			if i != 0: answer += " "

			coef = self.coef[i]
			degree = self.deg[i]

			# Coefficient level
			if coef in [-1, 1]: 
				if coef == -1:
					answer += '- ' if i else '-'
				else:
					answer += '+ ' if i  else ""

				answer += '1' if not degree else ''
			else:
				if not i:  
					answer += str(coef)
				else:
					answer += "- " if coef < 0 else f"+ "
					answer += str(abs(coef))

			# Degree level
			if not degree:
				pass
			elif degree == 1 :
				answer += 'x'
			else:
				answer += 'x^' + str(degree)

		return answer

	def __iter__(self):
		"""return (degree, coef) of polynomial by itération time.

		ex: >> p = Poly({2:1, 1:2})
			>> for items in p:
				  print(items)
			...# render
			(2, 1)
			(1, 2)
		
		"""

		for i in range(len(self.coef)):
			yield self.deg[i], self.coef[i]
	
	def __add__(self, val):

		if type(val) is Poly:
			all_deg_coef = list(self) + list(val)
			deg_coef = dict()

			for deg, coef in all_deg_coef:
				
				if deg not in deg_coef.keys():
					deg_coef[deg] = coef
				else:
					deg_coef[deg] += coef

		elif type(val) in [float, int]:

			deg_coef = dict(zip(self.deg, self.coef))

			if 0 not in deg_coef.keys():
				deg_coef[0] = val
			else:
				deg_coef[0] += val
		else:
			raise TypeError('Unsupported opération: Poly and non-Poly, non-int or non-float.')
		
		return Poly(deg_coef)

	def __sub__(self, poly):
		
		return self + (-1 * poly)
	
	def __mul__(self, number):
		""" Return value of multiplication:
			"*" operand for Poly with number type once (Poly * number, not number * Poly) 
		
		"""

		if type(number) in [int, float]:
			deg_coef = dict(zip(self.deg, map(lambda x: number * x, self.coef)))

			return Poly(deg_coef)
		else:
			raise TypeError('Unsupported opération: non-int or non-float and Poly')
	
	def __rmul__(self, poly):
		""" Value of Mutiplication for number * Poly """

		return self.__mul__(poly)

	def __truediv__(self, number):
		""" "/" operand for Poly with number (Poly / number , not number / Poly)  """

		if type(number) in [int, float]:
			return (1/number) * self
		else:
			raise TypeError('Unsupported opération: non-int or non-float and Poly')

	def eval(self, real):
		""" Return value of P(real) """

		if type(real) in [int, float]:
			result = 0
			for i in range(len(self.coef)):
				coef = self.coef[i]
				degree = self.deg[i]

				result += coef * (real**degree)

			return int(result) if float(result).is_integer() else result
		else:
			raise ValueError('Invalid unknow value')

	def derive(self):
		""" return polynôme's derive """

		# derive coefficients list
		new_c = [self.coef[i]*self.deg[i] for i in range(len(self.coef)) ]
		# derive degrees list
		new_d = [degree - 1 for degree in self.deg]
		
		new_poly = Poly(dict(zip(new_d, new_c)))
		return new_poly

	def primitive(self):
		""" return polynomial's primitiv """

		# primitive coefficients list
		new_c = [self.coef[i]/(self.deg[i] + 1) for i in range(0, len(self.coef) ) ]
		# primitive degrees list
		new_d = [degree + 1 for degree in self.deg]

		new_poly = Poly(dict(zip(new_d, new_c)))
		return new_poly

	def integral(self, a, b): 
		""" Retun value of polynomial's integral from a to b """

		try:
			a = float(a)
			b = float(b)
		except ValueError as msg:
			print("ValueError:", msg)
			exit()
		else:
			primit = self.primitive()

			integ = primit.eval(b) - primit.eval(a)

			return int(integ) if float(integ).is_integer() else integ
	
	def zeros(self, a, b, precision):
		"""zeros(a, b, prec) -> [i1, i2] # shortest interval of zero of polynomial,
			Shortest interval of P(x) = 0 solution by precision 

			By dichotomie

		"""

		try:
			a = float(a)
			b = float(b)
			precision = float(precision)
		except ValueError as msg:
			print("ValueError:", msg)
			exit()
		else:
			p = self.eval

			if a > b:
				a, b = b, a

			if p(a) * p(b) <= 0:
				while abs(a - b) > precision:
					mil = (a+b)/2
					if p(a) * p(mil) <= 0: 
						b = mil
					else: 
						a = mil

				return [a, b]
	
	def lim(self, a="inf"):
		pass

def main():
	# TEST
	print("\tTEST")
	p = Poly({3:2, 2:0, 1:-2, 0:1})

	print(f"P(x) = {p}")
	print(f"P(0) = {p.eval('f')}; P(1) = {p.eval(1)}; P(-4) = {p.eval(-4)}")
	print(f"P'(x) = {p.derive()}")
	print(f"Primitive of P(x) is {p.primitive()}")
	print(f"value of integraf's P(x) from -1 to 1 is {p.integral(-1, 1)}")
	print(f'In [-5, 5], P(x) = 0 => x in {p.zeros(-5,5, "f")}')
	
	# import pdb; pdb.set_trace()

if __name__ == "__main__":
	main()
