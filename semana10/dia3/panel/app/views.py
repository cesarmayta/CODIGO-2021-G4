from rest_framework.views import APIView
from rest_framework.response import Response

from rest_framework.permissions import IsAuthenticated


class Privado(APIView):

    permission_classes = (IsAuthenticated,)

    def get(self,request):
        content = {'mensaje':'estas entrando a una zona privada'}
        return Response(content)