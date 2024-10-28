import os
import shutil

from PIL import Image
from fpdf import FPDF


# определяем наличие файлов
def determiningFileExtension(image_folder):
    """
     Определяет и сортирует файлы в указанной папке:
     - Извлекает все имена файлов из указанной папки.
     - Сортирует файлы в порядке возрастания, учитывая числовую часть имени для корректного порядка.
     - Возвращает отсортированный список имен файлов.

     :param image_folder: Путь к папке с изображениями.
     :return: Список имен файлов, отсортированных от меньшего к большему.
     """
    # Создаем пустое множество для уникальных расширений и список для имен файлов
    file_names = []
    # Перебираем файлы в указанной папке
    for filename in os.listdir(image_folder):
        # Добавляем имя файла в список
        file_names.append(filename)
    # Сортируем список имен файлов, преобразуя числовые части для правильной сортировки
    file_names.sort(key=lambda x: int(os.path.splitext(x)[0]))
    print("Имена файлов, отсортированные от меньшего к большему:", file_names)

    return  file_names

def process_image_file(input_file: str, output_folder: str) -> None:
    """
    Обрабатывает изображение в зависимости от его формата:
    - Если формат JFIF или GIF, конвертирует в PNG и сохраняет в указанную папку.
    - Игнорирует файлы других форматов.

    :param input_file: Путь к входному файлу изображения.
    :param output_folder: Путь к папке для сохранения выходного файла.
    """
    # Проверка существования папки для сохранения
    os.makedirs(output_folder, exist_ok=True)

    # Получение имени файла и его расширения
    filename, file_extension = os.path.splitext(input_file)
    file_extension = file_extension.lower()
    output_file = os.path.join(output_folder, os.path.splitext(os.path.basename(input_file))[0] + '.png')

    try:
        if file_extension in ['.jfif', '.gif']:
            # Открытие и конвертация JFIF или GIF в PNG
            with Image.open(input_file) as img:
                img = img.convert("RGB")  # Преобразование изображения в RGB для PNG
                img.save(output_file, 'PNG')
            print(f"Файл {input_file} успешно конвертирован и сохранен как {output_file}")
        else:
            print(f"Файл {input_file} имеет неподдерживаемый формат и был проигнорирован.")
    except Exception as e:
        print(f"Ошибка при обработке файла {input_file}: {e}")


def creatingBook(files,image_folder,output_path="output.pdf"):
    """
       Создает PDF-документ из списка изображений.

       Этот метод перебирает все указанные изображения, добавляет их на страницы PDF и сохраняет документ в указанном пути.

       :param files: Список имен файлов изображений для добавления в PDF.
       :param image_folder: Путь к папке, содержащей изображения.
       :param output_path: Путь для сохранения созданного PDF-документа (по умолчанию "output.pdf").

       Исключения:
       - Выводит сообщение об ошибке, если изображение не найдено по указанному пути.
       """
    # Создаем объект PDF
    pdf = FPDF()

    # Перебираем все изображения в папке
    for file_name in files:
        try:
            # Открываем изображение
            image_path = image_folder + file_name
            image = Image.open(image_path)
            # Добавляем страницу в PDF
            pdf.add_page()
            # Вставляем изображение на страницу
            pdf.image(image_path, x=0, y=0, w=pdf.w)
        except FileNotFoundError:
            print(f"Изображение {image_path} не найдено.")

    # Сохраняем PDF
    pdf.output(output_path)


def start():
    """
        Запускает процесс обработки изображений и создания PDF-документа.

        Этот метод выполняет следующие действия:
        1. Указывает папку, содержащую исходные изображения.
        2. Вызывает метод для определения расширений файлов в указанной папке.
        3. Указывает папку для сохранения обработанных изображений и путь для сохранения итогового PDF-документа.
        4. Обрабатывает каждое изображение из исходной папки, конвертируя его при необходимости и сохраняя в указанную папку.
        5. Повторно определяет расширения файлов в папке сохранения изображений.
        6. Создает PDF-документ, используя обработанные изображения.

        Исключения:
        - Выводит сообщение об ошибке, если изображение не найдено в процессе обработки.
        """
    # Папка, где находятся изображения
    image_folder = "F:/1С/БГУ/1С БГУ книга/"
    files = determiningFileExtension(image_folder)
    image_path_save = "F:/1С/БГУ/Конвертация картинки/"
    output_path = "F:/1С/БГУ/Результат/Результат.pdf"

    for file_name in files:
        try:
            image_path = image_folder + file_name
            process_image_file(image_path,image_path_save)
        except FileNotFoundError:
            print(f"Изображение {image_path} не найдено.")

    files_save = determiningFileExtension(image_path_save)
    creatingBook(files_save,image_path_save,output_path)
