# Generated from LASyntax.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .LASyntaxParser import LASyntaxParser
else:
    from LASyntaxParser import LASyntaxParser

# This class defines a complete listener for a parse tree produced by LASyntaxParser.
class LASyntaxListener(ParseTreeListener):

    # Enter a parse tree produced by LASyntaxParser#programa.
    def enterPrograma(self, ctx:LASyntaxParser.ProgramaContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#programa.
    def exitPrograma(self, ctx:LASyntaxParser.ProgramaContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#declaracoes.
    def enterDeclaracoes(self, ctx:LASyntaxParser.DeclaracoesContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#declaracoes.
    def exitDeclaracoes(self, ctx:LASyntaxParser.DeclaracoesContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#declaracao_local.
    def enterDeclaracao_local(self, ctx:LASyntaxParser.Declaracao_localContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#declaracao_local.
    def exitDeclaracao_local(self, ctx:LASyntaxParser.Declaracao_localContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#variavel.
    def enterVariavel(self, ctx:LASyntaxParser.VariavelContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#variavel.
    def exitVariavel(self, ctx:LASyntaxParser.VariavelContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#identificador.
    def enterIdentificador(self, ctx:LASyntaxParser.IdentificadorContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#identificador.
    def exitIdentificador(self, ctx:LASyntaxParser.IdentificadorContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#dimensao.
    def enterDimensao(self, ctx:LASyntaxParser.DimensaoContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#dimensao.
    def exitDimensao(self, ctx:LASyntaxParser.DimensaoContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#tipo.
    def enterTipo(self, ctx:LASyntaxParser.TipoContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#tipo.
    def exitTipo(self, ctx:LASyntaxParser.TipoContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#tipo_basico.
    def enterTipo_basico(self, ctx:LASyntaxParser.Tipo_basicoContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#tipo_basico.
    def exitTipo_basico(self, ctx:LASyntaxParser.Tipo_basicoContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#tipo_basico_ident.
    def enterTipo_basico_ident(self, ctx:LASyntaxParser.Tipo_basico_identContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#tipo_basico_ident.
    def exitTipo_basico_ident(self, ctx:LASyntaxParser.Tipo_basico_identContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#tipo_estendido.
    def enterTipo_estendido(self, ctx:LASyntaxParser.Tipo_estendidoContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#tipo_estendido.
    def exitTipo_estendido(self, ctx:LASyntaxParser.Tipo_estendidoContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#valor_constante.
    def enterValor_constante(self, ctx:LASyntaxParser.Valor_constanteContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#valor_constante.
    def exitValor_constante(self, ctx:LASyntaxParser.Valor_constanteContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#registro.
    def enterRegistro(self, ctx:LASyntaxParser.RegistroContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#registro.
    def exitRegistro(self, ctx:LASyntaxParser.RegistroContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#declaracao_global.
    def enterDeclaracao_global(self, ctx:LASyntaxParser.Declaracao_globalContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#declaracao_global.
    def exitDeclaracao_global(self, ctx:LASyntaxParser.Declaracao_globalContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#parametro.
    def enterParametro(self, ctx:LASyntaxParser.ParametroContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#parametro.
    def exitParametro(self, ctx:LASyntaxParser.ParametroContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#parametros.
    def enterParametros(self, ctx:LASyntaxParser.ParametrosContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#parametros.
    def exitParametros(self, ctx:LASyntaxParser.ParametrosContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#corpo.
    def enterCorpo(self, ctx:LASyntaxParser.CorpoContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#corpo.
    def exitCorpo(self, ctx:LASyntaxParser.CorpoContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#cmd.
    def enterCmd(self, ctx:LASyntaxParser.CmdContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#cmd.
    def exitCmd(self, ctx:LASyntaxParser.CmdContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#cmdLeia.
    def enterCmdLeia(self, ctx:LASyntaxParser.CmdLeiaContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#cmdLeia.
    def exitCmdLeia(self, ctx:LASyntaxParser.CmdLeiaContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#cmdEscreva.
    def enterCmdEscreva(self, ctx:LASyntaxParser.CmdEscrevaContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#cmdEscreva.
    def exitCmdEscreva(self, ctx:LASyntaxParser.CmdEscrevaContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#cmdSe.
    def enterCmdSe(self, ctx:LASyntaxParser.CmdSeContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#cmdSe.
    def exitCmdSe(self, ctx:LASyntaxParser.CmdSeContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#cmdCaso.
    def enterCmdCaso(self, ctx:LASyntaxParser.CmdCasoContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#cmdCaso.
    def exitCmdCaso(self, ctx:LASyntaxParser.CmdCasoContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#cmdPara.
    def enterCmdPara(self, ctx:LASyntaxParser.CmdParaContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#cmdPara.
    def exitCmdPara(self, ctx:LASyntaxParser.CmdParaContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#cmdEnquanto.
    def enterCmdEnquanto(self, ctx:LASyntaxParser.CmdEnquantoContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#cmdEnquanto.
    def exitCmdEnquanto(self, ctx:LASyntaxParser.CmdEnquantoContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#cmdFaca.
    def enterCmdFaca(self, ctx:LASyntaxParser.CmdFacaContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#cmdFaca.
    def exitCmdFaca(self, ctx:LASyntaxParser.CmdFacaContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#cmdAtribuicao.
    def enterCmdAtribuicao(self, ctx:LASyntaxParser.CmdAtribuicaoContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#cmdAtribuicao.
    def exitCmdAtribuicao(self, ctx:LASyntaxParser.CmdAtribuicaoContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#cmdChamada.
    def enterCmdChamada(self, ctx:LASyntaxParser.CmdChamadaContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#cmdChamada.
    def exitCmdChamada(self, ctx:LASyntaxParser.CmdChamadaContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#cmdRetorne.
    def enterCmdRetorne(self, ctx:LASyntaxParser.CmdRetorneContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#cmdRetorne.
    def exitCmdRetorne(self, ctx:LASyntaxParser.CmdRetorneContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#selecao.
    def enterSelecao(self, ctx:LASyntaxParser.SelecaoContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#selecao.
    def exitSelecao(self, ctx:LASyntaxParser.SelecaoContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#item_selecao.
    def enterItem_selecao(self, ctx:LASyntaxParser.Item_selecaoContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#item_selecao.
    def exitItem_selecao(self, ctx:LASyntaxParser.Item_selecaoContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#constantes.
    def enterConstantes(self, ctx:LASyntaxParser.ConstantesContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#constantes.
    def exitConstantes(self, ctx:LASyntaxParser.ConstantesContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#numero_intervalo.
    def enterNumero_intervalo(self, ctx:LASyntaxParser.Numero_intervaloContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#numero_intervalo.
    def exitNumero_intervalo(self, ctx:LASyntaxParser.Numero_intervaloContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#op_unario.
    def enterOp_unario(self, ctx:LASyntaxParser.Op_unarioContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#op_unario.
    def exitOp_unario(self, ctx:LASyntaxParser.Op_unarioContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#exp_aritmetica.
    def enterExp_aritmetica(self, ctx:LASyntaxParser.Exp_aritmeticaContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#exp_aritmetica.
    def exitExp_aritmetica(self, ctx:LASyntaxParser.Exp_aritmeticaContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#termo.
    def enterTermo(self, ctx:LASyntaxParser.TermoContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#termo.
    def exitTermo(self, ctx:LASyntaxParser.TermoContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#fator.
    def enterFator(self, ctx:LASyntaxParser.FatorContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#fator.
    def exitFator(self, ctx:LASyntaxParser.FatorContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#op1.
    def enterOp1(self, ctx:LASyntaxParser.Op1Context):
        pass

    # Exit a parse tree produced by LASyntaxParser#op1.
    def exitOp1(self, ctx:LASyntaxParser.Op1Context):
        pass


    # Enter a parse tree produced by LASyntaxParser#op2.
    def enterOp2(self, ctx:LASyntaxParser.Op2Context):
        pass

    # Exit a parse tree produced by LASyntaxParser#op2.
    def exitOp2(self, ctx:LASyntaxParser.Op2Context):
        pass


    # Enter a parse tree produced by LASyntaxParser#op3.
    def enterOp3(self, ctx:LASyntaxParser.Op3Context):
        pass

    # Exit a parse tree produced by LASyntaxParser#op3.
    def exitOp3(self, ctx:LASyntaxParser.Op3Context):
        pass


    # Enter a parse tree produced by LASyntaxParser#parcela.
    def enterParcela(self, ctx:LASyntaxParser.ParcelaContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#parcela.
    def exitParcela(self, ctx:LASyntaxParser.ParcelaContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#parcela_unario.
    def enterParcela_unario(self, ctx:LASyntaxParser.Parcela_unarioContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#parcela_unario.
    def exitParcela_unario(self, ctx:LASyntaxParser.Parcela_unarioContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#parcela_nao_unario.
    def enterParcela_nao_unario(self, ctx:LASyntaxParser.Parcela_nao_unarioContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#parcela_nao_unario.
    def exitParcela_nao_unario(self, ctx:LASyntaxParser.Parcela_nao_unarioContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#exp_relacional.
    def enterExp_relacional(self, ctx:LASyntaxParser.Exp_relacionalContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#exp_relacional.
    def exitExp_relacional(self, ctx:LASyntaxParser.Exp_relacionalContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#op_relacional.
    def enterOp_relacional(self, ctx:LASyntaxParser.Op_relacionalContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#op_relacional.
    def exitOp_relacional(self, ctx:LASyntaxParser.Op_relacionalContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#expressao.
    def enterExpressao(self, ctx:LASyntaxParser.ExpressaoContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#expressao.
    def exitExpressao(self, ctx:LASyntaxParser.ExpressaoContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#termo_logico.
    def enterTermo_logico(self, ctx:LASyntaxParser.Termo_logicoContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#termo_logico.
    def exitTermo_logico(self, ctx:LASyntaxParser.Termo_logicoContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#fator_logico.
    def enterFator_logico(self, ctx:LASyntaxParser.Fator_logicoContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#fator_logico.
    def exitFator_logico(self, ctx:LASyntaxParser.Fator_logicoContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#parcela_logica.
    def enterParcela_logica(self, ctx:LASyntaxParser.Parcela_logicaContext):
        pass

    # Exit a parse tree produced by LASyntaxParser#parcela_logica.
    def exitParcela_logica(self, ctx:LASyntaxParser.Parcela_logicaContext):
        pass


    # Enter a parse tree produced by LASyntaxParser#op_logico_1.
    def enterOp_logico_1(self, ctx:LASyntaxParser.Op_logico_1Context):
        pass

    # Exit a parse tree produced by LASyntaxParser#op_logico_1.
    def exitOp_logico_1(self, ctx:LASyntaxParser.Op_logico_1Context):
        pass


    # Enter a parse tree produced by LASyntaxParser#op_logico_2.
    def enterOp_logico_2(self, ctx:LASyntaxParser.Op_logico_2Context):
        pass

    # Exit a parse tree produced by LASyntaxParser#op_logico_2.
    def exitOp_logico_2(self, ctx:LASyntaxParser.Op_logico_2Context):
        pass



del LASyntaxParser