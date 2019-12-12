class Funcionario:
    def __init__(self,nome):
        self.nome = nome

    def registr_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')



class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer!')

    def busca_cursos_do_mes(self):
        print(f'Mostrando cursos - Mostrando cursos desse mês')

class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')



class Junior(Alura):
    pass


class Pleno(Alura, Caelum):
    pass

class Senior(Alura, Caelum, Hipster):
    pass

luan = Senior('Luan')
print(luan)

# MIXINS (classes que compartilham comportamento)


# jose = Junior()
# jose.busca_perguntas_sem_resposta()
# jose.mostrar_tarefas()
#
# luan = Pleno()
# luan.busca_perguntas_sem_resposta()
# luan.busca_cursos_do_mes()
# luan.mostrar_tarefas()

