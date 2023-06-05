import sys
import telegram
import os
import time
import json
import asyncio
from datetime import datetime
from console_logging import console

with open('./configs/BotTelegram.json') as file:
    config = json.load(file)

TOKEN = config['TOKEN']
CHAT_ID = config['CHAT_ID']

log_filename = None

async def send_log_to_telegram(log_filename):
    # Verificar se o arquivo de log existe e não está vazio
    if os.path.isfile(log_filename) and os.path.getsize(log_filename) != 0:
        # Enviar o arquivo para o chat do Telegram
        bot = telegram.Bot(token=TOKEN)
        with open(log_filename, 'rb') as file:
            await bot.send_document(chat_id=CHAT_ID, document=file)

        # Excluir o arquivo
        os.remove(log_filename)
        console.success(f'LOG [{log_filename}] enviado!')
    else:
        console.info('Não Possui LOGS')
        os.remove(log_filename)
        time.sleep(1)

def msgtelegram():
    # Obter o timestamp atual
    current_time = datetime.now().strftime("%Y%m%d_%H%M%S")

    # Criar um novo nome de arquivo de log com base no timestamp
    log_filename = f"log_{current_time}.txt"

    # Redirecionar a saída padrão para o arquivo de log
    log_file = open(log_filename, 'w')
    sys.stdout = log_file
    
    try:
        time.sleep(30)
        # Restaurar a saída padrão para o console
        sys.stdout = sys.__stdout__

        # Fechar o arquivo de log
        log_file.close()

        # Enviar o conteúdo do arquivo de log para o Telegram
        asyncio.run(send_log_to_telegram(log_filename))

        # Obter um novo timestamp e nome de arquivo de log
        current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_filename = f"log_{current_time}.txt"

        # Redirecionar a saída padrão para o novo arquivo de log
        log_file = open(log_filename, 'w')
        sys.stdout = log_file

    except Exception as e:
         print(f"Ocorreu um erro: {str(e)}")

