from django.db import models

class Egresso(models.Model):
    # Informações Pessoais
    nome_completo = models.CharField(max_length=255)
    genero = models.CharField(
        max_length=50,
        choices=[
            ('Mulher Cisgênero', 'Mulher Cisgênero'),
            ('Mulher Transexual', 'Mulher Transexual'),
            ('Homem Cisgênero', 'Homem Cisgênero'),
            ('Homem Transexual', 'Homem Transexual'),
            ('Não Binário', 'Não Binário'),
            ('Prefiro não responder', 'Prefiro não responder'),
            ('Não sei', 'Não sei'),
            ('Outro', 'Outro')
        ]
    )
    data_nascimento = models.DateField()
    nacionalidade = models.CharField(max_length=50, choices=[('Brasileiro(a)', 'Brasileiro(a)'), ('Estrangeiro', 'Estrangeiro')])
    pais = models.CharField(max_length=100, blank=True, null=True)
    cor_raca = models.CharField(
        max_length=50,
        choices=[
            ('Preta', 'Preta'),
            ('Parda', 'Parda'),
            ('Amarela', 'Amarela'),
            ('Indígena', 'Indígena'),
            ('Não sei', 'Não sei'),
            ('Prefiro não responder', 'Prefiro não responder')
        ]
    )
    pessoa_com_deficiencia = models.BooleanField(default=False)
    tipo_deficiencia = models.CharField(max_length=255, blank=True, null=True)
    estado_civil = models.CharField(
        max_length=50,
        choices=[
            ('Solteiro(a)', 'Solteiro(a)'),
            ('Casado(a)', 'Casado(a)'),
            ('Divorciado(a)', 'Divorciado(a)'),
            ('União Estável', 'União Estável')
        ]
    )
    estado_residencia = models.CharField(max_length=2)
    municipio_residencia = models.CharField(max_length=255)

    # Formação Acadêmica
    instituicao_graduacao = models.CharField(max_length=255)
    curso_graduacao = models.CharField(max_length=255)
    ano_conclusao_graduacao = models.IntegerField()
    possui_pos_graduacao = models.BooleanField(default=False)
    cursos_pos_graduacao = models.ManyToManyField('CursoPosGraduacao', blank=True)

    # Profissional
    atualmente_empregado = models.BooleanField(default=False)
    emprego_atual = models.CharField(max_length=255, blank=True, null=True)
    area_atuacao = models.CharField(max_length=255)
    entrou_mercado_trabalho_12_meses = models.BooleanField(default=False)
    situacao_atual = models.CharField(
        max_length=50,
        choices=[
            ('Empregado na área de formação', 'Empregado na área de formação'),
            ('Empregado em área distinta', 'Empregado em área distinta'),
            ('Não estou empregado', 'Não estou empregado')
        ]
    )
    media_salarial = models.CharField(
        max_length=50,
        choices=[
            ('até 1 salário mínimo', 'até 1 salário mínimo'),
            ('entre 1 e 3 salários mínimos', 'entre 1 e 3 salários mínimos'),
            ('entre 4 e 7 salários mínimos', 'entre 4 e 7 salários mínimos'),
            ('mais que 7 salários mínimos', 'mais que 7 salários mínimos')
        ]
    )
    posicao_gestao = models.BooleanField(default=False)
    funcao_gestao = models.CharField(max_length=255, blank=True, null=True)
    instituicao_gestao = models.CharField(max_length=255, blank=True, null=True)

    # Contribuições Científicas e Sociais
    publicacoes_orientador = models.CharField(
        max_length=50,
        choices=[
            ('Não', 'Não'),
            ('Sim, de 1 a 2 publicações', 'Sim, de 1 a 2 publicações'),
            ('Sim, de 3 a 5 publicações', 'Sim, de 3 a 5 publicações'),
            ('Sim, mais de 5 publicações', 'Sim, mais de 5 publicações')
        ]
    )

    # Métodos auxiliares e metadados
    class Meta:
        verbose_name = 'Egresso'
        verbose_name_plural = 'Egressos'

    def __str__(self):
        return self.nome_completo


class CursoPosGraduacao(models.Model):
    # Detalhes dos cursos de pós-graduação
    nome = models.CharField(max_length=255)
    ano_conclusao = models.IntegerField()
    tipo = models.CharField(
        max_length=50,
        choices=[
            ('Especialização', 'Especialização'),
            ('Residência', 'Residência'),
            ('Mestrado', 'Mestrado'),
            ('Doutorado', 'Doutorado'),
            ('Pós-doutorado', 'Pós-doutorado')
        ]
    )
    instituicao = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nome} - {self.tipo}"


class MotivacaoPosGraduacao(models.Model):
    # Motivação para cursar a pós-graduação na UFDPar
    egresso = models.ForeignKey(Egresso, on_delete=models.CASCADE, related_name='motivacoes')
    descricao = models.CharField(
        max_length=255,
        choices=[
            ('Aumento salarial através da titulação', 'Aumento salarial através da titulação'),
            ('Possibilidade de reconhecimento e progressão profissional', 'Possibilidade de reconhecimento e progressão profissional'),
            ('Recomendação da instituição de vínculo de trabalho', 'Recomendação da instituição de vínculo de trabalho'),
            ('Interesse em melhor qualificação profissional', 'Interesse em melhor qualificação profissional'),
            ('Expansão das atividades para outros campos', 'Expansão das atividades para outros campos'),
            ('Não se aplica (ensino, pesquisa e extensão)', 'Não se aplica (ensino, pesquisa e extensão)')
        ]
    )

    def __str__(self):
        return f"{self.descricao} para {self.egresso}"


class ProgramaParticipacao(models.Model):
    # Programas de participação
    egresso = models.ForeignKey(Egresso, on_delete=models.CASCADE, related_name='programas_participacao')
    tipo_programa = models.CharField(
        max_length=50,
        choices=[
            ('Iniciação Científica e/ou Tecnológica', 'Iniciação Científica e/ou Tecnológica'),
            ('Extensão', 'Extensão'),
            ('Ensino', 'Ensino'),
            ('Monitoria', 'Monitoria')
        ]
    )
    bolsista = models.BooleanField(default=False)
    agencia_fomentadora = models.CharField(
        max_length=50,
        choices=[('CNPq', 'CNPq'), ('CAPES', 'CAPES'), ('FAPEPI', 'FAPEPI'), ('UFDPar', 'UFDPar'), ('Outra', 'Outra')],
        blank=True,
        null=True
    )
    especificar_agencia = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"{self.tipo_programa} - {self.egresso}"


class AvaliacaoCurso(models.Model):
    # Avaliação do último curso concluído
    egresso = models.ForeignKey(Egresso, on_delete=models.CASCADE, related_name='avaliacoes_curso')
    criterio = models.CharField(max_length=255)
    nota = models.IntegerField(choices=[(1, 'Péssimo'), (2, 'Ruim'), (3, 'Regular'), (4, 'Bom'), (5, 'Ótimo')])

    def __str__(self):
        return f"Avaliação {self.criterio} - Nota {self.nota}"


class AtividadePosConclusao(models.Model):
    # Atividades e Contribuições Científicas e Profissionais Pós-Conclusão
    egresso = models.ForeignKey(Egresso, on_delete=models.CASCADE, related_name='atividades_pos_conclusao')
    tipo_atividade = models.CharField(
        max_length=50,
        choices=[
            ('Eventos Científicos', 'Participação em eventos científicos'),
            ('Livros/Capítulos', 'Publicação de Livro(s) e/ou Capítulos'),
            ('Patentes/Softwares', 'Desenvolvimento de patentes ou softwares'),
            ('Prêmios', 'Recebimento de prêmios científicos ou profissionais'),
            ('Rede de Pesquisa', 'Colaboração em redes de pesquisa'),
            ('Políticas/Práticas', 'Contribuição para políticas e práticas')
        ]
    )

    def __str__(self):
        return f"{self.tipo_atividade} - {self.egresso}"
