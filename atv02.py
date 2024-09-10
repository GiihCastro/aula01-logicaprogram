nome = input("Digite seu nome:")
while True:
    try:
        idade = int(input("Digite sua idade:"))
        altura = float(input("Digite sua altura em metros:"))
        break
    except ValueError:
        print("Por favor, insira um número válido")

print("Seu nome é:", nome)
print("Tipo:", type(nome))
print("Sua idade é:", idade)
print("Tipo:", type(idade))
print("Sua altura é:", altura)
print("Tipo:", type(altura))