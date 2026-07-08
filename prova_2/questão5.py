nome_arquivo = input("Digite o nome do arquivo:")

try:
    arquivo = open(nome_arquivo)
    
    arquivo.readline()
    
    contagem_linhas = {}
    
    for linha in arquivo:
        linha_limpa = linha.strip()
        
        if linha_limpa:
            dados = linha_limpa.split()
            codigo_linha = dados[0]
            
            if codigo_linha in contagem_linhas:
                contagem_linhas[codigo_linha] = contagem_linhas[codigo_linha] + 1
            else:
                contagem_linhas[codigo_linha] = 1
                
    arquivo.close()
    
    for codigo, total in contagem_linhas.items():
        print(f"{codigo} {total}")

except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado.")