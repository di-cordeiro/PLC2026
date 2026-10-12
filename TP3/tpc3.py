
import sys
import re

def tokenize(input_string):
    reconhecidos = []
    linha = 1
    mo = re.finditer(r'(?P<VAR>\?[a-zA-Z0-9]+)|(?P<LING>@\w{2})|(?P<STRING>"[^"]*")|(?P<LIMIT>\bLIMIT\b)|(?P<NUM>\d+)|(?P<CONCEITO>[a-zA-Z0-9:]+)|(?P<DELIM>[{}.])|(?P<SKIP>[ \t]|#.*)|(?P<NEWLINE>\n)|(?P<ERRO>.)', input_string)
    for m in mo:
        dic = m.groupdict()
        if dic['VAR']:
            t = ("VAR", dic['VAR'], linha, m.span())

        elif dic['LING']:
            t = ("LING", dic['LING'], linha, m.span())
    
        elif dic['STRING']:
            t = ("STRING", dic['STRING'], linha, m.span())
    
        elif dic['LIMIT']:
            t = ("LIMIT", dic['LIMIT'], linha, m.span())
    
        elif dic['NUM']:
            t = ("NUM", dic['NUM'], linha, m.span())
    
        elif dic['CONCEITO']:
            t = ("CONCEITO", dic['CONCEITO'], linha, m.span())
    
        elif dic['DELIM']:
            t = ("DELIM", dic['DELIM'], linha, m.span())
    
        elif dic['SKIP']:
            t = ("SKIP", dic['SKIP'], linha, m.span())
    
        elif dic['NEWLINE']:
            t = ("NEWLINE", dic['NEWLINE'], linha, m.span())
    
        elif dic['ERRO']:
            t = ("ERRO", dic['ERRO'], linha, m.span())
    
        else:
            t = ("UNKNOWN", m.group(), linha, m.span())
        if not dic['SKIP'] and t[0] != 'UNKNOWN': reconhecidos.append(t)
    return reconhecidos

for linha in sys.stdin:
    for tok in tokenize(linha):
        print(tok)

