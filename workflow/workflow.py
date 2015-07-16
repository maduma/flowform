"""
Terms:
- form
collection data (name, date, email, ...)

- flow
a flow is a collection of forms

- workflow
a path from a start form to and end form.
a workflow is a state machine, each state is represented by a form and
events are derived from flow data.
e.g a function that take the flow and the current form and return the
next flow
"""

START_FORM = 'START'
END_FORM   = 'END'

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
