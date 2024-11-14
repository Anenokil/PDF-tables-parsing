import parse_pdfminer as p1
import parse_pdfplumber as p2
#import parse_pdfquery as p3
import parse_pdftotree as p4
import parse_pymupdf as p5
import parse_pypdf2 as p6
import parse_tabula as p7
import parse_pdftables as p8
import parse_camelot as p9

import os

funcs = {
    'pdfminer': p1.main,
    'pdfplumber': p2.main,
    #'pdfquery': p3.main,
    'pdftotree': p4.main,
    'pymupdf': p5.main,
    'pypdf2': p6.main,
    'tabula': p7.main,
    'pdftables': p8.main,
    'camelot': p9.main,
}


def run_all():
    input_path = 'inputs/example.pdf'
    output_dir = 'outputs'
    #p1.main(input_path, os.path.join(output_dir, 'out_pdfminer.txt'))
    #p2.main(input_path, os.path.join(output_dir, 'out_pdfplumber.txt'))
    #p3.main(input_path, os.path.join(output_dir, 'out_pdfquery.txt'))
    #p4.main(input_path, os.path.join(output_dir, 'out_pdftotree.txt'))
    #p5.main(input_path, os.path.join(output_dir, 'out_pymupdf.txt'))
    #p6.main(input_path, os.path.join(output_dir, 'out_pypdf2.txt'))
    #p7.main(input_path, os.path.join(output_dir, 'out_tabula.txt'))


def main():
    input_dir = 'inputs'
    output_dir = 'outputs'
    lib = 'camelot'
    func = funcs[lib]
    #for fn in os.listdir(input_dir):
    for fn in ['1_table_separated.pdf', '1_table_merged_cols.pdf']:
        name, ext = os.path.splitext(fn)
        if ext == '.pdf':
            print(fn)
            pdf_path = os.path.join(input_dir, fn)
            func(pdf_path, os.path.join(output_dir, f'out_{name}_{lib}.txt'))


main()
