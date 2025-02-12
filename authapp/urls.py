from django.urls import path
from .views import (
    RegisterAPIView, LoginAPIView, LogoutAPIView, 
    GetAllUsersAPIView, GetSingleUserAPIView, 
    UpdateUserAPIView, DeleteUserAPIView
)

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('users/', GetAllUsersAPIView.as_view(), name='get_all_users'),
    path('users/<int:user_id>/', GetSingleUserAPIView.as_view(), name='get_single_user'),
    path('users/update/<int:user_id>/', UpdateUserAPIView.as_view(), name='update_user'),
    path('users/delete/<int:user_id>/', DeleteUserAPIView.as_view(), name='delete_user'),
]


# from django.urls import path
# from .views import RegisterAPIView, LoginAPIView, LogoutAPIView

# urlpatterns = [
#     path('register/', RegisterAPIView.as_view(), name='register'),
#     path('login/', LoginAPIView.as_view(), name='login'),
#     path('logout/', LogoutAPIView.as_view(), name='logout'),
# ]
