

###################################################################################################
#Método que adiciona caracteres de escape "\" antes de caracteres especiais em strings
#
#Nome: escapeString
#Autor: Renan Basilio
#Versão: 1.0
#
#Algoritmo:
#   1. Traduz cada caracter especial em uma versão de si próprio precedida por "\"
#
#Utilização:
#   escapeString(inString)
#       inString é a string a se adicionar os caracteres de escape
#
#Caracteres especiais escapados por este método:
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