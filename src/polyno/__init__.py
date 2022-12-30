# coding: utf-8;

""" 
	Author: RidoineEl
	Object: Polynomial object (class)
"""

class Poly():
	""" Polynomial: dn*X^n + d_n'*X^n' + ..... d_0

	@param: dictionary object in format degree:coefficient,

	@attributes
		-degs : list of degrees sorted in descending order
		-coefs : list of coefficients according to degs
	
	@method:
		toString:
		degree:
		eval:
		derivative:
		primitive:
		integral:
		zero:
		lim:
		__repr__
		__add__
		__sub__
		__mul__
		__truediv__
	
	EXAMPLE:
		>> datas = {2:4, 1:2}
		>> p = Poly(datas)
		>> print(p)
		4*x^2 + 2*x
		>> p / 2
		2*x^2 + x
		>> p.eval(-1/2)
		0
		>> p.derivative()
		8*x + 2
		>> p2 == Poly({3:2, 2:4, 0:4})
		>> print(p2)
		2*x^3 + 4*x^2 + 4
		>> p + p2
		2*x^3 + 8*x^2 + 2*x + 4
		>> ##############################

	"""

	def __init__(self, datas={}):
		""" Polynomial parameter is absolute list of coefficients
			in descending order or dictionnary {degree:coef}

		"""

		self.degs = list()
		self.coefs = list()

		# Poly.coefs is list of polynomial degrees according to reversed sorted Poly.degs.
		# exemple: 
		#	for P2 = Poly({0:5, 3:2})
		#	P2.coefs is [2, 5], not [2, 0, 0, 5]

		if isinstance(datas, dict):
			datas = sorted(datas.items(), reverse=True)

			# deg:coef if coef not null
			for i, (deg, coef) in enumerate(datas):
				if coef != 0:
					if not float(deg).is_integer():
						raise ValueError("Error: degrees could be integers")

					self.degs.append(int(deg))
					self.coefs.append(float(coef))
		elif isinstance(datas, list):
			n = len(datas)

			for i, coef in enumerate(datas):
				if coef != 0:
					deg = n - i - 1

					self.degs.append(deg)
					self.coefs.append(float(coef))

		# Below, i could use datas, but because of int(deg) 
		# and float(coef) plus coef != 0 it's better that way
		self.degs_coefs = dict(zip(self.degs, self.coefs))

	def toString(self):
		return self.__repr__()

	def degree(self):
		return self.degs[0]

	def coefficients(self):
		""" Absolute coefficients list ex:[0, 2, 0, 0, ...] 

		"""

		degs_coefs = self.degs_coefs
		deg = self.degree()
		coefs = []

		for i in range(deg + 1):
			if i in self.degs: 
				coefs.append(degs_coefs[i])
			else: 
				coefs.append(0)

		return coefs
	def eval(self, value):
		""" Return value of P(real) 
			with Ruffini-Horner method

		"""

		if isinstance(value, float) or isinstance(value, int):
			# absolute coefficients
			coefs = self.coefficients()

			# calculate result
			result = coefs[-1]

			for i in range(len(coefs) - 2, -1, -1):
				result = result*value + coefs[i]

			return int(result) if float(result).is_integer() else result
		else:
			raise ValueError(f"Unsupported operation of {type(value)} and Poly")

	def derivative(self, k=1):
		""" return derivative of this polynomial 

		"""

		if k > len(self.degs) + 1:
			return Poly()
		if k == 0:
			return self

		# derivative coefficients list
		new_c = [coef*deg for deg, coef in self.degs_coefs.items()]
		# derivative degrees list
		new_d = [degree - 1 for degree in self.degs]
		
		new_poly = Poly(dict(zip(new_d, new_c)))

		return new_poly.derivative(k - 1)

	def primitive(self):
		""" return primitive of this polynomial 

		"""

		# primitive coefficients list
		new_c = [coef/(deg + 1) for deg, coef in self.degs_coefs.items()]
		# primitive degrees list
		new_d = [degree + 1 for degree in self.degs]

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

	def zero(self, a, b, precision=10e-7):
		""" Search solution of P(x) = 0 where x in [a, b] 

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

			if p(a) * p(b) > 0:
				return None

			while abs(a - b) > precision:
				if p(a) == 0: return a
				if p(b) == 0: return b

				mil = (a+b)/2

				if p(a) * p(mil) <= 0: 
					b = mil
				else: 
					a = mil

			return a

	def lim(self, x="inf"):
		pass

	########### SPECIALS METHODS ###########
	###########					###########
	def __repr__(self):
		""" Return polynomial string format
			example: >> p = Poly({2:1, 1:4, 0:8})
					 >> p
					 x^2 + 4x + 8
					 >> print(p)
					 x^2 + 4x + 8

		"""

		if not self.degs and not self.coefs:
			return "0"

		result = str()

		for i in range(len(self.coefs)): 
			if i != 0: result += " "

			coef = self.coefs[i]
			degree = self.degs[i]

			coef = round(coef, 3)
			if float(coef).is_integer(): coef = int(coef)
			
			# Coefficient level
			if coef in [-1, 1]: 
				if coef == -1:
					result += '- ' if i else '-'
				else:
					result += '+ ' if i  else ""

				result += '1' if not degree else ''
			else:
				if not i:  
					result += str(coef)
				else:
					result += "- " if coef < 0 else "+ "
					result += str(abs(coef))

			# Degree level
			if not degree:
				pass
			elif degree == 1 :
				result += 'x'
			else:
				result += 'x^' + str(degree)

		return result

	def __iter__(self):
		"""return (degree, coef) of polynomial per iteration.

		ex: >> p = Poly({2:1, 1:2})
			>> for items in p:
				  print(items)
			...
			(2, 1)
			(1, 2)
		
		"""

		for i in range(len(self.coefs)):
			yield self.degs[i], self.coefs[i]

	#+ ######### OPERATORS MANAGEMENT ###########
	############					  ###########
	def __add__(self, val):
		""" Add object to ...
			in the case of self + val

		"""

		if isinstance(val, Poly):
			# Add the coefficients according to the degrees

			all_deg_coef = list(self) + list(val)
			deg_coef = dict()

			for deg, coef in all_deg_coef:
				if deg not in deg_coef.keys():
					deg_coef[deg] = coef
				else:
					deg_coef[deg] += coef
		elif isinstance(val, int) or isinstance(val, float):
			# add val to coefficient whose degree is null

			deg_coef = dict(zip(self.degs, self.coefs))

			if 0 not in deg_coef.keys():
				# if 0 degree not exist
				deg_coef[0] = val
			else:
				# if 0 degree exist
				deg_coef[0] += val
		else:
			raise TypeError('Unsupported opération: Poly and non-Poly, non-int or non-float.')
		
		return Poly(deg_coef)

	def __radd__(self, val):
		""" addition in the case of val + self 

		"""

		return self + val



	def __neg__(self):
		""" unary '-' operator 

		"""

		return -1 * self

	def __sub__(self, val):
		""" Substraction of this and val, 
			in the case of self - val 

		"""

		return self + (-val)

	def __rsub__(self, val):
		""" substraction in the case of val - self 

		"""

		return self - val
	
	def __mul__(self, val):
		""" '*' operator in the case of self * val
		
		"""

		if isinstance(val, Poly):
			p = val

			# dict object whose keys is degs and values is coefs
			self_deg_coef = self.degs_coefs
			p_deg_coef = p.degs_coefs

			# degree (max of degrees) of self and val
			self_n = self.degree()
			p_n = p.degree()

			new_deg_coef = dict()

			for i in range(self_n + p_n + 1):
				# calculation of coefficient p_i
				p_i = 0

				for j in range(i + 1):
					if j in p.degs and i - j in self.degs:
						p_i += p_deg_coef[j] * self_deg_coef[i - j]

				new_deg_coef[i] = p_i

			return Poly(new_deg_coef)

		elif isinstance(val, int) or isinstance(val, float):
			nb = val

			new_coefs = [nb * x for x in self.coefs]
			deg_coef = dict(zip(self.degs, new_coefs))

			return Poly(deg_coef)
		else:
			raise TypeError(f'Unsupported opération: {type(val).__qualname__} and Poly')
	
	def __rmul__(self, val):
		""" '*' operator in the case of val * self

		"""

		return self * val

	def __truediv__(self, nb):
		""" "/" operand for Poly with number (Poly / nb , not nb / Poly)  """

		if isinstance(nb, float) or isinstance(nb, int):
			return (1/nb) * self
		else:
			raise TypeError(f"Unsupported '/' operation of {type(nb).__qualname__} and Poly")

	#######################################
	#######################################