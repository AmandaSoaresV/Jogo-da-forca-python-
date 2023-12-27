from random import randint, choice

def abertura():
    mensagem=f'''                
                # # # # # # # # # # # # # # # # #
                #                               #
                #   Bem Vindo ao Jogo da Forca  #
                #                               #
                #          乂❤‿❤乂             #
                #                               #
                # # # # # # # # # # # # # # # # #

    '''
    
    
    return mensagem
def regras():
    regras=''' Olá Jogador, a cada erro o jogador perde 2 pontos e cada acerto ganha-se os pontos estabelecidos de acordo com o número de letras que o usuário escolheu para a palavra.
    
    ♡ A quantidade mínima de letras que o usuário pode escolher é 3 e a máxima é 12
    
    ♡ Os pontos são:

         se escolha for 3 : 5 pontos 
         se escolha for 4 : 6 pontos 
         se escolha for 5 : 7 pontos 
         se escolha for 6 : 8 pontos 
         se escolha for 7 : 9 pontos 
         se escolha for 8 : 10 pontos
         se escolha for 9 : 11 pontos
         se escolha for 10 : 12 pontos
         se escolha for 11 : 13 pontos
         se escolha for 12 : 14 pontos

             TENHA UM BOM JOGO!!!!
     '''
    return regras

print(abertura())
print(regras())

class Palavra:
    palavras={}
    palavras[3]=["vou","Tem","sim","com","vai","seu","meu","fez","mas","sem","bar","lar","par","mar","ceu","veu","ovo","pai","mae","tio"]
    palavras[4]=["alta","ouco","seus","vida","esta","toma","boca","mato","loca","casa","vida","robo","olha","loja","faca","mais","esta","fato","soar","sede"]
    palavras[5]=["plena","afeto","vigor","senso","nobre","terno","assim","poder","etica","justo","muito","futil","anexo","sonho","amigo","mutuo","expor","haver","etnia","sonho"]
    palavras[6]=["indole","ilusao","anseio","escopo","adesao","casual","eficaz","receio","idiota","extase","formal","duvida","dadiva","lirico","legado","coagir","julgar","embora","metodo","objeto"]
    palavras[7]=["empatia","embuste","cônjuge","carater","familia","audacia","redimir","cultura","virtude","sintese","alegria","deboche","ademais","almejar","orgulho","excesso","saudade","exotico","amizade","piedade"]
    palavras[8]={"peculiar","essencia","ascensao","modestia","prudente","escrever","respeito","prodigio","passivel","distinto","abstrato","conceito","mediocre","criterio","conserto","consiste","conceder","enxergar","extensao","refletir"}
    palavras[9]=["reciproco","impressao","paradigma","concepcao","hipocrita","implicito","essencial","altruismo","vagabundo","aleatorio","esperanca","confianca","compaixao","analitico","discricao","explicito","ordinario","restricao","ignorante","consoante"]
    palavras[10]=["prescindir","referencia","subestimar","disposicao","equivocado","contemplar","finalidade","pertinente","divergente","iniquidade","espontaneo","estagnacao","excentrico","designacao","atribuicao","indolencia","fleumatico","intangivel","perscrutar","antagonico"]
    palavras[11]=["significado","perspectiva","contundente","intervenção","resistência","compreender","especulação","negligência","congruência","admoestação","intersecção","procedência","diplomático","sensacional","inteligível","dependência", "cerceamento","confluência","culminância","tendencioso"] 
    palavras[12]=["perseverança","condolências","remanescente","prerrogativa","extrovertido","complacência","condolências","remanescente","prerrogativa","extrovertido","complacência","procrastinar","discrepância","determinação","independente","consequência","intermitente","conveniência","imprevisível","procrastinar"]

class Jogo:
    def __init__(self,pontos,nome):
        self.pontos=pontos
        self.nome=nome
        self.palavras= Palavra()
        
        self.palavra = Jogo.palavra(escolha)

    def palavra(escolha):
        esp=''
        for i in range(escolha):     
            esp+=' _'
        return esp
     
    def atualizar(self,score,erro):
        carinha = ""
        braco = ""
        corpinho = ""
        perna = ""
        
        if erro==0:
            carinha=' '
            braco=' '
            corpinho=' '
            perna=' '
        if erro==1:
            carinha='( ͡ᵔ ͜ʖ ͡ᵔ)'
            braco=' '
            corpinho=' '
            perna=' '
        elif erro==2:
            carinha='( ͡ᵔ ͜ʖ ͡ᵔ)'
            braco='        _/¯'
            corpinho=' '
            perna=' '
        elif erro==3:
            carinha='( ͠0 ͟ʖ ͡0)'
            braco='¯\_  _/¯'
            corpinho=' '
            perna=' '
        elif erro==4:
            carinha='( ͠0 ʖ ͡0)'
            braco='¯\_ | _/¯'
            corpinho=' '
            perna=''
        elif erro==5:
            carinha='( ⊙ヮ⊙ )'
            braco='¯\_ | _/¯'
            corpinho=' '
            perna=' _/        '
        elif erro==6:          
            carinha=' ( ◑‿◐ ) '
            braco='¯\_ | _/¯'
            corpinho=' '
            perna=' _/   \_    '
    
        elif erro==7:
            carinha=' ( ◑‿◐ ) '
            braco='¯\_ | _/¯'
            corpinho='  | '
            perna=' _/   \_    '


        self.grafico = f'''         
         Pontuacao:  {score}
        
              _____________
              |           |
              |           | 
              |           |
              |       {carinha}
              |       {braco}          SUA PALAVRA COM {escolha} LETRAS e:
              |         {corpinho}
              |       {perna}
              |                                 
              |                               {self.palavra}
              |                                                        Nickname: {player1.nome}


        '''

class Pontuacao:
    score = 0
    def pontos(self, escolha):
        if escolha==3:
            self.score+=5
        elif escolha==4:
            self.score+=6
        elif escolha==5:
            self.score+=7
        elif escolha==6:
            self.score+=8
        elif escolha==7:
            self.score+=9
        elif escolha==8:
            self.score+=10
        elif escolha==9:
            self.score+=11
        elif escolha==10:
            self.score+=12
        elif escolha==11:
            self.score+=13
        elif escolha==12:
            self.score+=14
        return self.score

nome=input('Digite seu nickname: ')
escolha=int(input('Digite o numero de letras que voce quer na palavra: '))
player1=Jogo(0,nome)     

def main():

    palavras = Palavra()
    lista = palavras.palavras[escolha]
    palavra = choice(lista)
    underlines = Jogo.palavra(escolha)
    erro = 0
    pontuacao = 0
    while True:
        if erro == 7:
            print("GAME OVER!!!!")
            print(f" A palavra era '{palavra}'")
            print(f"Sua pontuação foi {pontuacao}")
            break

        letra = input('Digite uma letra: ')

        if not letra in palavra:
            erro += 1
            pontuacao-=2

        cont = 0
        indices = []
        for c in palavra:  
            
            if c == letra:
                indices.append(cont * 2 + 1)
            cont += 1

        for c in indices:
            underlines = underlines[:c] + letra + underlines[c + 1:]
        
        scr=Pontuacao()
        if letra in palavra:
            pontuacao += scr.pontos(escolha)
        player1.palavra = underlines

        palavra_nova = palavra
        for c in player1.palavra:
            if c in palavra_nova:
                palavra_nova = palavra_nova.replace(c, "")
        
        if not palavra_nova:
            player1.atualizar(pontuacao,erro)
            print(player1.grafico)
            mens='''                
                # # # # # # # # # # # # # # # # # # # # # # # #                                    
                #                                             #
                #         PARABÉNS VOCÊ VENCEUU!! (◍•ᴗ•◍)❤  #
                #           Obrigada por jogar..              #
                # # # # # # # # # # # # # # # # # # # # # # # #'''
            print(mens)
            print(f'Sua pontuação final foi {pontuacao}')
            break
            
        player1.atualizar(pontuacao, erro)
        print(player1.grafico)

main()