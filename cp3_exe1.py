'''
Em uma competição de salto em distância, cada atleta tem direito a realizar 
cinco saltos. O resultado do atleta será determinado pela média dos cinco valores
alcançados. Crie um programa em Python que receba o nome do atleta e as cinco
distâncias alcançadas por ele em seus saltos e depois informe o nome, os saltos e
a média dos saltos, o menor e o maior salto. O programa deve armazenar os valores alcançados em cada
salto em uma sequência e ser encerrado quando não for informado o nome do
atleta. Segue um exemplo de saída do programa:
'''

#Lista com o nome de cada salto
texto_saltos = ['1o', '2o', '3o', '4o', '5o']

while True:
    #Lista com os valores dos saltos
    saltos = [0, 0, 0, 0, 0]

    #variáveis
    media_saltos = 0
    soma = 0
    melhor_salto = 0
    pior_salto = 0

    nome_atleta = input('Nome: ')
    if nome_atleta != '':
        for i in range(5):
            saltos[i] = float(input(f'{texto_saltos[i]} salto'))
            soma+=saltos[i]
        
        media_saltos = soma/len(saltos) #5
        melhor_salto = saltos[0]
        pior_salto = saltos[0]

        for salto in saltos:
            if salto > melhor_salto:
                melhor_salto = salto
            if salto < pior_salto:
                pior_salto = salto
        
        #Exibindo os resultados
        print(f'Melhor salto:...........{melhor_salto}')
        print(f'Pior salto:.............{pior_salto}')
        print(f'{nome_atleta}:\n Média dos saltos.....{media_saltos:.2f}')
    else:
        print('informe o nome do atleta \n')
    
    print('Continuar? \n 1-Sim \n 2-Não \n')
    opcao = int(input('Opção: '))
    if opcao == 2:
        break
        
print('FIM do PROGRAMA')

