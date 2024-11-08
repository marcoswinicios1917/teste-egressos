# egressos/admin.py
from django.contrib import admin
from .models import (
    Egresso,
    CursoPosGraduacao,
    MotivacaoPosGraduacao,
    ProgramaParticipacao,
    AvaliacaoCurso,
    AtividadePosConclusao,
)

# Registrando os modelos no admin
admin.site.register(Egresso)
admin.site.register(CursoPosGraduacao)
admin.site.register(MotivacaoPosGraduacao)
admin.site.register(ProgramaParticipacao)
admin.site.register(AvaliacaoCurso)
admin.site.register(AtividadePosConclusao)
