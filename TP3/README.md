# TPC3

## Autor 

![Foto](https://github.com/di-cordeiro.png)

- **Nome**: Diana Rafaela Gonçalves Cordeiro
- **ID**: A112256

## Resumo

Construção de um analisador léxico para uma linguagem de query, como a usada na DBPedia. O analisador reconhece os seguintes tokens:

- **Comentários**: começam por `#` e vão até ao fim da linha; são ignorados
- **Variáveis**: começam por `?` seguido de caracteres alfanuméricos (ex.: `?nome`)
- **Língua**: começam por `@` seguido de 2 caracteres (ex.: `@en`)
- **Strings**: qualquer sequência entre aspas (ex.: `"Chuck Berry"`)
- **Palavra reservada**: `LIMIT`
- **Números**: valores numéricos (ex.: `1000`)
- **Conceitos**: as restantes sequências alfanuméricas, incluindo `:` (ex.: `select`, `dbo:MusicalArtist`)
- **Delimitadores**: `{`, `}` e `.`
- **Mudanças de linha**: token `NEWLINE`
- **Erros**: qualquer outro caráter é marcado como `ERRO`

Os espaços e tabs são ignorados.
Os tokens foram definidos num ficheiro JSON e o analisador foi gerado com o gen_tokenizer2.py dado nas aulas.

## Resultados 

- [Definição dos tokens](tokens_tpc3.json)
- [Analisador léxico gerado](tpc3.py)
- [Exemplo de entrada](exemplo.txt)
- [Resultado](resultado.txt)
- [Gerador](gen_tokenizer2.py)