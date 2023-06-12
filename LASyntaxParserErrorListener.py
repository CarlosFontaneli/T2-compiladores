# Criando o detector de erro de sintaxe personalizado
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener


class LASyntaxParserErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Erro próximo ao fim do arquivo
        if offendingSymbol.text == "<EOF>":
            raise Exception(
                f"Linha {offendingSymbol.line}: erro sintatico proximo a EOF"
            )
        # Erro localizado durante o programa
        else:
            raise Exception(
                f"Linha {offendingSymbol.line}: erro sintatico proximo a {offendingSymbol.text}"
            )
