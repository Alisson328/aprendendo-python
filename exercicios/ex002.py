'''
Simplifica uma fração dada
'''

def entrada():
    numerador = int(input('Numerador da fração: '))
    denominador = int(input('Denominador da fração: '))
    print('')
    return numerador,denominador

def calculos(n,d):
    restos = ['none']
    # queria que o índice fosse de acordo com o divisor, e não existe divisão por 0
    divisores = 0    
    controle = 0
    controle2 = -1

    while controle<1000:
        controle+=1        
        agregador = []
        agregador.append(n%controle)
        agregador.append(d%controle)
        restos.insert(controle,agregador)        

    for num in restos:
        controle2+=1
        if num[0]==0 and num[1]==0:
            divisores=controle2
    numeSimplificado = int(n/divisores)
    denoSimplificado = int(d/divisores)

    return divisores,restos,numeSimplificado,denoSimplificado

def saida(nume,deno,divi,numeS,denoS):
    print('A fração {}/{} pode ser simplificada por: {}'.format(nume,deno,divi))
    print('Fração simplificada: {}/{}'.format(int(nume/divi),int(deno/divi)))
    print('')

    print('Teste real: ')
    primeiraFrac = '{}/{} = {:.3f}'
    segundaFrac = '{}/{} = {:.3f}'
    print(primeiraFrac.format(nume,deno,numeS/denoS))
    print(segundaFrac.format(numeS,denoS,numeS/denoS))

numerador,denominador = entrada()
divisores,restos,numeSimplificado,denoSimplificado = calculos(numerador,denominador)
saida(numerador,denominador,divisores,numeSimplificado,denoSimplificado)