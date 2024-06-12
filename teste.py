def zerar_matriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])
    return [["" for _ in range(colunas)] for _ in range(linhas)]

# explicando o jogo
print("O Jogo da velha consiste em completar uma sequência de três números, sejam eles na diagonal, na vertical ou horizontal.")
print("A sacada do jogo está em não deixar seu adversário completar a tripla dele enquanto você completa a sua.")
print("As posições do jogo são as seguintes:")
matriz_posicao = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"{matriz_posicao[0]}")
print(f"{matriz_posicao[1]}")
print(f"{matriz_posicao[2]}")

print("Para realizar a jogada, digite o número da posição desejada")

matriz = zerar_matriz(matriz_posicao)
#matriz zerada para iniciar o jogo

cont = 0
while cont<9:
    #iniciando jogada do Jogador X)
    print("O jogador X irá jogar")
    posicao = int(input("Digite a posição da jogada: "))
    if posicao == 1:
        if matriz[0][0] == "":  
            matriz[0][0] = "X"
        else:
            print("Posição Inválida, Perdeu a jogada.")

    if posicao == 2:
        if matriz[0][1] == "":  
            matriz[0][1] = "X"
        else:
            print("Posição Inválida, Perdeu a jogada.")

    if posicao == 3:
        if matriz[0][2] == "":  
            matriz[0][2] = "X"
        else:
            print("Posição Inválida, Perdeu a jogada.")

    if posicao == 4:
        if matriz[1][0] == "":  
            matriz[1][0] = "X"
        else:
            print("Posição Inválida, Perdeu a jogada.")

    if posicao == 5:
        if matriz[1][1] == "":  
            matriz[1][1] = "X"
        else:
            print("Posição Inválida, Perdeu a jogada.")

    if posicao == 6:
        if matriz[1][2] == "":  
            matriz[1][2] = "X"
        else:
            print("Posição Inválida, Perdeu a jogada.")

    if posicao == 7:
        if matriz[2][0] == "":  
            matriz[2][0] = "X"
        else:
            print("Posição Inválida, Perdeu a jogada.")

    if posicao == 8:
        if matriz[2][1] == "":  
            matriz[2][1] = "X"
        else:
            print("Posição Inválida, Perdeu a jogada.")

    if posicao == 9:
        if matriz[2][2] == "":  
            matriz[2][2] = "X"
        else:
            print("Posição Inválida, Perdeu a jogada.")

    #verificando status
    if (matriz[0][0] == "X" and matriz[0][1] == "X" and matriz[0][2] == "X"): #posições 123
        print("O jogador X venceu!!")
        break
    elif (matriz[1][0] == "X" and matriz[1][1] == "X" and matriz[1][2] == "X"): #posições 456
        print("O jogador X venceu!!")
        break
    elif (matriz[2][0] == "X" and matriz[2][1] == "X" and matriz[2][2] == "X"): #posições 789
        print("O jogador X venceu!!")
        break
    elif (matriz[0][0] == "X" and matriz[1][0] == "X" and matriz[2][0] == "X"): #posicoes 147
        print("O jogador X venceu!!")
        break
    elif (matriz[0][1] == "X" and matriz[1][1] == "X" and matriz[2][1] == "X"): #258
        print("O jogador X venceu!!")
        break
    elif (matriz[0][2] == "X" and matriz[1][2] == "X" and matriz[2][2] == "X"):#369
        print("O jogador X venceu!!")
        break
    elif (matriz[0][0] == "X" and matriz[1][1] == "X" and matriz[2][2] == "X"):#159
        print("O jogador X venceu!!")
        break
    elif (matriz[0][2] == "X" and matriz[1][1] == "X" and matriz[2][0] == "X"):#357
        print("O jogador X venceu!!")
        break

    for l in range(3):
        for c in range(3):
            print(f'[{matriz[l][c]: ^5}]', end='')
        print('')
    cont += 1
    if cont==9:
        print("Deu velha! fim de jogo...")
        break
    

    #iniciando jogada do Jogador O)
    print("O jogador O irá jogar")
    posicao = int(input("Digite a posição da jogada: "))
    if posicao == 1:
        if matriz[0][0] == "":  
            matriz[0][0] = "O"
        else:
            print("Posição Inválida, Perdeu a jogada.")

    if posicao == 2:
        if matriz[0][1] == "":  
            matriz[0][1] = "O"
        else:
            print("Posição Inválida, Perdeu a jogada.")

    if posicao == 3:
        if matriz[0][2] == "":  
            matriz[0][2] = "O"
        else:
            print("Posição Inválida, Perdeu a jogada.")

    if posicao == 4:
        if matriz[1][0] == "":  
            matriz[1][0] = "O"
        else:
            print("Posição Inválida, Perdeu a jogada.")

    if posicao == 5:
        if matriz[1][1] == "":  
            matriz[1][1] = "O"
        else:
            print("Posição Inválida, Perdeu a jogada.")

    if posicao == 6:
        if matriz[1][2] == "":  
            matriz[1][2] = "O"
        else:
            print("Posição Inválida, Perdeu a jogada.")

    if posicao == 7:
        if matriz[2][0] == "":  
            matriz[2][0] = "O"
        else:
            print("Posição Inválida, Perdeu a jogada.")

    if posicao == 8:
        if matriz[2][1] == "":  
            matriz[2][1] = "O"
        else:
            print("Posição Inválida, Perdeu a jogada.")

    if posicao == 9:
        if matriz[2][2] == "":  
            matriz[2][2] = "O"
        else:
            print("Posição Inválida, Perdeu a jogada.")

    #verificando status
    if (matriz[0][0] == "O" and matriz[0][1] == "O" and matriz[0][2] == "O"):
        print("O jogador O venceu!!")
        break
    elif (matriz[1][0] == "O" and matriz[1][1] == "O" and matriz[1][2] == "O"):
        print("O jogador O venceu!!")
        break
    elif (matriz[2][0] == "O" and matriz[2][1] == "O" and matriz[2][2] == "O"):
        print("O jogador O venceu!!")
        break
    elif (matriz[0][0] == "O" and matriz[1][0] == "O" and matriz[2][0] == "O"):
        print("O jogador O venceu!!")
        break
    elif (matriz[0][1] == "O" and matriz[1][1] == "O" and matriz[2][1] == "O"):
        print("O jogador O venceu!!")
        break
    elif (matriz[0][2] == "O" and matriz[1][2] == "O" and matriz[2][2] == "O"):
        print("O jogador O venceu!!")
        break
    elif (matriz[0][0] == "O" and matriz[1][1] == "O" and matriz[1][1] == "O"):
        print("O jogador O venceu!!")
        break
    elif (matriz[0][2] == "O" and matriz[1][1] == "O" and matriz[2][0] == "O"):
        print("O jogador O venceu!!")
        break

    for l in range(3):
        for c in range(3):
            print(f'[{matriz[l][c]: ^5}]', end='')
        print('')
    cont += 1

    
    