# Definição da constante para a taxa de câmbio
DOLAR = 5.71

valor_em_dolar = float(input("Digite o valor em dólares: "))
valor_em_real = valor_em_dolar * DOLAR
print(f"O valor convertido em reels é: R$ {valor_em_real:.2f}")

