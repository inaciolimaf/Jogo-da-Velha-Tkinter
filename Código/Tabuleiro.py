class Tabuleiro():
    def __init__(self) -> None:
        self.tabuleiro = []
        self.iniciar_tabuleiro()

    def iniciar_tabuleiro(self):
        for x in range(3):
            linha = []
            for x in range(3):
                linha.append("")
            self.tabuleiro.append(linha)
        # Preenche o tabuleiro com ""

    def na_posicao(self, linha: int, coluna: int):
        return self.tabuleiro[linha][coluna]

    def mudar_posicao(self, linha: int, coluna: int, valor: str):
        self.tabuleiro[linha][coluna] = valor

    def verifica_vitoria(self):
        if self.tabuleiro[0][0] == self.tabuleiro[0][1] == self.tabuleiro[0][2] == "x"\
            or self.tabuleiro[1][0] == self.tabuleiro[1][1] == self.tabuleiro[1][2] == "x"\
                or self.tabuleiro[2][0] == self.tabuleiro[2][1] == self.tabuleiro[2][2]=="x":
                    return 'x'
        elif self.tabuleiro[0][0] == self.tabuleiro[0][1] == self.tabuleiro[0][2] == "o"\
            or self.tabuleiro[1][0] == self.tabuleiro[1][1] == self.tabuleiro[1][2] == "o"\
                or self.tabuleiro[2][0] == self.tabuleiro[2][1] == self.tabuleiro[2][2]=="o":
                    return 'o'
        elif self.tabuleiro[0][0] == self.tabuleiro[1][0] == self.tabuleiro[2][0] == "x"\
            or self.tabuleiro[0][1] == self.tabuleiro[1][1] == self.tabuleiro[2][1] == "x"\
                or self.tabuleiro[0][2] == self.tabuleiro[1][2] == self.tabuleiro[2][2]=="x":
                    return 'x'
        elif self.tabuleiro[0][0] == self.tabuleiro[1][0] == self.tabuleiro[2][0] == "o"\
            or self.tabuleiro[0][1] == self.tabuleiro[1][1] == self.tabuleiro[2][1] == "o"\
                or self.tabuleiro[0][2] == self.tabuleiro[1][2] == self.tabuleiro[2][2]=="o":
                    return 'o'
        elif self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] == "x"\
            or self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] == "x":
                return 'x'
        elif self.tabuleiro[0][0] == self.tabuleiro[1][1] == self.tabuleiro[2][2] == "o"\
            or self.tabuleiro[0][2] == self.tabuleiro[1][1] == self.tabuleiro[2][0] == "o":
                return 'o'
        else:
            return ''
        # Retorna o vencedor
