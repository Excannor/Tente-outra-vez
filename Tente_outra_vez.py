from random import randint

title = '''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠘⢻⠟⠃⡿⠛⠃⣾⣧⢀⡇⠛⣿⠛⢱⡟⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⠀⢰⡏⠉⢀⡇⢹⣾⠁⢀⡟⠀⣸⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠁⠀⠈⠉⠉⠈⠁⠀⠉⠀⠈⠁⠀⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢀⡴⠶⢦⠀⣴⠀⢠⡆⠶⣶⠶⢠⡶⢶⡄⠀⣴⡆⠀⠀⢰⡆⠀⣴⢠⡶⠶⠰⠶⣶⠄⠀⠀
⠀⢸⠁⠀⣼⢠⡏⠀⣸⠁⢀⡏⠀⢸⠷⣞⠁⣼⣁⣿⠀⠀⠈⡇⡼⠁⣸⠓⠂⢀⡾⠁⠀⠀⠀
⠀⠘⠓⠚⠁⠈⠛⠚⠃⠀⠘⠃⠀⠛⠀⠛⠘⠁⠀⠙⠀⠀⠀⠛⠁⠀⠛⠛⠃⠛⠛⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'''
print (title)
print ('Seja Bem-vindo, tente a sorte ')
sorteado = randint(1, 100)
palpite = 0

while palpite != sorteado:
        palpite = int(input (' Escreva seu palpite: '))
        if palpite == sorteado:
            print ('Você venceu!')
        if palpite > sorteado:
            print ('Menor que', palpite)
        if palpite < sorteado:
            print ('Maior que', palpite)
print ('Fim do jogo!')
