print('--------------------Bem-vindo a financeira Abdalla!---------------------\n'
      '----------Aqui realizamos seu sonho sem comprometer seu bolso!----------')
financeira = input('Deseja simular o financiamento de um imóvel?(S/N) ').upper()
nome = input('Qual o seu nome? ').capitalize()
imovel = float(input('{}, Qual o valor do imóvel? '.format(nome)))
salario = float(input('{}, Qual seu rendimento mensal? '.format(nome)))
while financeira == 'S':
    tempo = int(input('{}, em quantos anos deseja pagar o imóvel? '.format(nome)))
    prestacao = imovel / (tempo * 12)
    if (salario * 30) / 100 >= prestacao:
        print('Financimento aprovado')
        print('As prestações mensais serão dê {} durante {} anos '.format((salario * 30) / 100, tempo))
        break
    elif (salario * 30) / 100 < prestacao:
        print('Infelizmente o financiamento foi negado.')
        print('Tente novamente aumentando a quantidade de anos a pagar, '
                'não podemos de forma alguma comprometer tanto sua renda.')
        financeira = input('Deseja cotar novamente?(S/N) ').upper()