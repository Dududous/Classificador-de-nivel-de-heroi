nome = input('Digite o nome do herói: ')
xp = int(input("Digite a quantidade de Xp do herói: "))

if xp <= 1000:
    print(f"O Herói de nome {nome} está no nível de Ferro")
elif xp <= 2000:
    print(f"O Herói de nome {nome} está no nível de Bronze")
elif xp <= 5000:
    print(f"O Herói de nome {nome} está no nível de Prata")
elif xp <= 7000:
    print(f"O Herói de nome {nome} está no nível de Ouro")
elif xp <= 8000:
    print(f"O Herói de nome {nome} está no nível de Platina")
elif xp <= 9000:
    print(f"O Herói de nome {nome} está no nível de Ascendente")
elif xp <= 10000:
    print(f"O Herói de nome {nome} está no nível de Imortal")
elif xp > 10000:
    print(f"O Herói de nome {nome} está no nível de Radiante")                