import threading
import datetime
import time
import os
from Commands.Bot_Print import comandosbot
from Commands.clear import clear
from console_logging import console
from Commands.Mensagem import msgtelegram
from Commands.Mensagem import msgtelegram

agora = datetime.datetime.now()

# Obter a data e hora atual formatada
data_formatada = agora.strftime("%d/%m/%Y")
hora_formatada = agora.strftime("%H:%M:%S")

print("""
 _  _     _  _   ____   ____     _          _     
F L L]   FJ  L] /_  _\ F ___J   FJ         /.\    
J   \| L J |  | L[J  L]J |___:  J |        //_\\   
| |\   | | |  | | |  | | _____| | |       / ___ \  
F L\\  J F L__J J F  J F L____: F L_____ / L___J \ 
J__L \\__J\______/J____J________J________J__L   J__L
|__L  J__|J______F|____|________|________|__L   J__| 
                                                                                                                                
    """)

print('BOT INICIADO ÀS: ' + data_formatada + ' :: ' + hora_formatada + '\n\n')

def comandos():
    while True:
        comando = input('')

        # Executa o comando no CMD
        if comando != '' or comando != ' ' * 500:
            if comando == 'print':
                console.info('Enviando Print...')
                comandosbot()
                continue
            elif comando == 'clear':
                print('Limpando...')
                clear()
                continue
            elif comando == 'msg':
                msgtelegram()
                continue
            elif comando == 'stop':
                comandosbot()
                time.sleep(1)
                os._exit(1)
            else:
                console.error("Comando Invalido!")
                continue
        else:
            console.error("Comando Invalido!")
            continue

def printtochat():
    while True:
        msgtelegram()


# Iniciar a thread para comandos
monitoring_timer = threading.Thread(target= printtochat)
comands_thread = threading.Thread(target=comandos)

# Iniciar a thread de comandos e aguardar até que ela esteja em execução
comands_thread.start()
monitoring_timer.start()

# Aguardar a finalização da thread
monitoring_timer.join()