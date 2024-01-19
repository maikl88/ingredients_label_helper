import pandas as pd
import os


# Указываем директории
input_directory = 'data/'
output_directory = 'output_csv/'

# Создаем директорию для сохранения .csv файлов, если её нет
os.makedirs(output_directory, exist_ok=True)

# Получаем список файлов в директории
files = os.listdir(input_directory)

# Инициализируем счетчик конвертированных файлов
converted_files_count = 0

# Проходим по каждому файлу
for file in files:
    if file.endswith('.xlsx'):
        # Формируем полный путь к файлу
        input_file_path = os.path.join(input_directory, file)
        
        # Формируем имя для сохранения CSV файла в новой директории
        output_file_path = os.path.join(output_directory, file.split('.')[0] + '.csv')
        
        # Проверяем, существует ли уже .csv файл
        if os.path.exists(output_file_path):
            print(f"Файл {output_file_path} уже существует. Пропускаем конвертацию.")
        else:
            # Увеличиваем счетчик конвертированных файлов
            converted_files_count += 1
            
            # Читаем файл Excel
            df = pd.read_excel(input_file_path, header=None)
            
            # Сохраняем в CSV файл
            df.to_csv(output_file_path, index=None, header=False)
                                                      
            # Выводим DataFrame
            print(f"DataFrame for {file}:")
            print(df)
            print("\n")

# Выводим общее количество конвертированных файлов
print(f"Всего сконвертировано файлов: {converted_files_count}")