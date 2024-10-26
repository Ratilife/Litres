from PIL import Image
from fpdf import FPDF

# определяем расширения файлов
def determiningFileExtension():
    # Создаем пустое множество для уникальных расширений
    extensions = set()

    # Перебираем файлы в указанной папке
    for filename in os.listdir(image_folder):
        # Получаем расширение файла
        _, ext = os.path.splitext(filename)
        if ext:  # Добавляем расширение, если оно есть
            extensions.add(ext)
    # Выводим уникальные расширения
    print("Найденные расширения файлов:", extensions)
    return extensions


# Папка, где находятся изображения
image_folder = "'F:/1С/БГУ/1С БГУ книга"

# Создаем объект PDF
pdf = FPDF()

# Перебираем все изображения в папке
for i in range(380):
    # Формируем путь к изображению
    image_path = f"{image_folder}/{i}.jpg"  # Предполагаем, что изображения названы от 0 до 458 и имеют расширение .jpg
    try:
        # Открываем изображение
        image = Image.open(image_path)
        # Добавляем страницу в PDF
        pdf.add_page()
        # Вставляем изображение на страницу
        pdf.image(image_path, x=0, y=0, w=pdf.w)
    except FileNotFoundError:
        print(f"Изображение {image_path} не найдено.")

# Сохраняем PDF
pdf.output("output.pdf")

