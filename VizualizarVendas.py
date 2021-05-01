'''
ler 6 arquivos de excel e procurar na coluna vendas onde vendas foi maior que 55000,
se encontrar vendas maior que 55000 mostrar o mês, o valor de vendas, e o nome do vendedor, 
após isso, enviar um SMS avisando que alguém bateu a meta!
'''

import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACa7ac3ece159597c38e4c8ec7feb5bc45"
# Your Auth Token from twilio.com/console
auth_token  = "30739debbabba98430c3119d5ac38f3c"

client = Client(account_sid, auth_token)

#lista os meses do excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

#verifica cada mes da planilha do excel
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    #se na coluna vendas, as venda forem maiores que 55000 mil em qualquer lugar
    if(tabela_vendas['Vendas'] > 55000).any():
        #localizar o vendedor que teve venda maior que 55000
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        #localizar o valor da venda que foi maior que 55000
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        #mostra a mensagem
        #envia uma mensagem caso bata a meta
        message = client.messages.create(
            #aqui é necessário inclui o número que foi cadastrado no twilio, que quer receber mensagem
            to="+55", 
            #numero gerado pelo twilio para envio de mensagens
            from_="+12313548554",
            #texto da mensagem que vai ser enviada
            body=f'No mês {mes} alguém atingiu a meta,fez R${vendas:.2f} mil em vendas! Vendedor(a): {vendedor}')
        #caso isso seja printado a mensagem foi enviada!
        print(message.sid)
