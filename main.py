import pandas as pd
import os


# Указываем директории и путь до рецепта
input_directory = 'output_csv/'
output_directory = 'result/'
file_path_recipe = 'output_recipe_csv/Hand_cream.csv'

# Создаем директорию для сохранения .csv файлов, если её нет
os.makedirs(output_directory, exist_ok=True)

# Выбираем датафрейм с рецептом
recipe_df = pd.read_csv(file_path_recipe, header=None)

# Создаем пустой список
result_list = []

# Поиск ингредиентов
for index, row in recipe_df.iterrows():
    # Формируем полный путь к файлу
    input_file_path = os.path.join(input_directory, row[0] + '.csv')
    # Проверим существует ли этот путь
    if os.path.exists(input_file_path) == True:
        # Если путь существует, создаем датафрейм
        df = pd.read_csv(input_file_path, header=None)
        # Пересчитываем массовую долю простых ингредиентов
        df[1] = ((df[1] / 100) * (row[1] / 100)) * 100
        # Добавляем найденный существующий датафрейм сложного компонента в результирующий список
        result_list.append(df)
# Добавим датафрейм рецепта
result_list.append(recipe_df)

# Соединить все датафреймы из списка result_list в один датафрейм
finish_df = pd.concat(result_list, axis=0)


# Удаляем из датафрейма рецепт сложные ингредиенты
a = os.listdir(input_directory)
# Создаем пустой список
b = []
# Цикл для формирования списка сложных ингредиентов из названий файлов output_csv
for l in a:
    b.append(l.rstrip('.csv'))
# Удаляем все строчки, в которых есть сложные ингредиенты списка b из результирующего датафрейма
finish_df = finish_df[~finish_df[0].isin(b)]
# Сбрасываем индекс в результирующем датафрейме
finish_df = finish_df.reset_index(drop=True)

#Группировка, сортировка, сумма одинаковых ингредиентов и сброс индекса
finish_df = finish_df.groupby(0).sum().sort_values(by=1, ascending=False).reset_index()
print(finish_df)

# Преобразование столбца в строчку ингредиентов
output_list = finish_df[0].to_list()

# Печать списка ингредиентов
print('Ingredients: ' + ', ' .join(output_list).replace('_', ' ') + '.')

