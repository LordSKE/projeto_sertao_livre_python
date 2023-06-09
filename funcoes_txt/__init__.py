def salvarArquivos(arquivo, login):
    f = open(f'produtos_{login}.txt', 'a')
    f.write(arquivo)
    f.close()
    
def salvarProdutos(lista, login):
    for produtos in lista:
        if(produtos['Vendedor'] == login):
            nome = produtos['Modelo']
            valor = produtos['Valor']
            qtde = produtos['Quantidade']
            
            arquivo = f'Nome do produto - {nome}\n'
            arquivo = arquivo + f'Valor do produto - {valor}\n'
            arquivo = arquivo + f'Quantidade do produto - {qtde}\n\n'
            
            salvarArquivos(arquivo, login)
            
def lerArquivo(login):
    f = open(f'produtos_{login}.txt', 'r')
    print(40*'=')
    for linha in f.readlines():
        print(linha, end='')
    f.close()