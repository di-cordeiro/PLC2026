import re

### 1. Cabeçalhos: linhas iniciadas por "# texto", ou "## texto" ou "### texto"
# In: `# Exemplo`
# out: `<h1>Exemplo</h1>`

def cabecalho(texto):
    resultado = texto
    regex = re.match(r"(#{1,3})\s+(.*)", texto)
    if regex:
        nivel = len(regex.group(1))
        resultado = f"<h{nivel}>{regex.group(2)}</h{nivel}>"
    return resultado

print(cabecalho("# Exemplo"))     
print(cabecalho("### Exemplo 2"))
print(cabecalho("texto normal"))  

### 2. Bold: pedaços de texto entre "**":
#In: `Este é um **exemplo** ...`
#Out: `Este é um <b>exemplo</b> ...`


def bold(texto):
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", texto)

print(bold("**exemplo**"))
print(bold("**Olá!**"))
print(bold("**Este é um exemplo**"))

### 3. Itálico: pedaços de texto entre "*":
#In: `Este é um *exemplo* ...`
#Out: `Este é um <i>exemplo</i> ...`

def italico(texto):
    return re.sub(r"\*(.+?)\*", r"<i>\1</i>", texto)

print(italico("Este é um *exemplo* ..."))

### 4. Lista numerada:

#In:
#```
#1. Primeiro item
#2. Segundo item
#3. Terceiro item
#```

#Out:
#```
#<ol>
#<li>Primeiro item</li>
#<li>Segundo item</li>
#<li>Terceiro item</li>
#</ol>
#```

def converteBloco(m):
    bloco = m.group(0)
    itens = re.findall(r"^\d+\.\s+(.*)", bloco, re.MULTILINE)
    elementos = "\n".join(f"<li>{item}</li>" for item in itens)
    fim = "\n" if bloco.endswith("\n") else ""
    return f"<ol>\n{elementos}\n</ol>{fim}"

def listaNumerada(texto):
    return re.sub(r"(?:^\d+\.\s+.*\n?)+", converteBloco, texto, flags=re.MULTILINE)

print(listaNumerada("Exemplo\n1. Primeiro item\n2. Segundo item\n3. Terceiro item\nacabou"))

### 5. Link: [texto](endereço URL)
#In: `Como pode ser consultado em [página da UC](http://www.uc.pt)`
#Out: `Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>`

def link(texto):
    return re.sub(r"\[\s*(.+?)\s*\]\(([^)]+)\)", r'<a href="\2">\1</a>', texto)

print(link("Como pode ser consultado em [página da UC](http://www.uc.pt)"))


### 6. Imagem: ![texto alternativo](path para a imagem)
#In: Como se vê na imagem seguinte: `![imagem dum coelho](http://www.coellho.com) ...`
#Out: `Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/> ...`

def imagem(texto):
    return re.sub(r"!\[\s*(.+?)\s*\]\(([^)]+)\)", r'<img src="\2" alt="\1"/>', texto)

print(imagem("Como se vê na imagem seguinte: ![imagem dum coelho](http://www.coellho.com) ..."))
