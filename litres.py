from PIL import Image
from fpdf import FPDF

# определяем наличие файлов
def determiningFileExtension(image_folder):
    # Создаем пустое множество для уникальных расширений и список для имен файлов
    file_names = []
    # Перебираем файлы в указанной папке
    for filename in os.listdir(image_folder):
        # Добавляем имя файла в список
        file_names.append(filename)

    # Сортируем список имен файлов
    file_names.sort()

    print("Имена файлов, отсортированные от меньшего к большему:", file_names)

    return  file_names


# Папка, где находятся изображения
image_folder = "'F:/1С/БГУ/1С БГУ книга"
files = determiningFileExtension(image_folder)
# Создаем объект PDF
pdf = FPDF()

# Перебираем все изображения в папке
for file_name in files:
    try:
        # Открываем изображение
        image = Image.open(file_name)
        # Добавляем страницу в PDF
        pdf.add_page()
        # Вставляем изображение на страницу
        pdf.image(image_path, x=0, y=0, w=pdf.w)
    except FileNotFoundError:
        print(f"Изображение {image_path} не найдено.")

# Сохраняем PDF
pdf.output("output.pdf")

