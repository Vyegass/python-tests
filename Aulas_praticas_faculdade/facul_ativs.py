# Cria uma lista vazia para armazenar as notas do aluno.
lista_notas = []

# Define a função que calcula a média das notas.
def calcular_media(notas): 

# Usa 'sum' para somar os valores na lista e 'len' para contar a quantidade de itens.
    media = sum(notas) / len(notas)

# Retorna o valor da média calculada.
    return media

# Exibe o cabeçalho do programa.
print('-'*5, 'Sistema de Gestão de Notas', '-'*5)

# Usa um laço 'for' para repetir o processo de entrada de dados 3 vezes.
for i in range(3):

# Solicita uma nota por vez e a armazena na variável 'notas_aluno'.
    notas_aluno = float(input(f'Digite a {i + 1}° do aluno: '))

#  Chama a função 'calcular_media' uma única vez e armazena o resultado na variável 'media_final'.
    lista_notas.append(notas_aluno)

# chama a função uma unica vez e quarda o valor da média na variável 'media_final'
media_final = calcular_media(lista_notas)

# Exibe uma linha de separação para o relatório final.
print('-'*38)

# Exibe o início do relatório de notas. O argumento 'end' evita uma quebra de linha.
print('\nNotas do aluno(a):',end='')

# Usa um laço 'for' para percorrer e exibir cada nota na lista.
for c in lista_notas:

# Imprime cada nota com um espaço, mantendo-as na mesma linha.
    print(c, end=' ')

# Imprime a média final do aluno com duas casas decimais.
print(f'\nMédia do aluno: {media_final:.2f} ')

# Verifica se a média do aluno é maior que 7 para determinar sua situação.
if media_final > 7:
        
    print('Situação: Aluno Aprovado!')

# Executa este bloco se a condição do 'if' for falsa, indicando reprovação.
else: 
    print('Situação: Aluno reprovado!')
    