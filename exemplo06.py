
import os 

os.system("cls")

print("Exemplo de While com texto")

resposta = input("Deseja calcular a soma de dois números? (sim) ou (nao): ").lower()

while resposta == "sim":
    print("=================================")
    print("Calculando a SOMA de Dois Números")
    print("=================================")
    # 1 passo - Entrada
    v1 = int(input("Digite um número: "))
    v2 = int(input("Digite um número: "))
    # 2 passo - Processamento
    resultado = v1 + v2
    # 3 passo - Saída
    print("O resultado é: ", resultado)
    resposta = input("Digite (sim) para reiniciar, e (nao) para encerrar: ").lower()
else:
    input("Pressione <Enter> para encerrar o programa...")