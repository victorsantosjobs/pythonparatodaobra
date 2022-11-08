import array

#conversor binario para decimal dez digitos python


#digite dez numeros binarios

#a = input ("b1","b2")

#print os numeros em decimal são esses

binario=int(input("Escreva o numero de binario que será convertido, digite dez no caso:-"))
n=list(map(int, input("Escreva o binário e dê um espaço entre um e outro:-").strip().split()))
print(n)


#conversor
#binario = int(input("Digite o número (binário) para ser convertido para a base decimal: "))
n = len(str(binario))
valor_digitado = binario
decimal = 0
i = 0

while n >= 0:
  resto = binario % 10
  decimal = decimal + (resto * (2**i))
  n = n - 1
  i = i + 1
  binario = binario // 10

print("O número (binario) digitado",valor_digitado,", na base decimal, vale:",decimal)