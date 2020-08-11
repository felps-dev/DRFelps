from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import (
    HTTP_200_OK,
)
from rest_framework.response import Response
import requests


@api_view(["GET"])
@permission_classes((IsAuthenticated,))
def get_someurl(request, param):
    r = requests.get('http://www.someurl.com.br/api/%s' % (param))
    if (r.status_code != 200):
        return Response('Erro!, verifique o status code.', r.status_code)
    else:
        return Response(r.json(), HTTP_200_OK)
