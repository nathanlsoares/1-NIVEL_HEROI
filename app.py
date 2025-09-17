
def executar_app():
    print("Bem-vindo ao sistema de classificação de heróis!")
nome = input("Digite o nome do herói: ")
xp = int(input("Digite a quantidade de XP do herói: "))


for nível in ["Ferro", "Bronze", "Prata", "Ouro", "Platina", "Ascendente", "Imortal", "Radiante"]:
    if xp < 0:
        print("XP inválido. O valor de XP não pode ser negativo.")
        xp = int(input("Digite a quantidade de XP do herói: "))
        break
if xp <= 1000:
    nível = "Ferro"
elif xp >= 1001 and xp <= 2000:
    nível = "Bronze"
elif xp >= 2001 and xp <= 5000:
    nível = "Prata"
elif xp >= 5001 and xp <= 7000:
    nível = "Ouro"
elif xp >= 7001 and xp <= 8000:
    nível = "Platina"  
elif xp >= 8001 and xp <= 9000:
    nível = "Ascendente"        
elif xp >= 9001 and xp <= 10000:
    nível = "Imortal"
else:
    nível = "Radiante"  

print(f"O Herói de nome {nome} está no nível {nível}.")

while True:
    resposta = input("Deseja classificar outro herói? (s/n): ").lower()
    if resposta == 's':
        nome = input("Digite o nome do herói: ")
        xp = int(input("Digite a quantidade de XP do herói: "))
        for nível in ["Ferro", "Bronze", "Prata", "Ouro", "Platina", "Ascendente", "Imortal", "Radiante"]:
            if xp < 0:
                print("XP inválido. O valor de XP não pode ser negativo.")
                xp = int(input("Digite a quantidade de XP do herói: "))
                break
        if xp <= 1000:
            nível = "Ferro"
        elif xp >= 1001 and xp <= 2000:
            nível = "Bronze"
        elif xp >= 2001 and xp <= 5000:
            nível = "Prata"
        elif xp >= 5001 and xp <= 7000:
            nível = "Ouro"
        elif xp >= 7001 and xp <= 8000:
            nível = "Platina"  
        elif xp >= 8001 and xp <= 9000:
            nível = "Ascendente"        
        elif xp >= 9001 and xp <= 10000:
            nível = "Imortal"
        else:
            nível = "Radiante"  

        print(f"O Herói de nome {nome} está no nível {nível}.")
    elif resposta == 'n':
        print("Encerrando o sistema de classificação de heróis. Até mais!")
        break
    else:
        print("Resposta inválida. Por favor, digite 's' para sim ou 'n' para não.")