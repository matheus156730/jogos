from time import sleep
import random
import re

itens = {'y': 0, 'z': 0}

print('\033[1;97;40m2 ANOS ANTES...\n')
sleep(5)
print('MAIS DE 5 MILHÕES DE PESSOAS MORRIAM MUNDO AFORA POR CONTA DE UM VÍRUS QUE ASSOLOU A HUMANIDADE.')
sleep(5)
print('TENDO SEU INÍCIO NA CHINA, O VÍRUS SARS-COV-12 COMEÇOU A SE DISSEMINAR EM PROPORÇÕES DESESPERADORAS PARA A RAÇA HUMANA!')
sleep(5)
print('ALÉM DE SER CAPAZ DE LEVAR O INFECTADO À MORTE EM POUCOS MINUTOS, ESSE PATÓGENO TEM MUITA FACILIDADE PARA SE ESPALHAR.')
sleep(5)
print('APAVORANDO A POPULAÇÃO DE DIVERSOS PAÍSES, GOVERNOS E AUTORIDADES PERDERAM O CONTROLE DA SITUAÇÃO...')
sleep(5)
print('COM A PANDEMIA, VEIO O CAOS ECONÔMICO E CONSEQUENTEMENTE A FOME.')
sleep(5)
print('ATUALMENTE, AS MORTES AUMENTAM EXPONENCIALMENTE TODAS AS SEMANAS, O PLANETA VIROU UM CEMITÉRIO HUMANO!')
sleep(5)
print('PARA A ESPERANÇA DO MUNDO, UM GRUPO DE CIENTISTAS AUSTRÍACOS DESCOBRIU A FÓRMULA PARA CRIAR UMA VACINA...')
sleep(5)
print('NO ENTANTO, A PRINCIPAL SUBSTÂNCIA SÓ PODERIA SER ENCONTRADA NA AMAZÔNIA, EXTRAÍDA DE UMA PLANTA CHAMADA Victoria amazonica.')
sleep(5)
print('''EM UMA MASMORRA PROTEGIDA E DE DIFÍCIL ACESSO, NO SUBSOLO DA FLORESTA AMAZÔNICA,
OS AUSTRÍACOS INICIARAM O PROCESSO DE FABRICAÇÃO DA CURA APÓS EXTRAÍREM COM ÊXITO O COMPONENTE NECESSÁRIO...''')
sleep(7)
print('PORÉM, APÓS A FABRICAÇÃO SER CONCLUÍDA, UMA TRAGÉDIA OCORREU... OS PESQUISADORES ACABARAM SOTERRADOS NA MASMORRA!')
sleep(5)
print('VOCÊ!!! O ESCOLHIDO, É O RESPONSÁVEL POR ADENTRAR A PERIGOSA MASMORRA E TRAZER A CURA PARA TODA A HUMANIDADE!\n\033[0m\n')
sleep(5)
print(' ' * 25 + '\033[1;34;107mA MASMORRA\033[0m' + ' ' * 25)
print('\n\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mBEM VINDO À MASMORRA, ESCOLHIDO! SIGA SUA INTUIÇÃO, TODOS CONTAM COM VOCÊ!')

# ----------------------------------------------FUNÇÃO GAME OVER - SALA PRINCIPAL---------------------------------------------------------------------
def game_over():
    print('\033[0;34;49m\033[1;31;49mGAME OVER! VOCÊ FALHOU, ESCOLHIDO! AGORA NÃO HÁ MAIS ESPERANÇA!')
    print('\n\033[4;30mAPERTE "S" PARA JOGAR NOVAMENTE E "N" SE QUISER ENCERRAR O JOGO!')

    restart = input().upper().strip()

    while restart != 'S' and restart != 'N':
        print('\n\033[4;30mAPERTE "S" PARA JOGAR NOVAMENTE E "N" SE QUISER ENCERRAR O JOGO!')
        restart = input().upper().strip()

    if restart == 'S':
        sala_principal()

    elif restart == 'N':
        exit()
    # -------------------------------------------------FUNÇÃO GAME OVER - SALA SEGURA (CAMINHO DA ESQUERDA)-----------------------------------------------
def game_over2():
    print('\033[1;31;49mGAME OVER! VOCÊ FALHOU, ESCOLHIDO! AGORA NÃO HÁ MAIS ESPERANÇA!')
    print('\n\033[4;30mAPERTE "S" PARA VOLTAR À SALA SEGURA, "R" PARA REINICIAR O JOGO E "N" SE QUISER ENCERRAR O JOGO!')

    restart = input().upper().strip()

    while restart != 'S' and restart != 'N' and restart != 'R':
        print('\n\033[4;30mAPERTE "S" PARA VOLTAR À SALA SEGURA, "R" PARA REINICIAR O JOGO E "N" SE QUISER ENCERRAR O JOGO!')
        restart = input().upper().strip()

    if restart == 'S':
        sala_segura_esquerda()

    elif restart == 'R':
        sala_principal()

    elif restart == 'N':
        exit()
# -------------------------------------------------FUNÇÃO GAME OVER - SALA SEGURA (CAMINHO DA DIREITA)------------------------------------------------
def game_over3():
    print('\033[1;31;49mGAME OVER! VOCÊ FALHOU, ESCOLHIDO! AGORA NÃO HÁ MAIS ESPERANÇA!')
    print('\n\033[4;30mAPERTE "S" PARA VOLTAR À SALA SEGURA, "R" PARA REINICIAR O JOGO E "N" SE QUISER ENCERRAR O JOGO!')

    restart2 = input().upper().strip()

    while restart2 != 'S' and restart2 != 'N' and restart2 != 'R':
        print('\n\033[4;30mAPERTE "S" PARA VOLTAR À SALA SEGURA, "R" PARA REINICIAR O JOGO E "N" SE QUISER ENCERRAR O JOGO!')
        restart2 = input().upper().strip()

    if restart2 == 'S':
        sala_segura_direita()

    elif restart2 == 'R':
        sala_principal()

    elif restart2 == 'N':
        exit()
# ------------------------------------------------------------------FUNÇÃO GANHOU---------------------------------------------------------------------
def ganhou():
    print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mSempre soube que você realmente era o Escolhido!!!')
    print('''\n\033[1;32;49mVOCÊ VENCEU! A JORNADA FOI LONGA E DIFÍCIL, MAS COM CERTEZA VALEU A PENA. AGORA TUDO PODERÁ SER COMO ERA ANTES... 
COM A VACINA, EM POUCO TEMPO TUDO FICARÁ BEM NOVAMENTE. A HUMANIDADE ESTÁ SALVA!!!''')
    print('\n\033[1;39;49mCréditos: \nMatheus Oliveira Ferraz de Campos \nDiendly Antonielly Farnezi Miranda \nArthur Henrique Honorio Nassur')
# ------------------------------------------------------FUNÇÃO 1 (SALA PRINCIPAL)---------------------------------------------------------------------
def sala_principal():
    print('\n\033[0;34;49m\033[1;30;107mSALA PRINCIPAL')
    print('''\033[0;34;49m-Voz misteriosa: \033[1;39;49mVocê se encontra na sala principal da masmorra! À sua frente há duas portas...
Na porta à direita há vários buracos de bala... A porta da esquerda está aberta, mas a escuridão predomina na sala a seguir...
Faça sua escolha (D/E)!''')

    principal = input().upper().strip()

    while principal != 'D' and principal != 'E':
        print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mPreste atenção Escolhido! As únicas escolhas possíveis são D ou E!')
        principal = input().upper().strip()

    if principal == 'D':
        sala_do_armeiro()

    elif principal == 'E':
        sala_escura()
# ------------------------------------------------------------CAMINHO DA ESQUERDA---------------------------------------------------------------------
# ---------------------------------------------------------FUNÇÃO 2 (SALA ESCURA)---------------------------------------------------------------------
def sala_escura():
    print('\n\033[1;30;107mSALA ESCURA')
    print('''\033[0;34;49m-Voz misteriosa: \033[1;39;49mVocê acaba de entrar na sala mais escura de toda a masmorra... Sabe-se lá o que se pode 
encontrar aqui embaixo... Um odor distinto parece vir da porta à direita, adesivada com um trifólio...
Enquanto à sua esquerda, há uma porta toda ensanguentada...
Faça sua escolha (D/E)!''')

    escura = input().upper().strip()

    while escura != 'D' and escura != 'E':
        print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mPreste atenção Escolhido! As únicas escolhas possíveis são D ou E!')
        escura = input().upper().strip()

    if escura == 'D':
        print('\n\033[1;30;107mSALA DO GÁS')
        print('''\033[1;31;49mAO ENTRAR NA SALA DO GÁS, VOCÊ PERCEBEU QUE O ODOR ERA DE UMA SUBSTÂNCIA TÓXICA... 
VOCÊ MORREU POUCOS MINUTOS APÓS INALAR O GÁS!''')
        game_over()

    elif escura == 'E':
        sala_do_cadaver()
# -----------------------------------------------------FUNÇÃO 3 (SALA DO CADÁVER)---------------------------------------------------------------------
def sala_do_cadaver():
    print('\n\033[1;30;107mSALA DO CADÁVER')
    print('''\033[0;34;49m-Voz misteriosa: \033[1;39;49mO nome dessa sala fala por si só, escolhido... Ao adentrar, você se depara com
um homem morto usando uma máscara de gás. Nunca se sabe quando uma máscara dessa vai ser útil...''')
    print('\n\033[4;30mPressione "P" para pegar a máscara e "D" para deixá-la!')
    pegar = input().upper().strip()

    while pegar != 'P' and pegar != 'D':
        print('\n\033[4;30mPressione "P" para pegar a máscara e "D" para deixá-la!')
        pegar = input().upper().strip()

    if pegar == 'P':
        itens['y'] = 1
        print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mNão dúvido que será útil durante sua jornada!')

    elif pegar == 'D':
        itens['y'] = 0
        print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mFaltou coragem, escolhido?')

    sleep(4)
    print('''\033[0;34;49m-Voz misteriosa: \033[1;39;49mAgora há mais uma escolha a ser feita... Escolha com sabedoria, todos contam com você!
À direita, a próxima sala parece calma, bem iluminada e com som de cachoeira... Um paraíso...
Enquanto à esquerda, barulhos de grunhido chamam atenção atrás da porta...
Qual será sua escolha (D/E)?''')

    cadaver = input().upper().strip()

    while cadaver != 'D' and cadaver != 'E':
        print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mPreste atenção Escolhido! As únicas escolhas possíveis são D ou E!')
        cadaver = input().upper().strip()

    if cadaver == 'D':
        sala_segura_esquerda()

    elif cadaver == 'E':
        print('\n\033[1;30;107mSALA CHEIA DE CROCODILOS')
        print('''\033[1;31;49mAO ABRIR A PORTA, VOCÊ CAIU EM UM POÇO CHEIO DE CROCODILOS QUE ERAM CRIADOS PELOS PESQUISADORES AUSTRÍACOS...
UMA MORTE DOLOROSA... MAIS SABEDORIA DA PRÓXIMA VEZ ESCOLHIDO!''')
        game_over()
# ---------------------------------------------------------FUNÇÃO 4 (SALA SEGURA)---------------------------------------------------------------------
def sala_segura_esquerda():
    print('\n\033[0;34;49m\033[1;32;107mSALA SEGURA')
    print('\033[0;34;49m-Voz misteriosa: \033[1;39;49mQuem diria, escolhido? Você progrediu... Esta sala é segura, você está protegido aqui!')
    print('\n\033[4;30mA SALA SEGURA É UM CHECKPOINT, DE AGORA EM DIANTE VOCÊ VOLTA DAQUI SEMPRE QUE MORRER!')
    print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mSó há um caminho adiante, escolhido... É o seu destino! Siga em frente!')
    print('\n\033[4;30mPressiona "A" para abrir a porta!')
    abrir = input().upper().strip()

    while abrir != 'A':
        print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mVocê não quer seguir em frente, escolhido? A humanidade conta com você!')
        print('\n\033[4;30mPressiona "A" para abrir a porta!')
        abrir = input().upper().strip()

    sala_do_homem_ferido()
# ------------------------------------------------FUNÇÃO 6 (SALA DO HOMEM FERIDO)---------------------------------------------------------------------
def sala_do_homem_ferido():
    print('\n\033[0;30;107m\033[1;30;107mSALA DO HOMEM FERIDO')
    print('\033[0;34;49m-Voz misteriosa: \033[1;39;49mNo canto da sala há um homem gravemente machucado...')
    sleep(3)
    print('\n\033[0;33;49m-Homem ferido: \033[1;39;49mCof... Não é possível... Cof cof cof... Idiotas...')
    sleep(3)
    print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mDeseja ajudar o homem, escolhido?')
    print('\n\033[4;30mPressione "A" para ajudar e "P" para passar despercebido!')

    homem_ferido = input().upper().strip()

    while homem_ferido != 'A' and homem_ferido != 'P':
        print('\n\033[4;30mPressione "A" para ajudar e "P" para passar despercebido!')
        homem_ferido = input().upper().strip()

    if homem_ferido == 'A':
        print('''\n\033[0;33;49m-Homem ferido: \033[1;39;49mAjuda? Eu não preciso de você... Cof cof... Eu já perdi tudo, levaram meus filhos... 
Minha esposa... Cof cof... Eu e minha família servimos de cobaia assim como dezenas de pessoas... 
Minha sanidade mental foi embora por causa dessa pesquisa... Aqueles austríacos pagarão! Cof cof... 
O mundo quer ter a cura às custas do sofrimento meu e da minha família... Jamais permitirei!!!''')
        sleep(12)
        print('''\n\033[1;31;49mO HOMEM GUARDAVA UM PEDAÇO DE VIDRO E AVANÇOU PARA CIMA DE VOCÊ, MORTE RÁPIDA...
A SOLIDARIEDADE NEM SEMPRE É O MELHOR CAMINHO, ESCOLHIDO!''')
        game_over2()

    elif homem_ferido == 'P':
        sala_dos_cobaias()
# ----------------------------------------------------FUNÇÃO 7 (SALA DOS COBAIAS)---------------------------------------------------------------------
def sala_dos_cobaias():
    print('\n\033[0;30;107m\033[1;30;107mSALA DOS COBAIAS')
    print('''\033[0;34;49m-Voz misteriosa: \033[1;39;49mEssa sala parece ser o cativeiro dos cobaias, como o homem que você acabou de encontrar...
Esses corpos presos em macas eram pessoas usadas nos experimentos da vacina... A maioria enlouqueceu!''')
    print('''\033[0;34;49m-Voz misteriosa: \033[1;39;49mFelizmente ou infelizmente, nessa sala há vários compartimentos que armazenam milhares de
doses teste da vacina...''')
    print('\n\033[4;30mPressione "S" para pegar uma vacina e aplicá-la e "N" para ignorar!')

    tomar = input().upper().strip()

    while tomar != 'S' and tomar != 'N':
        print('\n\033[4;30mPressione "S" para pegar uma vacina e aplicá-la e "N" para ignorar!')
        tomar = input().upper().strip()

    if tomar == 'N':
        print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mInteressante... Não quis a vacina? Siga para a pŕoxima sala, escolhido!')
        print('\n\033[4;30mPressione "A" para abrir a porta!')
        cobaias = input().upper().strip()

        while cobaias != 'A':
            print('\n\033[4;30mPressione "A" para abrir a porta!')

        if cobaias == 'A':
            sala_contaminada()

    elif tomar == 'S':
        print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mMuito ingênuo, escolhido! Seja mais desconfiado na próxima vez!')
        print('''\n\033[1;31;49mVOCÊ, ASSIM COMO A MAIORIA DOS COBAIAS, SUCUMBIU À LOUCURA APÓS INJETAR A VACINA. ERA UMA VACINA EM FASE DE TESTE!''')
        game_over2()
# ----------------------------------------------------FUNÇÃO 8 (SALA CONTAMINADA)---------------------------------------------------------------------
def sala_contaminada():
    print('\n\033[0;34;49m\033[1;30;107mSALA CONTAMINADA')
    print('''\033[0;34;49m-Voz misteriosa: \033[1;39;49mEssa sala está completamente contaminada com o vírus mortal... 
Você acha que foi corajoso até aqui, escolhido?''')

    if itens['y'] == 1:
        sleep(4)
        print('''\033[0;34;49m-Voz misteriosa: \033[1;39;49mVocê será recompensado pela coragem que teve ao pegar a máscara daquele cadáver! 
Agora é a hora de usá-la!''')
        print('\n\033[4;30mPressione "C" para colocar a máscara e "N" para ignorar!')
        mascara = input().upper().strip()

        if mascara == 'C':
            print('''\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mÓtimo, dessa forma você não é contaminado pelo vírus, máscara salva!! 
Pelo que parece você está chegando ao fim da sua jornada... Imaginou que chegaria tão longe?... A vacina está próxima!''')
            print('''\033[0;34;49m-Voz misteriosa: \033[1;39;49mOs austríacos tomavam todo o cuidado do mundo com essa próxima sala... É a sala 
onde a vacina está guardada. A porta possui uma senha de 17 dígitos (sem contar espaços)... A senha é algo que foi de extrema importância 
para a fabricação da vacina!''')
            print('\n\033[4;30mPressione "T" para tentar acertar a senha e "D" para receber uma dica!')
            contaminada = input().upper().strip()

            while contaminada != 'T' and contaminada != 'D':
                print('\n\033[4;30mPressione "T" para tentar acertar a senha e "D" para receber uma dica!')
                contaminada = input().upper().strip()

            if contaminada == 'T':
                print('\n\033[4;30mDigite a senha!')
                senha = input().strip().capitalize()

                while senha != 'Victoriaamazonica':
                    print('\n\033[4;30mSenha incorreta, tente novamente! Se deseja ver a dica, digite "D"!')
                    senha = input().strip().capitalize()

                    if senha == 'D':
                        print('''\nDICA: A SENHA É O NOME CIENTÍFICO DE UMA PLANTA FUNDAMENTAL NA PREPARAÇÃO DA VACINA E TÍPICA DA AMAZÔNIA (SEM ESPAÇOS)!
OBS: A SENHA FOI CITADA NA INTRODUÇÃO DO JOGO!''')
                        senha = input().strip().capitalize()

                if senha == 'Victoriaamazonica':
                    sala_da_vacina_esquerda()

            if contaminada == 'D':
                print('''\n\033[4;30mDICA: A SENHA É O NOME CIENTÍFICO DE UMA PLANTA FUNDAMENTAL NA PREPARAÇÃO DA VACINA E TÍPICA DA AMAZÔNIA (SEM ESPAÇOS)!
OBS: A SENHA FOI CITADA NA INTRODUÇÃO DO JOGO!''')
                senha = input().strip().capitalize()

                while senha != 'Victoriaamazonica':
                    print('\n\033[4;30mSenha incorreta, tente novamente! Se deseja ver a dica, digite "D"!')
                    senha = input().strip().capitalize()

                    if senha == 'D':
                        print('''\nDICA: A SENHA É O NOME CIENTÍFICO DE UMA PLANTA FUNDAMENTAL NA PREPARAÇÃO DA VACINA E TÍPICA DA AMAZÔNIA (SEM ESPAÇOS)!
OBS: A SENHA FOI CITADA NA INTRODUÇÃO DO JOGO!''')
                        senha = input().strip().capitalize()

                if senha == 'Victoriaamazonica':
                    sala_da_vacina_esquerda()

        if mascara == 'N':
            print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mPor que, escolhido? Por que não usar a máscara?')
            print('\n\033[1;31;49mVOCÊ FOI CONTAMINADO PELO VÍRUS MORTAL, NINGUÉM SOBREVIVE A ESSE MALDITO VÍRUS SEM MÁSCARA!')
            game_over2()

    elif itens['y'] == 0:
        sleep(4)
        print('''\033[0;34;49m-Voz misteriosa: \033[1;39;49mA máscara daquele cadáver seria bem útil agora, hein? 
Mais coragem na próxima vez...''')
        print('\n\033[1;31;49mVOCÊ FOI CONTAMINADO PELO VÍRUS MORTAL... NINGUÉM SOBREVIVE A ESSE MALDITO VÍRUS SEM MÁSCARA!')
        print('\n\033[4;30mVocê deve retornar ao início do jogo para que faça escolhas diferentes e consiga progredir nessa fase!\n')
        game_over()


# -------------------------------------------FUNÇÃO 9 (SALA DA VACINA - ESQUERDA)---------------------------------------------------------------------
def sala_da_vacina_esquerda():
    print('\n\033[0;30;107m\033[1;30;107mSALA DA VACINA')
    print('''\033[0;34;49m-Voz misteriosa: \033[1;39;49mVocê chegou, escolhido! Esse sempre foi o seu destino! Você está na sala da vacina...
A vacina e a fórmula para a fabricação estão na cúpula de vidro no centro da sala!''')
    print('\n\033[4;30mAperte "P" para abrir a cúpula e pegá-los!')

    vacina_esquerda = input().upper().strip()

    while vacina_esquerda != 'P':
        print('''\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mVocê se dedicou tanto para chegar até aqui escolhido... 
A raça humana conta com você, pegue a vacina e a fórmula!''')
        print('\n\033[4;30mAperte "P" para abrir a cúpula e pegá-los!')
        vacina_esquerda = input().upper().strip()

    if vacina_esquerda == 'P':
        print('''\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mÓtimo, escolhido! Finalmente! 
A saída secreta da masmorra é pelo elevador no canto da sala...''')
        print('\n\033[4;30mPressione "C" para chamar o elevador e sair da masmorra!')
        elevador = input().upper().strip()

        while elevador != 'C':
            print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mVocê conseguiu, escolhido! Leve a cura para toda a humanidade!')
            print('\n\033[4;30mPressione "C" para chamar o elevador e sair da masmorra!')
            elevador = input().upper().strip()

        if elevador == 'C':
            ganhou()
# -------------------------------------------------------------CAMINHO DA DIREITA---------------------------------------------------------------------
# -------------------------------------------------------FUNÇÃO 10 (SALA ARMEIRO)---------------------------------------------------------------------
def sala_do_armeiro():
    print('\n\033[0;30;107m\033[1;30;107mSALA DO ARMEIRO')
    print('\033[0;34;49m-Voz misteriosa: \033[1;39;49mCorajoso, escolhido... Veio pelo caminho dos tiros... Interessante!')
    sleep(3)
    print('''\n\033[0;33;49m-Armeiro: \033[1;39;49mQue bom! Até que enfim alguém apareceu... Você deve ser o destinado a trazer a cura.
Bem... Eu já tentei chegar à sala da vacina e não tive coragem suficiente para seguir o caminho todo.''')
    sleep(7)
    print('''\033[0;33;49m-Armeiro: \033[1;39;49mJá que você está decidido a ir até a vacina, o máximo que posso fazer para ajudar é te dar uma arma...
Ela está carregada com balas de tranquilizante! Garanto que pode ser útil a você...''')
    print('\n\033[4;30mAperte "P" para pegar a arma do armeiro e "N" para ignorar!')

    pegar_arma = input().upper().strip()

    while pegar_arma != 'P' and pegar_arma != 'N':
        print('\n\033[4;30mAperte "P" para pegar a arma do armeiro e "N" para ignorar!')
        pegar_arma = input().upper().strip()

    if pegar_arma == 'P':
        print('\n\033[0;33;49m-Armeiro: \033[1;39;49mVocê não se arrependerá! Conto com você, boa sorte!')
        itens['z'] = 1

    elif pegar_arma == 'N':
        print('\n\033[0;33;49m-Armeiro: \033[1;39;49mTudo bem... De qualquer forma, boa sorte em sua jornada!')
        itens['z'] = 0

    print('''\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mDecida o seu próximo passo, escolhido! À sua direita, há um elevador.
Enquanto à sua esquerda, há uma porta com som de latidos ao fundo!
Faça sua escolha (D/E)!''')

    armeiro = input().upper().strip()

    while armeiro != 'D' and armeiro != 'E':
        print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mPreste atenção Escolhido! As únicas escolhas possíveis são D ou E!')
        armeiro = input().upper().strip()

    if armeiro == 'D':
        sala_do_elevador()

    elif armeiro == 'E':
        print('\n\033[0;34;49m\033[1;30;107mSALA DOS CACHORROS')
        print('\033[1;31;49mOS LATIDOS VINHAM DOS CACHORROS DE SEGURANÇA USADOS PELOS AUSTRÍACOS. ELES AVAMÇARAM ASSIM QUE VOCÊ ENTROU...')
        game_over()
# ---------------------------------------------------FUNÇÃO 11 (SALA DO ELEVADOR)---------------------------------------------------------------------
def sala_do_elevador():
    print('\n\033[0;30;107m\033[1;30;107mSALA DO ELEVADOR')
    print('''\033[0;34;49m-Voz misteriosa: \033[1;39;49mBem vindo ao elevador, escolhido... Aqui você pode escolher entre dois andares subterrâneos.
No botão do subsolo 1 há um desenho do mapa do Egito. Enquanto no botão do subsolo 2 há o desenho de uma gota d'água...
Faça sua escolha (1/2)!''')

    escolha_elevador = input().strip()

    while escolha_elevador != '1' and escolha_elevador != '2':
        print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mPreste atenção Escolhido! As únicas escolhas possíveis são 1 ou 2!')
        escolha_elevador = input().strip()

    if escolha_elevador == '1':
        sala_da_esfinge()

    elif escolha_elevador == '2':
        print('\n\033[0;34;49m\033[1;30;107mSALA DA ÁGUA')
        print('''\033[1;31;49mNÃO DEU NEM TEMPO DE ENTENDER O QUE ACONTECEU. O SUBSOLO 2 ESTAVA INUNDADO DE ÁGUA... AO ABRIR A PORTA, O 
ELEVADOR FOI TOMADO E VOCÊ FICOU SEM RESPIRAR!''')
        game_over()
# ----------------------------------------------------FUNÇÃO 12 (SALA DA ESFINGE)---------------------------------------------------------------------
def sala_da_esfinge():
    print('\n\033[0;30;107m\033[1;30;107mSALA DA ESFINGE')
    print('\033[0;34;49m-Voz misteriosa: \033[1;39;49mBem vindo à sala mais mítica da masmorra! Um clima estranho toma conta da sala...')
    sleep(3)
    print('''\n\033[0;33;49m-Esfinge: \033[1;39;49mQuem diria... Nunca imaginei encontrar alguém vivo por aqui... 
Para passar para a próxima sala não será tão fácil como você imagina... 
Você terá que me vencer em um jogo complexo que requer altíssimas habilidades estratégicas e conhecimento de mundo...''')
    sleep(12)
    print('\033[0;33;49m-Esfinge: \033[1;39;49mJOKENPÔ!!!')
    sleep(3)

    print('\n\033[0;33;49m-Esfinge: \033[1;39;49mVamos jogar! Escolha entre Pedra, Papel e Tesoura!')
    jokenpo_saida = 0
    jokenpo_escolha_do_pc = re.sub("[]'[]", '', str(random.choices(['Pedra', 'Tesoura', 'Papel'])))
    jokenpo_escolha_do_jogador = input().strip().capitalize()
    while jokenpo_escolha_do_jogador != 'Pedra' and jokenpo_escolha_do_jogador != 'Papel' and jokenpo_escolha_do_jogador != 'Tesoura':
        print('\n\033[0;33;49m-Esfinge: \033[1;39;49mNo JOKENPÔ só é permitido escolher entre Pedra, Papel ou Tesoura!')
        jokenpo_escolha_do_jogador = input().strip().capitalize()
    while jokenpo_saida == 0:
        while jokenpo_escolha_do_jogador == 'Pedra':
            if jokenpo_escolha_do_pc == 'Pedra':
                print('\n\033[0;33;49m-Esfinge: \033[1;39;49mEMPATAMOS! Você escolheu {} e eu escolhi {}! Vamos jogar de novo!'
                      .format(jokenpo_escolha_do_jogador, jokenpo_escolha_do_pc))
                jokenpo_escolha_do_pc = re.sub("[]'[]", '', str(random.choices(['Pedra', 'Tesoura', 'Papel'])))
                jokenpo_escolha_do_jogador = input().strip().capitalize()
                while jokenpo_escolha_do_jogador != 'Pedra' and jokenpo_escolha_do_jogador != 'Papel' and jokenpo_escolha_do_jogador != 'Tesoura':
                    print('\n\033[0;33;49m-Esfinge: \033[1;39;49mNo JOKENPÔ só é permitida a escolha de Pedra, Papel ou Tesoura!')
                    jokenpo_escolha_do_jogador = input().strip().capitalize()
            elif jokenpo_escolha_do_pc == 'Papel':
                print('\n\033[0;33;49m-Esfinge: \033[1;31;49mGANHEI! \033[1;39;49mVocê escolheu {} e eu escolhi {}! Jogaremos novamente!'
                    .format(jokenpo_escolha_do_jogador, jokenpo_escolha_do_pc))
                jokenpo_escolha_do_pc = re.sub("[]'[]", '', str(random.choices(['Pedra', 'Tesoura', 'Papel'])))
                jokenpo_escolha_do_jogador = input().strip().capitalize()
                while jokenpo_escolha_do_jogador != 'Pedra' and jokenpo_escolha_do_jogador != 'Papel' and jokenpo_escolha_do_jogador != 'Tesoura':
                    print('\n\033[0;33;49m-Esfinge: \033[1;39;49mNo JOKENPÔ só é permitida a escolha de Pedra, Papel ou Tesoura!')
                    jokenpo_escolha_do_jogador = input().strip().capitalize()
            elif jokenpo_escolha_do_pc == 'Tesoura':
                print('\n\033[0;33;49m-Esfinge: \033[1;32;49mVOCÊ GANHOU! \033[1;39;49mVocê escolheu {} e eu escolhi {}! Quem diria...'
                    .format(jokenpo_escolha_do_jogador, jokenpo_escolha_do_pc))
                jokenpo_saida = 1
                jokenpo_escolha_do_jogador = 'SAIR'
        while jokenpo_escolha_do_jogador == 'Papel':
            if jokenpo_escolha_do_pc == 'Papel':
                print('\n\033[0;33;49m-Esfinge: \033[1;39;49mEMPATAMOS! Você escolheu {} e eu escolhi {}! Vamos jogar de novo!'
                    .format(jokenpo_escolha_do_jogador, jokenpo_escolha_do_pc))
                jokenpo_escolha_do_pc = re.sub("[]'[]", '', str(random.choices(['Pedra', 'Tesoura', 'Papel'])))
                jokenpo_escolha_do_jogador = input().strip().capitalize()
                while jokenpo_escolha_do_jogador != 'Pedra' and jokenpo_escolha_do_jogador != 'Papel' and jokenpo_escolha_do_jogador != 'Tesoura':
                    print('\n\033[0;33;49m-Esfinge: \033[1;39;49mNo JOKENPÔ só é permitida a escolha de Pedra, Papel ou Tesoura!')
                    jokenpo_escolha_do_jogador = input().strip().capitalize()
            elif jokenpo_escolha_do_pc == 'Tesoura':
                print('\n\033[0;33;49m-Esfinge: \033[1;31;49mGANHEI! \033[1;39;49mVocê escolheu {} e eu escolhi {}! Jogaremos novamente!'
                    .format(jokenpo_escolha_do_jogador, jokenpo_escolha_do_pc))
                jokenpo_escolha_do_pc = re.sub("[]'[]", '', str(random.choices(['Pedra', 'Tesoura', 'Papel'])))
                jokenpo_escolha_do_jogador = input().strip().capitalize()
                while jokenpo_escolha_do_jogador != 'Pedra' and jokenpo_escolha_do_jogador != 'Papel' and jokenpo_escolha_do_jogador != 'Tesoura':
                    print('\n\033[0;33;49m-Esfinge: \033[1;39;49mNo JOKENPÔ só é permitida a escolha de Pedra, Papel ou Tesoura!')
                    jokenpo_escolha_do_jogador = input().strip().capitalize()
            elif jokenpo_escolha_do_pc == 'Pedra':
                print('\n\033[0;33;49m-Esfinge: \033[1;32;49mVOCÊ GANHOU! \033[1;39;49mVocê escolheu {} e eu escolhi {}! Quem diria...'
                    .format(jokenpo_escolha_do_jogador, jokenpo_escolha_do_pc))
                jokenpo_saida = 1
                jokenpo_escolha_do_jogador = 'SAIR'
        while jokenpo_escolha_do_jogador == 'Tesoura':
            if jokenpo_escolha_do_pc == 'Pedra':
                print('\n\033[0;33;49m-Esfinge: \033[1;31;49mGANHEI! \033[1;39;49mVocê escolheu {} e eu escolhi {}! Jogaremos novamente!'
                    .format(jokenpo_escolha_do_jogador, jokenpo_escolha_do_pc))
                jokenpo_escolha_do_pc = re.sub("[]'[]", '', str(random.choices(['Pedra', 'Tesoura', 'Papel'])))
                jokenpo_escolha_do_jogador = input().strip().capitalize()
                while jokenpo_escolha_do_jogador != 'Pedra' and jokenpo_escolha_do_jogador != 'Papel' and jokenpo_escolha_do_jogador != 'Tesoura':
                    print('\n\033[0;33;49m-Esfinge: \033[1;39;49mNo JOKENPÔ só é permitida a escolha de Pedra, Papel ou Tesoura!')
                    jokenpo_escolha_do_jogador = input().strip().capitalize()
            elif jokenpo_escolha_do_pc == 'Tesoura':
                print('\n\033[0;33;49m-Esfinge: \033[1;39;49mEMPATAMOS! Você escolheu {} e eu escolhi {}! Vamos jogar de novo!'
                    .format(jokenpo_escolha_do_jogador, jokenpo_escolha_do_pc))
                jokenpo_escolha_do_pc = re.sub("[]'[]", '', str(random.choices(['Pedra', 'Tesoura', 'Papel'])))
                jokenpo_escolha_do_jogador = input().strip().capitalize()
                while jokenpo_escolha_do_jogador != 'Pedra' and jokenpo_escolha_do_jogador != 'Papel' and jokenpo_escolha_do_jogador != 'Tesoura':
                    print('\n\033[0;33;49m-Esfinge: \033[1;39;49mNo JOKENPÔ só é permitida a escolha de Pedra, Papel ou Tesoura!')
                    jokenpo_escolha_do_jogador = input().strip().capitalize()
            elif jokenpo_escolha_do_pc == 'Papel':
                print('\n\033[0;33;49m-Esfinge: \033[1;32;49mVOCÊ GANHOU! \033[1;39;49mVocê escolheu {} e eu escolhi {}! Quem diria...'
                    .format(jokenpo_escolha_do_jogador, jokenpo_escolha_do_pc))
                jokenpo_saida = 1
                jokenpo_escolha_do_jogador = 'SAIR'

    print('''\n\033[0;33;49m-Esfinge: \033[1;39;49mFinalmente um oponente digno... Você é o primeiro a me derrotar nesse jogo...
Diante disso, você tem passagem livre para a próxima sala! Siga seu caminho!''')
    print('\n\033[4;30mPressione "A" para abrir a porta da próxima sala!')
    abrir = input().upper().strip()

    while abrir != 'A':
        print('\n\033[4;30mPressione "A" para abrir a porta da próxima sala!')
        abrir = input().upper().strip()

    if abrir == 'A':
        sala_segura_direita()
# ----------------------------------------------FUNÇÃO 13 (SALA SEGURA - DIREITA)---------------------------------------------------------------------
def sala_segura_direita():
    print('\n\033[0;34;49m\033[1;32;107mSALA SEGURA')
    print('\033[0;34;49m-Voz misteriosa: \033[1;39;49mVocê chegou à sala segura... Esta sala é como seu lar, você está protegido aqui!')
    print('\n\033[4;30mA SALA SEGURA É UM CHECKPOINT, DE AGORA EM DIANTE VOCÊ VOLTA DAQUI SEMPRE QUE MORRER!')
    print('''\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mHora de tomar mais uma decisão, escolhido... À sua esquerda há uma porta bem simples
de madeira com um brilhoso fixe de luz atravessando suas frestas. À direita há uma porta automática robusta de aço blindado...
Faça sua escolha (D/E)!''')

    segura_direita = input().upper().strip()

    while segura_direita != 'D' and segura_direita != 'E':
        print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mPreste atenção Escolhido! As únicas escolhas possíveis são D ou E!')
        segura_direita = input().upper().strip()

    if segura_direita == 'E':
        sala_do_cristal()

    elif segura_direita == 'D':
        print('\n\033[0;30;107m\033[1;30;107mSALA TRANCADA')
        print('\033[1;31;49mASSIM QUE VOCÊ ENTROU NA SALA, A PORTA BLINDADA SE TRANCOU AUTOMATICAMENTE... LOGO VOCÊ PERCEBE QUE NÃO HÁ MAIS SAÍDA!')
        game_over3()
# ----------------------------------------------------FUNÇÃO 14 (SALA DO CRISTAL)---------------------------------------------------------------------
def sala_do_cristal():
    print('\n\033[0;30;107m\033[1;30;107mSALA DO CRISTAL')
    print('''\033[0;34;49m-Voz misteriosa: \033[1;39;49mCuidado com os olhos, escolhido! A luz que vem dessa joia é extremamente forte...
Parece que os austríacos valorizavam muito essa pedra, a ponto de deixá-la em um pedestal tão protegido e em uma sala tão profunda na masmorra.''')
    sleep(8)
    print('''\033[0;34;49m-Voz misteriosa: \033[1;39;49mPara prosseguir, você deve pegar o cristal e colocá-lo no seu local de encaixe 
na porta da próxima sala... Sem o cristal não há como sair dessa sala.''')
    sleep(8)
    print('''\033[0;34;49m-Voz misteriosa: \033[1;39;49mNão é tão simples como parece! Há um sistema de segurança desenvolvido pelos austríacos para
detectar qualquer tipo de aproximação do cristal.... Você deve acertar a senha para chegar até ele!''')
    sleep(8)
    print('\033[0;34;49m-Voz misteriosa: \033[1;39;49mEm caso de erro na senha, o sistema te eliminará, escolhido! Tenha cuidado!')
    sleep(5)
    print('\033[0;34;49m-Voz misteriosa: \033[1;39;49mA senha tem 5 caracteres e é o nome do país onde todo o caos se iniciou!')
    print('\n\033[4;30mPressione "T" para tentar acertar a senha e "D" para receber uma dica!')

    cristal = input().upper().strip()

    while cristal != 'T' and cristal != 'D':
        print('\n\033[4;30mPressione "T" para tentar acertar a senha e "D" para receber uma dica!')
        cristal = input().upper().strip()

    if cristal == 'T':
        print('\n\033[4;30mDigite a senha!')
        senha2 = input().strip().capitalize()

        if senha2 != 'China':
            print('\n\033[0;34;49m\033[1;31;49mSENHA INCORRETA! VOCÊ FOI ELIMINADO PELO SISTEMA DE SEGURANÇA!')
            game_over3()

        elif senha2 == 'China':
            print('''\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mÓtimo, escolhido! Você passou pelo sistema de segurança... Agora é só pegar o cristal
e colocá-lo no seu local de encaixe na porta da próxima sala!''')
            print('\n\033[4;30mPressione "P" para pegar o cristal, encaixá-lo e seguir para a próxima sala!')
            seguir_cristal = input().upper().strip()

            while seguir_cristal != 'P':
                print('\n\033[4;30mPressione "P" para pegar o cristal, encaixá-lo e seguir para a próxima sala!')
                seguir_cristal = input().upper().strip()

            if seguir_cristal == 'P':
                sala_do_urso()

    elif cristal == 'D':
        print('''\n\033[4;30mDICA: A SENHA É O NOME DE UM PAÍS ASIÁTICO, ONDE O VÍRUS SURGIU!
OBS: A SENHA FOI CITADA NA INTRODUÇÃO DO JOGO!''')
        senha2 = input().strip().capitalize()

        if senha2 != 'China':
            print('\n\033[0;34;49m\033[1;31;49mSENHA INCORRETA! VOCÊ FOI ELIMINADO PELO SISTEMA DE SEGURANÇA!')
            game_over3()

        elif senha2 == 'China':
            print('''\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mÓtimo, escolhido! Você passou pelo sistema de segurança... Agora é só pegar o cristal
e colocá-lo no seu local de encaixe na porta da próxima sala!''')
            print('\n\033[4;30mPressione "P" para pegar o cristal, encaixá-lo e seguir para a próxima sala!')
            seguir_cristal = input().upper().strip()

            while seguir_cristal != 'P':
                print('\n\033[4;30mPressione "P" para pegar o cristal, encaixá-lo e seguir para a próxima sala!')
                seguir_cristal = input().upper().strip()

            if seguir_cristal == 'P':
                sala_do_urso()
# -------------------------------------------------------FUNÇÃO 15 (SALA DO URSO)---------------------------------------------------------------------
def sala_do_urso():
    print('\n\033[0;30;107m\033[1;30;107mSALA DO URSO')
    print('''\033[0;34;49m-Voz misteriosa: \033[1;39;49mUm urso selvagem habita essa sala... 
Ele parece estar faminto, a comida é bem escassa aqui embaixo... ''')

    if itens['z'] == 0:
        sleep(4)
        print('\033[0;34;49m-Voz misteriosa: \033[1;39;49mPelo visto o armeiro estava certo... Uma arma seria muito útil...')
        print('\n\033[1;31;49mVOCÊ FOI DEVORADO PELO URSO... NÃO TEVE NENHUMA CHANCE CONTRA A FERA!')
        print('\n\033[4;30mVocê deve retornar ao início do jogo para que faça escolhas diferentes e consiga progredir nessa fase!\n')
        game_over()

    elif itens['z'] == 1:
        sleep(4)
        print('\n\033[4;30mEm questão de segundos o urso parte para cima de você...')
        sleep(2)
        print('\033[4;30mVocê rapidamente desvia do golpe do urso com um mortal triplo duplo carpado e consegue sacar sua arma, mirando no animal...')
        print('\033[4;30mAperte "A" para atirar na besta e "N" ignorar!')
        atirar = input().upper().strip()

        while atirar != 'A' and atirar != 'N':
            print('\033[4;30mAperte "A" para atirar na besta e "N" ignorar!')
            atirar = input().upper().strip()

        if atirar == 'N':
            print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mEra só atirar, escolhido...')
            print('\n\033[1;31;49mVOCÊ FOI DEVORADO PELO URSO...')
            game_over3()

        elif atirar == 'A':
            print('''\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mUm mortal triplo duplo carpado? Quem diria... 
O escolhido, além de tudo, tem habilidades ninjas! Agora o urso está adormecido!''')
            print('\033[0;34;49m-Voz misteriosa: \033[1;39;49mVocê está chegando ao final da sua jornada escolhido... Siga para a próxima sala!')
            print('\n\033[4;30mAperte "A" para abrir a porta da próxima sala!')
            abrir_urso = input().upper().strip()

            while abrir_urso != 'A':
                print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mVocê quer mesmo continuar nessa sala? O urso vai acordar a qualquer momento!')
                print('\n\033[4;30mAperte "A" para abrir a porta da próxima sala!')
                abrir_urso = input().upper().strip()

            if abrir_urso == 'A':
                sala_da_vacina_direita()
# -------------------------------------------FUNÇÃO 16 (SALA DA VACINA - DIREITA)---------------------------------------------------------------------
def sala_da_vacina_direita():
    print('\n\033[0;30;107m\033[1;30;107mSALA DA VACINA')
    print('''\033[0;34;49m-Voz misteriosa: \033[1;39;49mVocê chegou, escolhido! Esse sempre foi o seu destino! Você está na sala da vacina...
A vacina e a fórmula para a fabricação estão na cúpula de vidro no centro da sala!
Só há um problema... A cúpula está trancada e há três opções de chave disponíveis!''')
    print('\n\033[4;30mDigite 1, 2 ou 3 para escolher entre a primeira, segunda e terceira chave!')

    chaves = input().upper().strip()

    while chaves != '1' and chaves != '2' and chaves != '3':
        print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mPreste atenção, escolhido! As únicas opções disponíveis são 1, 2 ou 3!')
        print('\n\033[4;30mDigite 1, 2 ou 3 para escolher entre a primeira, segunda e terceira chave!')
        chaves = input().upper().strip()

    if chaves == '3':
        print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mChave correta! A cúpula foi aberta e você já tem a vacina e a fórmula em mãos...')
        print('\033[0;34;49m-Voz misteriosa: \033[1;39;49mFinalmente! A saída secreta da masmorra é pelo elevador no canto da sala...')
        print('\n\033[4;30mPressione "C" para chamar o elevador e sair da masmorra!')
        elevador = input().upper().strip()

        while elevador != 'C':
            print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mVocê conseguiu, escolhido! Leve a cura para toda a humanidade!')
            print('\n\033[4;30mPressione "C" para chamar o elevador e sair da masmorra!')
            elevador = input().upper().strip()

        if elevador == 'C':
            ganhou()

    elif chaves == '1':
        print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mChave errada, escolhido! Tente outra!')
        print('\n\033[4;30mDigite 2 ou 3 para escolher entre a segunda e terceira chave!')
        chaves = input().upper().strip()

        while chaves != '2' and chaves != '3':
            print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mPreste atenção, escolhido! As únicas opções disponíveis são 2 ou 3!')
            print('\n\033[4;30mDigite 2 ou 3 para escolher entre a segunda e terceira chave!')
            chaves = input().upper().strip()

        if chaves == '2':
            print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mChave errada, escolhido! Tente outra!')
            print('\n\033[4;30mDigite 3 e teste a terceira chave!')
            chaves = input().upper().strip()

            while chaves != '3':
                print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mPreste atenção, escolhido! A única opção disponível é 3!')
                print('\n\033[4;30mDigite 3  teste a terceira chave!')
                chaves = input().upper().strip()

            if chaves == '3':
                print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mChave correta! A cúpula foi aberta e você já tem a vacina e a fórmula em mãos...')
                print('\033[0;34;49m-Voz misteriosa: \033[1;39;49mFinalmente! A saída secreta da masmorra é pelo elevador no canto da sala...')
                print('\n\033[4;30mPressione "C" para chamar o elevador e sair da masmorra!')
                elevador = input().upper().strip()

                while elevador != 'C':
                    print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mVocê conseguiu, escolhido! Leve a cura para toda a humanidade!')
                    print('\n\033[4;30mPressione "C" para chamar o elevador e sair da masmorra!')
                    elevador = input().upper().strip()

                if elevador == 'C':
                    ganhou()

        elif chaves == '3':
            print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mChave correta! A cúpula foi aberta e você já tem a vacina e a fórmula em mãos...')
            print('\033[0;34;49m-Voz misteriosa: \033[1;39;49mFinalmente! A saída secreta da masmorra é pelo elevador no canto da sala...')
            print('\n\033[4;30mPressione "C" para chamar o elevador e sair da masmorra!')
            elevador = input().upper().strip()

            while elevador != 'C':
                print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mVocê conseguiu, escolhido! Leve a cura para toda a humanidade!')
                print('\n\033[4;30mPressione "C" para chamar o elevador e sair da masmorra!')
                elevador = input().upper().strip()

            if elevador == 'C':
                ganhou()

    elif chaves == '2':
        print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mChave errada, escolhido! Tente outra!')
        print('\n\033[4;30mDigite 1 ou 3 para escolher entre a primeira e terceira chave!')
        chaves = input().upper().strip()

        while chaves != '1' and chaves != '3':
            print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mPreste atenção, escolhido! As únicas opções disponíveis são 1 ou 3!')
            print('\n\033[4;30mDigite 1 ou 3 para escolher entre a primeira e terceira chave!')
            chaves = input().upper().strip()

        if chaves == '1':
            print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mChave errada, escolhido! Tente outra!')
            print('\n\033[4;30mDigite 3 e teste a terceira chave!')
            chaves = input().upper().strip()

            while chaves != '3':
                print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mPreste atenção, escolhido! A única opção disponível é 3!')
                print('\n\033[4;30mDigite 3  teste a terceira chave!')
                chaves = input().upper().strip()

            if chaves == '3':
                print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mChave correta! A cúpula foi aberta e você já tem a vacina e a fórmula em mãos...')
                print('\033[0;34;49m-Voz misteriosa: \033[1;39;49mFinalmente! A saída secreta da masmorra é pelo elevador no canto da sala...')
                print('\n\033[4;30mPressione "C" para chamar o elevador e sair da masmorra!')
                elevador = input().upper().strip()

                while elevador != 'C':
                    print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mVocê conseguiu, escolhido! Leve a cura para toda a humanidade!')
                    print('\n\033[4;30mPressione "C" para chamar o elevador e sair da masmorra!')
                    elevador = input().upper().strip()

                if elevador == 'C':
                    ganhou()

        elif chaves == '3':
            print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mChave correta! A cúpula foi aberta e você já tem a vacina e a fórmula em mãos...')
            print('\033[0;34;49m-Voz misteriosa: \033[1;39;49mFinalmente! A saída secreta da masmorra é pelo elevador no canto da sala...')
            print('\n\033[4;30mPressione "C" para chamar o elevador e sair da masmorra!')
            elevador = input().upper().strip()

            while elevador != 'C':
                print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mVocê conseguiu, escolhido! Leve a cura para toda a humanidade!')
                print('\n\033[4;30mPressione "C" para chamar o elevador e sair da masmorra!')
                elevador = input().upper().strip()

            if elevador == 'C':
                ganhou()
# --------------------------------------------------------------CHAMADA PRINCIPAL---------------------------------------------------------------------
print('\n\033[4;30mAPERTE "S" PARA INICIAR O JOGO!')
comando_iniciar = input().upper().strip()

while comando_iniciar != 'S':
    print('\n\033[0;34;49m-Voz misteriosa: \033[1;39;49mInicie o jogo, escolhido! Você não vai se arrepender!')
    print('\n\033[4;30mAPERTE "S" PARA INICIAR O JOGO!')
    comando_iniciar = input().upper().strip()

if comando_iniciar == 'S':
    sala_principal()