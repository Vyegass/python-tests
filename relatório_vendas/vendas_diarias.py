
#vou primeiro mostrar uma pequena lista visual dos produtos, quantidade e preço. Para o usuário visualizar 

produto = ['Gás de 13kg', 'Gás de 8kg', 'Gás de 5kg'] 

preco = [135.00, 95.00, 75.00]

quantidade_no_estoque = [90,76,51]

print('\n{} {} {}\n'.format('-' * 10, 'Lista de produtos','-' * 16))

print('{:<15} {:<10} {:<10}\n'.format('PRODUTOS','PREÇO','QUANTIDADE'))

print(f'{produto[0]:<13}| R${preco[0]:<7.2f}| {quantidade_no_estoque[0]:>4} Unidades\n{produto[1]:<13}| R${preco[1]:<7.2f}| {quantidade_no_estoque[1]:>4} Unidades\n{produto[2]:<13}| R${preco[2]:<7.2f}| {quantidade_no_estoque[2]:>4} Unidades')
        
print('-' * 46)

#agora vou começar a parte "Logica" do Código

print('{} {} {}'.format('-'*10 , 'Lista de produtos vendidos', '-'*8))

print('\n{:>32}'.format('Primeiro produto vendido'))


primeiro_produto = input('Digite o produto vendido: ')
primeira_quantidade = int(input('Quantidade vendida: '))
primeiro_valor = float(input('Valor do produto: R$')) 

primeiro_subtotal = primeira_quantidade * primeiro_valor
print(f'\nTotal da primeira compra\nProduto: {primeiro_produto}\nSubtotal: R${primeiro_subtotal:.2f}')

print('\n{:>32}'.format('Segundo produto vendido'))

segundo_produto = input('Digite o produto vendido: ')
segunda_quantidade = int(input('Quantidade vendida: '))
segundo_valor = float(input('Valor do produto: R$'))

segundo_subtotal = segunda_quantidade * segundo_valor 
print(f'\nTotal da segunda compra\nProduto: {segundo_produto}\nSubtotal: R${segundo_subtotal:.2f}')


print('\n{:>32}'.format('Terceiro produto vendido'))

terceiro_produto = input('Digite o produto vendido:') 
terceira_quantidade = int(input('Quantidade vendida:'))
terceiro_valor = float(input('Valor do produto: R$'))

terceiro_subtotal = terceira_quantidade * terceiro_valor
print(f'\nTotal da terceira compra\nProduto: {terceiro_produto}\nSubtotal: R${terceiro_subtotal:.2f}')

print('\n {} {} {}'.format('-'*10 , 'RELATÓRIO DE VENDAS DIÁRIAS', '-'*8))

print(f'Primeira Compra do dia\nProduto:{primeiro_produto}\nQuantidade:{primeira_quantidade}\nValor: R${primeiro_valor:.2f}\nSubtotal: R${primeiro_subtotal:.2f}')
print(f'\nSegunda Compra do dia\nProduto:{segundo_produto}\nQuantidade:{segunda_quantidade}\nValor: R${segundo_valor:.2f}\nSubtotal: R${segundo_subtotal:.2f}')
print(f'\nTerceira Compra do dia\nProduto:{terceiro_produto}\nQuantidade:{terceira_quantidade}\nValor: R${terceiro_valor:.2f}\nSubtotal: R${terceiro_subtotal:.2f}')

print('\n {} {} {}'.format('-'*10 , 'Total Geral das Vendas no Dia','-'*8))
print(f'TOTAL: R${primeiro_subtotal + segundo_subtotal + terceiro_subtotal:.2f}')
print('-'*46)

print('Encerrando Progama...')
