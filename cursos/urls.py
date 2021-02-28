from django.urls import path

from .views import CursoAPIView, AvaliaçãoAPIView

urlpatterns = [
    path('cursos/', CursoAPIView.as_view(), name='cursos'),
    path('avaliacoes/', AvaliaçãoAPIView.as_view(), name='avaliacoes'),
]

