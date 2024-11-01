def prog4():
    print ("Digite alguns números inteiros, cada um seguido de um enter, digite apenas enter para sair")

    soma = 0
    contador = 0

    while True:
        try:
            linha = input("Digite um inteiro: ")
            if linha == "": #Usuário só digitou enter
                break
            else: #Linha não vazia
                numero_int = int(linha)
                soma += numero_int
                #soma = soma + numero_int
                contador += 1
        except ValueError as VErr:
            pass
    print("Quantidade de números digitados: ", contador)
    print(f"Soma = {soma} e Media = {soma/contador}")

def prog5():
    print ("Digite alguns números inteiros, cada um seguido de um enter, digite apenas enter para sair")

    soma = 0
    contador = 0

    while True:
        try:
            linha = input("Digite um inteiro: ")
            if linha == "": #Usuário só digitou enter
                break
            else: #Linha não vazia
                numero_int = int(linha)
                soma += numero_int
                contador += 1
        except ValueError as VErr:
            print("Conversão impossível")
            print("Resposta: ", VErr)
            while True:
                print("É pra digitar um inteiro!")
                print("Digite novamente")
                try:
                    linha2 = input()
                    numero_int2 = int(linha2)
                except:
                    pass
                else:
                    numero_int=numero_int2
                    soma += numero_int
                    contador += 1
                    break
    
    print("Quantidade de números digitados: ", contador)
    print("Soma = {0} e Media = {1:.0f}".format(soma,(soma/contador)))

def prog6():
    print ("Digite alguns números inteiros, cada um seguido de um enter, digite apenas enter para sair")

    soma = 0
    contador = 0

    while True:
        try:
            linha = input("Digite um inteiro: ")
            if linha == "": #Usuário só digitou enter
                break
            else: #Linha não vazia
                numero_int = int(linha)
                soma += numero_int
                contador += 1
        except ValueError as VErr:
            print("Conversão impossível")
            print("Resposta: ", VErr)
            while True:
                print("É pra digitar um inteiro!")
                print("Digite novamente")
                try:
                    linha2 = input()
                    numero_int2 = int(linha2)
                except:
                    pass
                else:
                    numero_int=numero_int2
                    soma += numero_int
                    contador += 1
                    break
    '''
        #Uso de if
    if (contador): #O contador é diferente de 0
        print("Soma = {0} e Media = {1:.0f}".format(soma,(soma/contador)))
    else:
        print("Não há dados para calcular")
        # print("Digite uma das opções: ")
    '''
        #Uso de try-except
    try:
        print("Soma = {0} e Media = {1:.0f}".format(soma,(soma/contador)))
    except ZeroDivisionError:
        print("Não há dados para calcular")

def prog7():
    soma = 0
    contador = 0
    while True:
        try:
            linha = input()
            if linha == "": #Usuário só digitou enter
                break
            else: #Linha não vazia
                numero_int = int(linha)
                soma += numero_int
                contador += 1
        except EOFError:
            break
        except ValueError as VErr:
            print("Conversão impossível")
            print("Resposta: ", VErr)
            while True:
                print("É pra digitar um inteiro!")
                print("Digite novamente")
                try:
                    linha2 = input()
                    numero_int2 = int(linha2)
                except:
                    pass
                else:
                    numero_int=numero_int2
                    soma += numero_int
                    contador += 1
                    break
    '''
        #Uso de if
    if (contador): #O contador é diferente de 0
        print("Soma = {0} e Media = {1:.0f}".format(soma,(soma/contador)))
    else:
        print("Não há dados para calcular")
        # print("Digite uma das opções: ")
    '''
        #Uso de try-except
    try:
        print("Soma = {0} e Media = {1:.0f}".format(soma,(soma/contador)))
    except ZeroDivisionError:
        print("Não há dados para calcular")




if __name__=="__main__":
   prog7()

