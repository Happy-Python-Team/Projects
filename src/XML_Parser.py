import xml.etree.ElementTree as ET
from openpyxl import Workbook


def create_excel_from_xml(xml_file_path, excel_file_path):
    # Чтение XML-файла
    tree = ET.parse(xml_file_path)
    root = tree.getroot()

    # Создание нового Excel-файла
    workbook = Workbook()
    sheet = workbook.active

    # Запись заголовков
    headers = []
    values = []
    for child in root[0]:
        headers.append(child.tag)
        values.append(child.text)
    sheet.append(['event name'] + headers)

    # Запись значений
    for event in root:
        values = []
        for child in event:
            values.append(child.text)
        sheet.append([event.attrib['name']] + values)

    # Сохранение Excel-файла
    workbook.save(excel_file_path)


# Путь к XML-файлу
xml_file_path = 'file.xml'
# Путь к создаваемому Excel-файлу
excel_file_path = 'testfile.xlsx'

# Вызов функции
create_excel_from_xml(xml_file_path, excel_file_path)
