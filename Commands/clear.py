import datetime

agora = datetime.datetime.now()

# Obter a data e hora atual formatada
data_formatada = agora.strftime("%d/%m/%Y")
hora_formatada = agora.strftime("%H:%M:%S")

def clear():
    print("\n" * 130)
    
    print("""
    _  _     _  _   ____   ____     _          _     
   F L L]   FJ  L] /_  _\ F ___J   FJ         /.\    
  J   \| L J |  | L[J  L]J |___:  J |        //_\\   
  | |\   | | |  | | |  | | _____| | |       / ___ \  
  F L\\  J F L__J J F  J F L____: F L_____ / L___J \ 
 J__L \\__J\______/J____J________J________J__L   J__L
 |__L  J__|J______F|____|________|________|__L   J__|
                                                                                                                                                             
    """)

    print('         BOT INICIADO ÀS: ' + data_formatada + ' :: ' + hora_formatada + '\n\n\n')
    print('\n' * 3)