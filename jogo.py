import random

def jogo_adivinhacao():
  """Jogo de adivinhação de números."""
  numero_secreto = random.randint(1, 100)
  tentativas = 0

  print("Bem-vindo ao jogo de adivinhação!")
  print("Tente adivinhar o número secreto entre 1 e 100.")

  while True:
    chute = int(input("Digite seu chute: "))
    tentativas += 1

    if chute < numero_secreto:
      print("O número secreto é maior.")
    elif chute > numero_secreto:
      print("O número secreto é menor.")
    else:
      print(f"Parabéns! Você acertou em {tentativas} tentativas.")
      break

# Iniciar o jogo
jogo_adivinhacao()
