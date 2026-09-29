import re 
# Expressão: ^(1*(0|10)*1?)$
#
# Explicação:
# ^ -> início da string
# 1* -> zero ou mais 1s iniciais (antes do primeiro 0 podem ser quantos quisermos) 
# (0|10)* -> a seguir pode ter zero ou mais blocos de "0" ou "10" (cada 1 vem sempre seguido de 0) 
# 1? -> no fim, pode ter opcionalmente um único 1
# $ -> fim da string 
#
# Assim, só irá aceitar strings binárias sem a sequência "011", pois depois do primeiro 0, um 1 só existe como parte de "10" ou como último carácter
# Exemplos: 
# "011011": rejeita
# "10111": rejeita
# "1101": aceita
# "101010": aceita
# "1111": aceita
# "11000101001": aceita

expressao = r"^(1*(0|10)*1?)$"

testes = ["011011", "10111", "1101", "101010", "1111", "11000101001"]
for s in testes: 
    print(s, "aceita" if re.match(expressao, s) else "rejeita")