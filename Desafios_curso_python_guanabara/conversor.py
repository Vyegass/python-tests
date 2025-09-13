print(' '*30+'|'+'-'*22+'|')
print('-'*30 +'+ Conversão de Números +'+'-'*30)
print(' '*30+'|'+'-'*22+'|')


num = int(input('Digite o número: '))
exibir_num = num


print('\n1-Binário\n2-Octal\n3-Hexadecimal\n4-Novo Número\n5-Sair') 

while True: 
    menu = str(input('\nescolha uma opção do menu: '))
    num = exibir_num
    lista = []

    if menu == '1':
        while num != 0:
            binario = num % 2 
            num = num // 2
            lista.append(binario)  

        print(f'O número {exibir_num} convertido para binário é',end=' ')
        for elemento in reversed(lista):
            print(elemento,end='',)
        print()
    
    elif menu == '2':
        while num != 0:
            octal = num % 8
            num = num // 8
            lista.append(octal)

   
        print(f'O número {exibir_num} convertido para Octal é',end=' ')
        for elemento in reversed(lista):
            print(elemento,end='')
        print()

    elif menu == '3':
        while num != 0:
            hexadecimal = num % 16
            num = num // 16 

            if hexadecimal == 15:
                hexadecimal = 'F'
            if hexadecimal == 14:
                hexadecimal = 'E'
            if hexadecimal == 13:
                hexadecimal = 'D'
            if hexadecimal ==  12:
                hexadecimal = 'C'
            if hexadecimal == 11:
                hexadecimal = 'B'
            if hexadecimal == 10:
                hexadecimal = 'A'

            lista.append(hexadecimal)

        print(f'O número {exibir_num} convertido para Hexadecimal é',end=' ')
        for elemento in reversed(lista):
            print(elemento,end='') 
        print()
        
    elif menu == '4':
        exibir_num = int(input('Digite o novo número: '))

    elif menu == '5':
        print('Encerrando...')
        break