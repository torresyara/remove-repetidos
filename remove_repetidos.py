"""
Recebe como parâmetro uma lista com números inteiros, os ordena, 
verifica se existem números repetidos e os remove. 
Devolve a lista alterada.
"""
def remove_repetidos(a: [int]):
	a.sort()
	return [a[i] for i in range(len(a)) if a[i] != a[i-1]]
	


print (remove_repetidos([7,3,33,12,3,3,3,7,12,100]))