nome_arquivo = input("Digite o nome do arquivo: ")

try:
    arquivo = open(nome_arquivo, "r", encoding="utf-8")
    
    try:
        for linha in arquivo:
            print(linha.rstrip().upper())
            
    finally:
        arquivo.close()

except FileNotFoundError:
    print(f"Erro: O arquivo '{nome_arquivo}' não foi encontrado.")