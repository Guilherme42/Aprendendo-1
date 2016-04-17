pessoas = {}
total = 0.0
print 'Digite os nomes seguidos de [ENTER] '
print 'entao digite os gastos seguidos de [ENTER].'
print 'Para encerrar deixe um nome em branco'
while(1):
    nome = raw_input('Digite um nome : ')
    if not nome:
        break
    while 1:
        resposta = raw_input('Quanto ele(a) gastou ? ')
        try:
            gasto = float(resposta)
            break
        except:
            print 'Numero invalido.'
    pessoas[nome] = gasto
    total = total + gasto

num_pessoas = len(pessoas)
print
print 'Total de pessoas : %d' % num_pessoas
print 'Total de gastos  : %d' % total
media = total / num_pessoas
print 'Gastos medios por pessoas : %d' % media
print
for nome in pessoas.keys():
    saldo = pessoas[nome] - media
    print 'Saldo de %s: %.2f' % (nome, saldo)