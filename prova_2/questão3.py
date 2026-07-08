nome_arquivo = input("Digite o nome do arquivo:")

try:
    arquivo = open(nome_arquivo)
    
    arquivo.readline()
    
    for linha in arquivo:
        linha_limpa = linha.strip()
        
        if linha_limpa:
            dados = linha_limpa.split()
            
            linha_prod = dados[0]
            turno      = dados[1]
            producao   = int(dados[2])
            defeitos   = int(dados[3])
            
            if producao > 0:
                taxa_defeitos = (defeitos / producao) * 100
            else:
                taxa_defeitos = 0.0
            
            print(f"Linha: {linha_prod} | Turno: {turno} | Producao: {producao} | Defeitos: {defeitos:02d} | Taxa de defeitos: {taxa_defeitos:.1f} %")
            
    arquivo.close()

except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado.")