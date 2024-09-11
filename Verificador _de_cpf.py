# Primeira parte - validadendo se o cpf retorna 11 numeros
def Validarcpf01(cpf):

    # Primeiro digito final xxx.xxx.xxx-Xx
    soma = 0
    num_aux = 10
    for i in range(9):
        soma += int(cpf[i]) * num_aux
        num_aux -= 1
    digito_1 = 0 if (soma * 10) % 11 > 9 else (soma * 10) % 11

    # Segundo digito final xxx.xxx.xxx-xX
    # Usando as mesmas variaves por que o valor que preciso ja foi guardado
    soma = 0
    num_aux = 11
    for i in range(10):
        soma += int(cpf[i]) * num_aux
        num_aux -= 1
    digito_2 = 0 if (soma * 10) % 11 > 9 else (soma * 10) % 11
   

    if digito_1 == int(cpf[9]) and digito_2 == int(cpf[10]):
        print("CPF CORRETO", f"Final do cpf é {digito_1}{digito_2}", sep="\n")
    else:
        print("CPF INCORRETO", f"Final do cpf não é {digito_1}{digito_2}",\
              f"O CPF CORRETO DEVERIA SER: {''.join(cpf[:9]) }-{digito_1}{digito_2}",
              
              
               sep="\n")



cpf_numerico = []
# while True:
#     cpf_numerico = []
#     cpf_base = list(input("digite seu cpf: "))
#     for i in range(len(cpf_base)):
#         if cpf_base[i].isdigit():
#             cpf_numerico.append(cpf_base[i])
#     if (len(cpf_numerico) == 11):
#         Validarcpf01(cpf_numerico)
#         if 's' not in input("Testar outro CPF?"):
#             break
#     else:
#         print("Nao foi possivel validar os numeros do CPF \nTente novamente")


import random
cpf = ""
for _ in range(11):
    cpf += str(random.randint(0,9))

print(cpf)
Validarcpf01(list(cpf))








