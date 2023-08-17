''''
Faça um programa em Python que leia (carregue via teclado) uma lista com os
modelos de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA, etc).
Carregue uma outra lista com o consumo desses carros, isto é, quantos
quilômetros cada um desses carros faz com um litro de combustível. Calcule e
mostre:
a. O modelo do carro mais econômico;
b. Quantos litros de combustível cada um dos carros cadastrados consome para
percorrer uma distância de 1000 quilômetros e quanto isto custará,
considerando que o litro da gasolina custe R$ 6,89 o litro. Abaixo segue uma
saída de exemplo. A disposição das informações deve ser o mais próxima
possível ao exemplo. Os dados são fictícios e podem mudar a cada execução
do programa.
'''

lista_carros = []
lista_consumo = []
n_carros = 5
preco_gasolina = 6.89
distancia = 1000
menor_consumo = 0
modelo = ''

for i in range(n_carros):
    carro = input('Modelo: ')
    lista_carros.append(carro)
    consumo = float(input('Consumo: '))
    lista_consumo.append(consumo)
    if lista_consumo[i] > menor_consumo:
        menor_consumo = lista_consumo[i]
        modelo = lista_carros[i]

for i in range(len(lista_carros)):
    print(f'{i+1} - {lista_carros[i]} - {lista_consumo[i]} - {(distancia / lista_consumo[i]):.1f} - de R$ {(distancia / lista_consumo[i] * preco_gasolina):.2f}')

print(f'O menor consumo é do: {modelo} com {menor_consumo}')
    


