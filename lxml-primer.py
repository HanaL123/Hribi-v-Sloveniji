from lxml import html
import requests
import csv
import re

def uvrstitev(res):
    cls = res.classes
    if 'result-medal--gold' in cls:
        return 1
    elif 'result-medal--silver' in cls:
        return 2
    elif 'result-medal--bronze' in cls:
        return 3
    m = re.search(r'#([0-9]+)', res.text)
    if m:
        return int(m.group(1))
    return None

link = "https://olympics.com/en/athletes/simone-biles"
stran = html.fromstring(requests.get(link).content)

tabela_tokyo = stran.xpath("//table[@class='sm-mb6 has-header']")[0]

vrstice = [vrstica.xpath("td")[1:] for vrstica in tabela_tokyo.xpath("tbody/tr")]
podatki = [(uvrstitev(result.getchildren()[0]), event.text, sport.text)
           for result, event, sport in vrstice]