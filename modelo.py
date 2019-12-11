class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def set_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()


class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao


class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
vingadores.set_like()
vingadores.set_like()
vingadores.set_like()

atlanta.set_like()
atlanta.set_like()

print(f'Nome: {vingadores.nome} - Likes: {vingadores.likes}')
print(f'Nome: {atlanta.nome} - Likes: {atlanta.likes}')


filmes_series = [vingadores , atlanta]
#Polimorfismo facilidade em apresentação, ou em acessar classes com mesma herança
#++ If em uma linha
for programa in filmes_series:
    detalhes = programa.duracao if hasattr(programa,'duracao') else programa.temporadas
    print(f'Nome: {programa.nome} - Tempo {detalhes} - Likes: {programa.likes}')


