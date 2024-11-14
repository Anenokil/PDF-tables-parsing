import pdfplumber


# Parsing
def main(ifn: str, ofn: str):
    page_texts = []
    with pdfplumber.open(ifn) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            page_texts.append(page_text)

    # Save result
    text = '\n\n\n'.join(page_texts)  # Separate pages with spaces
    with open(ofn, 'w') as fo:
        fo.write(text)


"""
* Выводит весь текст в порядке сверху вниз
* Таблицы:
  * Выводятся по одной
  * Выводятся по строкам
  * Сначала в одной строке заголовок
  * В следующих строках через пробел ячейки (! однозначно отделить столбцы невозможно)
* Нижний индекс выводится отдельной строкой (!)
"""
