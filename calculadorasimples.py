print("Calculadora Simples")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
opcao = int(input("Digite a opção desejada: "))

if opcao not in [1, 2, 3, 4]:
	print("Opção inválida, tente novamente!")
else:
	n1 = float(input("Digite o primeiro valor: "))
	n2 = float(input("Digite o segundo valor: "))
	if opcao == 1:
		print(n1 + n2)
	elif opcao == 2:
		print(n1 - n2)
	elif opcao == 3:
		print(n1 * n2)
	elif opcao == 4:
		if n2 == 0:
			print("Não é possível dividir por zero.")
		else:
			print(n1 / n2)
