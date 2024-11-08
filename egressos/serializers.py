from rest_framework import serializers
from .models import Egresso, CursoPosGraduacao, MotivacaoPosGraduacao, ProgramaParticipacao, AvaliacaoCurso, AtividadePosConclusao

class CursoPosGraduacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CursoPosGraduacao
        fields = ['id', 'nome', 'ano_conclusao', 'tipo', 'instituicao']

class MotivacaoPosGraduacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotivacaoPosGraduacao
        fields = ['id', 'descricao']

class ProgramaParticipacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgramaParticipacao
        fields = ['id', 'tipo_programa', 'bolsista', 'agencia_fomentadora', 'especificar_agencia']

class AvaliacaoCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AvaliacaoCurso
        fields = ['id', 'criterio', 'nota']

class AtividadePosConclusaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AtividadePosConclusao
        fields = ['id', 'tipo_atividade']

class EgressoSerializer(serializers.ModelSerializer):
    cursos_pos_graduacao = CursoPosGraduacaoSerializer(many=True, read_only=True)
    motivacoes = MotivacaoPosGraduacaoSerializer(many=True, read_only=True)
    programas_participacao = ProgramaParticipacaoSerializer(many=True, read_only=True)
    avaliacoes_curso = AvaliacaoCursoSerializer(many=True, read_only=True)
    atividades_pos_conclusao = AtividadePosConclusaoSerializer(many=True, read_only=True)

    class Meta:
        model = Egresso
        fields = [
            'id', 'nome_completo', 'genero', 'data_nascimento', 'nacionalidade', 'pais', 'cor_raca',
            'pessoa_com_deficiencia', 'tipo_deficiencia', 'estado_civil', 'estado_residencia', 
            'municipio_residencia', 'instituicao_graduacao', 'curso_graduacao', 'ano_conclusao_graduacao', 
            'possui_pos_graduacao', 'cursos_pos_graduacao', 'atualmente_empregado', 'emprego_atual', 
            'area_atuacao', 'entrou_mercado_trabalho_12_meses', 'situacao_atual', 'media_salarial', 
            'posicao_gestao', 'funcao_gestao', 'instituicao_gestao', 'publicacoes_orientador', 
            'motivacoes', 'programas_participacao', 'avaliacoes_curso', 'atividades_pos_conclusao'
        ]
