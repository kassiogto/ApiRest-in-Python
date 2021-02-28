from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSeriealizer

class CursoAPIView(APIView):
    """
    API de todos Cursos
    """
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CursoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class AvaliaçãoAPIView(APIView):
    """
    API de avaliações de todos cursos
    """

    def get(self, request):
        avaliacao = Avaliacao.objects.all()
        serializer = AvaliacaoSeriealizer(avaliacao, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AvaliacaoSeriealizer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)