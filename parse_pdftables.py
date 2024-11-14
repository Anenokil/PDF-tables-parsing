import pdftables_api


def main(ifn: str, ofn: str):
    c = pdftables_api.Client('ptcysb3cme3p')
    html = c.html(ifn, 'best-unicef-1')
