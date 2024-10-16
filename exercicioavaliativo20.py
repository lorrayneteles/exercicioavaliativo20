#Calcular o IMC(Índice de Massa Corporal)

massa_corporal = float(input("Digite a sua massa corporal em kg:"))

altura = float(input("Digite a sua altura em metros:"))

indice_massa_corporal = (massa_corporal) / ((altura)**2)

print(f'O IMC seu é de:',indice_massa_corporal)