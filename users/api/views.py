from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny
from users.api.serializers import UserProfileExampleSerializer

from users.models import UserProfileExample

class UserProfileExampleViewSet(ModelViewSet):
    serializer_class = UserProfileExampleSerializer
    permission_classes = [AllowAny]
    queryset = UserProfileExample.objects.all()
    http_method_names = ['get', 'put']


def autenticacao(x,y):
    if x == "allysonstudy2021@gmail.com" and y == "tatubola":
        return True
    return True 