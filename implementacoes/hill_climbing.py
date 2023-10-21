def hill_climbing(func, root):
    mutations = [100,50,25,10,5,1,0.5,0.1,0.0005]

    best_x = root

    while True:
        melhor_mutacao = best_x
        for m in mutations:
            novo_x = best_x + m

            if abs(func(best_x - m)) < abs(func(novo_x)):
                novo_x = best_x - m

            if abs(func(melhor_mutacao)) > abs(func(novo_x)):
                melhor_mutacao = novo_x


        if abs(func(melhor_mutacao)) < abs(func(best_x)):
            best_x = melhor_mutacao
            print(f'Melhor x encontrado: {best_x}')
        else:
            break
                


    return best_x



def funcao(x):
    return x**2 + 50*x + 50

best_x = hill_climbing(funcao, -137)

print(f'x: {best_x} y: {funcao(best_x)}')
