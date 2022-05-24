from openpyxl import load_workbook


def xlsx_to_tuple(file):
    """ Функция для преобразования xlsx в кортеж целых чисел """

    wb = load_workbook(file)
    sheet = wb.get_sheet_by_name('Sheet1')
    # sheet возвращает  объект-генератора, генерирующий кортежи
    articles = tuple(map(lambda x: int(x[0]), sheet.values))

    return articles
