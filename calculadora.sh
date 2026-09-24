#!/bin/bash

echo "=============================="
echo "   CALCULADORA INTELIGENTE"
echo "=============================="

read -p "Digite o primeiro número: " num1
read -p "Digite o segundo número: " num2

echo "Escolha a operação:"
echo "1 - Soma"
echo "2 - Subtração"
echo "3 - Multiplicação"
echo "4 - Divisão"

read -p "Opção: " opcao

case $opcao in
    1)
        resultado=$((num1 + num2))
        ;;
    2)
        resultado=$((num1 - num2))
        ;;
    3)
        resultado=$((num1 * num2))
        ;;
    4)
        resultado=$((num1 / num2))
        ;;
    *)
        echo "Opção inválida"
        exit 1
        ;;
esac

echo "Resultado: $resultado"
