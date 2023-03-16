# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 17:17:45 2022

Obs: esse bot só consegue enviar no máximo 15 emails antes do servidor conectar, por isso a solução foi criar outra
função que faz a mesma coisa, porém com emails diferentes. Os emails são capturados através de um arquivo excel e
jogaddo numa lista. Atenção para a lista e seus respectivos indices acessado pelo laço(for).

@author: Bruno Michelson
"""

import smtplib
import email.message
import senha as sh
import pandas as pd

dados = pd.read_csv('C:/Users/Acer/Documents/scripts/ingressantes2023.csv')
contatos = dados['E-mail']
print(contatos[0:25])
#print(contatos[13:25])

class Run_code():
    
    def __init__(self):
        self.tam = len(contatos)
    
    def enviar_email_1(self):
        print(contatos)
        for i in range(0, 16):
            corpo_email = '''
            <center><b><p>🙇🏻‍♂️Caros calouros, welcome to the family(hell)!🙇🏻‍♂️</p></b></center>
            <p>Aos que cairam de paraquedas e aos que entraram convictos em cursar geofísica (loucos), sejam todos muito bem-vindos!</p>
            <p>O Centro Acadêmico de geofísica (CAGef-UFRN) tem como objetivo representar os alunos no departamento de Geofísica - DGef. 
            Conversaremos em breve sobre os trabalhos do CA. Qualquer dúvida, curiosidade e dicas sobre o curso, entrem em contato conosco.</p>
            <p>Nós da equipe do CAGef aguardaremos vocês através do link do whatsapp. Segue o link para acesso aos grupos no WhatsApp:
            <b><a href='https://chat.whatsapp.com/JcNOTxilFsfDyagAFN6ktn'>Whatsapp_Grupo</a></p></b></p>
            <p></p>
            <p>A melhor forma de vós conheres é marcando uma reunião com todos na Sexta-feira 17/03/2023, auditório do DEGEF 13:30 H.</p>
            <p>Obs: Para de participar da nossa dinâmica, apenas copie e cole no zap o seguinte texto;</p>
            <p><b>💙*Formulário para Calouros da UFRN se apresentarem*💙</b></p>
            <p><b>*Nome:</b><p/>
            <p><b>*Apelidos:*</b></p>
            <p><b>*Idade:*</b></p>
            <p><b>*Cidade*</b></p>
            <p><b>*Cantor(a)/Banda favorita:*</b></p>
            <p><b>*Estado cívil:*</b></p>
            <p><b>*Sexualidade(se quiser):*</b></p>
            <p><b>*Expectativas do curso:*</b></p>
            <p><b>*Aleatoridade sobre você:*</b></p>
            <p><b>*Instagram:*</b></p>
            <p><b>*Foto(opcional):*</b></p>
            
            
            <center><p>Enfim, parabéns a todos vocês!</p>
            <p>Assinado;</p>
            <p>Sophia Bezares   | Presidente</p>
            <p>João Paulo   | Vicepresidente</p>
            <p>Bruno Michelson  | Diretor de políticas estudantis</p></center>
            '''
            msg = email.message.Message()
            assunto = 'Boas vindas'
            msg ['Subject'] = assunto
            msg ['From'] = sh.meu_email
        
            msg ['To'] = contatos[i]
            msg ['Cc'] = sh.exemplo_email
                
            password = sh.senha
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(corpo_email)
                
            #s = smtplib.SMTP('smtp.gmail.com: 587')
            s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
            s.starttls()
            #login Credentials for sending the email
            s.login(msg['From'], password)
            s.sendmail(msg['From'], msg['Cc'], msg.as_string().encode('utf-8'))
            print('Enviado com sucesso!')
            s.close()

    def enviar_email_2(self):

        for i in range(25, self.tam):
            corpo_email = '''
                <center><b><p>🙇🏻‍♂️Caros calouros, welcome to the family(hell)!🙇🏻‍♂️</p></b></center>
                <p>Aos que cairam de paraquedas e aos que entraram convictos em cursar geofísica (loucos), sejam todos muito bem-vindos!</p>
                <p>O Centro Acadêmico de geofísica (CAGef-UFRN) tem como objetivo representar os alunos no departamento de Geofísica - DGef. 
                Conversaremos em breve sobre os trabalhos do CA. Qualquer dúvida, curiosidade e dicas sobre o curso, entrem em contato conosco.</p>
                <p>Nós da equipe do CAGef aguardaremos vocês através do link do whatsapp. Segue o link para acesso aos grupos no WhatsApp:
                <b><a href='https://chat.whatsapp.com/JcNOTxilFsfDyagAFN6ktn'>Whatsapp_Grupo</a></p></b></p>
                <p></p>
                <p>A melhor forma de vós conheres é marcando uma reunião com todos na Sexta-feira 17/03/2023, auditório do DEGEF 13:30 H.</p>
                <p>Obs: Para de participar da nossa dinâmica, apenas copie e cole no zap o seguinte texto;</p>
                <p><b>💙*Formulário para Calouros da UFRN se apresentarem*💙</b></p>
                <p><b>*Nome:</b><p/>
                <p><b>*Apelidos:*</b></p>
                <p><b>*Idade:*</b></p>
                <p><b>*Cidade*</b></p>
                <p><b>*Cantor(a)/Banda favorita:*</b></p>
                <p><b>*Estado cívil:*</b></p>
                <p><b>*Sexualidade(se quiser):*</b></p>
                <p><b>*Expectativas do curso:*</b></p>
                <p><b>*Aleatoridade sobre você:*</b></p>
                <p><b>*Instagram:*</b></p>
                <p><b>*Foto(opcional):*</b></p>


                <center><p>Enfim, parabéns a todos vocês!</p>
                <p>Assinado;</p>
                <p>Sophia Bezares   | Presidente</p>
                <p>João Paulo   | Vicepresidente</p>
                <p>Bruno Michelson  | Diretor de políticas estudantis</p></center>
                '''
            msg = email.message.Message()
            assunto = 'Boas vindas'
            msg['Subject'] = assunto
            msg['From'] = sh.meu_email

            msg['To'] = contatos[i]
            msg['Cc'] = sh.exemplo_email

            password = sh.senha
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(corpo_email)

            s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
            s.starttls()
                # login Credentials for sending the email
            s.login(msg['From'], password)
            s.sendmail(msg['From'], msg['Cc'], msg.as_string().encode('utf-8'))
            print('Enviado com sucesso!')
            s.close()
    # fim!

go = Run_code()
#go.enviar_email_1()
go.enviar_email_2()
