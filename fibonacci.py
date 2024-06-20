def fibonacci(n):
  if n <= 0:
    return "O numero de termo deve ser maior que 0."

sequencia = [1,1]

for i in range(2, n):
  proximo_termo = sequencia[-1] + sequencia[-2]
  sequencia.append(proximo_termo)
return sequencia[:n]

num_termo = int(input("Digite o numero de termo da sequencia de fibonacci: "))

resultado = fibonacci(num_termo)

print(f"A sequencia de fibonacci com {num_termo} temos: {resultado}")
