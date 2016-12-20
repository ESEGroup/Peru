

###################################################################################################
#Metodo que adiciona caracteres de escape "\" antes de caracteres especiais em strings
#
#Nome: escapeString
#Autor: Renan Basilio
#Versao: 1.0
#
#Algoritmo:
#   1. Traduz cada caracter especial em uma versao de si proprio precedida por "\"
#
#Utilizacao:
#   escapeString(inString)
#       inString e a string a se adicionar os caracteres de escape
#
#Caracteres especiais escapados por este metodo:
#   ', ", \, /, <, >, -, [, ], ^, $, *
#
####################################################################################################
def escapeString(inString):
    escaped = inString.translate(inString.maketrans(
    {
    "'":"\'",
    "\"":"\"",
    "\\":"\\",
    "/":"\/",
    "<":"\<",
    ">":"\>",
    "-":"\-",
    "[":"\[",
    "]":"\]",
    "^":"\^",
    "$":"\$",
    "*":"\*"
    }))
    return escaped