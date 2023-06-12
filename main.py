import sys
from antlr4 import *
from LASyntaxLexer import LASyntaxLexer
from LASyntaxParser import LASyntaxParser
from antlr4.error.ErrorListener import ErrorListener


# Criando o detector de erro de sintaxe personalizado
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


# Leitura dos nomes e abertura dos arquivos
input_file_name = sys.argv[1]
output_file_name = sys.argv[2]
input_stream = FileStream(input_file_name, encoding="utf-8")
output = open(output_file_name, "w")

# Analisador léxico
lexer = LASyntaxLexer(input_stream)

# Tokens Stream
stream = CommonTokenStream(lexer)

# Analisador sintático
parser = LASyntaxParser(stream)

# Atualizando os detectores de erros pelos personalizados
lexer.removeErrorListeners()
parser.removeErrorListeners()
lexer.addErrorListener(LASyntaxLexerErrorListener())
parser.addErrorListener(LASyntaxParserErrorListener())

# Lista de erros
errors = []

try:
    # Chamando o parser
    parser.programa()

except Exception as e:
    errors.append(str(e))
    errors.append("Fim da compilacao")
    for error in errors:
        output.write(f"{error}\n")

    output.close()
