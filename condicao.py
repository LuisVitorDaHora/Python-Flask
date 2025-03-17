# Informações sobre o filme 

# nome = input ("Digite o nome do filme: \n")
# ano = int(input("Digite o ano de lançamento: \n"))
# nota = float(input("Digite a nota de avaliação do filme: \n"))

# #Verificar se o filme é recomendado

# if nota > 8.0 and ano > 2015:
#     print(f"O filme {nome} é muito bom. Recomendo assisti-lo. ")
# else:
#     print(f"O filme {nome} ainda não atingiu uma boa nota. ")

num1 = float(input("Digite o primeiro número: \n"))
num2 = float (input("Digite o segundo número: \n"))
operacao = input("Digite a operação a ser realizada: (+ - * /) \n")

if operacao == "+":
    resultado = num1 + num2

elif operacao == "-":
    resultado = num1 - num2

elif operacao == "*":
    resultado = num1 * num2

elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: Divisão por 0")
        resultado = 0

else:
    print ("Operação invalida")
    resultado = 0

print(f"Resultado da operação é: {resultado:.2f}")