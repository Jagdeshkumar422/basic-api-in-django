from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser
from .serializers import UserSerializer

# ✅ User Registration
class RegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ✅ Get All Users
class GetAllUsersAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        users = CustomUser.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# ✅ Get Single User
class GetSingleUserAPIView(APIView):
    permission_classes = [AllowAny]

    def get(self, request, user_id):
        user = get_object_or_404(CustomUser, id=user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)

# ✅ Update User
class UpdateUserAPIView(APIView):
    permission_classes = [AllowAny]

    def put(self, request, user_id):
        user = get_object_or_404(CustomUser, id=user_id)
        serializer = UserSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User updated successfully'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ✅ Delete User
class DeleteUserAPIView(APIView):
    permission_classes = [AllowAny]

    def delete(self, request, user_id):
        user = get_object_or_404(CustomUser, id=user_id)
        user.delete()
        return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

# ✅ Login API (JWT Token)
class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")

        user = CustomUser.objects.filter(username=username).first()
        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token)
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

# ✅ Logout API
class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        return Response({"message": "Successfully logged out."}, status=status.HTTP_205_RESET_CONTENT)




# from django.contrib.auth.models import User
# from rest_framework import serializers, status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework_simplejwt.tokens import RefreshToken

# # Serializer for User Registration
# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password']
#         extra_kwargs = {'password': {'write_only': True}}

#     def create(self, validated_data):
#         user = User.objects.create_user(**validated_data)
#         return user

# # API for User Registration
# class RegisterAPIView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         serializer = RegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# # API for Login and Token Generation
# class LoginAPIView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         username = request.data.get("username")
#         password = request.data.get("password")

#         user = User.objects.filter(username=username).first()
#         if user and user.check_password(password):
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token)
#             })
#         return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


# class LogoutAPIView(APIView):
#     permission_classes = [IsAuthenticated]  # ✅ Requires authentication

#     def post(self, request):
#         try:
#             # Logout only requires removing the token from the client side
#             return Response({"message": "Successfully logged out."}, 
#                             status=status.HTTP_205_RESET_CONTENT)
#         except Exception as e:
#             return Response({"error": str(e)}, 
#                             status=status.HTTP_400_BAD_REQUEST)

