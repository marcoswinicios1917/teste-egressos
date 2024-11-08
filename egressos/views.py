from rest_framework import viewsets, filters
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.parsers import JSONParser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.negotiation import DefaultContentNegotiation
from rest_framework.renderers import JSONRenderer
from .models import (
    Egresso,
    CursoPosGraduacao,
    MotivacaoPosGraduacao,
    ProgramaParticipacao,
    AvaliacaoCurso,
    AtividadePosConclusao
)
from .serializers import (
    EgressoSerializer,
    CursoPosGraduacaoSerializer,
    MotivacaoPosGraduacaoSerializer,
    ProgramaParticipacaoSerializer,
    AvaliacaoCursoSerializer,
    AtividadePosConclusaoSerializer
)

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10  # Quantidade de itens por página
    page_size_query_param = 'page_size'
    max_page_size = 100

class EgressoViewSet(viewsets.ModelViewSet):
    queryset = Egresso.objects.all()
    serializer_class = EgressoSerializer
    permission_classes = [AllowAny]  # Permissão temporária para testes
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nome_completo', 'curso_graduacao', 'area_atuacao']
    ordering_fields = ['nome_completo', 'ano_conclusao_graduacao']
    ordering = ['nome_completo']
    parser_classes = [JSONParser]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    content_negotiation_class = DefaultContentNegotiation
    renderer_classes = [JSONRenderer]
    format_kwarg = None  # Define format_kwarg como None para evitar erros

    def dispatch(self, request, *args, **kwargs):
        """Método dispatch customizado para configurar o renderer e o tipo de mídia aceito."""
        self.default_response_headers = {}
        
        # Configure o renderer manualmente
        request.accepted_renderer = JSONRenderer()
        request.accepted_media_type = request.accepted_renderer.media_type
        
        return super().dispatch(request, *args, **kwargs)

# Outros viewsets

class CursoPosGraduacaoViewSet(viewsets.ModelViewSet):
    queryset = CursoPosGraduacao.objects.all()
    serializer_class = CursoPosGraduacaoSerializer
    permission_classes = [AllowAny]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['nome', 'instituicao']
    ordering_fields = ['nome', 'ano_conclusao']
    ordering = ['nome']

class MotivacaoPosGraduacaoViewSet(viewsets.ModelViewSet):
    queryset = MotivacaoPosGraduacao.objects.all()
    serializer_class = MotivacaoPosGraduacaoSerializer
    permission_classes = [AllowAny]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['descricao']

class ProgramaParticipacaoViewSet(viewsets.ModelViewSet):
    queryset = ProgramaParticipacao.objects.all()
    serializer_class = ProgramaParticipacaoSerializer
    permission_classes = [AllowAny]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['tipo_programa', 'agencia_fomentadora']

class AvaliacaoCursoViewSet(viewsets.ModelViewSet):
    queryset = AvaliacaoCurso.objects.all()
    serializer_class = AvaliacaoCursoSerializer
    permission_classes = [AllowAny]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['criterio']

class AtividadePosConclusaoViewSet(viewsets.ModelViewSet):
    queryset = AtividadePosConclusao.objects.all()
    serializer_class = AtividadePosConclusaoSerializer
    permission_classes = [AllowAny]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['tipo_atividade']  # Corrigido para 'tipo_atividade' no search_fields
