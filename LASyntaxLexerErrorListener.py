from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener


# Criando o detector de erro léxico personalizado
class LASyntaxLexerErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error = str(e.input)[e.startIndex]

        # Erro de fechamento de comentário
        if error == "{":
            raise Exception(f"Linha {line}: comentario nao fechado")

        # Erro de fechamento de cadeia literal
        elif error == '"':
            raise Exception(f"Linha {line}: cadeia literal nao fechada")

        # Erro de simbolo desconhecido
        else:
            raise Exception(f"Linha {line}: {error} - simbolo nao identificado")
