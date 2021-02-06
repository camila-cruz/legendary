import re
from datetime import datetime, date, time, timedelta
from math import fabs

SUB_REGEX = r"((\d+:)+\d+,\d+)"
ENCODING = 'utf-8'
UNIDADES = ['horas', 'minutos', 'segundos', 'microssegundos']
intervalos_iniciais = []
intervalos_alterados = []

# Abre o arquivo de legenda e lê todas as linhas buscando intervalos
def abrir_arquivo(nome_do_arquivo):
    with open(nome_do_arquivo, encoding=ENCODING) as arquivo:
        for linha in arquivo:
            separar_intervalos(linha, intervalos_iniciais)

# Recorta os intervalos de tempo de cada legenda
def separar_intervalos(linha, intervalos):
    intervalo = re.findall(SUB_REGEX, linha)
    if (intervalo):
        intervalos.append([intervalo[0][0], intervalo[1][0]])

# Atualiza os intervalos no arquivo da legenda
def atualizar_intervalos(nome_do_arquivo_atual, nome_do_novo_arquivo):
    """
        Copia o arquivo de legenda para outro arquivo com o tempo dos intervalos modificados
    """
    cont = 0
    with open(nome_do_arquivo_atual, 'r',  encoding=ENCODING) as arquivo_existente, open(nome_do_novo_arquivo, 'w',  encoding=ENCODING) as novo_arquivo:
        for linha in arquivo_existente.readlines():
            intervalo = re.findall(SUB_REGEX, linha)
            if (intervalo):
                aux = intervalos_alterados[cont]
                novo_arquivo.write(aux[0] + ' --> ' + aux[1] + '\n')
                cont += 1
            else:
                novo_arquivo.write(linha)
            
# Passa por cada intervalo pra alterar o tempo
def alterar_intervalos(diff):
    """
        Passa por todos os intervalos para modificar o tempo de cada pelo que o usuário inseriu. 
    """
    if not diff:
        return

    for intervalos in intervalos_iniciais:
        # print(intervalos)
        novos_intervalos = []
        for intervalo in intervalos:
            novo_intervalo = modificar_tempo_intervalo(intervalo, diff)
            novos_intervalos.append(novo_intervalo)
            
        intervalos_alterados.append(novos_intervalos)
    
# Recebe os segundos que serão adicionados ou removidos de cada intervalo
def modificar_tempo_intervalo(intervalo, diff):
    """
        Realiza, no intervalo, a soma ou a subtração do tempo informado pelo usuário.
    """
    operacao = 'soma' if diff > 0 else 'subtracao'

    intervalo = formata_intervalo_para_tempo(intervalo)
    diff = formata_alteracao_de_tempo(diff)

    if operacao == 'soma':
        novo_intervalo = intervalo + diff
    else:
        novo_intervalo = intervalo - diff

    return formata_tempo_para_intervalo(novo_intervalo)

# Exibe os intervalos de início e fim de cada legenda
def mostrar_intervalos():
    for i in intervalos_iniciais:
        print (i)

def formata_intervalo_para_tempo(intervalo):
    """
        Formata o tempo da legenda em um objeto datetime.timedelta. Obs.: no tempo da legenda, os microssegundos 
        vão de 0 a 999; no objeto datetime.timedelta, vai de 0 a 999999. 
    """
    intervalo += '000'
    legenda = intervalo.replace(',', ':').split(':')
    legenda = list(map(int, legenda))   # Map function

    t = dict(zip(UNIDADES, legenda))

    tempo = timedelta(hours=t['horas'], minutes=t['minutos'], seconds=t['segundos'], microseconds=t['microssegundos'])
    # print(tempo)

    return tempo

def formata_tempo_para_intervalo(tempo):
    """
        Formata o tempo do tipo datetime.timedelta em uma String.
    """
    # Tira os últimos 3 caracteres que são os zeros
    intervalo = str(tempo).replace('.', ',')[:-3]   
    
    # Deixa as horas no formato HH
    horas = '0' if len(intervalo.split(':')[0]) < 2 else ''
    
    return horas + intervalo

def formata_alteracao_de_tempo(diff):
    """
        Formata a alteração de tempo na legenda informada pelo usuário para um objeto datetime.timedelta.
    """

    qtd_digitos_microsseg_timedelta = 6
    
    # Divide o número em strings com cada unidade de tempo
    # TODO: e se for separado por vírgula? Colocar um try-except
    diff = str(fabs(diff)).split('.')

    # diff[-1] é a posição dos microssegundos
    while len(diff[-1]) < qtd_digitos_microsseg_timedelta:
        diff[-1] += '0'

    diff = list(map(int, diff))
    d = dict(zip(UNIDADES[2:4], diff))

    tempo = timedelta(seconds=d['segundos'], microseconds=d['microssegundos'])
    # print(tempo)
    
    return tempo
