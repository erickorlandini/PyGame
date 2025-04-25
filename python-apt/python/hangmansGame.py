import random

palavras = ["estudo", "programacao", "desenvolver", "computador", "aprender"]
palavra_secreta = random.choice(palavras)
palavra_escondida = list("_" * len(palavra_secreta))
tentativas = 6
letras_chutadas = set()

while tentativas > 0:
    print("Palavra:" , "".join(palavra_escondida))
    print("Tentativas restantes:", tentativas)
    print("Letras ja chutadas:", ", ".join(letras_chutadas))
    palpite = input("Digite uma letra: ").lower()
    print("\n")

    if len(palpite) != 1 or not palpite.isalpha():
        print("Palpite inválido. Digite apenas uma letra.")
        continue

    if palpite in letras_chutadas:
        print("Você ja chutou essa letra. Tente outra.")
        continue

    letras_chutadas.add(palpite)

    if palpite in palavra_secreta:
        print("Você acertou!")
    for i in range(len(palavra_secreta)):
        if palavra_secreta[i] == palpite:
            palavra_escondida[i] = palpite
    if "_" not in palavra_escondida:
        print("Parabens! Você adivinhou a palavra:", palavra_secreta)
        break
    else:
        tentativas -= 1
        print("Você perdeu uma tentativa.")

if tentativas == 0:
    print("Fim do jogo! Você não conseguiu adivinhar a palavra.")
    print("A palavra secreta era:", palavra_secreta)