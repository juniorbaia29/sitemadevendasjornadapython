#Passo a passo
#Titulo - sistema de vendas
#Seção cadastrar vendas
    #Campo de data
    #Campo Vendedor
    #Campo produto
    #Campo Quantidade
    #Campo Valor
    #Botão cadastrar venda
        #quando eu clicar no botão -> adicionar a venda na tabela
#Seção vendas cadastradas
    #tabela com as vendas
#Seção Dashboard
    #Card/Métrica -> Faturamento Total
    #Gráfico de Barra/Coluna -> Venda por vendedor
    #Gráfico de Pizza -> Venda por produto

#py -m pip install streamlit pandas plotly
#py -m streamlit run codigo.py
import streamlit as st
import pandas as pd 
import plotly.express as px
#hospedar no github -> github.com/usuario/repositorio


#carregar a base de dados
tabela_vendas=pd.read_csv('vendas.csv')
st.write('# Sistema de Vendas')
#st.navigate() -> cria uma barra de navegação no sistema,
    # onde podemos colocar as seções do sistema 
    
#Seção de cadatro de vendas
#O comando 'st.sidebar' cria uma barra lateral no sistema,
            #  onde podemos colocar os campos de cadastro
st.sidebar.write('## Cadastrar Vendas')
data=st.sidebar.date_input('Data da Venda',min_value=pd.to_datetime
                           ('today'),max_value=pd.to_datetime
                           ('today'))
#O comando min_value=pd.to_datetime('today')
    #  define a data mínima que pode ser selecionada no campo de data, 
    # que nesse caso é a data atual.
#vendedor=st.text_input('Vendedor') 
vendedor=st.sidebar.selectbox('Vendedor', ['Claudio', 'Junior', 'Patricia', 'Paty'])     
#produto=st.text_input('Produto')
produto=st.sidebar.selectbox('Produto', ['Produto A', 
                    'Produto B', 'Produto C', 'Produto D'])
quantidade=st.sidebar.number_input('Quantidade', min_value=1)
#valor=st.number_input('Valor', min_value=0.0, format="%.2f")  
valor=st.sidebar.number_input('VAlor',min_value=0.0, format="%.2f")
botão_cadastrar=st.sidebar.button('Cadastrar Venda') 

#logica para cadastrar a venda
if botão_cadastrar:
#if expoe o valor da venda for menor ou igual a zero, 
 #exibir um aviso (opicional)
# if valor == 0 or quantidade == 0 or vendedor == 0 or produto == 0:
#        st.warning('venda com erro de preenchimento, verifique os campos e tente novamente!')
 #   else:('O valor da venda deve ser maior que zero!')
    nova_venda=[str(data), vendedor, produto, quantidade,valor]
    #o comando 'str(data)' converte a data em string, para que 
    # possa ser salva na tabela
    ultima_linha=len(tabela_vendas)
    tabela_vendas.loc[ultima_linha]=nova_venda
    tabela_vendas.to_csv('vendas.csv', index=False)
#o comando 'index=False' evita que o índice da tabela seja salvo no
    #  arquivo CSV
    st.success('Venda cadastrada com sucesso!')
    
#seção de visualizar vendas
st.write('## Vendas Cadastradas')
st.dataframe(tabela_vendas)  

#Editar ou visualizar vendas
#id_venda=st.number_input('ID da Venda', step=1)
#botão_editar=st.button('Editar Venda')

#seçõa de Dashboard 
st.write('## Dashboard')
#Card/Métrica -> Faturamento Total
faturamento = tabela_vendas['valor'].sum()
st.metric('Faturamento Total', f'R$ {faturamento:.2f}')
#Gráfico de Barra/Coluna -> Venda por vendedor
grafico1 = px.bar(tabela_vendas, x='vendedor', y='valor',
                 color='produto')
st.plotly_chart(grafico1)

#Gráfico de Pizza -> Venda por produto
grafico2 = px.pie(tabela_vendas, names='produto', values='valor',
                hole=0.5)
#comando: color_discrete_map=[] edita as cores do grafico de pizza
#comando 'hole' cria um gráfico de pizza com buraco no meio, 
                # parecido com um gráfico de rosca
st.plotly_chart(grafico2)   
