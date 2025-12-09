from rest_framework.response import Response
from rest_framework import status, permissions, generics
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, LoginSerializer, EmptySerializer


class RegisterView(generics.GenericAPIView):
    serializer_class = UserSerializer
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token,_ = Token.objects.get_or_create(user=user)
            return Response({'message': 'User registered successfully',
                            'username': user.username,
                            'email': user.email},
                             status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(username=username, password=password)
        
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({'refresh': str(refresh),
                             'access': str(refresh.access_token),
                             'name': user.username,
                             'email': user.email,
                             
            })
        return Response({'message': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

class LogoutView(generics.GenericAPIView):
    serializer_class = EmptySerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        if hasattr(request, 'access_token'):
            request.user.access_token.delete()
            
        return Response({'message': 'Logged out successfully!'}, status=status.HTTP_200_OK)
