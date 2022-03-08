# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 17:17:45 2022

@author: Bruno Michelson
"""
# Global 
import smtplib
import email.message

import pandas as pd
dados = pd.read_csv('C:/Users/Acer/Documents/scripts/emails.csv')

cornos = dados['contas']

tam = len(cornos)

class Main():
    
    print(cornos)
    
    def enviar_email():
        for i in range(0, tam):
            corpo_email = """
            <b><p>Caros calouros, welcome to the hell!</p></b>
            <p>Aos que cairam de paraquedas e aos que entraram convictos em cursar geofísica (loucos), sejam todos muito bem-vindos!</p>
            <p>O Centro Acadêmico de geofísica (CAGef-UFRN) tem como objetivo representar os alunos no departamento de Geofísica - DGef. 
            Conversaremos em breve sobre os trabalhos do CA. Qualquer dúvida, curiosidade e dicas sobre o curso, entrem em contato conosco.</p>
            <p>Nós da equipe do CAGef aguardaremos vocês atras do link do whatsapp. Segue o link para acesso aos grupos no WhatsApp:</p>
            <b><a href="https://chat.whatsapp.com/C6zzdvvzB5cLc4JIg8jusH">Whatsapp_Grupo</a></p></b>
            <style>
                a{
                    text-decoration: none;
                    background-color: yellow;
                    color: red;
                    border: 1px solid blue
                    padding:3px 5px;
                    }
            </style>
            <p>Enfim, parabéns a todos vocês!</p>
            <p>Assinado,</p>
            <p>Sophia Bezares(Presidente)</p>
           """
            msg = email.message.Message()
            assunto = 'Boas vindas'
            msg ["Subject"] = assunto
            msg ['From'] = 'cageofisicaufrn@gmail.com'
        
            msg ['Cc'] = cornos[i]
                
            password = 'geofisica2018'
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(corpo_email)
                
            s = smtplib.SMTP('smtp.gmail.com: 587')
            s.starttls()
            #login Credentials for sending the email
            s.login(msg['From'], password)
            s.sendmail(msg['From'], msg['Cc'], msg.as_string().encode('utf-8'))
            print('Enviado com sucesso!')
            


    '''def deleting():
        return cornos.pop(0)
    deleting()'''
        

Main.enviar_email()

'''for i in range(0, tam):
    Main()'''
    

    
        

  
    