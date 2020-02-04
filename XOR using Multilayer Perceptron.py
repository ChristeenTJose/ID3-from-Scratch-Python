import math
print("\t\t\tMultilayer Perceptron to calculate XOR(a,b):\n\n('a' and 'b' can take values 'True' or 'False':")
a=input("\n\nEnter the value of 'a': ")
b=input("\nEnter the value of 'b': ")
if (a not in ('True','False')) and  (b not in ('True','False')):
	print('\nInvalid inputs found, exiting...')
	exit(1)
else:
	def AND(x1,x2):
		b=-1.5
		w1=1
		w2=1
		output=perceptron(b,w1,w2,x1,x2)
		return output
	def OR(x1,x2):
		b=-0.5
		w1=1
		w2=1
		output=perceptron(b,w1,w2,x1,x2)
		return output
	def NOT(x1):
		b=0.5
		w1=-1
		output=perceptron(b,w1,x1)
		return output
	def perceptron(b,*w_x):
		if len(w_x)==2:
			z=b+w_x[0]*w_x[1]
		else:
			z=b+w_x[0]*w_x[2]+w_x[1]*w_x[3]
		g=1/(1+math.exp(-1*z))
		if g>=0.5:
			return 1;
		else:
			return 0;
	def XOR(a,b):
		output1=NOT(a)
		output2=NOT(b)
		output3=AND(a,output2)
		output4=AND(b,output1)
		output5=OR(output3,output4)
		return output5
	if a=='True':
		a_binary=1
	else:
		a_binary=0
	if b=='True':
		b_binary=1
	else:
		b_binary=0
	output=bool(XOR(a_binary,b_binary))
	print('\n\n\t\t\tXOR(',a,' , ',b,') = ',output)
