#! bin/bash
print('=' * 30)
print('  CALCULADORA INTELIGENTE  ')
print('=' * 30)

# Solicita dois números inteiro ao usuário
primeiro_núm = int(input('Primeiro número: '))
segundo_núm = int(input('Segundo número: '))

# As opção do usuário para escolher
print('''Operações matemáticas:
[ 1 ] Adição (+)
[ 2 ] Subtração (-)
[ 3 ] Multiplicação (x ou *)
[ 4 ] Divisão (÷ ou /)''')
opção = int(input('Qual a sua opção? '))

# Resultado de cada opção
if opção == 1:
        print(f'{primeiro_núm} + {segundo_núm} = {primeiro_núm + segundo_núm}')
if opção == 2:
        print(f'{primeiro_núm} - {segundo_núm} = {primeiro_núm - segundo_núm}')
if opção == 3:
        print(f'{primeiro_núm} x {segundo_núm} = {primeiro_núm * segundo_núm}')
if opção == 4:
        print(f'{primeiro_núm} ÷ {segundo_núm} = {primeiro_núm / segundo_núm}')


output_dir = "home/pedro_henrique/modulo1/python"
