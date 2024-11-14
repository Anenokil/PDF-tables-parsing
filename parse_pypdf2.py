import PyPDF2


def main(ifn: str, ofn: str):
    pdf_file = open(ifn, 'rb')
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Parsing
    page_texts = []
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        page_texts.append(page_text)
    print(page_texts)  # list[str]

    # Save result
    text = '\n\n\n'.join(page_texts)  # Separate pages with spaces
    with open(ofn, 'w') as fo:
        fo.write(text)


"""
* Выводит весь текст в непредсказуемом порядке (!)
* Таблицы:
  * Все таблицы с одной страницы выводятся вперемешку (!)
  * Выводятся по строкам
  * Сначала заголовки всех таблиц (одна строка - один заголовок)
  * В следующих строках через пробел ячейки (! однозначно отделить столбцы невозможно)
"""
