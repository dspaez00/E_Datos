
def fibo(n):
	# Escriba aquí el código para calcular el n-esimo valor de la serie de fibonacci de forma no recursiva (use ciclos).
	cont=0
	print("Que posición desea conocer")
	pos=input()
	while cont =< pos:
		suma = suma + cont
		cont = cont + 1
	if cont == pos:
		print('El número de la posición {} es {}'.format(pos,suma))
	pass

def fibo_rec(n):
	# Escriba aquí el código para calcular el n-esimo valor de la serie de fibonacci de forma recursiva (NO use ciclos).
	print("Que posición desea conocer de 1 a 10")
	pos=input()
	
	pass
	

print(fibo(10))
print(fibo_rec(10))
	
