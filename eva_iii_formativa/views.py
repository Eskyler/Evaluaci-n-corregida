from django.contrib.auth import authenticate, logout
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status
from rest_framework.response import Response

@csrf_exempt
@api_view(['POST'])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    if username is None or password is None:
        return Response({'ERROR': 'Por favor ingrese usuario y/o contraseña en conjunto'},
                        status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)

    if not user:
        return Response({'ERROR': 'Credenciales no válidas'},
                        status=status.HTTP_404_NOT_FOUND)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=status.HTTP_200_OK)

@api_view(['POST','GET'])
@permission_classes([IsAuthenticated])
def userLogout(request):
    request.user.auth_token.delete()
    logout(request)
    return Response({'status': 'Se ha cerrado sesión exitosamente'},
                    status=status.HTTP_200_OK)