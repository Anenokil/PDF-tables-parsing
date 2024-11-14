import camelot
# Required: cv2, ghostscript


def main(ifn: str, ofn: str):
    tables = camelot.read_pdf(ifn, pages='all')
    tables_pd = [table.df for table in tables]
    for table in tables_pd:
        print(table, '\n\n')
