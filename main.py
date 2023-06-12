import sys
from antlr4 import *
from LASyntaxLexer import LASyntaxLexer
from LASyntaxParser import LASyntaxParser
from LASyntaxParserErrorListener import LASyntaxParserErrorListener
from LASyntaxLexerErrorListener import LASyntaxLexerErrorListener


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
