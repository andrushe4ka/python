
operators = ['+', '-', '*', '/', '<', '=', '>', '?']

def get_n_arg(operator):
	if operators.count(operator) == 0:
		return(0)
	if operators.index(operator) < 7:
		return(2)
	else:
		return(3)

def is_operator(element):
	return(operators.count(element) > 0)

def is_variable(element):
	return(element.isalpha())

def get_vars(elements):
	formula_vars = []
	for element in elements:
		if not is_operator(element): 
			if is_variable(element):
				if formula_vars.count(element) == 0:
					formula_vars.append(element)
	try:
		formula_vars.sort()
	except:
		return(formula_vars)
	return(formula_vars)
	
def calc_formula(elements, value_set, var_to_val):
	try:
		if len(elements) == 1:
			return(value_set[0])
		operator = elements.pop()
		if not is_operator(operator):
			return(0)
		operands = []
	except:
		return(0)
	for i in range(get_n_arg(operator)):
		try:
			element = elements.pop()
		except:
			return(0)	
		if is_operator(element):
			elements.append(element)
			operands.append(calc_formula(elements, value_set, var_to_val))
		elif is_variable(element):
			try:
				if var_to_val.index(element) >= len(value_set):
					operands.append(0)
				else:
					operands.append(int(value_set[var_to_val.index(element)]))
			except:
				return(0)
		else:
			try:
				tmp = int(element)
			except:
				return(0)
			operands.append(tmp)
	try:
		if len(operands) < 2:
			return(0)
		if operator == '+':
			return(operands[1] + operands[0])
		if operator == '-':
			return(operands[1] - operands[0])
		if operator == '*':
			return(operands[1] * operands[0])
		if operator == '/':
			if operands[0] == 0:
				return(0)
			return(operands[1] // operands[0])
		if operator == '<':
			return(operands[1] < operands[0])
		if operator == '=':
			return(operands[1] == operands[0])
		if operator == '>':
			return(operands[1] > operands[0])
		if operator == '?':
			if len(operands) < 3:
				return(0)
			if operands[2]:
				return(operands[1])
			else:
				return(operands[0])
	except:
		return(0)
	return(0)

def calc(d):
	try:
		K = int(d[0])
		Formula_elements = d[1].split(' ')
		N = int(d[2])
		Value_set = d[3].split(' ')
		
		var_to_val = get_vars(Formula_elements)
	
		return(calc_formula(Formula_elements, Value_set, var_to_val))
	except:
		return(0)

if __name__ == '__main__':
	K = input()
	Formula = input()
	N = input()
	Value_sets = []
	try:
		Num = int(N)
	except:
		Num = 1
	for i in range(Num):
		Value_sets.append(input())
	for value_set in Value_sets:
		print(calc([K, Formula, N, value_set]))
