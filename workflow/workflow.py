"""
workflow: function that take the flow and the current form and 
return the next form
"""

START_FORM = 'START'
END_FORM   = 'END'

# create workflow unconditionaly following a defined order or form
def sequentialWorkflowFactory(forms):
	def workflow(form, flow=None):
		if form == START_FORM:
			return forms[0]
		position = forms.index(form)
		if position < len(forms) - 1:
			return forms[position + 1]
		return END_FORM
	return workflow

def main():
	forms = [6, 1, 4, 2, 3, 5]
	workflow = sequentialWorkflowFactory(forms)
	print(forms)
	print(workflow(START_FORM)) # 6
	print(workflow(4)) # 2
	print(workflow(5)) # END
	print('')
	
	forms = ['name', 'surname', 'email', 'age', 'genre']
	workflow = sequentialWorkflowFactory(forms)
	print(forms)
	print(workflow(START_FORM)) # name
	print(workflow('email')) # age
	print(workflow('genre')) # END
	print(workflow('surname')) # email
	
if __name__ == '__main__':
	main()
