# egressos/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from egressos.views import (
    EgressoViewSet,
    CursoPosGraduacaoViewSet,
    MotivacaoPosGraduacaoViewSet,
    ProgramaParticipacaoViewSet,
    AvaliacaoCursoViewSet,
    AtividadePosConclusaoViewSet,
)

# Criação do roteador para registrar as ViewSets
router = DefaultRouter()
router.register(r'egressos', EgressoViewSet, basename='egresso')
router.register(r'cursos-pos-graduacao', CursoPosGraduacaoViewSet, basename='curso-pos-graduacao')
router.register(r'motivacoes-pos-graduacao', MotivacaoPosGraduacaoViewSet, basename='motivacao-pos-graduacao')
router.register(r'programas-participacao', ProgramaParticipacaoViewSet, basename='programa-participacao')
router.register(r'avaliacoes-curso', AvaliacaoCursoViewSet, basename='avaliacao-curso')
router.register(r'atividades-pos-conclusao', AtividadePosConclusaoViewSet, basename='atividade-pos-conclusao')

# URLs
urlpatterns = [
    path('', include(router.urls)),  # Inclui as rotas da API registradas no roteador
]
