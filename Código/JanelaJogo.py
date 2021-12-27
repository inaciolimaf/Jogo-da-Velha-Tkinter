from tkinter import *
from PIL import Image, ImageTk
# Para acessar imagens .jpg
from Tabuleiro import Tabuleiro
from Jogador import *
from tkinter import messagebox
import time

class JanelaJogo():
    def __init__(self, nomeJogador1: str, nomeJogador2: str) -> None:
        self.jogador1 = Jogador(nomeJogador1, "x", 0)
        self.jogador2 = Jogador(nomeJogador2, "o", 0)
        self.tabuleiro = Tabuleiro()
        # Objeto que vai conter os valores do tabuleiro
        self.jogada_vez = "x"
        self.quant_jogadas = 0
        self.vencedor = ""
        self.resultado_Jogador=0
        self.inicia_a_janela()

    def inicia_a_janela(self):
        self.janelaJogo = Tk()
        self.configuraJanela()
        self.atualiza_resultados()
        # Cria o label com os resultados de vitorias
        self.foto_Vazio = self.__PegaImagemJpg("Vazio.jpg", 60)
        self.foto_X = self.__PegaImagemJpg("X.jpg", 60)
        self.foto_O = self.__PegaImagemJpg("Bola.jpg", 60)
        # Pega cada imagem para colocar no tabuleiro
        self.atualiza_botao_tabuleiro()
        # Cria o tabuleiro na janela
        self.cria_botao_reiniciar()
        self.janelaJogo.mainloop()

    def cria_botao_reiniciar(self):
        Button(self.janelaJogo, text="Reiniciar o jogo",
               command=self.reiniciar).grid(row=3, pady=10)

    def reiniciar(self):
        self.atualiza_botao_tabuleiro()
        # Limpa o tabuleiro na janela criando um novo
        self.quant_jogadas = 0
        self.tabuleiro = Tabuleiro()
        # Limpa o tabuleiro criando um novo

    def atualiza_botao_tabuleiro(self):
        self.tabuleiro_janela = Frame(self.janelaJogo)
        self.tabuleiro_janela.grid(row=2, column=0, pady=20, padx=20)
        # Cria um frame para ter o tabuleiro na janela
        self.botoes = [[], [], []]
        # Cria a matriz para armazenar os botoes
        for x in range(3):
            for y in range(3):
                self.botoes[x].append(self.cria_casa_tabuleiro(x, y))
                # Esse código só funciona se usar uma função separada para criar o botão
                # se não o botão executara a função usando o x e y na hora de quando for apertado,
                # ou seja, sempre 2 e 2. Usando a função cria_casa_tabuleiro() o x e o y são os
                # valores na hora que o botão foi criado ou seja na posição certa do botão
                self.botoes[x][y].grid(row=x, column=y)
                # Cria o botao e coloca na matriz

    def cria_casa_tabuleiro(self, x, y):
        return Button(self.tabuleiro_janela, image=self.foto_Vazio,
                      command=lambda: self.clica_botao(x, y))
        # Cria uma casa no tabulerito como sendo um botão

    def clica_botao(self, x, y):
        # Função sera executada quando o botão for clicado
        if self.tabuleiro.na_posicao(x, y) == "":
            # Executa o código se a casa estiver vazia
            self.quant_jogadas += 1
            self.tabuleiro.mudar_posicao(x, y, self.jogada_vez)
            # Muda a posição no tabuleiro
            if self.jogada_vez == 'o':
                self.botoes[x][y]['image'] = self.foto_O
            else:
                self.botoes[x][y]['image'] = self.foto_X
            # Muda a imagem do botão
            self.mudar_vez()
            self.vencedor = self.tabuleiro.verifica_vitoria()
            # Calcula o vencedor da partida
            if self.vencedor in ["x", "o"]:
                # Se o vencedor existir
                if self.jogador1.jogada == self.vencedor:
                    mensagem = f"O vencedor é o {self.jogador1.nome} ({self.vencedor})"
                    self.jogador1.vitorias += 1
                elif self.jogador2.jogada == self.vencedor:
                    mensagem = f"O vencedor é o {self.jogador2.nome} ({self.vencedor})"
                    self.jogador2.vitorias += 1
                # Cria a mensagem de acordo com o nome do jogador
                messagebox.showinfo(title="Vencedor:", message=mensagem)
                # Cria uma janela com as informações do vencedor
                self.reiniciar()
            elif self.quant_jogadas == 9:
                messagebox.showinfo(title="Deu velha", message="Deu velha")
                self.reiniciar()
            self.atualiza_resultados()
            # Atualiza os valores da tabela de resultados e reinicia o tabuleiro

    def mudar_vez(self):
        if self.jogada_vez == "x":
            self.jogada_vez = "o"
        elif self.jogada_vez == "o":
            self.jogada_vez = "x"

    def atualiza_resultados(self):
        # Cria a tabela com os resultados
        if self.jogada_vez == self.jogador1.jogada:
            vez_do_jogador = self.jogador1
        elif self.jogada_vez == self.jogador2.jogada:
            vez_do_jogador = self.jogador2
        if self.resultado_Jogador:
            self.resultado_Jogador.destroy()
            # Apaga o Label se ele já estiver criado
        self.resultado_Jogador = Label(
            self.janelaJogo, text=f"Vitórias:\n{self.jogador1.nome}: {self.jogador1.vitorias}\n{self.jogador2.nome}: {self.jogador2.vitorias}\n A vez é do jogador: {vez_do_jogador.nome}", font=("Times", 15))
        self.resultado_Jogador.grid(row=0, column=0)

    def configuraJanela(self):
        self.janelaJogo.geometry('+500+200')
        # Configura a posição incial da janela
        self.janelaJogo.title("Jogo da Velha")
        self.janelaJogo.resizable(False, False)
        # Não permite que a janela seja mudada de tamanho
        self.janelaJogo.iconphoto(True, self.__PegaImagemJpg("X.jpg", 15))
        # Seleciona o icone da janela


    def __PegaImagemJpg(self, nome: str, resolucao: int):
        # Parte necessária porque o Tkinter não suporta arquivos.jpg
        imagem = Image.open(nome)
        # Abre a imagem
        imagem = imagem.resize((resolucao, resolucao))
        # Configura a resolução da imagem
        imagem = ImageTk.PhotoImage(imagem)
        # Passa a imagem para um jeito que o Tkinter aceita
        return imagem
