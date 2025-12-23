<<<<<<< HEAD
from rest_framework import permissions, generics
=======
>>>>>>> 4dc37a49b7dad19216068153343c7b64f103f831
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
<<<<<<< HEAD
from .serializers import UserSerializer
=======
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, LoginSerializer, EmptySerializer
>>>>>>> 4dc37a49b7dad19216068153343c7b64f103f831


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
<<<<<<< HEAD
    serializer_class = UserSerializer
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
=======
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']
>>>>>>> 4dc37a49b7dad19216068153343c7b64f103f831

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
<<<<<<< HEAD
=======
    serializer_class = EmptySerializer
>>>>>>> 4dc37a49b7dad19216068153343c7b64f103f831
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        if hasattr(request, 'access_token'):
            request.user.access_token.delete()
            
        return Response({'message': 'Logged out successfully!'}, status=status.HTTP_200_OK)
