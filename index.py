#Desafio Classificador de nivel de heroi em python

nome = str(input('Qual o nome do seu herói: '))

xp = int(input('Qual o nível de experiência do herói: '))

if  xp <= 1000:
    nivel = 'Ferro'
elif 1001 <= xp <= 2000:
    nivel = 'Bronze'
elif 2001 <= xp <= 5000:
    nivel = 'Prata'
elif 5001 <= xp <= 7000:
    nivel = 'Ouro'
elif 7001 <= xp <= 8000:
    nivel = 'Platina'
elif 8001 <= xp <= 9000:
    nivel = 'Ascendente'
elif 9001 <= xp <= 10000:
    nivel = 'Imortal'
elif xp >= 10001:
    nivel = 'Radiante'

print('O Herói {} está no nível de {}.' .format(nome, nivel))