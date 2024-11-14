import pandas as pd
import pdftotree  # SKLEARN_ALLOW_DEPRECATED_SKLEARN_PACKAGE_INSTALL=True
from html_table_parser.parser import HTMLTableParser


def main(ifn: str, ofn: str):
    tree = pdftotree.parse(ifn)
    #print(tree)

    # Вариант 1: pandas
    # Сразу получаем таблицы
    html_tables = pd.read_html(tree)
    for table in html_tables:
        print(table, '\n\n')

    # Вариант 2: HTMLTableParser
    # Получаем строки в виде списков
    p = HTMLTableParser()
    p.feed(tree)
    for table in p.tables:
        print(table)


"""
Работает, но криво
* В качестве таблиц воспринимает любые чертежи и графики
* Самая первая ячейка в таблице - NaN
* Теряет последнюю строку таблицы
"""
