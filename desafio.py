
##############################################################################
file_path = r'C:\Users\agenc\Downloads\arq.txt'
output_file = r'C:\Users\agenc\Downloads\novo_arq.txt'

try:
    with open(file_path, 'r', encoding='utf-8') as file:
       
        linhas = file.readlines()
    
        linhas_sem_cabecalho = linhas[11:]
    
   
    with open(output_file, 'w', encoding='utf-8') as file:

        file.writelines(linhas_sem_cabecalho)
    
    print(f"Arquivo '{output_file}' foi salvo com sucesso.")

except FileNotFoundError:
    print(f"Arquivo '{file_path}' não encontrado.")
except Exception as e:
    print(f"Erro ao processar o arquivo '{file_path}': {e}")
    
###########################################################################      
         
input_file = r'C:\Users\agenc\Downloads\novo_arq.txt'
output_file = r'C:\Users\agenc\Downloads\linhas_terminadas_com_m.txt'

def filtrar_linhas_terminadas_com_m(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
            linhas = infile.readlines()
            
            for line in linhas:
                if line.strip()[-1] == 'm':
                    outfile.write(line)
    
    except FileNotFoundError:
        print(f"Arquivo '{input_file}' não encontrado.")
    except Exception as e:
        print(f"Erro ao processar o arquivo '{input_file}': {e}")

try:
    filtrar_linhas_terminadas_com_m(input_file, output_file)
    # Contar o número total de linhas escritas no arquivo de saída
    with open(output_file, 'r', encoding='utf-8') as file:
        num_linhas = sum(1 for _ in file)
    
except FileNotFoundError:
    print(f"Arquivo '{input_file}' não encontrado.")
except Exception as e:
    print(f"Erro ao processar o arquivo '{input_file}': {e}")

 ###########################################################################      

input_file = r'C:\Users\agenc\Downloads\linhas_terminadas_com_m.txt'
output_file = r'C:\Users\agenc\Downloads\linhas_formatadas.txt'

def formatar_colunas(file_path, output_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as infile, open(output_path, 'w', encoding='utf-8') as outfile:
            linhas = infile.readlines()
            
            for line in linhas:
                campos = [campo.rstrip() for campo in line.split('#')]
                
                outfile.write(' '.join(f"{campo: <20}" for campo in campos) + '\n')
    
    except FileNotFoundError:
        print(f"Arquivo '{file_path}' não encontrado.")
    except Exception as e:
        print(f"Erro ao processar o arquivo '{file_path}': {e}")

try:
    formatar_colunas(input_file, output_file)
    
    print(f"Dados formatados foram salvos no arquivo '{output_file}'.")

except FileNotFoundError:
    print(f"Arquivo '{input_file}' não encontrado.")
except Exception as e:
    print(f"Erro ao processar o arquivo '{input_file}': {e}")

 ###########################################################################      

import csv

input_file = r'C:\Users\agenc\Downloads\linhas_formatadas.txt'
output_file_txt = r'C:\Users\agenc\Downloads\novas_linhas_sem_zero.txt'
output_file_csv = r'C:\Users\agenc\Downloads\empreiteiras_contagem.csv'

def criar_arquivo_sem_zero(file_path, posicoes):
    try:
        with open(file_path, 'r', encoding='utf-8') as infile:
            linhas = infile.readlines()

        novas_linhas = [line for line in linhas if not any(line[pos] == '0' for pos in posicoes)]

        with open(output_file_txt, 'w', newline='', encoding='utf-8') as outfile:
            outfile.writelines(novas_linhas)

        print(f"Arquivo '{output_file_txt}' criado com sucesso.")

        return novas_linhas

    except FileNotFoundError:
        print(f"Arquivo '{file_path}' não encontrado.")
    except Exception as e:
        print(f"Erro ao processar o arquivo '{file_path}': {e}")

def contar_empreiteiras(linhas, posicao):
    empreiteiras_count = {
        'Empreiteira 1': 0,
        'Empreiteira 2': 0,
        'Empreiteira 3': 0,
        'Empreiteira 4': 0,
        'Empreiteira 5': 0,
        'Empreiteira Propia': 0
    }

    for line in linhas:
        if len(line) > posicao:
            caractere = line[posicao]
            if caractere == '1':
                empreiteiras_count['Empreiteira 1'] += 1
            elif caractere == '2':
                empreiteiras_count['Empreiteira 2'] += 1
            elif caractere == '3':
                empreiteiras_count['Empreiteira 3'] += 1
            elif caractere == '4':
                empreiteiras_count['Empreiteira 4'] += 1
            elif caractere == '5':
                empreiteiras_count['Empreiteira 5'] += 1
            elif caractere == 'P':
                empreiteiras_count['Empreiteira Propia'] += 1

    try:
        # Escrever os resultados no novo arquivo CSV
        with open(output_file_csv, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Empreiteira', 'Quantidade'])
            for empreiteira, quantidade in empreiteiras_count.items():
                writer.writerow([empreiteira, quantidade])

        print(f"Arquivo '{output_file_csv}' criado com sucesso.")

    except Exception as e:
        print(f"Erro ao criar o arquivo CSV '{output_file_csv}': {e}")

# Definir as posições desejadas (568, 569, 567, 570) para verificar os caracteres
posicoes = [567, 568, 569, 570]

# Posição inicial e final do caractere que define a empreiteira
posicao_inicio = 138
posicao_fim = 144

try:
    # Criar o arquivo sem linhas com '0' nas posições especificadas
    novas_linhas = criar_arquivo_sem_zero(input_file, posicoes)

    # Contar e escrever as ocorrências das empreiteiras no arquivo CSV
    if novas_linhas:
        contar_empreiteiras(novas_linhas, posicao_inicio)

except FileNotFoundError:
    print(f"Arquivo '{input_file}' não encontrado.")
except Exception as e:
    print(f"Erro ao processar o arquivo '{input_file}': {e}")