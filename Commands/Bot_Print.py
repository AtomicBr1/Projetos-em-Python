import os
import pyautogui
import asyncio
import json
from telegram import Bot
from console_logging import console
from httpcore import ConnectTimeout
from httpx import ConnectTimeout as HTTPXConnectTimeout

with open('./configs/BotTelegram.json') as file:
    config = json.load(file)

token = config['TOKEN']
chatid = config['CHAT_ID']

def main():
    # Local onde a captura de tela será salva
    screenshot_path = 'screenshot.png'

    # Captura de tela
    pyautogui.screenshot(screenshot_path)

    # Função assíncrona para enviar a captura de tela
    async def send_screenshot():
        # Envia a captura de tela usando o bot do Telegram
        bot = Bot(token)

        try:
            with open(screenshot_path, 'rb') as photo:
                await bot.send_photo(chat_id=chatid, photo=photo)
        except (ConnectTimeout, HTTPXConnectTimeout):
            print('Erro de tempo limite durante o envio da captura de tela.')
        except Exception as e:
            print('Ocorreu um erro ao enviar a captura de tela:', str(e))

        # Remove o arquivo de captura de tela
        os.remove(screenshot_path)

    # Create and set the event loop explicitly
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # Executa a função assíncrona e aguarda a conclusão
    loop.run_until_complete(send_screenshot())
    loop.close()
    console.success('Print Enviado!')

def comandosbot():
    main()
