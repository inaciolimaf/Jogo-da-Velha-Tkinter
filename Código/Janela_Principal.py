from tkinter import *
from PIL import Image, ImageTk
from JanelaJogo import JanelaJogo


class JanelaPrincipal:
    def __init__(self) -> None:
        self.janelaPrincipal = Tk()
        self.cria_botao_iniciar()
        self.cria_entry()
        self.cria_label_pedir_nome()
        self._configura_janela()
        self.janelaPrincipal.mainloop()

    def _configura_janela(self):
        self.janelaPrincipal.geometry('+500+200')
        # Configura a posição incial da janela
        self.janelaPrincipal.title("Jogo da Velha")
        self.janelaPrincipal.resizable(False, False)
        # Não permite que a janela seja mudada de tamanho
        self.janelaPrincipal.iconphoto(True, self.__pega_imagem_jpg("X.jpg", 15))
        # Seleciona o icone da janela

    @staticmethod
    def __pega_imagem_jpg(nome: str, resolucao: int):
        # Parte necessária porque o Tkinter não suporta arquivos.jpg
        imagem = Image.open(nome)
        # Abre a imagem
        imagem = imagem.resize((resolucao, resolucao))
        # Configura a resolução da imagem
        imagem = ImageTk.PhotoImage(imagem)
        # Passa a imagem para um jeito que o Tkinter aceita
        return imagem

    def cria_botao_iniciar(self):
        self.iniciarJogo = Button(
            self.janelaPrincipal, text="Iniciar o Jogo", font=("Times", 15),
            command=self.clique_botao).grid(row=2, column=0, columnspan=2, pady=10)

    def cria_label_pedir_nome(self):
        self.jogador1Label = Label(self.janelaPrincipal,
                                   text="Digite o nome do Jogador 1:", font=("Times", 15), padx=10, pady=10)
        self.jogador1Label.grid(row=0, column=0)
        self.jogador2Label = Label(self.janelaPrincipal,
                                   text="Digite o nome do Jogador 2:", font=("Times", 15))
        self.jogador2Label.grid(row=1, column=0)

    def cria_entry(self):
        self.jogador1Entry = Entry(self.janelaPrincipal, font=(
            "Times", 20))
        self.jogador1Entry.grid(row=0, column=1, padx=10, pady=10)
        self.jogador2Entry = Entry(self.janelaPrincipal, font=(
            "Times", 20))
        self.jogador2Entry.grid(row=1, column=1, padx=10, pady=10)

    def clique_botao(self):
        nome_jogador1 = self.jogador1Entry.get()
        nome_jogador2 = self.jogador2Entry.get()
        # Pega os valores digitados nas caixas de texto
        if nome_jogador1 == "" or nome_jogador2 == "":
            Label(self.janelaPrincipal, text="Digite o jogador 1 e o jogador 2 para continuar.",
                  font=("Times", 15)).grid(row=4, column=0, columnspan=2)
            return
            # Se alguma das caixas de texto estiver em branco pede para digitar os nomes e não faz mais nada
        self.janelaPrincipal.destroy()
        # Fecha a primeira janela
        JanelaJogo(nome_jogador1, nome_jogador2)
        # Cria outra nova
