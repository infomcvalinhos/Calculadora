#adição
def add(x, y):
  return x + y 

#subtração
def sub(x, y):
  return x - y

#multiplicação
def mult(x, y):
  return x * y

#divisão
def div(x, y):
  return x / y

#calculadora
print("selecione uma operação.")
print("1. adição")
print("2. subtração")
print("3. multiplicação")
print("4. divisão")

while True:
  escolha = input("Escolha um numero (1/2/3/4): ")
  if escolha in ('1', '2', '3', '4'):

    num1 = float(input("digite um numero:"))
    num2 =  float(input("digite outro numero:"))

  if escolha == '1':
    print(num1, "+", num2, "=", add(num1, num2))

  elif escolha == '2':
    print(num1, "-", num2, "=", sub(num1, num2))

  elif escolha == '3':
    print(num1, "*", num2, "=", mult(mum1, num2))

  elif escolha == '4':
    print(num1, "/", num2, "=", div(num1, num2))

  else:
    print("FILA DA PUTA, VAI TOMAR NO SEU CU, CARALHOOO!!!! PÕE O NÚMERO CERTO NESSA PORRA!!!") 