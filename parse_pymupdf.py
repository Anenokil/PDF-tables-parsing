#import pandas as pd
import pymupdf  # = import fitz (?)


def main(ifn: str, ofn: str):
    doc = pymupdf.open(ifn)

    for page in doc:
        tabs = page.find_tables()
        try:
            for tab in tabs:
                df = tab.to_pandas()
                print(df.to_string(), '\n\n')
        except IndexError:
            print('\n\nerror\n\n')


"""
Хорошо работает
* Всё правильно считывает и конвертируется в pandas.DataFrame
"""
