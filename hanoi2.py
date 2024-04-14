from typing import NewType

Disco = NewType('Disco', int)

class OrdemIncorreta(Exception):
    def __init__(self, topo: int, base: int) -> None:
        super().__init__("Não é possível colocar um disco de tamanho %d em cima de um disco de tamanho %d" % (topo, base))

class Torre:
    """Classe para uma torre"""
    def __init__(self, nb_discos: int) -> None:
        """Criação de uma torre"""
        self._torre = [Disco(tamanho) for tamanho in range(1, nb_discos + 1)]
        self._torre.reverse()  # ordena a pilha do maior para o menor

    def pop_disco_topo(self) -> Disco:
        """Remove e retorna o disco do topo desta torre."""
        return self._torre.pop()

    def adicionar_disco(self, disco: Disco) -> None:
        """Adiciona um disco ao topo da torre.
        Levanta OrdemIncorreta se o disco a ser adicionado for muito grande.
        """
        if len(self._torre) and self._torre[-1] < disco:
            raise OrdemIncorreta(disco, self._torre[-1])
        self._torre.append(disco)

    @property
    def altura(self) -> int:
        """Número de discos na torre."""
        return len(self._torre)

    def __repr__(self) -> str: 
        """Imprime os elementos da torre"""
        return repr(self._torre)


class Tabuleiro:
    """Classe para o tabuleiro completo"""
    def __init__(self, nb_discos: int) -> None:
        self.passos = 0  # Inicializa o contador de passos
        self._iniciar_tabuleiro(nb_discos)

    def _iniciar_tabuleiro(self, nb_discos: int) -> None:
        self._torres = [Torre(nb_discos), Torre(0), Torre(0)]

    def mover(self, de_torre: int, para_torre: int) -> None: 
        """Move de uma torre para outra (torres especificadas como um int de 1-3).  
        Imprime um erro se o movimento for inválido."""
        # Convertendo de índice 1 para índice 0.
        de_torre -= 1
        para_torre -= 1
        # Realiza o movimento, imprime exceção se falhar.
        try:
            disco = self._torres[de_torre].pop_disco_topo()
            try:
                self._torres[para_torre].adicionar_disco(disco)
            except OrdemIncorreta:
                # não solte o disco! Coloque-o de volta onde o pegamos e levante a exceção novamente.
                self._torres[de_torre].adicionar_disco(disco)
                raise
        except Exception as e:
            print('Movimento falhou:', str(e))
        else:
            self.passos += 1  # Incrementa o contador de passos
            self._verificar_vitoria()
            print(self)


    def _verificar_vitoria(self) -> None:
        """Verifica se todos os discos foram movidos para a última torre (condição de vitória).
        Se o jogador alcançou a vitória, reinicia o jogo.
        """
        if sum(torre.altura for torre in self._torres) == self._torres[2].altura:
            print('Vitória:')                
            print(self)
            print('Novo tabuleiro:')
            self._iniciar_tabuleiro(self._torres[2].altura)   

    def __repr__(self) -> str:
        """Imprime as torres"""
        return "\n".join([repr(torre) for torre in self._torres]) + "\n"


if __name__ == '__main__':
    nb_discos = int(input("Digite o número de discos: "))
    jogo = Tabuleiro(nb_discos)
    jogo.mover(1,3)
    jogo.mover(1,3)
    jogo.mover(1,2)
    jogo.mover(3,2)   
    jogo.mover(1,3)
    jogo.mover(2,1)    
    jogo.mover(2,3)  
    jogo.mover(1,3)
    print(f"Quantidade de passos dados: {jogo.passos}")

