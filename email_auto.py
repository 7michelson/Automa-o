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
import senha as UU

import pandas as pd
dados = pd.read_excel('C:/Users/Acer/Documents/scripts/Contatos Ingressantes 2022.1_Inscristos Até 09032022.xlsx')

contatos = dados['E-mail']


class Run_code():
    
    def __init__(self):
        self.tam = len(contatos)
    
    def enviar_email_1(self):
        print(contatos)
        for i in range(0, 15):
            corpo_email = '''
            <center><b><p>🙇🏻‍♂️Caros calouros, welcome to the family(hell)!🙇🏻‍♂️</p></b></center>
            <p>Aos que cairam de paraquedas e aos que entraram convictos em cursar geofísica (loucos), sejam todos muito bem-vindos!</p>
            <p>O Centro Acadêmico de geofísica (CAGef-UFRN) tem como objetivo representar os alunos no departamento de Geofísica - DGef. 
            Conversaremos em breve sobre os trabalhos do CA. Qualquer dúvida, curiosidade e dicas sobre o curso, entrem em contato conosco.</p>
            <p>Nós da equipe do CAGef aguardaremos vocês através do link do whatsapp. Segue o link para acesso aos grupos no WhatsApp:
            <b><a href="https://chat.whatsapp.com/C6zzdvvzB5cLc4JIg8jusH">Whatsapp_Grupo</a></p></b></p>
            <p></p>
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
            msg ["Subject"] = assunto
            msg ['From'] = UU.meu_email
        
            msg ['To'] = UU.exemplo_email
            msg ['Cc'] = contatos[i]
                
            password = UU.senha
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(corpo_email)
                
            s = smtplib.SMTP('smtp.gmail.com: 587')
            s.starttls()
            #login Credentials for sending the email
            s.login(msg['From'], password)
            s.sendmail(msg['From'], msg['Cc'] and msg['To'], msg.as_string().encode('utf-8'))
            print('Enviado com sucesso!')

    def enviar_email_2(self):

        for i in range(15, self.tam):
            corpo_email = '''
                <center><b><p>🙇🏻‍♂️Caros calouros, welcome to the family(hell)!🙇🏻‍♂️</p></b></center>
                <p>Aos que cairam de paraquedas e aos que entraram convictos em cursar geofísica (loucos), sejam todos muito bem-vindos!</p>
                <p>O Centro Acadêmico de geofísica (CAGef-UFRN) tem como objetivo representar os alunos no departamento de Geofísica - DGef. 
                Conversaremos em breve sobre os trabalhos do CA. Qualquer dúvida, curiosidade e dicas sobre o curso, entrem em contato conosco.</p>
                <p>Nós da equipe do CAGef aguardaremos vocês através do link do whatsapp. Segue o link para acesso aos grupos no WhatsApp:
                <b><a href="https://chat.whatsapp.com/C6zzdvvzB5cLc4JIg8jusH">Whatsapp_Grupo</a></p></b></p>
                <p></p>
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
            msg["Subject"] = assunto
            msg['From'] = UU.meu_email

            msg['To'] = UU.exemplo_email
            msg['Cc'] = contatos[i]

            password = UU.senha
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(corpo_email)

            s = smtplib.SMTP('smtp.gmail.com: 587')
            s.starttls()
                # login Credentials for sending the email
            s.login(msg['From'], password)
            s.sendmail(msg['From'], msg['Cc'] and msg['To'], msg.as_string().encode('utf-8'))
            print('Enviado com sucesso!')
        # fim!

go = Run_code()
go.enviar_email_1()
go.enviar_email_2()
