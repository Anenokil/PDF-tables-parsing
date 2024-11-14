# Код взят отсюда: https://stackoverflow.com/questions/26494211/extracting-text-from-a-pdf-file-using-pdfminer-in-python
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO


# Parsing
def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec='utf-8', laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)

    fp = open(path, 'rb')
    pagenos = set()

    for page in PDFPage.get_pages(fp, pagenos, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text


# Save result
def main(ifn: str, ofn: str):
    text = convert_pdf_to_txt(ifn)
    with open(ofn, 'w') as fo:
        fo.write(text)


"""
* Выводит весь текст в порядке сверху вниз
* Таблицы:
  * Выводятся по одной
  * Выводятся по столбцам группами произвольного размера (!)
  * Сначала заголовок
  * В следующих строках через пробел ячейки (! однозначно отделить столбцы невозможно)
"""
