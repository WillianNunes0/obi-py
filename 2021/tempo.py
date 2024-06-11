"""
Sara adora trocar mensagens com amigos. Como ela recebe e envia muitas mensagens, está preocupada com o tempo que seus amigos esperam para receber respostas das mensagens. As seguintes regras de etiqueta são sempre obedecidas:
as únicas mensagens que Sara envia são respostas a mensagens que ela recebeu.
Sara envia no máximo uma mensagem como reposta a uma mensagem que recebeu.
um amigo de Sara nunca envia uma nova mensagem para Sara até que tenha recebido resposta da mensagem que enviou anteriormente.
O aplicativo de mensagens que Sara e seus amigos usam recebe e envia mensagens instantaneamente. O envio e o recebimento de mensagens são chamados de eventos. O aplicativo registra cada evento na ordem em que os eventos ocorrem, usando dois tipos de registro:
R X indica que uma mensagem foi recebida do amigo X.
E X indica que uma mensagem foi enviada ao amigo X.
O aplicativo usa ainda um outro tipo de registro, para indicar o tempo que se passou entre dois eventos consecutivos, na forma
T X indicando que X segundos se passaram entre o evento anterior e o evento posterior a esse registro.
Se não há registro do tipo T X entre dois registros de eventos consecutivos significa que exatamente 1 segundo se passou entre esses dois eventos. O Tempo de Resposta de uma mensagem é o tempo que se passa entre o recebimento da mensagem por Sara e o envio da resposta a essa mensagem por Sara. Se um amigo recebeu respostas para todas as suas mensagens,
o Tempo de Resposta Total para esse amigo é a soma dos Tempos de Respostas para as mensagens desse amigo; caso contrário o Tempo de Resposta Total para esse amigo é -1. Dada a lista de registros do aplicativo de Sara, sua tarefa é determinar o Tempo de Resposta Total para cada amigo.
"""
registros = int(input())

tempo_de_resposta =  {}
esperando_resposta = {}
ultimo_tempo = 0

for _ in range(registros):
    entrada = input().split()
    tipo = entrada[0]
    x = int(entrada[1])

    if tipo == 'T':
        ultimo_tempo = ultimo_tempo + x - 1
    else:
        ultimo_tempo += 1
    
    if tipo == 'R':
        if x not in tempo_de_resposta:
            tempo_de_resposta[x] = 0
        esperando_resposta[x] = ultimo_tempo

    
    elif tipo == 'E':
        if x in esperando_resposta:
            tempo_de_resposta[x] = tempo_de_resposta + (ultimo_tempo-esperando_resposta[x])
            del esperando_resposta[x]

for amigo in esperando_resposta :
    tempo_de_resposta[amigo] = -1

for amigo in sorted(tempo_de_resposta.keys()):
    print(f'{amigo} {tempo_de_resposta[amigo]}')