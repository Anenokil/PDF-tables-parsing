from tabula import read_pdf
# pip install JPype1
# Java is required


def main(ifn: str, ofn: str):
    df_temp = read_pdf(ifn, pages='all', multiple_tables=True, stream=True)
    for table in df_temp:
        print(table, '\n\n')


"""
Работает, но немного криво
* В качестве таблиц воспринимает любые чертежи и графики
* Одна таблица немного наехала на другую
"""
