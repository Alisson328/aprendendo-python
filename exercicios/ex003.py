def entrada():
    dia = int(input('Entre o dia: '))
    while dia<0 or dia>31:
        print('Valor inválido, tente novamente.')        
        dia = int(input('Entre o dia: '))

    mes = int(input('Entre o mês: '))
    while mes<=0 or mes>12:
        print('Valor inválido, tente novamente. ')
        mes = int(input('Entre o mês: '))

    ano = int(input('Entre o ano: '))    

    return dia,mes,ano

def conversao(d,m,a):
    listaMeses = ['none','Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']    
    # para que o índice seja de acordo com o mês, por isso 'none'
    mesConvertido = listaMeses[m]
    saida = '{dia} de {mes} de {ano}'
    print(saida.format(dia=d,mes=mesConvertido,ano=a))

dia,mes,ano = entrada()
conversao(dia,mes,ano)