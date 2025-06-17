nota1 = input("insira a 1ª nota aqui:")
nota1 = float(nota1)

nota2 = input("insira a 2ª nota aqui:")
nota2 = float(nota2)

media = (nota1+nota2)/2
media = float(media)
print("Sua média é de:", media)

if media >=6:
    print("Status: Aprovado")
else:
    print("Status: Reprovado")