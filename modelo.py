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

    # def imprime(self):
    #     print(f'Nome: {self.nome} Ano {self.ano} - Likes: {self.likes}')

    def __str__(self):
        return f'Nome: {self.nome} Ano {self.ano} - Likes: {self.likes}'

class Filme(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    # def imprime(self):
    #     print(f'Nome: {self.nome} Ano {self.ano} - Duracao {self.duracao} min - Likes: {self.likes}')

    def __str__(self):
        return f'Nome: {self.nome} Ano {self.ano} - Duracao {self.duracao} min - Likes: {self.likes}'

class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    # def imprime(self):
    #     print(f'Nome: {self.nome} Ano {self.ano} - Duracao {self.temporadas} temporadas - Likes: {self.likes}')

    def __str__(self):
        return f'Nome: {self.nome} Ano {self.ano} - Duracao {self.temporadas} temporadas - Likes: {self.likes}'

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)

vingadores.set_like()
vingadores.set_like()
vingadores.set_like()

atlanta.set_like()
atlanta.set_like()

#print(f'Nome: {vingadores.nome} - Likes: {vingadores.likes}')
#print(f'Nome: {atlanta.nome} - Likes: {atlanta.likes}')


filmes_series = [vingadores , atlanta]
#Polimorfismo (utilizar uma função unica sem olhar de quem ele esta executando o imprime)
for programa in filmes_series:
    # Deixando o print mais PYTONICO
    print(programa)


