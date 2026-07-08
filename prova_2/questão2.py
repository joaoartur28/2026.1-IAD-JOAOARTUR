nome_arquivo = input("Digite o nome do arquivo:")
try:
    arquivo = open(nome_arquivo)
    
    arquivo.readline()
    
    quantidades = []
    
    for linha in arquivo:
        linha_limpa = linha.strip()
        
        if linha_limpa:
            valor = float(linha_limpa)
            quantidades.append(valor)
            
    arquivo.close()
    
    qtd_observacoes = len(quantidades)
    
    producao_total = sum(quantidades)
    
    producao_media = producao_total / qtd_observacoes
    
    menor_producao = min(quantidades)
    
    maior_producao = max(max(quantidades)) 
    maior_producao = max(quantidades)
    
    amplitude = maior_producao - menor_producao
    
    print(f"a) Quantidade de observações: {qtd_observacoes}")
    print(f"b) Produção total: {producao_total}")
    print(f"c) Produção média: {producao_media:.2f}")
    print(f"d) Menor produção observada: {menor_producao}")
    print(f"e) Maior produção observada: {maior_producao}")
    print(f"f) Amplitude da produção: {amplitude}")

except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado.")
except ZeroDivisionError:
    print("Erro: O arquivo está vazio ou não possui registros válidos para calcular a média.")