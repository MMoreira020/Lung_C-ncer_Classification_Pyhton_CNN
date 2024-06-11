import os
import pydicom
from matplotlib import pyplot as plt
import math

def dicom_to_png(dicom_path, output_path, subdir_name):
    # Carregamento o arquivo DICOM
    dicom_data = pydicom.dcmread(dicom_path)

    pixel_array = dicom_data.pixel_array
    
    # Montar os subdiretórios
    filename_extension = os.path.splitext(os.path.basename(dicom_path))
    png_filename = f"{subdir_name}_{filename_extension[0]}.png"  
    png_path = os.path.join(output_path, png_filename)

    # Salvar a imagem como PNG
    plt.imsave(png_path, pixel_array, cmap="gray")

    print(f"Conversão concluída: {dicom_path} -> {png_path}")

# Diretório contendo os arquivos DICOM
dicom_directory = "C://Users//maste//OneDrive//Área de Trabalho//normal//paciente01"

# Diretório de saída para os arquivos PNG
output_directory = "D://Iniciação_Moises//Pacientes//Normal//treino"

# Diretório de saída 
os.makedirs(output_directory, exist_ok=True)

# Iterar sobre os diretórios e subdiretórios
for root, dirs, files in os.walk(dicom_directory):
    subdir_name = os.path.basename(root)
    total_files = len(files)
    
    # Intervalo de imagens a serem selecionadas
    start_index = math.ceil(total_files * 0.25)  # Início (25%)
    end_index = math.ceil(total_files * 0.8)    # Fim (75%)
    
    # Quantidade de imagens a serem selecionadas
    num_selected_files = math.ceil((end_index - start_index))
    
    # Ordenar os arquivos DICOM
    files.sort()
    
    # Iterar sobre os arquivos DICOM e converter apenas uma porcentagem
    for i, dicom_filename in enumerate(files[start_index:end_index]):
        dicom_path = os.path.join(root, dicom_filename)

        
        if dicom_filename.lower().endswith('.dcm'):
            # Verificar se o índice atual é um dos selecionados
            if i % (end_index - start_index) < num_selected_files:
                dicom_to_png(dicom_path, output_directory, subdir_name)