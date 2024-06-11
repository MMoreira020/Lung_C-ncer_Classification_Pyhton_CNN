import os
from matplotlib import pyplot as plt
import math
import shutil

def copy_and_rename_png(png_path, output_path, subdir_name):
    # Montar os subdiretórios
    filename_extension = os.path.splitext(os.path.basename(png_path))
    png_filename = f"{subdir_name}_{filename_extension[0]}.png"  
    png_dest_path = os.path.join(output_path, png_filename)

    # Copiar e renomear o arquivo PNG
    shutil.copy(png_path, png_dest_path)

    print(f"Cópia e renomeação concluídas: {png_path} -> {png_dest_path}")

# Diretório contendo os arquivos PNG
png_directory = "C://Users//maste//OneDrive//Área de Trabalho//normal//paciente102"
# Diretório de saída para os arquivos PNG
output_directory = "D://Iniciação_Moises//Pacientes//Normal//validação"

# Criar o diretório de saída, se não existir
os.makedirs(output_directory, exist_ok=True)    

# Iterar sobre os diretórios e subdiretórios
for root, dirs, files in os.walk(png_directory):
    subdir_name = os.path.basename(root)
    total_files = len(files)
    
    # Intervalo de imagens a serem selecionadas
    start_index = math.ceil(total_files * 0.25)  # Início (25%)
    end_index = math.ceil(total_files * 0.8)    # Fim (75%)
    
    # Quantidade de imagens a serem selecionadas
    num_selected_files = math.ceil((end_index - start_index))
    
    # Ordenar os arquivos PNG
    files.sort()
    
    # Iterar sobre os arquivos PNG e copiar apenas uma porcentagem
    for i, png_filename in enumerate(files[start_index:end_index]):
        png_path = os.path.join(root, png_filename)
        
        if png_filename.lower().endswith('.png'):
            # Verificar se o índice atual é um dos selecionados
            if i % (end_index - start_index) < num_selected_files:
                copy_and_rename_png(png_path, output_directory, subdir_name)
