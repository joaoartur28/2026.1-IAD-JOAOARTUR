nome_arquivo = input("Digite o nome do arquivo:")

try:
    arquivo = open(nome_arquivo)
    
    arquivo.readline()
    
    producao_linhas = {}
    
    for linha in arquivo:
        linha_limpa = linha.strip()
        
        if linha_limpa:
            dados = linha_limpa.split()
            
            codigo_linha = dados[0]
            qtd_produzida = int(dados[2]) 
            
            if codigo_linha in producao_linhas:
                producao_linhas[codigo_linha] = producao_linhas[codigo_linha] + qtd_produzida
            else:
                producao_linhas[codigo_linha] = qtd_produzida
                
    arquivo.close()
    
    for codigo, total_produzido in producao_linhas.items():
        print(f"{codigo} {total_produzido}")

except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado.")